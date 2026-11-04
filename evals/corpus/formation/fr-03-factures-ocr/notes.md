# Notes : formation, fr, paire 3

Source : jeu d'exemples fictifs de la version 3.0, Matériel de formation, Paire 3 (FR) : vérifier les factures lues par OCR. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Ouverture calquée « Plongez dans » (https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/).
- Adjectif surutilisé « innovante », famille « innovant » mesurée sur du français de presse (https://arxiv.org/html/2605.25358).
- Surutilisation de « notamment », deux fois en trois phrases (https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr; statut perçu, chiffre sans source primaire).
- Style impersonnel et conditionnel : « Il pourrait être pertinent d'envisager [...] ce qui représenterait » (https://ar5iv.labs.arxiv.org/html/2306.05871). Remplacé par un constat neutre, sans trancher à la place de l'auteur.
- Section « Défis » du type « malgré ses nombreux avantages, [sujet] fait face à des défis », finie sur une note vaguement positive (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Supprimée, sans rien ajouter à sa place.
- Distracteurs manifestement faux (« 4 000 », « aucune, l'OCR est parfait ») qui ne reflètent pas les erreurs réelles des apprenants (https://arxiv.org/html/2404.02124; https://elearningindustry.com/why-pedagogy-should-drive-ai-course-generation-not-the-other-way-around). Gardés tels quels : énoncé et réponses protégés (type-formation.md); signalés.
- Tiret cadratin entre « 40 à vérifier » et « notamment » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Clôture « J'espère que ce module vous aidera ! », avec espaces non conformes à l'OQLF avant « ? » et « ! » (https://ar5iv.labs.arxiv.org/html/2306.05871; https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles). Supprimée.

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre du module, objectifs (« à la fin de ce module, vous serez capable de », ou « By the end of this module, you will be able to »), étapes, encadré « À retenir » s'il y en a un, exercice.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 6.

Exemption : paragraph_count.

La réécriture de référence retire des paragraphes entiers de remplissage (slogans, survol, clôture), ce que la règle dure 5 du skill interdit. Les tests du corpus ignorent la seule comparaison du nombre de paragraphes pour cette paire; chiffres, gras et liens restent comparés. Ce n'est pas un modèle de la règle dure 5 : un cas d'evals bâti sur elle exige le compte de avant.md.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type formation --compare avant.md
```
