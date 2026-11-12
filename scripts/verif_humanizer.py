#!/usr/bin/env python3
"""verif_humanizer: deterministic checks for the humanizer skill.

Usage:
    python3 -I scripts/verif_humanizer.py FILE --lang fr|en
        [--type article|page_web|publicite|chronique|formation|general]
        [--compare ORIGINAL] [--json] [--skip-quotes] [--allow-footer-dash]
        [--ignore ITEM]... [--ignore-line N]... [--kill-list PATH] [--verbose]

FILE may be "-" (stdin). Report on stdout, logs on stderr. Exit codes: 0 no
"error" finding, 1 at least one, 2 invalid call, unreadable file or invalid
kill list. An editing aid toward the author's voice, not a detector. The kill
list may use the compiled format ("match", "level") or the raw research format
("niveau", "type"), converted at load time.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import statistics
import sys
import unicodedata
from collections import Counter
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Optional

__version__ = "3.1.0"
LOG = logging.getLogger("verif_humanizer")

# Built with chr() so the file never holds these characters literally.
EM_DASH, EN_DASH, NBSP, NNBSP = chr(0x2014), chr(0x2013), chr(0x00A0), chr(0x202F)
LDQUO, RDQUO, LSQUO, RSQUO = chr(0x201C), chr(0x201D), chr(0x2018), chr(0x2019)
ELLIPSIS, POINTER, REGIE_MARK, PROTECT = chr(0x2026), chr(0x1F449), chr(0x25B6), chr(0xE000)
DASH_CLASS = "[" + re.escape(EM_DASH + EN_DASH) + "]"
SP = "[ " + NBSP + NNBSP + "]"

CHECKS: tuple[str, ...] = (
    "dash", "kill_list", "triad", "staccato", "sentence_uniformity", "long_sentence", "comma_load", "verbless",
    "bold_density", "inline_header_list", "emoji", "curly_quotes", "title_case", "not_x_but_y", "hedging_stack",
    "hard_wrap", "exclamation", "typography_fr", "paragraph_count", "numbers", "urls", "timecodes", "headings",
    "spoken_length", "bold_numeric", "protected_emoji")
COMPARE_CHECKS = CHECKS[CHECKS.index("paragraph_count"):]
TYPES: tuple[str, ...] = ("article", "page_web", "publicite", "chronique", "formation", "general")
TYPE_ALIASES: dict[str, str] = {"page": "page_web", "page_service": "page_web", "pub": "publicite"}
SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}
CATEGORIES = ("vocabulaire", "formules", "ouvertures", "clotures", "ponctuation", "structure")
LEVELS = ("mesure", "guide", "blogue", "maison")
TEXT_KINDS = ("prose", "list", "heading", "blockquote")

# Thresholds, one row per type (type-*.md files, section 6).
_TH_KEYS = ("triads_per_1000", "staccato_run", "staccato_severity", "cv_min", "long_sentence_words",
            "long_sentence_severity", "bold_non_numeric_per_1000", "bold_numeric_exempt", "bold_any_warning",
            "inline_header_list_severity", "emoji_policy", "emoji_limit", "emoji_limit_severity",
            "exclamation_warning_from", "section_char_limit", "comma_max", "comma_severity", "verbless_severity")
# The last three columns and the 30-word limit outside chronique and publicite date from 3.1.0 (P81 to P83).
THRESHOLDS: dict[str, dict[str, object]] = {t: {"vocab_density": {"fr": 6, "en": 8}, "cv_min_sentences": 12,
                                                **dict(zip(_TH_KEYS, row))} for t, row in {
    "article": (3, 3, "warning", 0.35, 30, "warning", 4, True, False, "warning", "pointer_once", None, None, 2, None,
                3, "warning", "warning"),
    "page_web": (4, 3, "info", 0.30, 30, "warning", 8, True, False, "info", "each", None, None, 2, None,
                 3, "warning", "info"),
    "publicite": (6, 3, "info", 0.30, 25, "info", None, False, True, "warning", "limit", 10, "error", 3, 3000,
                  3, "info", "info"),
    "chronique": (3, 4, "warning", 0.40, 30, "warning", 2, False, False, "warning", "each", None, None, 3, None,
                  3, "warning", "info"),
    "formation": (4, 3, "warning", 0.30, 30, "warning", 12, True, False, "info", "limit", 3, "warning", 2, None,
                  3, "warning", "warning"),
    "general": (3, 3, "warning", 0.35, 30, "warning", 4, False, False, "warning", "each", None, None, 2, None,
                3, "warning", "warning"),
}.items()}

# Pattern IDs per check: (fr, en).
PATTERN_IDS: dict[str, tuple[Optional[str], Optional[str]]] = {
    "dash": ("P54", "P14"), "triad": ("P64", "P10"), "staccato": ("P64", "P31"), "long_sentence": ("P81", "P81"),
    "comma_load": ("P82", "P82"), "verbless": ("P83", None), "bold_density": ("P57", "P15"), "inline_header_list": ("P57", "P16"), "emoji": ("P57", "P18"),
    "curly_quotes": ("P56", "P19"), "title_case": ("P58", "P17"), "not_x_but_y": ("P63", "P09"),
    "hedging_stack": ("P61", "P24"), "exclamation": ("P72", "P72"), "typography_fr": ("P56", None),
    "vocabulaire": ("P51", "P07"), "formules": ("P50", "P23"), "ouvertures": ("P46", "P46"),
    "clotures": ("P48", "P25"), "ponctuation": ("P57", "P18"), "structure": ("P42", "P42")}
KILL_SEVERITY = {"vocabulaire": "info", "formules": "warning", "ouvertures": "warning", "clotures": "warning",
                 "ponctuation": "info", "structure": "error"}
SOURCES = {"sentence_uniformity": "references/patterns-en.md P38 and P45; SKILL.md hard rule 10",
           "hard_wrap": "SKILL.md hard rule 6",
           **{c: "SKILL.md hard rule 12; references/patterns-fr.md P81 to P83"
              for c in ("long_sentence", "comma_load", "verbless")},
           **{c: "SKILL.md hard rules 2, 5 and 7" for c in COMPARE_CHECKS}}

WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ0-9]+(?:[’'-][A-Za-zÀ-ÖØ-öø-ÿœŒ0-9]+)*")
SPLIT_RE = re.compile(r"(?<=[.!?…])\s+(?=[«\"A-ZÀ-ÖØ-Þ0-9])|(?<=:)\s+(?=[A-ZÀ-Þ])")
ABBREV_RE = re.compile(r"(?<!\w)(?:M\.|Mme\.?|p\.\s?ex\.|etc\.|c\.-à-d\.|env\.|no\.|art\.|e\.g\.|i\.e\.|Mr\.|Dr\.|"
                       r"vs\.|U\.S\.)|(?<=\d)\.(?=\d)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^\s*(?:[-*+•]|\d{1,3}[.)])\s+")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$")
TIMECODE_RE = re.compile(r"(?<!\d)\d{1,2}:\d{2}(?::\d{2})?(?!\d)")
EMOJI_RE = re.compile("[" + chr(0x1F000) + "-" + chr(0x1FAFF) + chr(0x2600) + "-" + chr(0x27BF) + chr(0x2B00) + "-"
                      + chr(0x2BFF) + "]")
BOLD_RE = re.compile(r"\*\*(?=\S)(.+?)(?<=\S)\*\*|__(?=\S)(.+?)(?<=\S)__")
FINAL_PUNCT = (".", "!", "?", ELLIPSIS, ":", "»", '"', RDQUO, ")")
MASKS = ((re.compile(r"`[^`\n]+`"), 0), (re.compile(r"\]\([^)\s]*(?:\s+\"[^\"]*\")?\)"), 1),
         (re.compile(r"https?://[^\s<>\"]+"), 0), (re.compile(r"</?[A-Za-z!][^>\n]*>"), 0))

# Raw research format conversion.
HOLE_RE = re.compile(r"\[[^\]]*\]|_{3,}|\.\.\.|" + ELLIPSIS + r"|(?<![A-Za-z])[XY](?![A-Za-z])")
DEDICATED_RE = re.compile(r"tiret|em dash|en dash|emoji|\*\*|^(?:it's|it is|this is|that's) not\b|^not (?:only|just|x)"
                          r"\b|^ce n'est pas|^pas seulement|^non seulement|^il ne s'agit pas")
CHAT_RESIDUE = frozenset((
    "as an ai language model|as of my last knowledge update|up to my last training update|i hope this helps|"
    "certainly!|en tant qu'ia|en tant qu'intelligence artificielle/qu'ia|je suis desole, je ne peux pas generer|"
    "j'espere que cela vous aidera|c'est une excellente question|expand on all areas. be more detailed and specific."
    "|utm_source=chatgpt.com|:contentreference[oaicite|sure! here is an essay in response to your prompt:").split("|"))
RAW_EXTRA = {"link in bio": {"exempt_types": ["publicite"]}, "lien en bio": {"exempt_types": ["publicite"]},
             "« foire aux questions »": {"severity": "warning"}}
INFLECT = {w: w[:-1] + "(?:e|es|ed|ing)" for w in "delve underscore showcase leverage navigate elevate streamline "
           "resonate embrace enhance grapple utilize prioritize".split()}
INFLECT.update({w: w + "(?:s|ed|ing)?" for w in "foster garner empower highlight harness".split()},
               tapestry="tapestr(?:y|ies)", boasts="boast(?:s|ed|ing)?", unravel="unravel(?:s|l?ed|l?ing)?")

_G = r"[^.!?;\n]{1,80}?"
_IT = r"(?:it|this|that)(?:'s| is| was)"
NOT_X_BUT_Y = {
    "en": [r"\b" + _IT + r"\s+not\s+(?:just\s+|only\s+|merely\s+|simply\s+)?(?:about\s+)?" + _G + r"[,;.:]\s*" + _IT
           + r"\b", r"\b(?:it|this|that)\s+(?:isn't|wasn't)\s+(?:just\s+|only\s+)?(?:about\s+)?" + _G + r"[,;.:]\s*"
           + _IT + r"\b", r"\bnot\s+(?:just|only|merely|simply)\s+" + _G + r",?\s+but\b",
           r"\bnot\s+because\s+" + _G + r",?\s+but\s+because\b", r"\bno\s+\w+(?:\s+\w+)?\.\s+(?:just|only)\s+\w+"],
    "fr": [r"\bce\s+n'est\s+pas\s+" + _G + r"[,;.:]\s*c'est\b", r"\bil\s+ne\s+s'agit\s+pas\s+" + _G
           + r"[,;.:]\s*il\s+s'agit\b", r"\bnon\s+seulement\s+[^.!?\n]{1,120}?\bmais\s+(?:aussi|egalement|encore)\b",
           r"\bpas\s+(?:seulement|juste|uniquement)\s+" + _G + r",?\s+mais\b",
           r"\bil\s+n'y\s+a\s+pas\s+(?:de\s+|d')[^.!?\n]{1,60}?\.\s+il\s+y\s+a\b"]}
FR_HEADING_OPPOSITION = re.compile(r"^\s*([^,\n]{1,60},\s+pas\s+[^,\n]{1,40}?)\s*$")
HEDGES = {"en": "may|might|could|possibly|potentially|perhaps|arguably|somewhat|likely|presumably|seemingly|it seems|"
                "appears to|to some extent|in some cases|generally|typically|tends to|relatively",
          "fr": "pourrait|pourraient|pourrions|puisse|peut-etre|possiblement|potentiellement|eventuellement|semble|"
                "semblent|il semble|semble-t-il|en quelque sorte|dans une certaine mesure|dans certains cas|"
                "generalement|relativement|plutot|susceptible|susceptibles|probablement|a priori"}
FUNCTION_WORDS = {"en": set("a an the and or but for nor of on in to at by with from as vs via is are".split()),
                  "fr": set("le la les un une des de du et ou à au aux en pour par sur dans avec sans que qui".split())}
TYPO_FR = ((r"\$\s?\d", "warning", "dollar sign before the number (write 1 300 $)"),
           (r"(?<![\w.,])(?<!section )(?<!article )(?<!chapitre )(?<!partie )(?<!version )\d+\.\d{1,2}(?![\d.])",
            "warning", "decimal point (use a decimal comma)"),
           ("«(?!" + SP + ")", "info", "no space after «"), ("(?<!" + SP + ")»", "info", "no space before »"),
           (r"(?<=[\w)»*]):(?=\s|$|\*)", "info", "no space before the colon"),
           (r" [?!;]", "info", "plain space before ? ! or ; (Quebec usage: no space)"))

# Sentence form, P81 to P83 (3.1.0). The French verb test is a heuristic built to be generous: a sentence it
# reports as verbless almost always is one, and it misses some. Reading every sentence stays the real check.
COMMA_RE = re.compile(r"(?<!\d),|,(?!\d)")
SENTENCE_END = (".", "!", "?", ELLIPSIS)
FR_TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿœŒ]+(?:['" + RSQUO + r"-][A-Za-zÀ-ÖØ-öø-ÿœŒ]+)*|\d+|[,;:()«»]")
FR_FORMULA_RE = re.compile(
    r"^(?:merci|bonjour|bonsoir|salut|bravo|félicitations|pardon|désolée?|cordialement|salutations|au plaisir|"
    r"à bientôt|à demain|à la semaine prochaine|d'accord|bien sûr|avec plaisir|bonne (?:journée|soirée|semaine|fin|"
    r"continuation|lecture|chance|écoute)|bon (?:week-end|matin|après-midi|retour|succès|courage)|joyeu(?:x|ses))\b")
FR_VERB_FORMS = frozenset((
    "suis es est sommes êtes sont étais était étions étiez étaient serai seras sera serons serez seront serais serait "
    "serions seriez seraient sois soit soyons soyez soient fut furent ai as a avons avez ont avais avait avions aviez "
    "avaient aurai auras aura aurons aurez auront aurais aurait aurions auriez auraient aie aies ait ayons ayez aient "
    "eut eurent vais vas va allons allez vont irai iras ira irons irez iront irais irait iraient aille aillent fais "
    "fait faisons faites font ferai feras fera ferons ferez feront ferais ferait feraient fasse fassent peux peut "
    "pouvons pouvez peuvent pourrai pourras pourra pourrons pourrez pourront pourrais pourrait pourraient puisse "
    "puissent veux veut voulons voulez veulent voudrai voudra voudrons voudrez voudront voudrais voudrait voudraient "
    "veuille veuillez dois doit devons devez doivent devrai devra devrons devrez devront devrais devrait devraient "
    "doive sais sait savons savez savent saurai saura saurons saurez sauront saurais saurait sache sachez vois voit "
    "voyons voyez voient verrai verra verrons verrez verront verrais verrait prévoit prévoient revoit viens vient "
    "venons venez viennent viendra viendront viendrait tiens tient tenons tenez tiennent tiendra devient deviennent "
    "revient reviennent obtient obtiennent contient contiennent maintient maintiennent retient retiennent appartient "
    "appartiennent soutient soutiennent convient conviennent parvient parviennent provient proviennent intervient "
    "interviennent prévient survient détient prends prend prenons prenez prennent prendra prendront prendrait "
    "comprends comprend comprenons comprenez comprennent apprends apprend apprennent apprenez reprend reprennent "
    "reprenez entreprend surprend mets met mettons mettez mettent mettra permet permettent permettez permettra promet "
    "promettent transmet transmettent transmettez admet soumet soumettent remet remettent émet dis dit disons dites "
    "disent dira diront dirait prédit lis lit lisons lisez lisent lira relit relisez écris écrit écrivons écrivez "
    "écrivent écrira décrit décrivent inscrit inscrivent inscrivez prescrit suit suivons suivez suivent suivra "
    "poursuit poursuivent vit vivent vivons connais connaît connaissons connaissez connaissent paraît paraissent "
    "apparaît apparaissent disparaît disparaissent reconnaît reconnaissent naît crois croit croyons croyez croient "
    "boit boivent reçois reçoit recevons recevez reçoivent recevra recevrez recevront aperçoit conçoit conçoivent "
    "perçoit perçoivent pars part partons partez partent sors sort sortons sortez sortent sers sert servons servez "
    "servent sent sentons sentez sentent dort dorment repart ressort ressent ouvre ouvrent ouvrons ouvrez couvre "
    "couvrent couvrons couvrez découvre découvrent souffre souffrent réponds répond répondent répondons répondez "
    "répondra attends attend attendent attendons attendez entends entend entendent rend rendent rendons rendez vend "
    "vendent vendons vendez perd perdent perdons perdez dépend dépendent correspond correspondent descend descendent "
    "défend défendent étend étendent tend tendent prétend suspend confond résout résolvent rejoint rejoignent "
    "joignent joignez atteint atteignent craint craignent produisent produisons réduit réduisent conduit conduisent "
    "construit construisent traduit traduisent introduit introduisent déduit déduisent suffit suffisent plaît "
    "plaisent vaut valent vaudra vaudrait faut faudra faudrait fallait inclut incluent conclut concluent exclut "
    "excluent courent parcourt parcourent meurt meurent finit choisit réussit fournit remplit établit définit "
    "garantit agit réagit réfléchit investit réunit saisit convertit grandit ralentit aboutit avertit bâtit élargit "
    "enrichit franchit subit unit vieillit obéit rétablit répartit raccourcit alourdit éclaircit voici voilà").split())
# Third person singular of common -er verbs. Many are also nouns or adjectives ("facture", "ferme"), so they count
# as a verb only when no determiner, preposition or number comes right before.
FR_ER_FORMS = frozenset((
    "accepte accompagne accorde accélère achète active adapte additionne adresse affiche affirme agrège aide ajoute "
    "ajuste alerte alimente allège alloue améliore amène analyse annonce annule anticipe appelle applique apporte "
    "apprécie approuve appuie archive arrête arrive assemble assigne associe assume assure attache attire attribue "
    "augmente autorise automatise avance avise baisse bascule bloque boucle branche brise cache calcule calibre cause "
    "centralise cesse change charge cherche chiffre cible circule cite clarifie classe clique coche code collabore "
    "collecte combine commande commence communique compare compense compile complète complique compose compte "
    "concentre concerne confie configure confirme connecte conseille conserve considère consigne consiste consolide "
    "consomme constate constitue consulte contacte continue contribue contrôle convoque copie corrige coupe coûte "
    "crée croise cumule date déborde débute décide déclare déclenche décompose découpe dégage délègue demande démarre "
    "démontre dépasse dépense déplace dépose désigne dessine détaille détecte détermine développe devine dicte "
    "diffère diffuse diminue dirige discute dispose distingue distribue divise documente domine donne double doute "
    "dresse dure échange échappe éclaire économise écoute écrase édite efface effectue élimine émane embarque emploie "
    "emporte encadre enchaîne engage enlève enregistre enseigne entraîne entre envoie épargne équilibre équipe essaie "
    "estime étale étudie évalue évite évolue examine exécute exerce exige existe explique exploite explore exporte "
    "expose exprime facilite facture fausse ferme figure filtre finance fixe fonctionne fonde force forme formule "
    "frappe fusionne gagne garde génère gère glisse gonfle groupe guide habite hésite identifie ignore illustre "
    "imagine implique importe impose imprime indique influence informe initie injecte inspire installe intègre "
    "interroge invite isole jette joue juge justifie laisse lance libère lie limite liste livre localise loge loue "
    "manipule manque marche marque masque mène mentionne mérite mesure migre mobilise modifie monte montre multiplie "
    "navigue nécessite négocie nettoie nomme normalise note notifie numérise numérote observe occupe offre opère optimise "
    "ordonne organise oriente oublie paie parle partage participe passe paye pense perdure persiste pèse pilote place "
    "planifie plafonne porte pose possède pousse pratique précède précise préfère prépare présente préserve presse "
    "prête priorise procure profite programme progresse projette prolonge propose protège prouve provoque publie "
    "quitte raconte rajoute ramène range rappelle rapporte rapproche rassemble rassure rate rattache réalise "
    "recalcule recense recherche réclame recommande recopie récupère rédige redonne réfère reflète refuse regarde "
    "regroupe règle rejette relance relève relie remarque rembourse remonte remplace rencontre renforce renouvelle "
    "renseigne rentre renvoie répare répète réplique repose représente réserve résiste respecte ressemble reste "
    "résume retarde retire retourne retrouve réutilise révèle révise risque roule saute sauve sauvegarde scanne "
    "sélectionne semble sépare signale signe signifie simplifie simule situe sollicite sonne souhaite soulève "
    "souligne stocke structure subsiste suggère supporte suppose supprime surveille synchronise tarde télécharge "
    "téléverse termine teste tire tombe touche tourne trace traite transfère transforme travaille traverse trie "
    "trompe trouve tue unifie utilise valide varie vérifie verse veille vide vise visite vote achève atteste capte "
    "comporte consacre découle dénote désactive désamorce écarte élève émerge encourage engendre englobe entame "
    "entoure épuise expédie favorise fige freine gaspille gêne grimpe hausse héberge incarne incite incombe insiste "
    "lève mêle mise motive néglige nuance occasionne oppose pénalise plaide plonge prime prive puise raccorde "
    "rallonge rattrape recule redresse relâche rémunère renonce repère repousse résulte retombe sature serre "
    "soigne suscite surcharge surestime témoigne tolère tranche transite transporte triple valorise vante "
    "verrouille voyage").split())
FR_VERB_SUFFIX_RE = re.compile(r"(?:ez|ait|aient|rais|rai|ront|rons|era|ira|dra|vra|rra|ura|issons|issent)$")
FR_NOT_VERB = frozenset((
    "assez chez nez rez forfait lait trait portrait souhait extrait retrait attrait parfait bienfait méfait abstrait "
    "distrait front affront vrai frais marais patrons environs citrons poissons boissons frissons buissons client "
    "patient ingrédient récent différent présent absent urgent agent argent talent accident incident précédent "
    "excellent évident fréquent permanent pertinent cohérent content lent dent vent cent souvent parent "
    "transparent apparent concurrent président prudent intelligent compétent latent contingent "
    "continent adolescent innocent décent violent accent couvent torrent orient").split())
FR_MENT_VERBS = frozenset(("aiment estiment ferment confirment forment nomment résument consomment expriment "
                           "impriment suppriment transforment informent réclament programment affirment calment "
                           "animent compriment déforment priment sèment").split())
FR_SUBJECTS = frozenset("je tu il elle on ils elles ça cela ceci qui ne se".split())
FR_INVERTED = frozenset("je tu il elle on nous vous ils elles moi toi le la les lui leur y en ce t".split())
FR_PREPOSITIONS = frozenset("à de pour avec sans chez par sur sous vers entre selon contre devant derrière "
                            "envers parmi malgré".split())
FR_DETERMINERS = frozenset("le la les un une des du ce cet cette ces mon ma mes ton ta tes son sa ses notre nos "
                           "votre vos leur leurs chaque plusieurs quelques tout toute tous toutes".split())
FR_NOUN_CONTEXT = FR_DETERMINERS | FR_PREPOSITIONS | frozenset(
    "l d au aux quel quelle quels quelles aucun aucune dans depuis pendant avant après dès comme seul "
    "seule même autre autres premier première dernier dernière nouveau nouvelle bon bonne grand grande petit petite "
    "prochain prochaine deux trois quatre cinq six sept huit neuf dix".split())
FR_NUMBER_WORDS = frozenset("deux trois quatre cinq six sept huit neuf dix cent mille".split())
CUT_END_RE = re.compile(r"(?:(?:^|[\s.])[A-ZÀ-Þ]|\b(?:inc|ltée|enr|ltd|corp|janv|févr|sept|oct|nov|déc))\.$")


def _is_verb_fr(word: str, prev: str, nxt: str, raw: str) -> bool:
    """One lowercase French word: a conjugated form, by list, by ending, or by its place in the clause.

    prev is the previous word, "" at the start of a clause, "," after a comma, a closing bracket or quote, or a
    number: there a word in -e counts only when its object follows ("…, offre le même outil").
    """
    if word in FR_VERB_FORMS:
        return word != "a" or raw.endswith("a")  # the letter in "Option A" is not the verb
    if len(word) >= 4 and word not in FR_NOT_VERB:
        if word.endswith("ent"):
            if word in FR_MENT_VERBS or not word.endswith("ment"):
                return True
        elif FR_VERB_SUFFIX_RE.search(word):
            return True
    if prev in FR_NOUN_CONTEXT or not word.endswith("e") or len(word) < 5:
        return word in FR_ER_FORMS and prev not in FR_NOUN_CONTEXT and prev not in ("", ",")
    if prev == "":  # "Surveille la boîte."
        return word in FR_ER_FORMS and nxt in FR_DETERMINERS
    followed = nxt in FR_DETERMINERS or nxt in FR_NUMBER_WORDS or nxt.isdigit()  # "prépare la", "comporte six"
    return followed if prev == "," else followed or word in FR_ER_FORMS


def has_finite_verb_fr(sentence: str) -> bool:
    """True when a French sentence seems to hold a conjugated verb (heuristic, P83)."""
    tokens = [t.replace(RSQUO, "'") for t in FR_TOKEN_RE.findall(sentence)]
    prev, pending = "", False  # previous word of the clause; a subject or "ne" waiting for its verb
    for index, raw in enumerate(tokens):
        low = raw.lower()
        if not low[0].isalpha():
            prev, pending = ("," if low.isdigit() or low in ",)»" else ""), pending and low.isdigit()
            continue
        if pending:
            return True
        nxt = tokens[index + 1].lower() if index + 1 < len(tokens) else ""
        nxt = "le" if nxt.startswith("l'") else nxt
        head, _, rest = low.partition("'")
        if rest:  # elision: j'utilise, n'est, s'ajoute, qu'il, l'approuve, d'abord
            if head in ("j", "n", "m", "t") or (head == "s" and rest not in ("il", "ils")):
                return True
            if rest in FR_SUBJECTS:
                prev, pending = rest, True
                continue
            low, prev = rest, {"d": "de", "l": prev}.get(head, "que")
        if "-" in low:  # inversion or imperative with a pronoun: dites-le-moi, est-ce, peut-on
            parts = low.split("-")
            if low != "rendez-vous" and all(part in FR_INVERTED for part in parts[1:]):
                return True
            if _is_verb_fr(parts[-1], "le", "", parts[-1]):  # "court-circuitent": lists and endings only
                return True
            prev = low
            continue
        if low in FR_SUBJECTS or (low in ("nous", "vous") and prev not in FR_PREPOSITIONS):
            prev, pending = low, True
            continue
        before = tokens[index - 2].lower() if index >= 2 else ""
        if (prev in ("le", "la", "les") and low in FR_ER_FORMS and before[:1].isalpha()
                and before not in FR_NOUN_CONTEXT and before not in ("et", "ou", "ni", "mais")):
            return True  # object pronoun, then the verb: "Le délai la désamorce."
        if _is_verb_fr(low, prev, nxt, raw[-len(low):]):
            return True
        prev = low
    return False


@dataclass
class Line:
    """A line and its class."""
    number: int
    text: str
    base: str = ""
    meta: bool = False
    level: int = 0

    @property
    def kind(self) -> str:
        return "meta_block" if self.meta and self.base not in ("frontmatter", "code", "html_comment") else self.base


@dataclass
class Sentence:
    """A sentence on one line; start and end are 0-based columns."""
    line: int
    start: int
    end: int
    words: int
    unit: Optional[int]
    section: int
    kind: str


# ---------------------------------------------------------------- text helpers

def prepare_text(text: str) -> str:
    """NFC and LF line endings."""
    return unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")


def read_text(path: str) -> str:
    """Read a file, or stdin for "-", as UTF-8 (BOM tolerated)."""
    return prepare_text((sys.stdin.buffer.read() if path == "-" else Path(path).read_bytes()).decode("utf-8-sig"))


def normalize_for_match(text: str) -> tuple[str, list[int]]:
    """Casefolded, accent-free text, straight apostrophes, plain spaces; plus a map to source columns."""
    out: list[str] = []
    mapping: list[int] = []
    for index, char in enumerate(text):
        if char in (RSQUO, LSQUO, chr(0x02BC)):
            char = "'"
        elif char in (NBSP, NNBSP):
            char = " "
        pieces = "".join(c for c in unicodedata.normalize("NFD", char) if unicodedata.category(c) != "Mn").casefold()
        out.append(pieces)
        mapping.extend([index] * len(pieces))
    return "".join(out), mapping


def _norm(text: str) -> str:
    return normalize_for_match(text)[0]


def _blank(match: "re.Match[str]") -> str:
    return " " * len(match.group(0))


def mask_line(text: str) -> str:
    """Blank inline code, link targets, URLs and HTML tags, keeping columns."""
    for regex, keep in MASKS:
        text = regex.sub(lambda m: m.group(0)[:keep] + " " * (len(m.group(0)) - keep), text)
    return text


def neutralize(text: str, kind: str) -> str:
    """Masked line without structural markers and emphasis marks (same length)."""
    text = mask_line(text)
    if kind == "heading":
        text = re.sub(r"^\s*#+", _blank, text)
    elif kind in ("list", "blockquote"):
        text = LIST_RE.sub(_blank, re.sub(r"^\s*(?:>\s?)+", _blank, text), count=1)
    return re.sub(r"(?<!\w)_+|_+(?!\w)", _blank, re.sub(r"[*`]", " ", text))


def ends_with_final_punct(text: str) -> bool:
    return text.rstrip().rstrip("*_`").rstrip().endswith(FINAL_PUNCT)


def sentence_spans(text: str) -> list[tuple[int, int, int]]:
    """Sentences of a neutralized line as (start, end, word count); abbreviations and decimals protected."""
    protected = ABBREV_RE.sub(lambda m: m.group(0).replace(".", PROTECT), text)
    spans, position = [], 0
    for bound in [m.start() for m in SPLIT_RE.finditer(protected)] + [len(text)]:
        seg = text[position:bound]
        if WORD_RE.search(seg):
            spans.append((position + len(seg) - len(seg.lstrip()), position + len(seg.rstrip()), len(WORD_RE.findall(seg))))
        position = bound
    return spans


# ---------------------------------------------------------------- classification

def _basic_class(text: str) -> tuple[str, int]:
    s, heading = text.strip(), HEADING_RE.match(text)
    for kind, hit in (("blank", not s), ("rule", re.match(r"^\s{0,3}(?:(?:-\s*){3,}|(?:\*\s*){3,}|(?:_\s*){3,})$", text)),
                      ("heading", heading), ("table", s.startswith("|")), ("blockquote", s.startswith(">")),
                      ("list", LIST_RE.match(text)), ("regie", s.startswith(REGIE_MARK)),
                      ("timecode", re.match(r"^\s*\[?\d{1,2}:\d{2}", text))):
        if hit:
            return kind, len(heading.group(1)) if kind == "heading" else 0
    return "prose", 0


def classify_lines(text: str) -> list[Line]:
    """Classify every line; a thematic break is class "rule" and is not a paragraph."""
    lines = [Line(i + 1, t) for i, t in enumerate(text[:-1].split("\n") if text.endswith("\n") else text.split("\n"))]
    start = 0
    if lines and lines[0].text.strip() == "---":
        end = next((j for j in range(1, len(lines)) if lines[j].text.strip() in ("---", "...")), None)
        for line in lines[:end + 1] if end else []:
            line.base, start = "frontmatter", end + 1
    fence: Optional[str] = None
    in_comment = False
    for line in lines[start:]:
        opening = re.match(r"^\s*(```|~~~)", line.text)
        if fence is not None or opening:
            line.base = "code"
            if fence is None:
                fence = opening.group(1)
            elif line.text.strip().startswith(fence):
                fence = None
        elif in_comment or line.text.lstrip().startswith("<!--"):
            line.base = "html_comment"
            in_comment = "-->" not in (line.text if in_comment else line.text.split("<!--", 1)[1])
        else:
            line.base, line.level = _basic_class(line.text)
    meta: Optional[int] = None
    for line in lines:
        if line.base in ("frontmatter", "code", "html_comment"):
            continue
        if meta is not None and line.base == "heading" and line.level <= meta:
            meta = None
        if meta is None and re.search("ne pas publier|do not publish", line.text, re.IGNORECASE):
            meta = line.level if line.base == "heading" else 6  # a plain marker line ends at any heading
        line.meta = meta is not None
    return lines


def paragraph_units(lines: list[Line]) -> tuple[list[list[int]], dict[int, int]]:
    """Paragraph units as lists of line numbers, and line number to unit index."""
    units: list[list[int]] = []
    line_to_unit: dict[int, int] = {}
    prose_open = False
    for line in lines:
        if line.base in ("frontmatter", "code", "html_comment", "blank", "rule") or \
                (line.base == "table" and TABLE_SEP_RE.match(line.text)):
            prose_open = False
            continue
        if line.base == "prose" and prose_open:
            units[-1].append(line.number)
        else:
            units.append([line.number])
        prose_open = line.base == "prose" and not ends_with_final_punct(line.text)
        line_to_unit[line.number] = len(units) - 1
    return units, line_to_unit


def count_paragraphs(text: str) -> int:
    """Number of paragraph units (hard rule 5)."""
    return len(paragraph_units(classify_lines(prepare_text(text)))[0])


def extract_numbers(text: str, lang: str) -> list[str]:
    """Numbers written in digits, normalized with Decimal (timecodes and URLs excluded)."""
    fr = lang == "fr"
    pattern = r"(?<![\w.,])\d+" + (r"(?:" + SP + r"\d{3}(?!\d))*(?:[.,]\d+)*" if fr else r"(?:,\d{3}(?!\d))*(?:\.\d+)?")
    found: list[str] = []
    for match in re.finditer(pattern, TIMECODE_RE.sub(_blank, "\n".join(map(mask_line, prepare_text(text).split("\n"))))):
        token = re.sub(SP, "", match.group(0))
        if fr and not token.startswith("0."):  # "0.015" is a decimal, never a thousands group
            token = re.sub(r"\.(?=\d{3}(?!\d))", "", token)
        token = token.replace(",", ".") if fr else token.replace(",", "")
        try:
            found.append(format(Decimal(token).normalize(), "f"))
        except InvalidOperation:
            LOG.debug("number not parsed: %r", token)
    return found


# ---------------------------------------------------------------- kill list

def _literal_regex(segment: str) -> str:
    """Regex for a normalized segment: flexible spaces, optional space before ! ? ; :."""
    out = re.sub(r"\s+", r"\\s+", re.escape(re.sub(r"\s+", " ", segment)).replace("\\ ", " "))
    return re.sub(r"(?:\\s\+)?(\\?[!?;:])", r"\\s?\1", out)


def _word_pattern(item: str) -> str:
    """Word-bounded regex; holes ([...], X, ___, ...) become bounded gaps."""
    parts = [_norm(p) for p in HOLE_RE.split(item)]
    text = "\0".join(parts).strip()
    body = r"[^.!?\n]{1,80}?".join(_literal_regex(p) for p in parts)
    return (r"(?<!\w)" if text[:1].isalnum() else "") + body + (r"(?!\w)" if text[-1:].isalnum() else "")


def _convert_raw(entry: dict[str, Any], lang: str, category: str) -> Optional[dict[str, Any]]:
    """Convert a raw research entry to the compiled format; None means skip."""
    item, note = entry["item"].strip(), entry.get("note")
    gloss = re.match(r"^(.*?\S)\s*\(([^()]*)\)\s*$", item)
    if gloss:
        item, note = gloss.group(1).strip(), gloss.group(2).strip()
    if entry.get("type") == "description" or DEDICATED_RE.search(_norm(item)):
        return None
    item = re.sub(r"^(?:fl[eè]che|symbole)\s+(?=\S+$)", "", item, flags=re.IGNORECASE)
    norm = _norm(item)
    out = {"item": item, "match": "word", "level": entry.get("niveau", entry.get("level")),
           "source": entry.get("source"), "note": note}
    if re.search(r"[=→{}<>@#]|^[:?]", item):
        out.update(item=re.sub(r":\d+\]\{index=\d+\}$", "", item).lstrip("?"), match="literal")
    elif HOLE_RE.search(item):
        out.update(match="regex", pattern=_word_pattern(item))
    elif lang == "en" and category == "vocabulaire" and norm in INFLECT:
        out.update(match="regex", pattern=r"(?<!\w)" + INFLECT[norm] + r"(?!\w)")
    final = _norm(out["item"])
    if final in CHAT_RESIDUE or norm in CHAT_RESIDUE:
        out["severity"] = "error"
    out.update(RAW_EXTRA.get(final, {}))
    return out


def compile_kill_list(data: dict[str, Any]) -> dict[str, Any]:
    """Validate and compile a kill list (compiled or raw format); ValueError names the faulty entry."""
    if not isinstance(data, dict):
        raise ValueError("kill list root must be a JSON object")
    compiled: dict[str, Any] = {"_compiled": True, "fr": [], "en": []}
    for lang in ("fr", "en"):
        for category, entries in (data.get(lang) or {}).items():
            if category not in CATEGORIES or not isinstance(entries, list):
                raise ValueError(f"kill list {lang}: unknown category {category!r} or not a list")
            for entry in entries:
                where = f"{lang}/{category} entry {entry.get('item') if isinstance(entry, dict) else entry!r}"
                if not isinstance(entry, dict) or not isinstance(entry.get("item"), str) or not entry["item"].strip():
                    raise ValueError(f"{where}: missing or empty 'item'")
                if "match" not in entry and (entry := _convert_raw(entry, lang, category)) is None:
                    continue
                kind, severity, exempt = entry.get("match"), entry.get("severity"), entry.get("exempt_types") or []
                if entry.get("level") not in LEVELS or not entry.get("source"):
                    raise ValueError(f"{where}: 'level' must be one of {', '.join(LEVELS)} and 'source' is required")
                if kind not in ("word", "literal", "regex") or (kind == "regex" and not entry.get("pattern")) or \
                        (severity is not None and severity not in SEVERITY_ORDER) or not isinstance(exempt, list):
                    raise ValueError(f"{where}: invalid 'match', 'pattern', 'severity' or 'exempt_types'")
                item = entry["item"].strip()
                pattern = {"regex": entry.get("pattern"), "literal": re.escape(_norm(item))}.get(kind) or \
                    _word_pattern(item)
                try:
                    regex = re.compile(pattern, re.IGNORECASE)
                except re.error as exc:
                    raise ValueError(f"{where}: invalid regex {pattern!r}: {exc}") from exc
                compiled[lang].append({**entry, "item": item, "norm": _norm(item), "category": category,
                                       "regex": regex, "exempt_types": [TYPE_ALIASES.get(t, t) for t in exempt]})
        compiled[lang].sort(key=lambda e: (-len(e["norm"]), e["norm"]))  # "crucial role" before "crucial"
    return compiled


_DEFAULT: dict[str, Any] = {}


def load_kill_list(path: "Path | None" = None) -> dict[str, Any]:
    """Load and compile a kill list (default: kill_list.json next to this script)."""
    if path is None and _DEFAULT:
        return _DEFAULT
    target = Path(path) if path is not None else Path(__file__).resolve().parent / "kill_list.json"
    compiled = compile_kill_list(json.loads(target.read_text(encoding="utf-8-sig")))
    return _DEFAULT.update(compiled) or compiled if path is None else compiled


# ---------------------------------------------------------------- analyzer

class Analyzer:
    """Run every check, and the comparison with the original, on one text."""

    def __init__(self, text: str, lang: str, content_type: str, original: Optional[str], skip_quotes: bool,
                 allow_footer_dash: bool, ignore: tuple[str, ...], ignore_lines: tuple[int, ...],
                 kill_list: Optional[dict[str, Any]]) -> None:
        content_type = TYPE_ALIASES.get(content_type, content_type)
        if lang not in ("fr", "en") or content_type not in TYPES:
            raise ValueError(f"unsupported lang {lang!r} or type {content_type!r}")
        self.text, self.lang, self.type, self.li = prepare_text(text), lang, content_type, int(lang == "en")
        self.th = THRESHOLDS[content_type]
        self.original = None if original is None else prepare_text(original)
        self.skip_quotes, self.allow_footer_dash = skip_quotes, allow_footer_dash or content_type == "article"
        self.ignore, self.ignore_lines = tuple(ignore), tuple(ignore_lines)
        kill_list = load_kill_list() if kill_list is None else kill_list
        self.kill_list = kill_list = kill_list if kill_list.get("_compiled") else compile_kill_list(kill_list)
        ignored = {_norm(i).strip() for i in self.ignore}
        self.entries = [e for e in kill_list[lang] if e["norm"] not in ignored and content_type not in e["exempt_types"]]
        self.lines = classify_lines(self.text)
        self.by_number = {line.number: line for line in self.lines}
        self.units, self.line_to_unit = paragraph_units(self.lines)
        self.findings: list[dict[str, Any]] = []
        self.sections: list[dict[str, Any]] = [{"heading": None, "line": 1, "lines": []}]
        self.sentences: list[Sentence] = []
        self.line_sentences: dict[int, list[int]] = {}
        self.unit_sentences: dict[Optional[int], list[int]] = {}
        self.section_sentences: dict[int, list[int]] = {}
        for line in self.lines:
            if line.base == "heading":
                if not self.sections[-1]["lines"] and self.sections[-1]["heading"] is None:
                    self.sections.pop()
                self.sections.append({"heading": HEADING_RE.match(line.text).group(2), "line": line.number, "lines": []})
            elif line.kind not in ("frontmatter", "html_comment", "meta_block"):
                self.sections[-1]["lines"].append(line)
            for start, end, words in sentence_spans(neutralize(line.text, line.base)) if line.kind in TEXT_KINDS else []:
                unit, section, index = self.line_to_unit.get(line.number), len(self.sections) - 1, len(self.sentences)
                self.sentences.append(Sentence(line.number, start, end, words, unit, section, line.kind))
                for key, table in ((line.number, self.line_sentences), (unit, self.unit_sentences),
                                   (section, self.section_sentences)):
                    table.setdefault(key, []).append(index)
        self.stat_sentences = [s for s in self.sentences if s.kind in ("prose", "list")]
        self.words = sum(len(WORD_RE.findall(neutralize(l.text, l.base))) for l in self.lines
                         if l.kind in ("prose", "list"))

    def per1000(self, count: float) -> float:
        return count * 1000 / self.words if self.words else 0.0

    def text_lines(self, tables: bool = False) -> list[Line]:
        """Lines whose prose is analyzed; blockquotes skipped with --skip-quotes; table rows on request."""
        kinds = TEXT_KINDS[:3] + (() if self.skip_quotes else ("blockquote",))
        return [l for l in self.lines if l.kind in kinds or (tables and l.kind == "table"
                                                              and not TABLE_SEP_RE.match(l.text))]

    def sentence_at(self, line: int, column: int) -> Optional[int]:
        indexes = self.line_sentences.get(line, [])
        found = [i for i in indexes if self.sentences[i].start <= column < max(self.sentences[i].end,
                                                                               self.sentences[i].start + 1)]
        return (found or indexes or [None])[-1] if not found else found[0]

    def add(self, check: str, severity: str, line: Optional[int], column: Optional[int], message: str,
            item: Optional[str] = None, category: Optional[str] = None, pattern_id: Any = "default",
            level: Optional[str] = None, source: Optional[str] = None) -> None:
        excerpt = paragraph = None
        if line is not None:
            start = max(0, (column or 1) - 41)
            excerpt = self.by_number[line].text[start:start + 80].strip()
            unit = self.line_to_unit.get(line)
            paragraph = None if unit is None else unit + 1
            if line in self.ignore_lines:
                message, severity = f"ignored by --ignore-line (was {severity}: {message})", "info"
        self.findings.append({
            "id": 0, "check": check, "severity": severity, "line": line, "column": column, "paragraph": paragraph,
            "excerpt": excerpt, "message": message, "item": item, "category": category,
            "pattern_id": PATTERN_IDS.get(check, (None, None))[self.li] if pattern_id == "default" else pattern_id,
            "level": level, "source": source or SOURCES.get(check)})

    # 1. dash
    def footer_line(self) -> Optional[tuple[int, int]]:
        """(line, 0-based column) of the footer-dash signature: an emphasized line (*Firm name, em dash, tagline*)
        whose em dash comes within its first 80 characters; last match in the last quarter of non-code lines."""
        lines = [l for l in self.lines if l.base != "code"]
        found = None
        for line in lines[int(len(lines) * 0.75):]:
            lead = re.match(r"^\s*[*_]+", line.text)
            norm, mapping = normalize_for_match(line.text[lead.end():] if lead else "")
            hit = re.match(r"\s*\w[^" + EM_DASH + r"\n]{0,79}?" + EM_DASH, norm)
            if lead and hit:
                found = (line.number, lead.end() + mapping[hit.end() - 1])
        return found

    def check_dash(self) -> None:
        footer = self.footer_line() if self.allow_footer_dash else None
        key, chronique = "", self.type == "chronique"
        for line in self.lines:
            n, text = line.number, line.text
            if line.base == "frontmatter" and re.match(r"^\s*[A-Za-z_][\w-]*\s*:", text):
                key = text.split(":", 1)[0].strip().lower()
            ranges = [m.span() for m in re.finditer(r"\d{1,2}:\d{2}(?::\d{2})?\s*" + DASH_CLASS + r"\s*\d{1,2}:\d{2}",
                                                    text)] if chronique else []
            quotes = [m.span() for m in re.finditer("«[^»\n]*»|\"[^\"\n]*\"|" + LDQUO + "[^" + RDQUO + "\n]*" + RDQUO,
                                                    text)] if self.skip_quotes else []
            for match in re.finditer(DASH_CLASS, text):
                col, name = match.start(), "U+2014" if match.group(0) == EM_DASH else "U+2013"
                exception = "footer-dash" if footer == (n, col) else "timecode-dash" if any(
                    a <= col < b for a, b in ranges) else "quote" if self.skip_quotes and (
                    line.kind == "blockquote" or any(a < col < b for a, b in quotes)) else None
                if exception:
                    self.add("dash", "info", n, col + 1, f"declared exception {exception}", exception)
                elif line.base == "frontmatter":
                    self.add("dash", "error" if key in ("title", "meta_description") else "warning", n, col + 1,
                             f"{name} in front matter field '{key}'")
                elif line.kind in ("code", "regie", "meta_block"):
                    self.add("dash", "warning", n, col + 1, f"{name} in a {line.kind} line")
                else:
                    self.add("dash", "error", n, col + 1, f"{name} outside declared exceptions")
            for match in re.finditer(r"(?<=\S) - (?=\S)", mask_line(text)) if line.kind == "prose" else []:
                if not (text[match.start() - 1].isdigit() and text[match.end()].isdigit()):
                    self.add("dash", "warning", n, match.start() + 2, "spaced hyphen used as a dash", "spaced-hyphen")

    # 2. kill list
    def check_kill_list(self) -> None:
        self.kill_counts = Counter({c: 0 for c in CATEGORIES})
        unit_vocab: dict[int, set[str]] = {}
        for line in self.text_lines(tables=True):
            views = {False: normalize_for_match(mask_line(line.text)), True: normalize_for_match(line.text)}
            taken: list[tuple[int, int]] = []
            for e in self.entries:
                norm, mapping = views[e["match"] == "literal"]
                for match in e["regex"].finditer(norm):
                    start, end = match.span()
                    cat, col = e["category"], mapping[start] if end > start else 0
                    if end <= start or any(start < b and a < end for a, b in taken):
                        continue
                    if cat == "ouvertures":
                        rest = norm[max(norm.rfind(c, 0, start) for c in ".!?:" + ELLIPSIS) + 1:start]
                        if not re.fullmatch(r"[^\w,;]*(?:\d{1,3}[.)])?[^\w,;]*", rest):
                            continue
                    severity = e.get("severity") or KILL_SEVERITY[cat]
                    index = self.sentence_at(line.number, col) if cat == "clotures" and not e.get("severity") else None
                    if index is not None:
                        s = self.sentences[index]
                        if index not in self.unit_sentences.get(s.unit, [])[-2:] + self.section_sentences[s.section][-2:]:
                            severity = "info"
                    taken.append((start, end))
                    self.kill_counts[cat] += 1
                    if cat == "vocabulaire" and line.number in self.line_to_unit:
                        unit_vocab.setdefault(self.line_to_unit[line.number], set()).add(e["norm"])
                    pid = e.get("pattern_id") or PATTERN_IDS[cat][self.li]
                    note = f" [{e['note']}]" if e.get("note") else ""
                    self.add("kill_list", severity, line.number, col + 1, f"{cat}: \"{e['item']}\" ({pid}, "
                             f"{e['level']}){note}", e["item"], cat, pid, e["level"], e["source"])
        pid, limit = PATTERN_IDS["vocabulaire"][self.li], self.th["vocab_density"][self.lang]
        self.vocab_density = self.per1000(self.kill_counts["vocabulaire"])
        if self.vocab_density > limit:
            self.add("kill_list", "warning", None, None, f"vocabulary density {self.vocab_density:.1f} per 1000 words "
                     f"above {limit}", "density", "vocabulaire", pid)
        for unit, items in sorted(unit_vocab.items()):
            if len(items) >= 3:
                self.add("kill_list", "warning", self.units[unit][0], 1, f"{len(items)} vocabulary items in one "
                         f"paragraph: {', '.join(sorted(items))}", "cluster", "vocabulaire", pid)

    # 3. triads
    def check_triads(self) -> None:
        elem = r"(\w[\w'-]*(?:\s+\w[\w'-]*){0,3})"
        regex = re.compile(r"(?<![\w'-])(?<!, )(?<!,)" + elem + r",\s+" + elem + r",?\s+" + (
            "(?:et|ou)" if self.lang == "fr" else "(?:and|or)") + r"\s+" + elem + r"(?![\w'-])")
        hits = []
        for line in self.text_lines():
            norm, mapping = normalize_for_match(neutralize(line.text, line.base))
            hits += [(line.number, mapping[m.start()] + 1, self.line_to_unit.get(line.number), m.group(0))
                     for m in regex.finditer(norm) if not all(re.fullmatch(r"[\d\s.,]+", p) for p in m.groups())]
        per_unit = Counter(h[2] for h in hits)
        for n, col, unit, text in hits:
            self.add("triad", "warning" if unit is not None and per_unit[unit] >= 2 else "info", n, col,
                     f"three-item list: \"{text}\"")
        self.triad_count, density = len(hits), self.per1000(len(hits))
        if density > self.th["triads_per_1000"]:
            self.add("triad", "warning", None, None, f"triad density {density:.1f} per 1000 words above "
                     f"{self.th['triads_per_1000']}")

    # 4 to 6. rhythm
    def check_rhythm(self) -> None:
        run: list[Sentence] = []
        previous = 0
        for s in self.sentences + [Sentence(0, 0, 0, 99, None, 0, "end")]:
            gap = {self.by_number[n].kind for n in range(previous + 1, s.line)} - {"blank", "prose"}
            if s.kind != "prose" or s.words > 3 or gap:
                if len(run) >= self.th["staccato_run"]:
                    self.add("staccato", str(self.th["staccato_severity"]), run[0].line, run[0].start + 1,
                             f"{len(run)} consecutive sentences of 3 words or fewer")
                run = []
            if s.kind == "prose" and s.words <= 3:
                run.append(s)
            previous = s.line
        lengths = [s.words for s in self.stat_sentences]
        st = self.sentence_stats = _sentence_stats(lengths)
        if len(lengths) >= self.th["cv_min_sentences"] and st["cv"] < self.th["cv_min"]:
            self.add("sentence_uniformity", "warning", None, None, f"sentence length CV {st['cv']:.2f} below "
                     f"{self.th['cv_min']:.2f} (mean {st['mean']:.1f}, stdev {st['stdev']:.1f})")
        limit = self.th["long_sentence_words"]
        for s in self.stat_sentences if limit else []:
            if s.words > limit:
                self.add("long_sentence", str(self.th["long_sentence_severity"]), s.line, s.start + 1,
                         f"sentence of {s.words} words (limit {limit}): cut it at a full stop, one idea per sentence",
                         pattern_id="P68" if self.type == "chronique" else "default")

    # 6b, 6c. commas that pile up, sentences without a conjugated verb (3.1.0)
    def check_sentence_form(self) -> None:
        eligible = {l.number for l in self.text_lines()}
        limit, self.comma_max_seen, self.verbless_count = int(self.th["comma_max"]), 0, 0
        after_initial = (0, False)  # (line, the previous sentence stopped on an initial such as "Jean T.")
        for s in self.sentences:
            if s.line not in eligible or s.kind not in ("prose", "list"):
                continue
            line = self.by_number[s.line]
            text = neutralize(line.text, line.base)[s.start:s.end]
            commas = len(COMMA_RE.findall(text))
            self.comma_max_seen = max(self.comma_max_seen, commas)
            if commas > limit:
                self.add("comma_load", str(self.th["comma_severity"]), s.line, s.start + 1,
                         f"{commas} commas in one sentence (limit {limit}): cut the sentence, or drop the commas "
                         "that separate nothing (a plain enumeration may stay)")
            # Not a sentence to judge: a bold run-in label, a "label: value" line, a name cut on its initial,
            # a line with no final stop (greeting, caption, signature), a polite formula, a byline or a footer
            # (whole line in emphasis, or items split by a middle dot).
            label = any(m.start() <= s.start and s.end <= m.end() for m in BOLD_RE.finditer(mask_line(line.text)))
            label = (label or chr(0xB7) in line.text or chr(0x2192) in line.text
                     or bool(re.fullmatch(r"\s*([*_]).*\1\s*", line.text)))
            initial = bool(CUT_END_RE.search(text))
            cut_name, after_initial = after_initial == (s.line, True), (s.line, initial)
            body = text.rstrip("»\"" + RDQUO + ") ")
            cut_name = cut_name or text.count(")") > text.count("(")  # tail of a bracket cut on an abbreviation
            if (self.lang != "fr" or s.kind != "prose" or s.words < 2 or label or initial or cut_name or ":" in text
                    or not body.endswith(SENTENCE_END) or FR_FORMULA_RE.match(text.lower().replace(RSQUO, "'"))
                    or has_finite_verb_fr(text)):
                continue
            self.verbless_count += 1
            self.add("verbless", str(self.th["verbless_severity"]), s.line, s.start + 1,
                     f"no conjugated verb found in this {s.words}-word sentence (heuristic): give it a verb, or "
                     "attach it to its neighbour")

    # 7, 8. bold
    def check_bold(self) -> None:
        spans = numeric = 0
        counted: list[tuple[int, int]] = []
        for line in self.text_lines():
            for match in BOLD_RE.finditer(mask_line(line.text)) if line.kind != "heading" else []:
                is_numeric = bool(re.search(r"\d", match.group(0)))
                spans, numeric = spans + 1, numeric + is_numeric
                if self.th["bold_any_warning"]:
                    self.add("bold_density", "warning", line.number, match.start() + 1,
                             "bold markup shows as asterisks on LinkedIn and Meta")
                if not (is_numeric and self.th["bold_numeric_exempt"]):
                    counted.append((line.number, match.start() + 1))
            for match in re.finditer("«" + SP + r"*\*\*[^*\n]+\*\*" + SP + "*»", line.text):
                self.add("bold_density", "info", line.number, match.start() + 1, "bold word inside quotes")
        self.bold_stats = {"spans": spans, "numeric": numeric, "non_numeric": spans - numeric,
                           "non_numeric_per_1000_words": round(self.per1000(spans - numeric), 2)}
        limit = self.th["bold_non_numeric_per_1000"]
        if limit is not None and self.per1000(len(counted)) > limit:
            self.add("bold_density", "warning", *counted[0], f"{len(counted)} bold spans, "
                     f"{self.per1000(len(counted)):.1f} per 1000 words above {limit}")
        run: list[int] = []
        for line in self.lines + [Line(0, "", "blank")]:
            if line.kind == "list" and re.match(r"^\s*(?:[-*+•]|\d{1,3}[.)])\s+\*\*[^*\n]+?(?:\s*:\s*\*\*|\*\*\s*:)",
                                                line.text):
                run.append(line.number)
                continue
            if len(run) >= 3:
                self.add("inline_header_list", str(self.th["inline_header_list_severity"]), run[0], 1,
                         f"{len(run)} consecutive bullets starting with a bold label and a colon")
            run = []

    # 9. emoji
    def check_emoji(self) -> None:
        hits: list[tuple[int, int, str]] = []
        starting = 0
        for line in self.lines:
            if line.kind in ("frontmatter", "code", "html_comment", "meta_block") or \
                    (line.kind == "blockquote" and self.skip_quotes):
                continue
            masked = mask_line(line.text)
            hits += [(line.number, m.start() + 1, m.group(0)) for m in EMOJI_RE.finditer(masked)]
            starting += bool(EMOJI_RE.match(re.sub(r"^[\s>#*_]*(?:[-*+•]\s+|\d{1,3}[.)]\s+)?[\s*_]*", "", masked)))
        self.emoji_stats = {"count": len(hits), "lines_starting_with_emoji": starting,
                            "chars": sorted({h[2] for h in hits})}
        policy, limit = self.th["emoji_policy"], self.th["emoji_limit"]
        if policy == "limit" and len(hits) > limit:
            self.add("emoji", str(self.th["emoji_limit_severity"]), *hits[limit][:2], f"{len(hits)} emoji, more "
                     f"than {limit}")
        allowed = next((h for h in hits if h[2] == POINTER), None) if policy == "pointer_once" else None
        for hit in hits if policy != "limit" else []:
            if hit is not allowed:
                self.add("emoji", "warning", hit[0], hit[1], f"emoji {hit[2]}", hit[2])
        if starting >= 3:
            self.add("emoji", "warning", None, None, f"{starting} lines start with an emoji")

    # 10. quotes
    def check_quotes(self) -> None:
        lines = self.text_lines(tables=True)
        joined = "\n".join(mask_line(l.text) for l in lines)
        straight = bool(re.search(r"\w'\w", joined))
        for line in lines:
            masked = mask_line(line.text)
            if self.lang == "en":
                for match in re.finditer("[" + LDQUO + RDQUO + LSQUO + RSQUO + "]", masked):
                    double = match.group(0) in (LDQUO, RDQUO)
                    self.add("curly_quotes", "warning" if double or straight else "info", line.number,
                             match.start() + 1, "curly double quote" if double else "curly apostrophe or single quote")
                continue
            for match in re.finditer("[\"" + LDQUO + "][^\"" + LDQUO + RDQUO + "\n]{1,200}[\"" + RDQUO + "]", masked):
                self.add("curly_quotes", "warning", line.number, match.start() + 1, "English double quotes, use « »")
        if self.lang == "fr" and straight and re.search(r"\w" + RSQUO + r"\w", joined):
            self.add("curly_quotes", "info", None, None, "mixed straight and curly apostrophes")

    # 11. title case
    def check_title_case(self) -> None:
        for line in self.lines:
            words = WORD_RE.findall(neutralize(line.text, "heading")) if line.kind == "heading" else []
            if self.lang == "fr":
                words = [re.sub(r"^(?:l|d|qu|j|n|s|c|m|t)['’](?=.)", "", w, flags=re.IGNORECASE) for w in words]
            content = [w for w in words[1:] if not ((w.isupper() and len(w) > 1) or w[0].isdigit()
                                                     or w.lower() in FUNCTION_WORDS[self.lang])]
            capitals = sum(w[0].isupper() for w in content)
            if len(words) >= 4 and capitals >= 3 and capitals / len(content) >= 0.7:
                self.add("title_case", "warning", line.number, 1, f"Title Case heading ({capitals}/{len(content)})")

    # 12. not X but Y
    def check_not_x_but_y(self) -> None:
        regexes = [re.compile(p) for p in NOT_X_BUT_Y[self.lang]]
        for line in self.text_lines():
            norm, mapping = normalize_for_match(neutralize(line.text, line.base))
            hits = [(m.start(), m.group(0)) for r in regexes for m in r.finditer(norm)]
            opposition = FR_HEADING_OPPOSITION.match(norm) if line.kind == "heading" and self.lang == "fr" else None
            hits += [(opposition.start(1), opposition.group(1))] if opposition else []
            for start, text in hits:
                col = mapping[start]
                if line.kind == "heading":
                    severity, pid, where = "error", PATTERN_IDS["not_x_but_y"][self.li], "in a heading"
                elif self.lang == "fr" and self.closes_section(line.number, col):
                    severity, pid, where = "error", "P63", "closing a section"
                else:
                    severity, pid, where = "warning", PATTERN_IDS["not_x_but_y"][self.li], "in the text"
                self.add("not_x_but_y", severity, line.number, col + 1, f"negative parallelism {where}: \"{text[:60]}\"",
                         pattern_id=pid)

    def closes_section(self, number: int, column: int) -> bool:
        """True in the last sentence of a paragraph followed by a heading or the end of the file."""
        unit = self.line_to_unit.get(number)
        if unit is None or (unit + 1 < len(self.units) and self.by_number[self.units[unit + 1][0]].base != "heading"):
            return False
        return self.sentence_at(number, column) == self.unit_sentences.get(unit, [None])[-1]

    # 13. hedging
    def check_hedging(self) -> None:
        terms = sorted(HEDGES[self.lang].split("|"), key=len, reverse=True)
        regex = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(t) + r"(?!\s+qu)" * (t == "plutot") for t in terms)
                           + r")(?!\w)")
        eligible = {l.number for l in self.text_lines()}
        for s in self.sentences:
            line = self.by_number[s.line]
            found = set(regex.findall(_norm(neutralize(line.text, line.base)[s.start:s.end]))) if s.line in eligible \
                else set()
            if len(found) >= 2:
                self.add("hedging_stack", "warning", s.line, s.start + 1, f"{len(found)} hedges in one sentence: "
                         f"{', '.join(sorted(found))}")

    # 14. hard wrap
    def check_hard_wrap(self) -> None:
        wraps = [a.number for a, b in zip(self.lines, self.lines[1:])
                 if a.kind in ("prose", "blockquote") and b.kind == a.kind and len(a.text.rstrip()) >= 40
                 and not (ends_with_final_punct(a.text) or a.text.endswith("  ") or a.text.rstrip().endswith("\\"))
                 and re.match(r"^\s*(?:>\s?)*[a-zà-ÿœ0-9]", b.text)]
        block: list[Line] = []
        for line in self.lines + [Line(0, "", "blank")]:
            if line.kind == "prose":
                block.append(line)
                continue
            sizes = [len(l.text.rstrip()) for l in block[:-1]]
            if len(block) >= 3 and all(60 <= x <= 100 for x in sizes) and max(sizes) - min(sizes) <= 5 \
                    and not set(wraps) & {l.number for l in block}:
                wraps.append(block[0].number)
            block = []
        for n in sorted(wraps):
            self.add("hard_wrap", "error" if len(wraps) >= 2 else "warning", n, 1, "paragraph hard-wrapped at a fixed "
                     "column")

    # 15. exclamation
    def check_exclamation(self) -> None:
        self.exclamations = 0
        for line in self.lines:
            for match in re.finditer(r"!+", mask_line(line.text)) if line.kind in ("prose", "list") else []:
                self.exclamations += 1
                if len(match.group(0)) >= 2:
                    self.add("exclamation", "warning", line.number, match.start() + 1, "repeated exclamation marks", "!!")
                else:
                    self.add("exclamation", "warning" if self.exclamations >= self.th["exclamation_warning_from"]
                             else "info", line.number, match.start() + 1, f"exclamation mark #{self.exclamations}")

    # 16. French typography
    def check_typography_fr(self) -> None:
        for line in self.text_lines(tables=True) if self.lang == "fr" else []:
            for pattern, severity, message in TYPO_FR:
                for match in re.finditer(pattern, mask_line(line.text), re.IGNORECASE):
                    self.add("typography_fr", severity, line.number, match.start() + 1, message)

    # compare with the original
    def spoken_words(self, text: str) -> int:
        return sum(len(WORD_RE.findall(re.sub(r"\[[^\]]*\]", " ", neutralize(l.text, l.base))))
                   for l in classify_lines(text) if l.kind in ("prose", "list"))

    def bold_numeric(self, text: str) -> list[str]:
        return [" ".join(sorted(extract_numbers(m.group(0), self.lang))) for l in classify_lines(text)
                if l.kind in ("prose", "list", "blockquote") for m in BOLD_RE.finditer(mask_line(l.text))
                if re.search(r"\d", m.group(0))]

    def compare(self) -> Optional[dict[str, Any]]:
        if self.original is None:
            return None
        orig, out = self.original, self.text

        def lost(a: list[str], b: list[str]) -> list[str]:
            return list((Counter(a) - Counter(b)).elements())

        p_orig, p_out = count_paragraphs(orig), count_paragraphs(out)
        if p_orig != p_out:
            self.add("paragraph_count", "warning", None, None, f"paragraph count changed: {p_orig} in original, {p_out} "
                     "in output (allowed only for a paragraph made of tells alone, declared in Changements)")
        n_orig, n_out = extract_numbers(orig, self.lang), extract_numbers(out, self.lang)
        missing, added = sorted(lost(n_orig, n_out), key=Decimal), sorted(lost(n_out, n_orig), key=Decimal)
        urls = sorted(lost(_urls(orig), _urls(out)))
        codes = sorted(lost(TIMECODE_RE.findall(orig), TIMECODE_RE.findall(out)))
        severity = "error" if self.type == "article" else "warning"
        bold = lost(self.bold_numeric(orig), self.bold_numeric(out))
        emoji = max(0, orig.count(POINTER) - out.count(POINTER))
        for check, values, sev, label in (("numbers", missing, "error", "number {} of the original is missing"),
                                          ("numbers", added, "warning", "number {} added"),
                                          ("urls", urls, "error", "URL missing: {}"),
                                          ("timecodes", codes, "error", "timecode missing: {}"),
                                          ("bold_numeric", bold, severity, "bold numeric span lost: {}"),
                                          ("protected_emoji", [POINTER] * emoji, severity, "{} removed")):
            for value in values:
                self.add(check, sev, None, None, label.format(value), value)
        h_orig, h_out = ([l.level for l in classify_lines(t) if l.base == "heading"] for t in (orig, out))
        if h_orig != h_out:
            self.add("headings", "warning", None, None, f"headings changed: {len(h_orig)} in original, {len(h_out)} in "
                     "output (or levels differ)")
        # 3.1.0: the pass must not add long sentences, comma piles or verbless sentences (hard rule 12).
        base = Analyzer(orig, self.lang, self.type, None, self.skip_quotes, self.allow_footer_dash, self.ignore, (),
                        self.kill_list)
        base.check_rhythm()
        base.check_sentence_form()
        form = {}
        for check in ("long_sentence", "comma_load", "verbless"):
            before, after = (sum(f["check"] == check and f["line"] is not None for f in a.findings)
                             for a in (base, self))
            form[check] = {"original": before, "output": after}
            if after > before:
                self.add(check, "warning", None, None, f"{after} in the output, {before} in the original: the pass "
                         "must not add any")
        delta = None
        if self.type == "chronique":
            s_orig, s_out = self.spoken_words(orig), self.spoken_words(out)
            delta = round((s_out - s_orig) * 100 / s_orig, 2) if s_orig else 0.0
            if abs(delta) > 10:
                self.add("spoken_length", "warning", None, None, f"spoken words changed by {delta:+.1f}%")
        return {"original": None, "paragraphs_original": p_orig, "paragraphs_output": p_out,
                "paragraphs_equal": p_orig == p_out, "numbers_missing": missing, "numbers_added": added,
                "urls_missing": urls, "timecodes_missing": codes, "headings_original": len(h_orig),
                "headings_output": len(h_out), "spoken_words_delta_pct": delta, "bold_numeric_missing": bold,
                "protected_emoji_missing": emoji, "sentence_form": form}

    # report
    def run(self) -> dict[str, Any]:
        for check in (self.check_dash, self.check_kill_list, self.check_triads, self.check_rhythm,
                      self.check_sentence_form, self.check_bold,
                      self.check_emoji, self.check_quotes, self.check_title_case, self.check_not_x_but_y,
                      self.check_hedging, self.check_hard_wrap, self.check_exclamation, self.check_typography_fr):
            check()
        compare, sections, limit = self.compare(), [], self.th["section_char_limit"]
        for sec in self.sections:
            body = "\n".join(l.text for l in sec["lines"]).strip()
            first = next((self.units[self.line_to_unit[l.number]] for l in sec["lines"] if l.number in self.line_to_unit),
                         [])
            sections.append({"heading": sec["heading"], "line": sec["line"], "characters": len(body),
                             "first_paragraph_chars": len("\n".join(self.by_number[n].text for n in first).strip())})
            if limit and len(body) > limit:  # no dedicated check name: reported under long_sentence
                self.add("long_sentence", "warning", sec["line"], 1, f"section \"{sec['heading']}\" has {len(body)} "
                         f"characters, above the {limit} LinkedIn maximum", "section-length", pattern_id=None)
        self.findings.sort(key=lambda f: (f["line"] is None, f["line"] or 0, SEVERITY_ORDER[f["severity"]],
                                          f["column"] or 0, CHECKS.index(f["check"])))
        for index, finding in enumerate(self.findings, 1):
            finding["id"] = index
        counts = Counter(f["severity"] for f in self.findings)
        allowed = sum(f["check"] == "dash" and f["item"] in ("footer-dash", "timecode-dash", "quote")
                      for f in self.findings)
        stats = {"words": self.words, "characters": len(self.text), "paragraphs": len(self.units),
                 "sections": sections, "spoken_words": self.spoken_words(self.text) if self.type == "chronique" else None,
                 "sentences": {**self.sentence_stats, "commas_max": self.comma_max_seen,
                               "verbless": self.verbless_count},
                 "dashes": {"em": self.text.count(EM_DASH), "en": self.text.count(EN_DASH), "allowed": allowed},
                 "bold": self.bold_stats, "emoji": self.emoji_stats, "triads": self.triad_count,
                 "exclamations": self.exclamations, "kill_list": {**{c: self.kill_counts[c] for c in CATEGORIES},
                                                                  "vocabulaire_per_1000_words": round(self.vocab_density, 2)}}
        return {"tool": "verif_humanizer", "version": __version__, "file": None, "lang": self.lang, "type": self.type,
                "options": {"compare": None, "skip_quotes": self.skip_quotes, "allow_footer_dash": self.allow_footer_dash,
                            "ignore": list(self.ignore), "ignore_lines": list(self.ignore_lines)},
                "result": "fail" if counts["error"] else "pass", "exit_code": int(counts["error"] > 0),
                "counts": {s: counts[s] for s in SEVERITY_ORDER}, "stats": stats, "compare": compare,
                "findings": self.findings}


def _sentence_stats(lengths: list[int]) -> dict[str, Any]:
    n = len(lengths)
    mean, stdev = (statistics.fmean(lengths), statistics.pstdev(lengths)) if n else (0.0, 0.0)
    return {"count": n, "mean": round(mean, 2), "stdev": round(stdev, 2), "cv": round(stdev / mean, 2) if n else 0.0,
            "median": round(float(statistics.median(lengths)), 2) if n else 0.0,
            "share_under_8": round(sum(x < 8 for x in lengths) / n, 2) if n else 0.0,
            "share_over_30": round(sum(x > 30 for x in lengths) / n, 2) if n else 0.0, "max": max(lengths, default=0)}


def _urls(text: str) -> list[str]:
    return [u.rstrip(".,;:)") for u in re.findall(r"https?://[^\s)<>\]\"]+", text)]


def analyze(text: str, lang: str, content_type: str = "general", *, original: Optional[str] = None,
            skip_quotes: bool = False, allow_footer_dash: bool = False, ignore: tuple[str, ...] = (),
            ignore_lines: tuple[int, ...] = (), kill_list: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    """Return the JSON report for a text ("file" is None)."""
    return Analyzer(text, lang, content_type, original, skip_quotes, allow_footer_dash, ignore, ignore_lines,
                    kill_list).run()


def format_text(report: dict[str, Any]) -> str:
    """Short human summary."""
    out = [f"verif_humanizer {report['version']} | file={report['file']} | lang={report['lang']} | type={report['type']}"]
    for f in report["findings"]:
        where = f"L{f['line']}:{f['column'] or 1}" if f["line"] is not None else "-"
        quote = f" | «{f['excerpt']}»" if f["excerpt"] and f["check"] != "kill_list" else ""
        out.append(f"{f['severity'].upper():<8} {where:<7} {f['check']:<12} {f['message']}{quote}")
    s, c, n = report["stats"], report["compare"], report["counts"]
    out.append(f"Stats: words={s['words']} paragraphs={s['paragraphs']} sentences={s['sentences']['count']} "
               f"mean={s['sentences']['mean']} stdev={s['sentences']['stdev']} cv={s['sentences']['cv']} "
               f"bold_non_numeric={s['bold']['non_numeric']} emoji={s['emoji']['count']}")
    if c is not None:
        form = " ".join(f"{k}={v['output']}/{v['original']}" for k, v in c["sentence_form"].items())
        out.append(f"Compare: paragraphs {c['paragraphs_output']}/{c['paragraphs_original']} "
                   f"numbers_missing={len(c['numbers_missing'])} urls_missing={len(c['urls_missing'])} {form}")
    out.append(f"Result: {report['result'].upper()} ({n['error']} error, {n['warning']} warning, {n['info']} info) "
               f"exit={report['exit_code']}")
    return "\n".join(out)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="verif_humanizer", description="Deterministic checks for humanizer.")
    parser.add_argument("file", metavar="FILE", help="text to check, or - for stdin")
    parser.add_argument("--lang", required=True, choices=("fr", "en"))
    parser.add_argument("--type", dest="content_type", default="general", choices=TYPES + tuple(TYPE_ALIASES))
    parser.add_argument("--compare", metavar="ORIGINAL")
    parser.add_argument("--ignore", action="append", default=[], metavar="ITEM")
    parser.add_argument("--ignore-line", action="append", default=[], type=int, metavar="N")
    parser.add_argument("--kill-list", metavar="PATH")
    for flag in ("--json", "--skip-quotes", "--allow-footer-dash", "--verbose"):
        parser.add_argument(flag, action="store_true")
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:  # argparse exits 2 on a bad call, 0 on --help
        return exc.code if isinstance(exc.code, int) else 2
    logging.basicConfig(stream=sys.stderr, format="%(levelname)s verif_humanizer: %(message)s",
                        level=logging.DEBUG if args.verbose else logging.WARNING, force=True)
    try:
        kill_list = load_kill_list(Path(args.kill_list) if args.kill_list else None)
        original = read_text(args.compare) if args.compare else None
        report = analyze(read_text(args.file), args.lang, args.content_type, original=original,
                         skip_quotes=args.skip_quotes, allow_footer_dash=args.allow_footer_dash,
                         ignore=tuple(args.ignore), ignore_lines=tuple(args.ignore_line), kill_list=kill_list)
    except (OSError, UnicodeDecodeError, re.error, ValueError) as exc:  # JSONDecodeError is a ValueError
        LOG.error("cannot run (kill list %s, file %s): %s", args.kill_list or "default", args.file, exc)
        return 2
    report["file"], report["options"]["compare"] = args.file, args.compare
    if report["compare"] is not None:
        report["compare"]["original"] = args.compare
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else format_text(report))
    return report["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
