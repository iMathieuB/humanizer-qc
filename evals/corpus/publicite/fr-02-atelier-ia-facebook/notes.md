# Notes : publicite, fr, paire 2

Source : jeu d'exemples fictifs de la version 3.0, Publicité LinkedIn ou Meta, Paire 2 (FR) : Atelier IA pour une équipe, Meta fil Facebook. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Formule du « paysage numérique en constante évolution », supprimée : https://seranking.com/fr/blog/bon-prompt-chatgpt/
- Adjectifs gonflés « essentielle » et « cruciale », supprimés : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- « Innovant », mot mesuré comme surutilisé en français (Juzek 2026), retiré du texte et du titre : https://arxiv.org/html/2605.25358
- Verbe répété par ChatGPT « favoriser » et nominalisation « la mise en place d'une démarche d'appropriation des outils », remplacés par un verbe conjugué (« apprendre à votre équipe à se servir des outils ») : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/ et https://arxiv.org/abs/2411.18382v1
- Triade de fragments « Concret. Pratique. Efficace. », vraie de n'importe quel atelier, supprimée : https://www.pangram.com/fr/signs-of-ai-writing et https://superdesign.dev/blog/fix-generic-ai-landing-page
- Empilement d'impératifs et de points d'exclamation (« Obtenez votre place dès maintenant ! Profitez-en ! »), retiré du texte; l'impératif reste dans le bouton prédéfini « S'inscrire » : https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features et https://arxiv.org/html/2601.04925v1
- Typographie non québécoise (espace avant le point d'exclamation, dollar à gauche, point décimal), corrigée selon l'OQLF : 2 400 $ et 300 $ : https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles
- Tirets cadratins en incise, retirés avec l'incise : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : étiquettes de champ (texte d'introduction ou principal, titre, bouton), bouton d'appel à l'action prédéfini et son impératif, puces de faits sans émoji, longueurs recommandées par la plateforme.

## Remarques de la source

Longueurs de l'Après : texte principal, 150 caractères (fourchette de 50 à 150); titre, 22 caractères sur 27. Vérification : 2 400 $ divisé par 8 personnes donne 300 $ par personne.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 3, apres.md en compte 3.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type publicite --compare avant.md
```
