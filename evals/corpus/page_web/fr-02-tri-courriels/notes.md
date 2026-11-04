# Notes : page_web, fr, paire 2

Source : jeu d'exemples fictifs de la version 3.0, Page web de service ou d'offre, Paire 2 (FR) : Tri automatisé des courriels. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Formule de liaison « Il est important de noter que », supprimée : https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/
- Phrase creuse de langue de bois (« un défi majeur pour les entreprises »), remplacée par le calcul qui chiffre le problème : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative
- Phrase à base de noms (« la mise en place d'une optimisation complète du traitement des demandes »), supprimée parce que le paragraphe suivant dit concrètement ce que fait l'agent : https://arxiv.org/abs/2411.18382v1
- Verbes répétés par ChatGPT « assurer » et « répondre aux besoins », supprimés : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Bénéfices interchangeables (« Gagnez du temps. Travaillez mieux. Grandissez plus vite. », équivalent de « Save time. Work smarter. Scale faster. »), retirés pour leur contenu, pas pour leur forme courte : https://superdesign.dev/blog/fix-generic-ai-landing-page
- Connecteurs « Par ailleurs » et « De plus », supprimés : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Clôture « En somme » suivie d'une conclusion vague et creuse de portée générale, supprimée : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr et https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre de la page, puces de bénéfices (gardées, sans émoji), tableau d'offres s'il y en a un, prix et conditions, appel à l'action impératif, mentions légales.

## Remarques de la source

La mention « conformément à la Loi 25 » est gardée telle quelle : les mentions de conformité ne sont pas retirées (https://dailyhive.com/vancouver/ai-ads-metro-vancouver-legal-standards).

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 5.

Exemption : paragraph_count.

La réécriture de référence retire des paragraphes entiers de remplissage (slogans, survol, clôture), ce que la règle dure 5 du skill interdit. Les tests du corpus ignorent la seule comparaison du nombre de paragraphes pour cette paire; chiffres, gras et liens restent comparés. Ce n'est pas un modèle de la règle dure 5 : un cas d'evals bâti sur elle exige le compte de avant.md.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type page_web --compare avant.md
```
