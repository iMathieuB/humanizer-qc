# Notes : chronique, fr, paire 3

Source : jeu d'exemples fictifs de la version 3.0, Script de chronique vidéo parlée, Paire 3 (FR) : saisie des soumissions chez un couvreur. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- **Hésitations mécaniques** (« Euh... vous savez... hum ») : supprimées, elles sonnent ajoutées après coup plutôt que naturelles. Source : https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- **Ouverture « Dans le monde actuel »** : remplacée par le chiffre du cas. Source : https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- **Calques de l'anglais** (« adresser la question », « faire du sens ») : supprimés ou remplacés par « peut servir ». Source : https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr
- **Formule « Il est crucial de comprendre »** : supprimée. Source : https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/
- **Typographie non québécoise** (espace avant « ? » et « ! », symbole du dollar à gauche) : dollar placé à droite après une espace, plus d'espace parasite. Source : https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles
- **Participe présent et imparfait dans un texte dit** (« employant », « demandant », « représentait ») : remplacés par le présent et des phrases courtes. Source : https://pedagogie.ac-toulouse.fr/emi/node/1198
- **Style impersonnel au conditionnel** (« Il pourrait être pertinent d'envisager ») : remplacé par une recommandation au « je ». Source : https://ar5iv.labs.arxiv.org/html/2306.05871
- **Tiret cadratin** : remplacé par une phrase à part. Source : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : codes temporels, titres de segment et lignes de régie (▶), identiques d'une version à l'autre.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 8, apres.md en compte 8.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type chronique --compare avant.md
```
