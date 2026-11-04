# Notes : chronique, fr, paire 1

Source : jeu d'exemples fictifs de la version 3.0, Script de chronique vidéo parlée, Paire 1 (FR) : relances de factures impayées. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- **Ouverture « Dans un monde où »** : remplacée par le fait chiffré du cas. Source : https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/
- **Survol qui annonce le programme** (« nous allons voir trois choses ») : supprimé; l'accroche reprend un fait déjà présent dans le segment du coût. Source : https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- **Adjectifs gonflés** (« crucial », « essentiel ») : supprimés, le chiffre porte l'enjeu. Sources : https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/ et https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- **Formule de liaison « Il est important de noter »** : supprimée. Source : https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/
- **Tiret cadratin** : l'incise devient une phrase à part. Source : https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative
- **Point-virgule et deux-points dans un texte dit** : remplacés par des points, une idée par phrase. Sources : https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/ et https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/
- **Nominalisations** (« la mise en place », « l'élimination ») : remplacées par des verbes conjugués, sans « toutes seules » ni « automatiquement », promesses cachées dans la grammaire. Source : https://arxiv.org/abs/2411.18382v1
- **Appel à l'action générique** (« abonnez-vous pour plus de contenu ») : aucune action propre au sujet dans la source, donc rien d'inventé; « N'oubliez pas de » retiré, le rappel gardé (règle dure 5) et signalé dans Ce qui sonne encore IA. Source : https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : codes temporels, titres de segment et lignes de régie (▶), identiques d'une version à l'autre. Secteur retiré des deux fichiers (l'incise ne garde que « 22 employés »).

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 9, apres.md en compte 9.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type chronique --compare avant.md
```
