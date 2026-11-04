# Notes : page_web, en, paire 5

Source : jeu d'exemples fictifs de la version 3.0, Page web de service ou d'offre, Paire 5 (EN) : Process audit for manufacturers. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Hollow formula "Unlock the full potential", removed: https://www.eesel.ai/blog/ai-ad-copy-generator
- Evaluative adjectives "meticulous" and "innovative", removed: https://arxiv.org/html/2403.07183
- Style verbs "delves", "underscoring" and "showcases", replaced by "tells you" or cut: https://arxiv.org/html/2406.07016
- Vague link "associated with" instead of the exact relation, removed ("your processes"): https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Inverted parallelism "Y rather than X" ("value rather than complexity"), rewritten as a plain statement of what the report says: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- "Less like a _ and more like" ("less like an audit and more like a roadmap to growth"), rewritten as one plain sentence kept as a paragraph (hard rule 5): https://graphite.io/five-percent/research/ai-tells
- Aspirational, slogan-like tone ("roadmap to growth", "every opportunity hiding in plain sight"), cut down: https://arxiv.org/html/2512.03373v1
- Em dashes, replaced by "or" or removed with the clause they introduced: https://arxiv.org/html/2603.27006

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre de la page, puces de bénéfices (gardées, sans émoji), tableau d'offres s'il y en a un, prix et conditions, appel à l'action impératif, mentions légales.

## Remarques de la source

The fee-waiver condition is kept word for word: conditions and fine print are not removed (https://dailyhive.com/vancouver/ai-ads-metro-vancouver-legal-standards). The "What's included" list stays, since bullets help scanning on a service page (https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/).

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 10, apres.md en compte 10.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type page_web --compare avant.md
```
