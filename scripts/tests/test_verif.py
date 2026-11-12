"""Tests for verif_humanizer.py: python3 -I -m unittest discover -s scripts/tests -v"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[2]
_spec = importlib.util.spec_from_file_location("verif_humanizer", Path(__file__).resolve().parents[1] / "verif_humanizer.py")
vh = importlib.util.module_from_spec(_spec)
sys.modules["verif_humanizer"] = vh  # dataclasses need the module registered
_spec.loader.exec_module(vh)

EM, EN, NBSP = chr(0x2014), chr(0x2013), chr(0x00A0)
LDQ, RDQ, RSQ = chr(0x201C), chr(0x201D), chr(0x2019)
POINTER, ROCKET, REGIE = chr(0x1F449), chr(0x1F680), chr(0x25B6)

BAD_FR = ("# Dans un monde qui évolue à un rythme effréné\n\n"
          f"Dans le monde actuel, l'automatisation change tout {EM} vraiment tout.\n\n"
          "Notre approche est rapide, simple et efficace. Elle est souple, claire et robuste. "
          "Il est important de noter que l'outil joue un rôle crucial dans ce cadre.\n\n"
          "En outre, notre solution est innovante, holistique et révolutionnaire.\n\n"
          "En conclusion, ce n'est pas un outil, c'est une révolution.\n")
CLEAN_FR = ("# Mesurer une tâche avant de l'automatiser\n\n"
            "Un courriel prend deux minutes à traiter. Ça semble peu.\n\n"
            "Sur une année, la boîte en reçoit 25 000. Quelqu'un passe quatre heures par jour à les lire "
            "avant de répondre au client qui attend depuis lundi.\n\n"
            "Personne n'avait encore fait le calcul sur une année entière.\n")
BAD_EN = ("# The Ultimate Guide To Seamless Workflow Automation\n\n"
          f"In today's fast-paced world, teams delve into a rich tapestry of tools {EM} and it shows {ROCKET}.\n\n"
          f"Moreover, it's important to note that this {LDQ}game-changer{RDQ} may potentially help. "
          "It's not just a tool, it's a revolution. Fast, simple, and effective.\n")
CLEAN_EN = ("# How to measure a task before automating it\n\n"
            "An email takes two minutes to process. That sounds small.\n\n"
            "Over a year, the mailbox receives 25,000 of them. Someone spends four hours a day reading them "
            "before answering the client who has been waiting since Monday.\n")


def run_main(args: list[str]) -> tuple[int, str]:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        code = vh.main(args)
    return code, buffer.getvalue()


def found(report: dict, check: str) -> list[dict]:
    return [f for f in report["findings"] if f["check"] == check]


def checks(report: dict, severity: str) -> set[str]:
    return {f["check"] for f in report["findings"] if f["severity"] == severity}


def sev(text: str, check: str, lang: str = "fr", kind: str = "general", **kw) -> list[str]:
    return [f["severity"] for f in found(vh.analyze(text, lang, kind, **kw), check)]


class TestCli(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)

    def write(self, name: str, text: str) -> str:
        path = Path(self._tmp.name) / name
        path.write_text(text, encoding="utf-8")
        return str(path)

    def report(self, text: str, *args: str) -> tuple[int, dict]:
        code, out = run_main([self.write("t.md", text), *args, "--json"])
        return code, json.loads(out)

    def test_bad_fr_fails(self) -> None:
        code, r = self.report(BAD_FR, "--lang", "fr", "--type", "article")
        self.assertEqual((code, r["exit_code"], r["result"]), (1, 1, "fail"))
        self.assertGreaterEqual(r["counts"]["error"], 2)
        self.assertTrue({"dash", "not_x_but_y"} <= checks(r, "error"))
        self.assertIn("P63", [f["pattern_id"] for f in found(r, "not_x_but_y")])
        self.assertGreaterEqual(r["stats"]["triads"], 3)
        self.assertIn("warning", [f["severity"] for f in found(r, "triad")])
        kill = found(r, "kill_list")
        self.assertTrue({"ouvertures", "formules", "clotures"} <= {f["category"] for f in kill})
        self.assertTrue(all(f["level"] in vh.LEVELS and f["source"] for f in kill if f["item"] not in ("density", "cluster")))
        self.assertEqual(r["stats"]["dashes"]["em"], 1)
        out = run_main([self.write("b.md", BAD_FR), "--lang", "fr"])[1].strip().splitlines()
        self.assertTrue(out[0].startswith(f"verif_humanizer {vh.__version__} | file=") and out[-1].startswith("Result: FAIL"))

    def test_clean_texts_pass(self) -> None:
        for text, lang in ((CLEAN_FR, "fr"), (CLEAN_EN, "en")):
            code, r = self.report(text, "--lang", lang, "--type", "article")
            self.assertEqual(code, 0)
            self.assertEqual(r["counts"]["warning"] + r["counts"]["error"], 0, r["findings"])

    def test_bad_en_fails(self) -> None:
        code, r = self.report(BAD_EN, "--lang", "en")
        self.assertEqual(code, 1)
        self.assertTrue(set("dash kill_list title_case curly_quotes hedging_stack emoji not_x_but_y triad".split())
                        <= {f["check"] for f in r["findings"]})
        self.assertIn("delve", [f["item"] for f in found(r, "kill_list")])

    def test_compare_changed_number(self) -> None:
        original = self.write("avant.md", CLEAN_FR)
        changed = self.write("apres.md", CLEAN_FR.replace("25 000", "30 000"))
        code, out = run_main([changed, "--lang", "fr", "--compare", original, "--json"])
        r = json.loads(out)
        self.assertEqual(code, 1)
        c = r["compare"]
        self.assertEqual((c["numbers_missing"], c["numbers_added"], c["paragraphs_equal"]), (["25000"], ["30000"], True))
        self.assertEqual(c["original"], original)
        self.assertEqual({f["item"]: f["severity"] for f in found(r, "numbers")}, {"25000": "error", "30000": "warning"})
        self.assertIn("Compare: paragraphs 4/4 numbers_missing=1", run_main([changed, "--lang", "fr", "--compare", original])[1])

    def test_compare_same_and_paragraphs(self) -> None:
        original = self.write("avant.md", CLEAN_FR)
        self.assertEqual(run_main([original, "--lang", "fr", "--compare", original])[0], 0)
        merged = self.write("m.md", CLEAN_FR.replace("peu.\n\nSur", "peu. Sur"))
        r = json.loads(run_main([merged, "--lang", "fr", "--compare", original, "--json"])[1])
        self.assertIn("paragraph_count", checks(r, "warning"))
        self.assertNotIn("paragraph_count", checks(r, "error"))

    def test_exit_code_2(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(run_main([self.write("a.md", CLEAN_FR), "--lang", "de"])[0], 2)
            self.assertEqual(run_main([str(Path(self._tmp.name) / "missing.md"), "--lang", "fr"])[0], 2)
        bad = self.write("kl.json", json.dumps({"fr": {"vocabulaire": [
            {"item": "crucial", "match": "regex", "pattern": "(", "level": "mesure", "source": "x"}]}}))
        with self.assertLogs("verif_humanizer", level="ERROR") as logs:
            code, _ = run_main([self.write("a.md", CLEAN_FR), "--lang", "fr", "--kill-list", bad])
        self.assertEqual(code, 2)
        self.assertIn("crucial", "\n".join(logs.output))

    def test_json_key_order(self) -> None:
        r = self.report(CLEAN_FR, "--lang", "fr")[1]
        self.assertEqual(list(r), "tool version file lang type options result exit_code counts stats compare "
                                  "findings".split())
        self.assertEqual(list(r["options"]), "compare skip_quotes allow_footer_dash ignore ignore_lines".split())
        self.assertEqual((r["compare"], self.report(CLEAN_FR, "--lang", "fr", "--type", "pub")[1]["type"]), (None, "publicite"))
        self.assertEqual(list(r["stats"]), "words characters paragraphs sections spoken_words sentences dashes bold "
                                           "emoji triads exclamations kill_list".split())
        bad = self.report(BAD_FR, "--lang", "fr")[1]
        self.assertEqual(list(bad["findings"][0]), "id check severity line column paragraph excerpt message item "
                                                   "category pattern_id level source".split())



class TestMatching(unittest.TestCase):
    def kill(self, text: str, lang: str = "fr", **kw) -> list[dict]:
        return found(vh.analyze(text, lang, **kw), "kill_list")

    def test_accents_case_and_boundaries(self) -> None:
        self.assertTrue(self.kill("Plongeons dans le sujet.") and self.kill("plongeons dans le sujet."))
        custom = {"fr": {"vocabulaire": [{"item": "élevé", "match": "word", "level": "blogue", "source": "x"}]}}
        self.assertTrue(self.kill("Un coût eleve.", kill_list=custom) and self.kill("Un coût ÉLEVÉ.", kill_list=custom))
        self.assertIn("assurer", [f["item"] for f in self.kill("Il faut assurer le suivi.")])
        self.assertNotIn("assurer", [f["item"] for f in self.kill("Il faut rassurer le client.")])

    def test_optional_space_before_punctuation(self) -> None:
        for text in ("Bien sûr! Voici la suite.", f"Bien sûr{NBSP}! Voici la suite.", "Bien sûr ! Voici la suite."):
            self.assertIn("ouvertures", [f["category"] for f in self.kill(text)], text)

    def test_position_rules(self) -> None:
        self.assertNotIn("ouvertures", [f["category"] for f in self.kill("On dit souvent soyons clairs. Bon.")])
        text = "En résumé, voici le plan. Une phrase. Une autre phrase. La dernière phrase ici.\n"
        self.assertEqual([f["severity"] for f in self.kill(text) if f["category"] == "clotures"], ["info"])

    def test_chat_residue_and_ignore(self) -> None:
        self.assertEqual(vh.analyze("Voici le texte. J'espère que cela vous aidera.\n", "fr")["exit_code"], 1)
        r = vh.analyze("Il faut assurer le suivi.\n", "fr", ignore=("assurer",))
        self.assertNotIn("assurer", [f["item"] for f in found(r, "kill_list")])
        self.assertEqual(r["options"]["ignore"], ["assurer"])

    def test_normalize_and_invalid_entry(self) -> None:
        norm, mapping = vh.normalize_for_match(f"Élevé{NBSP}l{RSQ}été")
        self.assertEqual((norm, len(mapping)), ("eleve l'ete", len(norm)))
        with self.assertRaises(ValueError) as ctx:
            vh.compile_kill_list({"fr": {"vocabulaire": [{"item": "mot", "match": "word", "level": "x", "source": "s"}]}})
        self.assertIn("mot", str(ctx.exception))


class TestDashes(unittest.TestCase):
    BODY = "".join(f"Ligne de contenu numéro {i}.\n\n" for i in range(12))
    FOOTER = f"*Cabinet Exemple inc. {EM} Conseil en automatisation, Québec.*\n"

    def dashes(self, text: str, kind: str = "general", **kw) -> list[tuple[str, str]]:
        return [(f["severity"], f["item"]) for f in found(vh.analyze(text, "fr", kind, **kw), "dash")]

    def first(self, text: str, kind: str = "general", **kw) -> str:
        return self.dashes(text, kind, **kw)[0][0]

    def test_footer_dash(self) -> None:
        self.assertEqual(self.dashes(self.BODY + self.FOOTER, "article"), [("info", "footer-dash")])
        meta = self.BODY + self.FOOTER + "\n## NE PAS PUBLIER\n\nNote interne.\n"
        self.assertEqual(self.dashes(meta, "article"), [("info", "footer-dash")])
        self.assertEqual(self.first(self.BODY + self.FOOTER), "error")
        self.assertEqual(self.dashes(self.BODY + self.FOOTER, allow_footer_dash=True), [("info", "footer-dash")])
        twice = self.dashes(self.BODY + self.FOOTER + "\n" + self.FOOTER, "article")
        self.assertEqual(sorted(s for s, _ in twice), ["error", "info"])

    def test_timecode_dash(self) -> None:
        text = f"[0:00{EN}0:30] Accroche du script.\n"
        self.assertEqual(self.dashes(text, "chronique"), [("info", "timecode-dash")])
        self.assertEqual(self.first(text), "error")

    def test_skip_quotes(self) -> None:
        for text in (f"> Avant {EM} exemple cité.\n", f"Il a dit « oui {EM} non » hier.\n", f'Il a dit "oui {EM} non" hier.\n'):
            self.assertEqual(self.first(text), "error", text)
            self.assertEqual(self.dashes(text, skip_quotes=True), [("info", "quote")], text)
        self.assertEqual(self.first(f'Il a dit "oui {EM} non hier.\n', skip_quotes=True), "error")

    def test_severity_by_context(self) -> None:
        self.assertEqual(self.first(f"{REGIE} Plan large {EM} musique.\n"), "warning")
        self.assertEqual(self.first(f"Texte.\n\n## NE PAS PUBLIER\n\nNote {EM} interne.\n"), "warning")
        front = f"---\ntitle: Titre {EM} test\nslug: a{EM}b\n---\n\nTexte.\n"
        self.assertEqual([s for s, _ in self.dashes(front)], ["error", "warning"])
        self.assertEqual(self.first(f"---\nmeta_description: Résumé {EN} court\n---\n\nTexte.\n"), "error")
        self.assertEqual(self.first(f"Texte.\n\n```\nx = 1 {EM} 2\n```\n"), "warning")

    def test_spaced_hyphen_and_ignore_line(self) -> None:
        self.assertEqual(self.dashes("Le geste - celui qui coûte - se mesure.\n")[0][1], "spaced-hyphen")
        self.assertEqual(self.dashes("Entre 10 - 20 courriels.\n"), [])
        r = vh.analyze(f"Titre.\n\nUn tiret {EM} ici.\n", "fr", ignore_lines=(3,))
        self.assertEqual((found(r, "dash")[0]["severity"], r["exit_code"], r["options"]["ignore_lines"]), ("info", 0, [3]))
        self.assertIn("ignored by --ignore-line", found(r, "dash")[0]["message"])


class TestChecks(unittest.TestCase):
    def test_staccato_and_rhythm(self) -> None:
        self.assertIn("warning", sev("Concret. Pratique. Efficace. Voilà ce que je propose aujourd'hui.\n", "staccato"))
        self.assertFalse(sev("Ça marche. Le reste demande une vraie mesure du geste.\n", "staccato"))
        uniform = " ".join(["Cette phrase compte six mots exactement."] * 12) + "\n"
        self.assertEqual(sev(uniform, "sentence_uniformity"), ["warning"])
        varied = " ".join(("Oui." if i % 2 else "Cette phrase est nettement plus longue que la précédente, et de loin.")
                          for i in range(12))
        self.assertFalse(sev(varied, "sentence_uniformity"))
        long_one = "Le client envoie " + " ".join(["mot"] * 29) + ".\n"  # 32 words
        self.assertEqual(sev(long_one, "long_sentence", kind="chronique"), ["warning"])
        for kind in ("article", "page_web", "formation", "general"):  # 30-word limit everywhere since 3.1.0
            self.assertEqual(sev(long_one, "long_sentence", kind=kind), ["warning"], kind)
        self.assertEqual(sev(long_one, "long_sentence", kind="publicite"), ["info"])
        self.assertFalse(sev("Le client envoie " + " ".join(["mot"] * 27) + ".\n", "long_sentence"))
        ids = {k: found(vh.analyze(long_one, "fr", k), "long_sentence")[0]["pattern_id"] for k in ("chronique", "general")}
        self.assertEqual(ids, {"chronique": "P68", "general": "P81"})

    def test_comma_load(self) -> None:
        piled = "Le système, une fois branché, lit le bon, le classe, puis prépare la facture, sans autre saisie.\n"
        self.assertEqual(sev(piled, "comma_load"), ["warning"])  # 5 commas
        self.assertEqual(sev(piled, "comma_load", kind="publicite"), ["info"])
        self.assertEqual(sev(piled, "comma_load", "en"), ["warning"])
        self.assertFalse(sev("Le système lit le bon, le classe, puis prépare la facture.\n", "comma_load"))  # 2
        self.assertFalse(sev("Les prix sont 1,5 $, 2,5 $, 3,5 $ et 4,25 $ selon le volume.\n", "comma_load"))  # decimals
        self.assertEqual(vh.analyze(piled, "fr")["stats"]["sentences"]["commas_max"], 5)

    def test_verbless(self) -> None:
        for text in ("Dix heures d'accompagnement sur un mois, sans engagement pour la suite.\n", "Pas de pitch.\n",
                     "Un prix clair pour vos trois départements.\n", "Avec la consigne, 7 sur 8.\n",
                     "Trois agents dans vos outils et à votre nom, en service en six semaines.\n"):
            self.assertEqual(sev(text, "verbless"), ["warning"], text)
            self.assertEqual(sev(text, "verbless", kind="chronique"), ["info"], text)
        for text in ("Le système prépare la pro forma.\n", "Le chef de département l'approuve avant l'envoi.\n",
                     "Vous cochez les choix retenus et vous signez juste en dessous.\n", "Dites-le-moi avant de signer.\n",
                     "Ce montant couvre toute la portée du forfait.\n", "Les travaux débutent dans les deux semaines.\n",
                     "LibreOffice, une suite gratuite, offre le même genre d'outil.\n", "Le délai la désamorce.\n",
                     "L'Agent #1 filtre le signal du bruit dès la première seconde.\n", "Surveille la boîte courriel.\n",
                     "L'urgence et l'autorité court-circuitent la prudence.\n", "Voici l'offre révisée.\n",
                     "Cet accompagnement pour PME comporte six étapes d'environ un mois.\n",
                     "La page d'aide du fournisseur le réserve toujours aux clients américains.\n"):
            self.assertFalse(sev(text, "verbless"), text)
        # Not sentences to judge: label, label and value, greeting, closing, formula, list item, heading, footer.
        for text in ("**Délais.** Les travaux débutent dans les deux semaines.\n", "Choix retenus :\n",
                     "**Validité :** jusqu'au 11 décembre 2026.\n", "Bonjour Madame Tremblay,\n\nCordialement,\n",
                     "Merci de votre confiance.\n", "- Table des tarifs par client.\n", "## Une offre claire\n",
                     "*Atelier Boréal inc., cabinet-conseil, Montréal.*\n", "Oui.\n",
                     "Le système appartient à Les Entreprises Jean T. Tremblay inc. Il reste à vous.\n"):
            self.assertFalse(sev(text, "verbless"), text)
        self.assertFalse(sev("No surprise fees.\n", "verbless", "en"))  # French only
        self.assertEqual(vh.analyze("Pas de pitch. Pas de vente.\n", "fr")["stats"]["sentences"]["verbless"], 2)

    def test_compare_sentence_form(self) -> None:
        before = "Le forfait couvre dix heures d'accompagnement, sans engagement pour la suite.\n"
        after = "Dix heures d'accompagnement sur un mois. Sans engagement pour la suite.\n"
        r = vh.analyze(after, "fr", original=before)
        self.assertEqual(r["compare"]["sentence_form"]["verbless"], {"original": 0, "output": 2})
        self.assertIn("the pass must not add any", [f["message"] for f in found(r, "verbless") if f["line"] is None][0])
        same = vh.analyze(before, "fr", original=before)
        self.assertFalse([f for f in found(same, "verbless") + found(same, "long_sentence") if f["line"] is None])

    def test_bold(self) -> None:
        self.assertIn("warning", sev("Un **point** et un **autre** et un **troisième** ici.\n", "bold_density", kind="article"))
        numeric = "Le coût est de **36 000 $** par année pour cette boîte, ce qui reste raisonnable.\n"
        self.assertFalse(sev(numeric, "bold_density", kind="article"))
        self.assertIn("warning", sev(numeric, "bold_density", kind="publicite"))
        self.assertEqual(sev("- **Vitesse :** rapide\n- **Coût :** bas\n- **Qualité :** haute\n", "inline_header_list"),
                         ["warning"])
        self.assertFalse(sev("- vitesse\n- coût\n- qualité\n", "inline_header_list"))

    def test_emoji_policy(self) -> None:
        self.assertFalse(sev(f"Écrivez-moi {POINTER} ici.\n", "emoji", kind="article"))
        self.assertEqual(sev(f"Lancement {ROCKET} demain.\n", "emoji", kind="article"), ["warning"])
        self.assertIn("error", sev(" ".join([ROCKET] * 11) + "\n", "emoji", kind="publicite"))
        self.assertIn("warning", sev("".join(f"{ROCKET} point {i}\n\n" for i in range(3)), "emoji", kind="publicite"))

    def test_quotes_and_title_case(self) -> None:
        self.assertEqual(sev(f"He said {LDQ}yes{RDQ} today.\n", "curly_quotes", "en"), ["warning", "warning"])
        self.assertFalse(sev('He said "yes" today.\n', "curly_quotes", "en"))
        self.assertEqual(sev('Il a dit "oui" hier.\n', "curly_quotes"), ["warning"])
        self.assertFalse(sev("Il a dit « oui » hier.\n", "curly_quotes"))
        self.assertEqual(sev("# How To Measure Every Repetitive Task\n", "title_case", "en"), ["warning"])
        self.assertFalse(sev("# How to measure every repetitive task\n", "title_case", "en"))
        self.assertEqual(sev("# Mesurer Chaque Tâche Avant De Payer\n", "title_case"), ["warning"])

    def test_not_x_but_y(self) -> None:
        self.assertEqual(sev("Ce n'est pas un outil, c'est une méthode. Et elle marche.\n\nSuite.\n", "not_x_but_y"),
                         ["warning"])
        self.assertEqual(sev("## Une méthode, pas un outil\n\nTexte.\n", "not_x_but_y"), ["error"])
        self.assertEqual(sev("It's not a tool, it's a method.\n", "not_x_but_y", "en"), ["warning"])
        self.assertFalse(sev("C'est le volume mensuel qui décide du prix.\n", "not_x_but_y"))

    def test_hedging_stack(self) -> None:
        self.assertEqual(sev("Cela pourrait peut-être aider.\n", "hedging_stack"), ["warning"])
        self.assertFalse(sev("Cela pourrait aider.\n", "hedging_stack"))
        self.assertFalse(sev("Choisissez plutôt que d'attendre, cela pourrait aider.\n", "hedging_stack"))

    def test_hard_wrap_and_paragraphs(self) -> None:
        wrapped = ("Ce paragraphe a été coupé à une colonne fixe par un outil\n"
                   "qui ne respecte pas la règle d'une ligne par paragraphe\n"
                   "et la suite continue encore sur cette ligne.\n")
        self.assertEqual(vh.count_paragraphs(wrapped), 1)
        self.assertEqual(sev(wrapped, "hard_wrap"), ["error", "error"])
        self.assertEqual(vh.count_paragraphs("# Titre\n\nUn.\nDeux.\n\n- a\n- b\n\n| a |\n|---|\n| b |\n"), 7)

    def test_exclamation_and_typography(self) -> None:
        bangs = sorted(found(vh.analyze("Bravo! Super! Encore!!\n", "fr"), "exclamation"), key=lambda f: f["column"])
        self.assertEqual([f["severity"] for f in bangs], ["info", "warning", "warning"])
        self.assertIn("warning", sev("Le prix est de $1300 par mois.\n", "typography_fr"))
        self.assertIn("warning", sev("Il coûte 32.50 par mois.\n", "typography_fr"))
        self.assertFalse(sev("Il coûte 32,50 $ par mois.\n", "typography_fr"))
        self.assertFalse(sev("Price is $1300.\n", "typography_fr", "en"))

    def test_numbers_normalization(self) -> None:
        self.assertEqual(vh.extract_numbers("$1300", "fr"), vh.extract_numbers(f"1{NBSP}300 $", "fr"))
        self.assertEqual(vh.extract_numbers("32.50", "fr"), vh.extract_numbers("32,50", "fr"))
        self.assertEqual(vh.extract_numbers("$0.015", "fr"), vh.extract_numbers("0,015 $", "fr"))
        self.assertEqual(vh.extract_numbers("1,300", "en"), ["1300"])
        self.assertEqual(vh.extract_numbers("À 10:30, 2,4 minutes.", "fr"), ["2.4"])

    def test_bold_numeric_and_protected_emoji(self) -> None:
        original = f"Le coût est de **36 000 $** par année.\n\nÉcrivez-moi {POINTER} ici.\n"
        output = "Le coût est de 36 000 $ par année.\n\nÉcrivez-moi ici.\n"
        r = vh.analyze(output, "fr", "article", original=original)
        self.assertEqual((r["compare"]["bold_numeric_missing"], r["compare"]["protected_emoji_missing"]), (["36000"], 1))
        self.assertTrue({"bold_numeric", "protected_emoji"} <= checks(r, "error"))
        self.assertIn("bold_numeric", checks(vh.analyze(output, "fr", "page_web", original=original), "warning"))

    def test_sections_publicite(self) -> None:
        r = vh.analyze("## LinkedIn\n\n" + "Une phrase de publicité assez ordinaire. " * 80 + "\n", "fr", "publicite")
        self.assertIn("section-length", [f["item"] for f in r["findings"]])
        short = "".join(f"## Variante {i}\n\n" + "Une phrase de publicité. " * 30 + "\n\n" for i in range(6))
        r = vh.analyze(short, "fr", "publicite")
        self.assertGreater(r["stats"]["characters"], 3000)
        self.assertNotIn("section-length", [f["item"] for f in r["findings"]])
        self.assertEqual((len(r["stats"]["sections"]), r["stats"]["sections"][0]["heading"]), (6, "Variante 0"))


class TestCorpus(unittest.TestCase):
    def test_corpus_pairs(self) -> None:
        corpus = SKILL_DIR / "evals" / "corpus"
        pairs = sorted(p for p in corpus.glob("*/*-*") if (p / "apres.md").is_file()) if corpus.is_dir() else []
        if not pairs:
            self.skipTest("evals/corpus/ absent or empty")
        for pair in pairs:
            lang, kind = pair.name.split("-", 1)[0], pair.parent.name
            with self.subTest(pair=f"{kind}/{pair.name}"):
                before = vh.read_text(str(pair / "avant.md"))
                r = vh.analyze(vh.read_text(str(pair / "apres.md")), lang, kind, original=before)
                notes = (pair / "notes.md").read_text(encoding="utf-8") if (pair / "notes.md").is_file() else ""
                declared = re.search(r"^Exemption : ([a-z_, ]+)\.?$", notes, re.M)  # comparison checks waived in notes.md
                exempt = {c.strip() for c in declared.group(1).split(",")} & {"paragraph_count", "numbers"} if declared else set()
                errors = [f["message"] for f in r["findings"] if f["severity"] == "error" and f["check"] not in exempt]
                self.assertEqual(errors, [])
                counts = vh.analyze(before, lang, kind)["counts"]
                self.assertGreater(counts["error"] + counts["warning"], 0)


class TestTree(unittest.TestCase):
    def test_no_dash_outside_exceptions(self) -> None:
        offenders = []
        for path in sorted(SKILL_DIR.rglob("*")):
            skipped = {".git", "dist", ".pytest_cache"} & set(path.relative_to(SKILL_DIR).parts)
            if not path.is_file() or skipped or path.suffix not in (".md", ".py", ".json", ".yaml", ".sh", ".txt") or \
                    path.name in ("avant.md", "kill_list.json"):
                continue
            rel, quoting = path.relative_to(SKILL_DIR).as_posix(), False
            for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
                marker = re.match(r"^\s*\*\*(Avant|Before|Après|After)\b[^*\n]*\*\*", line)
                quoting = marker.group(1) in ("Avant", "Before") if marker else quoting
                if not re.search("[" + EM + EN + "]", line) or (quoting and line.lstrip().startswith(">")):
                    continue
                if rel.startswith("evals/corpus/article/") and path.name == "apres.md" and \
                        re.match(r"^\s*[*_]+\w[^" + EM + r"\n]{0,79}?" + EM, line):
                    continue
                if rel.startswith("evals/corpus/chronique/") and re.search(r"\d:\d{2}\s*[" + EM + EN + r"]\s*\d", line):
                    continue
                offenders.append(f"{rel}:{number}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
