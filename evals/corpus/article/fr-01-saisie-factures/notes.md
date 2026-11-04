# Notes : article, fr, paire 1

Source : jeu d'exemples fictifs de la version 3.0, Article de blogue SEO, GEO et AEO, Paire 1 (FR) : coût de la saisie manuelle des factures. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Majuscules superflues dans les titres : « Combien Coûte Vraiment Le Traitement... » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; casse de titre anglaise, https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style).
- Ouverture interchangeable : « Dans le paysage numérique actuel qui évolue rapidement » (https://textcortex.com/fr/post/%C3%A9diter-contenu-ia; https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content). Retirée; la phrase garde son seul fait (l'enjeu pour les PME québécoises).
- Adjectifs gonflés : « crucial », « essentiel » (https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).
- Formule de liaison : « Il est important de noter que » (https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/).
- Abus du gras : gras retiré des adjectifs « crucial » et « essentiel », gardé sur les six chiffres, élément protégé de type-article.md (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Tiret cadratin : entre « Les chiffres parlent d'eux-mêmes » et « et ils sont révélateurs » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Typographie non conforme à l'OQLF : dollar à gauche, point décimal, espace avant « ? » et « ! » (https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles; espaces systématiques perçues comme signe, https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).
- Nominalisations : « La mise en place d'une automatisation permet l'optimisation de... et la réduction des... » (https://arxiv.org/abs/2411.18382v1).

## Structures conservées

H2 en forme de question, gras gardé sur chaque chiffre, ordre des faits de avant.md.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 2, apres.md en compte 2.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type article --compare avant.md
```
