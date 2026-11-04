# Notes : article, en, paire 4

Source : jeu d'exemples fictifs de la version 3.0, Article de blogue SEO, GEO et AEO, Paire 4 (EN) : time spent on quotes. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Title case in headings: "How Long Does It Really Take To Prepare A Quote?" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style).
- Interchangeable opening: "In today's fast-paced world" (https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content).
- Em dash: between "no longer a detail" and "it's a competitive advantage" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2603.27006).
- "It's not X, it's Y": "It's not a sales problem, it's a process problem" (https://arxiv.org/html/2510.15061).
- Style verbs in excess: "delve", "showcasing" (https://arxiv.org/html/2406.07016).
- GPT-6 era vocabulary: "dependable", "leverage", "quietly" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Marketing verb instead of "has": "offers a dependable way" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Present participial clauses: "totaling", "cutting", "showcasing" (https://arxiv.org/html/2410.16107).

## Structures conservées

H2 question followed by the answer, every figure (60 quotes, 45 minutes, 45 hours, 15 minutes, 30 hours, $55, $1,650, $19,800), bold kept on the two results only.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 2, apres.md en compte 2.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type article --compare avant.md
```
