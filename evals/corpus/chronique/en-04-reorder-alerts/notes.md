# Notes : chronique, en, paire 4

Source : jeu d'exemples fictifs de la version 3.0, Script de chronique vidéo parlée, Paire 4 (EN) : reorder alerts for a hardware store. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- **Filler openers** ("In this video", "Let's dive in", "The truth is"): cut, the hook opens on the dollar figure. Source: https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026
- **Negative parallelism** ("aren't just an inventory problem, they're a revenue problem"): replaced by the plain number. Sources: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing and https://arxiv.org/html/2510.15061
- **Em dash**: removed, the clause became separate sentences. Sources: https://arxiv.org/html/2603.27006 and https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Style verb cluster** ("delve", "underscoring", "showcasing"): cut, the numbers are stated directly. Source: https://arxiv.org/html/2406.07016
- **Present participial clauses** ("each stockout costing", "leaving little time"): rewritten as finite verbs in short sentences. Source: https://arxiv.org/html/2410.16107
- **GPT-6 era vocabulary** ("leveraging", "foster"): replaced by plain words. Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Rule of three** ("efficiency, accuracy, and growth"): dropped, the script states the one concrete change. Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Generic call to action** ("Follow for more automation tips!"): replaced by an action tied to the topic. Source: https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : codes temporels, titres de segment et lignes de régie (▶), identiques d'une version à l'autre.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 9, apres.md en compte 9.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type chronique --compare avant.md
```
