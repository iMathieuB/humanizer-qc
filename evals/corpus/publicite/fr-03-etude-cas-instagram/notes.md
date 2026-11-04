# Notes : publicite, fr, paire 3

Source : jeu d'exemples fictifs de la version 3.0, Publicité LinkedIn ou Meta, Paire 3 (FR) : Cas d'un cabinet comptable, Meta fil Instagram. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Ouverture « Voici ce qu'il faut savoir », supprimée; le texte commence par le cas : https://www.pangram.com/fr/signs-of-ai-writing
- Calques de l'anglais « adresser son problème » et « ça fait du sens », retirés : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr
- Flèche vers la droite et coche verte en tête de ligne (➡️, ✅), retirées; les chiffres passent dans deux phrases : https://www.pangram.com/fr/signs-of-ai-writing et https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Connecteur « Il est important de noter que », supprimé : https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/
- Verbes répétés par ChatGPT « permettre » et « assurer » : « permet d'assurer » ramené à « assure » : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Clôture « En somme » suivie d'une phrase vague et générale, supprimée : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr et https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA
- Tiret cadratin, retiré avec la remarque qu'il introduisait : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : étiquettes de champ (texte d'introduction ou principal, titre, bouton), bouton d'appel à l'action prédéfini et son impératif, puces de faits sans émoji, longueurs recommandées par la plateforme.

## Remarques de la source

Longueurs de l'Après : première phrase du texte principal, 122 caractères sur 125 recommandés, le reste suit après la troncature; titre, 36 caractères sur 40. Vérification : 60 courriels à 2 minutes donnent 120 minutes, soit 2 heures par jour, et 10 heures sur cinq jours.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 4.

Exemption : paragraph_count.

La réécriture de référence retire des paragraphes entiers de remplissage (slogans, survol, clôture), ce que la règle dure 5 du skill interdit. Les tests du corpus ignorent la seule comparaison du nombre de paragraphes pour cette paire; chiffres, gras et liens restent comparés. Ce n'est pas un modèle de la règle dure 5 : un cas d'evals bâti sur elle exige le compte de avant.md.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type publicite --compare avant.md
```
