# Notes : page_web, fr, paire 1

Source : jeu d'exemples fictifs de la version 3.0, Page web de service ou d'offre, Paire 1 (FR) : Diagnostic d'automatisation. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Titre à trous « The AI-powered [X] for modern [Y] » (« La solution propulsée par l'IA pour les PME modernes »), remplacé par un titre qui dit ce que l'offre livre : https://superdesign.dev/blog/fix-generic-ai-landing-page
- Ouverture « Dans un monde où » sur un sujet général, supprimée au profit d'une phrase qui dit à qui sert l'offre : https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/
- Adjectif gonflé « crucial », supprimé : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Formule creuse « libérer votre potentiel », supprimée : https://www.eesel.ai/fr/blog/generateur-de-texte-publicitaire-ia
- Verbes répétés par ChatGPT « permettre » et « offrir », remplacés par des verbes d'action (« analysons », « je vous remets ») : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- « Pas seulement X, mais aussi Y » (« pas seulement un rapport, mais aussi un véritable levier de croissance »), phrase retirée parce qu'elle n'apporte aucun fait : https://www.pangram.com/fr/signs-of-ai-writing
- Tiret cadratin, remplacé par une virgule : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative
- Émoji en tête de chaque puce (« Affixing emoji at the beginning of section titles or list entries »), émojis retirés, puces gardées : https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre de la page, puces de bénéfices (gardées, sans émoji), tableau d'offres s'il y en a un, prix et conditions, appel à l'action impératif, mentions légales.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type page_web --compare avant.md
```
