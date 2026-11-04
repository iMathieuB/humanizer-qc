# Notes : page_web, fr, paire 3

Source : jeu d'exemples fictifs de la version 3.0, Page web de service ou d'offre, Paire 3 (FR) : Saisie automatisée des factures fournisseurs. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Ouverture « Voici ce qu'il faut savoir », retirée du titre : https://www.pangram.com/fr/signs-of-ai-writing
- Formule creuse du « paysage numérique en constante évolution », supprimée : https://seranking.com/fr/blog/bon-prompt-chatgpt/
- Mot surutilisé mesuré « innovant » (Juzek 2026, presse française), supprimé : https://arxiv.org/html/2605.25358
- Adjectif « captivant » (famille de « captiver », premier mot surutilisé chez Juzek, et liste de Digitad), supprimé avec l'« expérience » qu'il qualifiait : https://arxiv.org/html/2605.25358 et https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Calques de l'anglais « adresser un enjeu » et « faire du sens », supprimés ou remplacés par « convient » : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr
- Tiret cadratin, supprimé avec le segment qu'il isolait : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative
- Ton aspirationnel (« Imaginez un avenir où... ce qui compte vraiment »), qui fait slogan plutôt que message, ramené à son seul fait (« Chaque facture trouve sa place. »), gardé comme paragraphe (règle dure 5) : https://arxiv.org/html/2512.03373v1
- Émoji en tête de chaque ligne du tableau : tableau gardé tel quel (élément protégé), conflit signalé dans Changements : https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre de la page, puces de bénéfices (gardées, sans émoji), tableau d'offres s'il y en a un, prix et conditions, appel à l'action impératif, mentions légales.

## Remarques de la source

Le tableau des trois offres est gardé : trois offres réelles avec volumes et prix ne sont pas une rangée de cartes automatique (https://superdesign.dev/blog/fix-generic-ai-landing-page). Les frais d'installation et l'engagement de 12 mois restent visibles.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 9, apres.md en compte 9.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type page_web --compare avant.md
```
