# Notes : formation, en, paire 4

Source : jeu d'exemples fictifs de la version 3.0, Matériel de formation, Paire 4 (EN) : mapping a purchase approval workflow. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Style verbs and overused words: "delve", "crucial", "underscores" (https://arxiv.org/html/2406.07016; students scanning course materials for "crucial" and "delve": https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/).
- Prompt residue left in the material: "Expand on all areas. Be more detailed and specific." (https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/). Removed.
- Em dash between "approval mapping" and "a key step" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; models well above the human reference rate: https://arxiv.org/html/2603.27006).
- Inline-header vertical list with one identical form per item: "**Map:** ... **Measure:** ... **Prioritize:** ..." (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style). Replaced by numbered steps, a structure the type keeps.
- Present participial clauses: "Leveraging...", "Tracking...", "Fostering..." (https://arxiv.org/html/2410.16107).
- GPT-6 era vocabulary: "leveraging", "fostering", "steady" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- "It's not just X, it's Y" construction: "It's not just a diagram, it's a roadmap" (https://arxiv.org/html/2510.15061).
- Vague link: "the second approver is associated with 2 of those days" instead of the exact relation (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Now: "2 of those days are spent waiting for the second approver."

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre du module, objectifs (« à la fin de ce module, vous serez capable de », ou « By the end of this module, you will be able to »), étapes, encadré « À retenir » s'il y en a un, exercice.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 9, apres.md en compte 9.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type formation --compare avant.md
```
