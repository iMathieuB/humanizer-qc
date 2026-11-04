# Notes : formation, fr, paire 2

Source : jeu d'exemples fictifs de la version 3.0, Matériel de formation, Paire 2 (FR) : écrire une règle de tri des courriels. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Majuscules superflues dans le titre : « Écrire Une Règle De Tri Des Courriels » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; casse de titre anglaise, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style).
- Ouverture « Voici ce qu'il faut savoir » (https://www.pangram.com/fr/signs-of-ai-writing). Ramenée à une phrase qui dit le sujet du module.
- Calques de l'anglais : « adresser le tri », « Ça fait du sens » (https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr; typologie des emprunts, https://vitrinelinguistique.oqlf.gouv.qc.ca/25444/les-emprunts-a-langlais/typologie-des-emprunts).
- Triades : « simple, rapide et efficace », retirée; « trier, tester, ajuster », gardée dans l'encadré « À retenir » (élément protégé) et signalée (https://www.pangram.com/fr/signs-of-ai-writing; « LLMs overuse the rule of three. », https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Forme identique répétée en liste verticale à intertitre en gras : gras des intertitres retiré, puces gardées (règle dure 5) (https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- Construction « pas seulement X, mais aussi Y » (https://www.pangram.com/fr/signs-of-ai-writing).
- Tiret cadratin entre « 100 sont des infolettres » et « soit 40 % » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Typographie non conforme à l'OQLF : dollar à gauche, point décimal et espace avant « ! » (https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles; espaces systématiques perçues comme signe, https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre du module, objectifs (« à la fin de ce module, vous serez capable de », ou « By the end of this module, you will be able to »), étapes, encadré « À retenir » s'il y en a un, exercice.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 10, apres.md en compte 10.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type formation --compare avant.md
```
