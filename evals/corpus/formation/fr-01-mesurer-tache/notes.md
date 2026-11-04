# Notes : formation, fr, paire 1

Source : jeu d'exemples fictifs de la version 3.0, Matériel de formation, Paire 1 (FR) : mesurer une tâche avant de l'automatiser. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Résidu de consigne adressée au modèle : « Développe toutes les sections. Sois plus détaillé et précis. », transposition du cas « expand on all areas. Be more detailed and specific. » trouvé dans des notes de cours (https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/). Supprimé.
- Ouverture interchangeable : « Dans un monde où [...] à un rythme effréné » (https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/). Retirée; la phrase garde son seul fait.
- Adjectifs gonflés : « crucial », « essentielle » (https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).
- Nominalisations : « La mise en place d'un relevé permet l'identification du geste » (https://www.slate.fr/tech-internet/intelligence-artificielle-ia-chatbot-chatgpt-texte-litterature-internet-ecriture; plus de noms, moins de verbes : https://www.letemps.ch/articles/chatgpt-a-son-propre-style-mais-pour-combien-de-temps). Devenu un impératif : « Nommez le geste ».
- Formule de liaison : « Il est important de noter que » (https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/).
- Tiret cadratin entre « l'identification du geste » et « un verbe » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Ton générique qui ignore le vécu de l'équipe : encadré « la mesure est essentielle » et exercice « une tâche de votre choix » sans lien avec l'exemple (https://360learning.com/fr/blog/generation-contenus-formation-ia/). Encadré et exercice gardés tels quels (éléments protégés, aucun détail fourni par l'auteur) et signalés dans Ce qui sonne encore IA.
- Clôture « En conclusion » qui résume ce qui précède (https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr). Ramenée à une consigne courte, gardée comme paragraphe (règle dure 5).

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : titre du module, objectifs (« à la fin de ce module, vous serez capable de », ou « By the end of this module, you will be able to »), étapes, encadré « À retenir » s'il y en a un, exercice.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 10, apres.md en compte 10.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type formation --compare avant.md
```
