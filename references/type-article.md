# Type : Article de blogue SEO, GEO et AEO

Billet de blogue à indexer et à faire citer par les moteurs de réponse, en français ou en anglais. Script : `--type article`. Indices de structure : H1, H2 et FAQ. Mode en conversation : interactif; en pipeline : un skill de publication ou de révision (section 7). Du fichier de langue, lis l'index et les sections de la section 5 seulement.

## 1. Éléments protégés

1. Structure H1, H2, H3 : un H1 avec le mot-clé primaire, des H2 et des H3 en nombre fixé par le gabarit de rédaction de l'auteur. Les moteurs de réponse extraient les intertitres et le paragraphe qui les suit.
2. La phrase-réponse de 15 à 20 mots sous chaque H2 : chaque H2 doit s'extraire seul.
3. La FAQ AEO : 6 à 8 questions en H3, réponse dans la première phrase, 80 à 150 mots, H2 « Questions fréquentes : … » qui porte le sujet.
4. Le gras sur les chiffres-clés : dose le gras de la prose seulement.
5. Les tableaux, dont celui des paliers, avec leurs plages « X à Y ».
6. Les liens et les sources inline avec leur année : citer ses sources aide la visibilité dans les moteurs de réponse (https://arxiv.org/html/2311.09735v3).
7. Chiffres, faits et citations au caractère près; seule la typographie OQLF change.
8. Les drapeaux [À VÉRIFIER] et [NEEDS SOURCE], visibles jusqu'à vérification.
9. Le CTA avec 👉 et son lien, et le libellé de l'offre repris tel quel du gabarit de l'auteur.
10. La ligne signature du pied de page (en italique ou en gras : nom de l'entreprise, tiret cadratin, puis une courte accroche), exception déclarée `footer-dash`, seul tiret cadratin permis, automatique avec `--type article` (une seule ligne signature, aucun paramètre `exceptions=` à passer).
11. La ligne « Publié le … | Par … » sous le H1 : métadonnées.
12. Le front matter YAML et le bloc « NE PAS PUBLIER » (données d'injection). Un tiret dans les champs publiés `title` et `meta_description` se corrige comme une retouche typographique; un tiret ailleurs dans le front matter ou dans le bloc « NE PAS PUBLIER » reste tel quel (constat `warning`).
13. Le texte standard de l'auteur (présentation de l'entreprise, paliers, CTA standard), sauf ses tirets, qui sortent, et le H2 du CTA, qui prend un deux-points.
14. Les anecdotes de mandats anonymisées : expertise de première main; ne rends jamais un cas plus identifiable.
15. Les termes techniques gardés en anglais (workflow, ERP, ROI, agent) : usage B2B québécois.
16. Les entités nommées (Montréal, PME, programmes, organismes) : les passages cités en sont denses.

## 2. Structures légitimes à ne pas signaler

- H2 en question suivi tout de suite de sa réponse (neutralise P47 et P53 pour l'intertitre).
- Phrase de définition en tête de chaque H2, même d'allure gabarit (neutralise P59).
- Court résumé de tête qui donne la conclusion (neutralise P44 et P53).
- Langage définitif « X est … » : ne l'adoucis pas (neutralise P61).
- Tableaux comparatifs et listes dans les sections techniques (neutralise P43 et P16).
- Gras sur les chiffres-clés et sur peu d'énoncés critiques (neutralise P15 et P57 pour les chiffres).
- Mot-clé primaire répété 2 ou 3 fois, dont H1, premier H2 et méta-description (neutralise P45).
- Plan Accroche, Problème, Normalisation, Décryptage, Implications, Solution, Positionnement, CTA, FAQ réelle et visible (neutralise P59).
- CTA explicite avec 👉 (neutralise P18 et P70 pour cette ligne).
- Prose claire et fluide : elle aide la visibilité.

## 3. Tics propres au type

- Ouverture interchangeable (« Dans le paysage numérique actuel… »). https://textcortex.com/fr/post/%C3%A9diter-contenu-ia
- Transition de navigation (« Maintenant que nous avons vu X, passons à Y »); paragraphe que n'importe quel autre blogue publierait tel quel; affirmation sans donnée ni source. https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content
- Article qui résume ce que d'autres disent; longueur gonflée pour une cible. https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Section « Conclusion » par réflexe, résumé en fin de section; section « Défis » à formule fixe qui finit en note positive; majuscule à chaque mot des intertitres; gras semé dans la prose. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- « Plonger dans », « tirer parti », « vaste tapisserie » (liste d'éditeur, à dater). https://www.eesel.ai/fr/blog/how-to-edit-ai-written-blog-posts
- Bourrage de mots-clés au-delà de 1 à 2 %; ton persuasif plaqué. https://arxiv.org/html/2311.09735v3
- Deux-points d'annonce dans une phrase de corps, surtout dans une phrase ajoutée après une passe de révision (permis dans les H2 et H3). Règle maison du skill.
- Introduction qui annonce le plan; FAQ aux questions que personne ne pose; H2 symétriques. Hypothèse non sourcée, ne pas traiter comme établie (à signaler en audit seulement).

## 4. Registre

Écrit vivant; titres porteurs d'un verbe fort et d'un résultat, 12 mots au plus; aucune locution conversationnelle dans un titre ou un intitulé de colonne. Ton expert et direct pour un dirigeant de PME pressé; vouvoiement. Un profil de voix (`voix-auteur.md`) ou un échantillon de l'auteur l'emporte sur ce registre par défaut.

## 5. Patrons prioritaires

(fr) : patterns-fr.md seulement; (en) : patterns-en.md seulement; sinon les deux.

- P54 Tiret cadratin en français (fr); P14 Em dashes (and en dashes): cut them (en)
- P51 Vocabulaire gonflé en français (fr); P07 Overused "AI vocabulary" words (en)
- P40 Nominalisations
- P15 Overuse of boldface (en)
- P57 Mise en forme de clavardage (fr)
- P47 Reformulation de la question (fr)
- P61 Style impersonnel et consensuel (fr)
- P63 « Non seulement X, mais aussi Y » (fr)
- P44 Résumé en fin de section
- P48 Clôture de dissertation (fr)
- P58 Majuscules superflues dans les titres (fr); P17 Title case in headings (en)
- P56 Typographie non québécoise ou incohérente (fr)
- P46 Ouverture « Dans un monde où »
- P50 Connecteurs et formules de liaison lourds (fr)
- P53 Annonces et survols en français (fr)
- P81 Phrase trop longue à l'écrit, P82 Virgules sans fonction, P83 Phrase sans verbe conjugué (fr); P81 et P82 (en)

## 6. Seuils du script pour ce type

| Seuil | article |
|---|---|
| Densité vocabulaire, `warning` au-delà (pour 1 000 mots) | fr 6, en 8 |
| Triades, `warning` au-delà (pour 1 000 mots) | 3 |
| Staccato : phrases consécutives de 3 mots ou moins | 3, `warning` |
| CV minimal des phrases (si 12 phrases ou plus) | 0,35 |
| Phrase longue, mots | 30, `warning` |
| Virgules dans une phrase, au-delà de | 3, `warning` |
| Phrase sans verbe conjugué (français) | `warning` |
| Gras non numérique, `warning` au-delà (pour 1 000 mots) | 4 |
| Listes à intitulé en gras | `warning` |
| Émojis | 👉 permis une fois; tout autre émoji `warning` |
| `!` : `warning` à partir de | 2 |
| Longueur par section (caractères) | aucun |

Ces seuils sont ceux de verif_humanizer.py; en cas d'écart, le script fait foi.

## 7. Ce que les pipelines attendent

- **Skill de publication** : humanizer passe avant l'injection dans le CMS, un appel par langue (FR et EN), après une copie de sauvegarde des originaux. Si une passe de révision de fond a lieu, elle passe avant; humanizer reste la dernière passe, refaite après tout changement. Zéro tiret sauf `footer-dash`; dans un H2 ou un H3, le tiret devient « : » (« ### Étape 1 : prise de l'appel »); dans le H1, le segment après le tiret passe entre parenthèses; « e-mail » devient « courriel », guillemets « », plages « X à Y »; grep final des deux tirets : seul le pied de page reste.
- **Gabarit de rédaction** : il fixe la structure de la section 1 (par exemple le mot-clé dans 3 questions de FAQ au moins, une méta-description de 150 à 160 caractères); n'en change pas la longueur.
- **Passe de révision de fond** : toute phrase ajoutée, même à la demande de l'auteur, repasse par humanizer avant de lui être montrée. Ne défais aucune de ses décisions (régime de titre, phrase-réponse, H2 de FAQ, CTA). Une dictée s'applique à la lettre.
- **Révision d'une page déjà publiée** : `passages=` sur la prose ajoutée, aucun chiffre nouveau.

## 8. Liste de contrôle

- [ ] Aucun tiret cadratin ni demi-cadratin, sauf la ligne signature?
- [ ] Les H2 et H3 qui avaient un tiret ont-ils un deux-points?
- [ ] Le nombre et l'ordre des H1, H2 et H3 sont-ils identiques à l'entrée?
- [ ] Chaque H2 commence-t-il encore par sa phrase-réponse autonome?
- [ ] La FAQ garde-t-elle toutes ses questions, réponse en première phrase?
- [ ] Chiffres, sources, liens et drapeaux [À VÉRIFIER] sont-ils identiques à l'entrée?
- [ ] Le gras des statistiques et le 👉 du CTA sont-ils toujours là?
- [ ] Les tableaux sont-ils intacts, avec des plages « X à Y »?
- [ ] « e-mail » est-il devenu « courriel », et les guillemets français sont-ils « »?
- [ ] L'ouverture entre-t-elle dans le sujet sans formule ni annonce du plan?
- [ ] Aucune section ne finit-elle sur un résumé d'elle-même?
- [ ] Aucun deux-points d'annonce ajouté dans une phrase de corps?
- [ ] Chaque paragraphe tient-il sur une ligne, et leur nombre est-il le même qu'à l'entrée?
- [ ] Aucune phrase de plus de 30 mots, aucune virgule sans fonction, un verbe conjugué dans chaque phrase?

## 9. Exemple court

Exemple fictif, abrégé (paire `evals/corpus/article/fr-02-agent-tri-courriels`).

**Avant**
> Maintenant que nous avons vu pourquoi la boîte de réception déborde, passons à la solution. Un agent de tri de courriels est un outil innovant qui permet non seulement de classer les messages, mais aussi de préparer des réponses. Par ailleurs, il lit chaque courriel entrant, le range dans l'un de 4 dossiers et rédige un brouillon pour ceux qui demandent une réponse.

**Après**
> Un agent de tri de courriels est un programme qui lit chaque courriel entrant, le range dans l'un de 4 dossiers et rédige un brouillon pour ceux qui demandent une réponse.

Corrigés : transition de navigation (P53), « innovant » (P51), « non seulement… mais aussi » (P63), connecteur (P50). Gardés : langage définitif, le chiffre 4, un paragraphe.
