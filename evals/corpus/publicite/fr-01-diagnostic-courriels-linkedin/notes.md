# Notes : publicite, fr, paire 1

Source : jeu d'exemples fictifs de la version 3.0, Publicité LinkedIn ou Meta, Paire 1 (FR) : Diagnostic des courriels, LinkedIn image unique. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Ouverture « Dans un monde où » sur un sujet général, remplacée par le calcul des 5 heures, qui tient dans les 150 premiers caractères : https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/
- Formule creuse « libérez votre potentiel », supprimée : https://www.eesel.ai/fr/blog/generateur-de-texte-publicitaire-ia
- Verbes répétés par ChatGPT « permettre » et « offrir », supprimés avec la phrase vide qui les portait : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Deux adjectifs enchaînés « claire et personnalisée », remplacés par « écrite pour votre entreprise » : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- « Pas seulement X, mais aussi Y » (« pas seulement un rapport, mais aussi un véritable levier de croissance »), phrase retirée parce qu'elle n'apporte aucun fait : https://www.pangram.com/fr/signs-of-ai-writing
- Émoji en tête de ligne (🚀, ✅), retirés; les puces de faits restent, sans émoji : https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Tiret cadratin, retiré en scindant la phrase : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative
- Titre à trous « The AI-powered [X] for modern [Y] » (« La solution propulsée par l'IA pour les PME modernes »), remplacé par un titre qui dit l'offre et le prix : https://superdesign.dev/blog/fix-generic-ai-landing-page

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : étiquettes de champ (texte d'introduction ou principal, titre, bouton), bouton d'appel à l'action prédéfini et son impératif, puces de faits sans émoji, longueurs recommandées par la plateforme.

## Remarques de la source

Longueurs de l'Après : texte d'introduction, 144 caractères avant la liste; titre, 51 caractères sur 70.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 7, apres.md en compte 7.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type publicite --compare avant.md
```
