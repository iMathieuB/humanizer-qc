# Notes : chronique, fr, paire 2

Source : jeu d'exemples fictifs de la version 3.0, Script de chronique vidéo parlée, Paire 2 (FR) : rappels de rendez-vous en clinique. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- **Ouverture « Voici ce qu'il faut savoir »** : supprimée, l'accroche entre directement dans le sujet. Source : https://www.pangram.com/fr/signs-of-ai-writing
- **Ton positif enjoué et éloge du sujet** (« absolument passionnant », « tout simplement remarquable ») : supprimés, le montant récupéré suffit. Sources : https://www.scientificamerican.com/podcast/episode/how-tools-like-notebooklm-create-ai-generated-podcasts et https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- **Construction « non seulement X, mais aussi Y »** : remplacée par deux phrases courtes. Source : https://www.pangram.com/fr/signs-of-ai-writing
- **Triade** (« l'horaire, l'équipe et les patients ») : réduite à ce que le script développe vraiment. Sources : https://www.pangram.com/fr/signs-of-ai-writing et https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Phrase à subordonnées en « qui », « que », « parce que »** : découpée en phrases d'une idée. Sources : https://pedagogie.ac-toulouse.fr/emi/node/1198 et https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice
- **Mots de liaison lourds** (« car », « en effet », « par ailleurs ») : supprimés. Sources : https://pedagogie.ac-toulouse.fr/emi/node/1198 et https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- **Variation élégante** (« rendez-vous », « plages horaires », « consultation », « créneaux ») : on répète « rendez-vous », comme on le dirait à voix haute. Sources : https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice et https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Clôture « En conclusion » et conclusion vague de portée générale** (« solution incontournable pour toutes les cliniques ») : remplacée par une recommandation précise. Sources : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr et https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : codes temporels, titres de segment et lignes de régie (▶), identiques d'une version à l'autre.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type chronique --compare avant.md
```
