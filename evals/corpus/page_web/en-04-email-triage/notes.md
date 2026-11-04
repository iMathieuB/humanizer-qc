# Notes : page_web, en, paire 4

Source : jeu d'exemples fictifs de la version 3.0, Page web de service ou d'offre, Paire 4 (EN) : Email triage for property management offices. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Templated headline "The AI-powered [X] for modern [Y]", replaced by a headline that names the task and the audience: https://superdesign.dev/blog/fix-generic-ai-landing-page
- Interchangeable benefits "Save time. Work smarter. Scale faster." ("True of every product, specific to none"): the string is cut to one imperative, "Save time.", kept as a paragraph (hard rule 5); the cost calculation moves up: https://superdesign.dev/blog/fix-generic-ai-landing-page
- "It's not X, it's Y" ("isn't just a tool, it's a dependable partner"), removed: https://arxiv.org/html/2510.15061
- GPT-6 era vocabulary (dependable, quietly, foster, leverage), removed: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Present participial clauses ("Leveraging...", "ensuring...", "allowing..."), rewritten as finite clauses or cut: https://arxiv.org/html/2410.16107
- Marketing verbs "features", "offers" and "boasts" instead of a plain verb, replaced by "drafts", "never sends", "lasts": https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (boasts: https://arxiv.org/html/2412.11385)
- Emoji at the start of every list entry, removed while keeping the bullets: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Em dashes, replaced by a period and by "or": https://arxiv.org/html/2603.27006

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre de la page, puces de bénéfices (gardées, sans émoji), tableau d'offres s'il y en a un, prix et conditions, appel à l'action impératif, mentions légales.

## Remarques de la source

The imperative call to action "Book a call" stays: a standard CTA is a platform convention, not a tell (https://business.linkedin.com/advertise/ads/best-practices/sponsored-content-tips).

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type page_web --compare avant.md
```
