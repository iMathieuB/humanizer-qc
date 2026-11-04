# Notes : formation, en, paire 5

Source : jeu d'exemples fictifs de la version 3.0, Matériel de formation, Paire 5 (EN) : estimating the time a quote template saves. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Template placeholders: "[Company Name]" removed, the "2026-XX-XX" date cut back to the known year, nothing filled with an invented value (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Overused common words: "comprehensive", "insights", "Notably", "Additionally" (https://arxiv.org/html/2406.07016).
- Marketing verbs instead of a plain "has" or a direct statement: "offers valuable insights", "features pre-filled fields" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Em dash between "10 minutes" and "10 hours in total" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2603.27006).
- Section-ending summary that restates the core idea: "In short, timing your quotes reveals your savings." (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing, listed among historical indicators). Removed.
- "Challenges" section in the "Despite its [positive words], [subject] faces challenges" form, ending on a vaguely positive note (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Cut down to one plain sentence and kept as a paragraph (hard rule 5); flagged in Ce qui sonne encore IA.
- Corrective disclaimer: "should be treated as a starting point rather than a guarantee" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://graphite.io/five-percent/research/ai-tells). Reworded as a plain note, with no new instruction.
- Obviously wrong distractors ("5 minutes", "1 million minutes") that do not reflect real learner errors (https://arxiv.org/html/2404.02124; https://elearningindustry.com/why-pedagogy-should-drive-ai-course-generation-not-the-other-way-around). Kept as is: stems and answers are protected (type-formation.md); flagged, with a suggestion left to the author.

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre du module, objectifs (« à la fin de ce module, vous serez capable de », ou « By the end of this module, you will be able to »), étapes, encadré « À retenir » s'il y en a un, exercice.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type formation --compare avant.md
```
