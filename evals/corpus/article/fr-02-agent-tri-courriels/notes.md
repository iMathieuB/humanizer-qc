# Notes : article, fr, paire 2

Source : jeu d'exemples fictifs de la version 3.0, Article de blogue SEO, GEO et AEO, Paire 2 (FR) : définition d'un agent de tri de courriels. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Transition de navigation : « Maintenant que nous avons vu..., passons à... » (https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content).
- Adjectif surutilisé mesuré en français : « innovant » (https://arxiv.org/html/2605.25358).
- Construction « non seulement X, mais aussi Y » (https://www.pangram.com/fr/signs-of-ai-writing).
- Connecteurs en série : « Par ailleurs », « De plus », « Dans cette optique », « ainsi » (https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).
- Style impersonnel et conditionnel : « il pourrait être pertinent d'envisager » remplacé par une recommandation à la première personne (https://ar5iv.labs.arxiv.org/html/2306.05871).
- Calque de l'anglais : « adresser la surcharge » (https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr; définition de l'emprunt, https://vitrinelinguistique.oqlf.gouv.qc.ca/25444/les-emprunts-a-langlais/typologie-des-emprunts).
- Triade de clôture : « rapidité, fiabilité et tranquillité d'esprit » (https://www.pangram.com/fr/signs-of-ai-writing).
- Espace avant le point d'interrogation dans l'intertitre (https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).

## Structures conservées

H2 en question, langage définitif en première phrase (« est un programme qui »), chiffres de l'exemple.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 2, apres.md en compte 2.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type article --compare avant.md
```
