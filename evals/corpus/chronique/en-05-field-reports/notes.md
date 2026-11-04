# Notes : chronique, en, paire 5

Source : jeu d'exemples fictifs de la version 3.0, Script de chronique vidéo parlée, Paire 5 (EN) : field reports at a plumbing company. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- **Opening overview that announces the program** ("Today we'll cover three things"): replaced by the cost of the problem. Source: https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- **Relentlessly positive tone and praise of the subject** ("one of the most inspiring projects we've ever seen"): cut. Sources: https://www.scientificamerican.com/podcast/episode/how-tools-like-notebooklm-create-ai-generated-podcasts and https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- **Evaluative adjectives** ("commendable", "meticulous"): cut. Source: https://arxiv.org/html/2403.07183
- **Elegant variation** ("technicians", "field staff", "crew"): the script repeats "technicians" and "reports", as a speaker would. Sources: https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice and https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Too many clauses for one breath** ("who... which... who... which means"): split into one idea per sentence. Source: https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice
- **Colon in spoken text** ("Today we'll cover three things:", "At $32 an hour:"): replaced by commas and periods. Source: https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/
- **Inverted parallelism "Y rather than X"** ("Rather than retyping, the team now dictates"): stated as what happens now. Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Vague link** ("closely associated with the coordinator's schedule"): replaced by the exact relation, the coordinator gets the 8 hours back. Source: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : codes temporels, titres de segment et lignes de régie (▶), identiques d'une version à l'autre.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type chronique --compare avant.md
```
