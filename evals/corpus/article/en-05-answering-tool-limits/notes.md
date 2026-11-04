# Notes : article, en, paire 5

Source : jeu d'exemples fictifs de la version 3.0, Article de blogue SEO, GEO et AEO, Paire 5 (EN) : limits of an AI answering tool. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Template section title in "X and Y" form, in title case: "Challenges And Limitations" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style).
- Formulaic "Challenges" section that opens with "Despite its..." and ends on a vaguely positive note ("the future looks bright") (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Corrective disclaimer: "should not be confused with" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Evaluative adjectives: "commendable", "meticulous" (https://arxiv.org/html/2403.07183).
- Common words in excess, stacked: "Additionally", "underscoring", "crucial", "comprehensive" (https://arxiv.org/html/2406.07016).
- "less like a _ and more like": "less like a receptionist and more like a triage desk" (https://graphite.io/five-percent/research/ai-tells).
- Navigation transition: "Now that we've covered the limitations, let's turn to the next steps" (https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content).
- "Conclusion" section that restates the section above ("In summary"): heading renamed, "In summary" and the navigation sentence cut, the closing sentence kept with its facts only (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## Structures conservées

Both headings stay, rewritten as descriptive headings in sentence case; the test figures (30 days, 412 of 520, 108, 79%) are unchanged; bold stays on the one statistic.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 4, apres.md en compte 4.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type article --compare avant.md
```
