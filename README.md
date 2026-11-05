# humanizer-qc

Version dérivée de [humanizer](https://github.com/blader/humanizer), le skill de Siqi Chen publié sous licence MIT. Les 33 patrons de sa version 2.8.0, la calibration de voix et l'exemple complet viennent de ce projet. Cette édition y ajoute le français du Québec, cinq types de contenu, trois modes de travail et un script de vérification. Le suffixe « -qc » la distingue du skill d'origine : les deux peuvent être installés côte à côte.

Derived from [humanizer](https://github.com/blader/humanizer), the skill by Siqi Chen released under the MIT License. The 33 patterns of its version 2.8.0, the voice calibration and the full example come from that project. This edition adds Quebec French, five content types, three working modes and a verification script. The "-qc" suffix sets it apart from the original skill, so both can be installed side by side. [English version below](#english).

## Français

### Ce que fait le skill

Ce skill est une passe d'édition pour Claude. Il relit un texte rédigé ou réécrit avec l'aide d'une IA, retire les tics d'écriture que la recherche et les guides éditoriaux associent aux modèles de langue, et ramène le texte vers la voix de son auteur. Le fond ne change pas : les chiffres, les sources, les liens, les citations, la FAQ, l'appel à l'action et le minutage d'un script restent tels quels.

Le catalogue compte 74 patrons, de P01 à P74, répartis dans deux fichiers : un pour le français du Québec, un pour l'anglais. Chaque patron donne son niveau de preuve (étude mesurée, guide éditorial, billet de praticien ou règle maison), un exemple avant et après, un faux positif à ne pas signaler et ses sources.

Le skill reconnaît cinq types de contenu, en plus d'un type général : article de blogue SEO, GEO et AEO, page web de service ou étude de cas, publicité LinkedIn ou Meta, script vidéo parlé, matériel de formation. Pour chacun, il sait quels éléments protéger et quelles structures ne sont pas des tics, comme la FAQ d'un article ou une ligne de minutage.

Il travaille en trois modes. En mode interactif, il montre un brouillon, la liste de ce qui sonne encore IA, la version finale et les changements. En mode pipeline, appelé par un autre skill ou par un script, il rend une sortie lisible par une machine, avec une ligne STATUT. En mode audit, il évalue le texte sans le réécrire.

Il vérifie son résultat avec `scripts/verif_humanizer.py`, un script Python sans dépendance externe qui compare la version finale à l'original : tirets cadratins, retours à la ligne forcés, formules usées, chiffres perdus ou ajoutés, liens manquants, nombre de paragraphes.

Les instructions du skill sont rédigées en français. Claude les suit aussi pour un texte anglais, avec le fichier de patrons anglais.

### Ce qu'il ne fait pas

Il ne cherche pas à tromper un détecteur d'IA. Il ne vise aucun score et ne promet pas un texte « indétectable » : les détecteurs se trompent souvent sur des textes humains, et un texte précis dans la voix de son auteur vaut mieux qu'un texte trafiqué pour une machine. Il n'efface pas non plus les traces d'usage de l'IA, car la transparence reste la décision de l'auteur.

Il n'ajoute aucun fait, chiffre, nom, source ou anecdote, et il n'en retire aucun. Il n'insère pas de fautes exprès, pas de familiarité plaquée, pas de mots rares pour « faire humain ».

Il ne remplace pas une révision de fond. Si le plan, l'argument ou le ton d'ensemble ne tiennent pas, faites d'abord cette révision; humanizer-qc passe en dernier.

Il ne publie rien et n'envoie rien. Il écrit seulement dans le fichier fourni ou dans un dossier temporaire. Le script de vérification n'est pas un détecteur d'IA : il relève des signes précis pour aider la relecture.

### Installer dans claude.ai

1. Téléchargez `humanizer-qc.zip` (page Releases du dépôt). Le zip contient un dossier `humanizer-qc/` avec `SKILL.md`; si vous le refaites vous-même, gardez cette forme.
2. Dans claude.ai, ouvrez Personnaliser, puis Skills.
3. Téléversez le fichier zip.
4. Activez le skill. Claude s'en servira quand vous écrirez par exemple « humanise ce texte » ou « ça sonne IA ».

### Installer dans Claude Code

Copiez le dossier du skill dans `~/.claude/skills/humanizer-qc/` pour l'avoir dans tous vos projets, ou dans `.claude/skills/humanizer-qc/` à la racine d'un seul projet. Le plus simple est de décompresser `humanizer-qc.zip` dans `~/.claude/skills/`, ou de cloner ce dépôt dans `~/.claude/skills/humanizer-qc`. Le fichier `SKILL.md` doit se trouver directement dans ce dossier. Ouvrez ensuite une nouvelle session de Claude Code : le skill figure parmi les skills disponibles.

### Utiliser le skill

Demandez simplement « humanise ce texte », « passe humanizer sur l'article », « ça sonne IA », « rends ça naturel » ou « relis pour le ton ». Vous pouvez préciser le type, le mode et la langue : `type=article`, `mode=audit`, `lang=fr`.

Pour que le résultat colle à votre voix, joignez un échantillon de votre écriture. Vous pouvez aussi créer `references/voix-auteur.md` dans le dossier du skill, avec votre registre, la longueur habituelle de vos phrases, les mots que vous aimez et les formulations que vous refusez. Le skill le lit s'il existe. Ce fichier vous appartient : retirez-le si vous partagez votre copie du skill.

Un autre skill peut l'appeler en mode pipeline avec une ligne de paramètres :

```
humanizer-qc mode=pipeline type=article lang=fr fichier=article.md sortie=article-final.md
```

### Lancer le script de vérification

Le script demande Python 3 et aucune autre bibliothèque. Depuis le dossier du skill :

```
python3 -I scripts/verif_humanizer.py texte-final.md --lang fr --type article --compare texte-original.md
```

Sous Windows, remplacez `python3` par `python` ou `py`. Le script affiche ses constats (`error`, `warning`, `info`) et rend le code 0 s'il ne trouve aucune erreur, 1 s'il en trouve au moins une, 2 si l'appel est invalide. L'option `--json` donne le rapport complet. Types acceptés : `article`, `page_web`, `publicite`, `chronique`, `formation`, `general`.

Pour lancer les tests du script :

```
python3 -I -m unittest discover -s scripts/tests -v
```

Avec pytest installé, `pytest scripts/tests` fonctionne aussi.

### Contenu du dossier

| Chemin | Rôle |
|---|---|
| `SKILL.md` | Instructions du skill, lues par Claude |
| `references/patterns-fr.md`, `references/patterns-en.md` | Catalogue des patrons, un fichier par langue |
| `references/type-*.md` | Règles propres à chaque type de contenu |
| `references/detecteurs.md` | Position face aux détecteurs, garde-fous, gabarit du mode audit |
| `references/appels-et-coexistence.md` | Paramètres du mode pipeline, coexistence avec une autre passe de révision |
| `scripts/verif_humanizer.py`, `scripts/kill_list.json` | Script de vérification et sa liste de formules |
| `scripts/tests/` | Tests du script |
| `evals/` | Paires avant et après fictives et cas d'évaluation (absents du zip) |
| `CHANGELOG.md`, `LICENSE` | Journal des versions et licence |

### Crédits et licence

Le skill d'origine, [humanizer](https://github.com/blader/humanizer), est l'œuvre de Siqi Chen et de ses contributeurs, sous licence MIT. Il s'appuie sur la page [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), tenue par le WikiProject AI Cleanup. Plusieurs exemples « Before » des patrons P01 à P08 citent cette page, dont le texte est diffusé sous licence CC BY-SA 4.0.

Édition pour le français du Québec : Mathieu Brassard ([Groupe Ordinata](https://ordinata.ca)). Licence MIT, voir `LICENSE`.

## English

### What the skill does

This skill is an editing pass for Claude. It rereads text written or rewritten with AI help, removes the writing tells that research and editorial guides link to language models, and brings the text back to its author's voice. The substance stays the same: numbers, sources, links, quotes, the FAQ, the call to action and the timing of a script are kept as they are.

The catalog holds 74 patterns, P01 to P74, split between two files: one for Quebec French, one for English. Each pattern states its level of evidence (measured study, editorial guide, practitioner post or house rule), gives a before and after example and a false positive to leave alone, and lists its sources.

The skill knows five content types plus a general one: SEO, GEO and AEO blog post, service page or case study, LinkedIn or Meta ad, spoken video script, training material. For each type it knows what to protect and which structures are not tells, such as an article's FAQ or a timecode line.

It works in three modes. Interactive mode shows a draft, a list of what still sounds like AI, the final version and the changes. Pipeline mode, called by another skill or by a script, returns machine-readable output with a STATUT line. Audit mode assesses the text without rewriting it.

It checks its result with `scripts/verif_humanizer.py`, a Python script with no external dependency that compares the final version with the original: em dashes, hard line wraps, stock phrases, lost or added numbers, missing links, paragraph count.

The skill's instructions are written in French. Claude follows them for English text too, with the English pattern file.

### What it does not do

It does not try to fool AI detectors. It aims at no score and promises no "undetectable" text: detectors often misjudge human writing, and precise text in the author's own voice serves better than text doctored for a machine. It does not erase traces of AI use either, because disclosure stays the author's call.

It adds no fact, number, name, source or anecdote, and removes none. It inserts no deliberate typos, no forced casual tone and no rare words to "sound human".

It does not replace a substantive edit. If the outline, the argument or the general tone do not hold up, do that edit first; humanizer-qc runs last.

It publishes nothing and sends nothing. It writes only to the file it was given or to a temporary folder. The verification script is not an AI detector: it flags specific signs to help the review.

### Install in claude.ai

1. Download `humanizer-qc.zip` (Releases page of the repository). The zip holds a `humanizer-qc/` folder with `SKILL.md`; keep that layout if you build it yourself.
2. In claude.ai, open Customize, then Skills.
3. Upload the zip file.
4. Turn the skill on. Claude will use it when you write, for example, "humanize this" or "this sounds like AI".

### Install in Claude Code

Copy the skill folder to `~/.claude/skills/humanizer-qc/` to have it in every project, or to `.claude/skills/humanizer-qc/` at the root of a single project. The simplest way is to unzip `humanizer-qc.zip` into `~/.claude/skills/`, or to clone this repository into `~/.claude/skills/humanizer-qc`. `SKILL.md` must sit directly in that folder. Then start a new Claude Code session: the skill appears among the available skills.

### Use the skill

Just ask "humanize this" or "this sounds like AI", or in French « humanise ce texte » or « ça sonne IA ». You can set the type, the mode and the language: `type=article`, `mode=audit`, `lang=en`.

To match your voice, attach a sample of your writing. You can also create `references/voix-auteur.md` in the skill folder with your register, your usual sentence length, the words you like and the phrasings you reject. The skill reads it when it exists. That file is yours: remove it if you share your copy of the skill.

Another skill can call it in pipeline mode with a parameter line:

```
humanizer-qc mode=pipeline type=article lang=en fichier=post.md sortie=post-final.md
```

### Run the verification script

The script needs Python 3 and no other library. From the skill folder:

```
python3 -I scripts/verif_humanizer.py final.md --lang en --type article --compare original.md
```

On Windows, replace `python3` with `python` or `py`. The script prints its findings (`error`, `warning`, `info`) and exits with code 0 when it finds no error, 1 when it finds at least one, 2 when the call is invalid. The `--json` option gives the full report. Accepted types: `article`, `page_web`, `publicite`, `chronique`, `formation`, `general`.

To run the script's tests:

```
python3 -I -m unittest discover -s scripts/tests -v
```

With pytest installed, `pytest scripts/tests` works too.

### Folder contents

| Path | Purpose |
|---|---|
| `SKILL.md` | Skill instructions, read by Claude |
| `references/patterns-fr.md`, `references/patterns-en.md` | Pattern catalog, one file per language |
| `references/type-*.md` | Rules for each content type |
| `references/detecteurs.md` | Position on detectors, safeguards, audit mode template |
| `references/appels-et-coexistence.md` | Pipeline mode parameters, coexistence with another editing pass |
| `scripts/verif_humanizer.py`, `scripts/kill_list.json` | Verification script and its list of stock phrases |
| `scripts/tests/` | Script tests |
| `evals/` | Fictional before and after pairs and evaluation cases (not in the zip) |
| `CHANGELOG.md`, `LICENSE` | Version history and license |

### Credits and license

The original skill, [humanizer](https://github.com/blader/humanizer), is the work of Siqi Chen and its contributors, under the MIT License. It builds on the [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) page, maintained by WikiProject AI Cleanup. Several "Before" examples in patterns P01 to P08 quote that page, whose text is available under CC BY-SA 4.0.

Quebec French edition: Mathieu Brassard ([Groupe Ordinata](https://ordinata.ca/en/)). MIT License, see `LICENSE`.
