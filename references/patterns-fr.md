# Patrons en français du Québec (humanizer 3.0.0)

Lis l'index, puis seulement les patrons utiles : Grep sur `^### Pnn` (par exemple `^### P51`). Ne lis pas le fichier en entier. Niveaux : `mesure` (étude ou mesure quantitative), `guide` (guide éditorial ou institutionnel, dont Wikipédia), `blogue` (billet d'éditeur ou de praticien), `maison` (règle du skill : formule relevée par sa propre évaluation, ou rejet documenté dans le profil de voix de l'auteur, qui passe avant les trois autres pour sa voix). Identifiants partagés avec `patterns-en.md`. Vérification : constat de `scripts/verif_humanizer.py`, ou `lecture`. Un tic isolé ne prouve rien; cherche les grappes. Cette passe rapproche le texte de la voix de son auteur : ce n'est pas un outil d'indétectabilité.

Sections : index, voix et souffle, patrons communs, patrons propres au français, règles maison de la 3.1, particularités québécoises et typographie, faux positifs en français, signes humains à préserver.

## Index

| ID | Patron | Niveau | Types | Vérification |
|---|---|---|---|---|
| P40 | Nominalisations | mesure | tous | lecture |
| P42 | Résidus de génération | guide | tous | kill_list/structure |
| P43 | Petits tableaux et titres vides | guide | article, page_web, formation | lecture |
| P44 | Résumé en fin de section | guide | article, formation, chronique | lecture |
| P45 | Contenu répétitif | mesure | article, page_web | lecture |
| P46 | Ouverture « Dans un monde où » | blogue | article, page_web, publicite, chronique | kill_list/ouvertures |
| P47 | Reformulation de la question | mesure | article, formation | lecture |
| P48 | Clôture de dissertation | guide | article, page_web, formation | kill_list/clotures |
| P49 | Restes de conversation et flatterie | mesure | tous | lecture |
| P50 | Connecteurs et formules de liaison lourds | blogue | tous | kill_list/formules |
| P51 | Vocabulaire gonflé en français | mesure | tous | kill_list/vocabulaire |
| P52 | Calques de l'anglais | guide | tous | lecture |
| P53 | Annonces et survols en français | blogue | article, chronique, formation | lecture |
| P54 | Tiret cadratin en français | guide | tous | dash |
| P55 | Point-virgule et deux-points en série | blogue | chronique, article | lecture |
| P56 | Typographie non québécoise ou incohérente | guide | tous | typography_fr, curly_quotes |
| P57 | Mise en forme de clavardage | mesure | page_web, publicite, article, formation | kill_list/ponctuation, bold_density, inline_header_list, emoji |
| P58 | Majuscules superflues dans les titres | guide | article, page_web, formation | title_case |
| P59 | Plan gabarit | guide | page_web, formation, article | lecture |
| P60 | Langue de bois et phrases creuses | guide | page_web, article, publicite | lecture |
| P61 | Style impersonnel et consensuel | mesure | article, page_web, chronique | hedging_stack |
| P62 | Aucun détail propre au lecteur | blogue | formation, article, page_web | lecture |
| P63 | « Non seulement X, mais aussi Y » | mesure | tous | not_x_but_y |
| P64 | Triades en français | mesure | publicite, page_web, formation | triad, staccato |
| P65 | Participe présent en fin de phrase | blogue | article, page_web, chronique | lecture |
| P66 | Verbes passe-partout (permettre, offrir, assurer) | blogue | page_web, publicite, formation | lecture |
| P67 | Hésitations mécaniques | blogue | chronique | lecture |
| P68 | Phrase trop longue pour une respiration | guide | chronique | long_sentence |
| P69 | Ton enjoué et éloge du sujet | blogue | chronique, publicite | lecture |
| P70 | Appel à l'action générique | blogue | chronique, publicite | lecture |
| P71 | Titre à trous | blogue | publicite, page_web | lecture |
| P72 | Slogans en fragments et impératifs empilés | blogue | publicite | exclamation |
| P73 | Formule aspirationnelle creuse | blogue | publicite, page_web | lecture |
| P74 | Distracteurs invraisemblables | mesure | formation | lecture |
| P81 | Phrase trop longue à l'écrit | maison | tous | long_sentence |
| P82 | Virgules sans fonction | maison | tous | comma_load |
| P83 | Phrase sans verbe conjugué | maison | article, page_web, formation, general | verbless |

## Voix et souffle

Accorde le texte à la voix de son auteur; ne l'imite pas.

Si `references/voix-auteur.md` existe (profil de voix facultatif écrit par l'utilisateur), suis-le.

Pour un autre auteur, calibre-toi sur son échantillon : longueur et variété des phrases, pronoms, vouvoiement ou tutoiement, ponctuation, mots favoris.

Reprends ses proportions, pas ses tics.

Une phrase retirée ne laisse pas de trou : rattache la précédente et la suivante (parce que, alors, mais, donc).

Jamais de phrase de remplissage pour combler un vide : coupe, ou reprends un fait déjà présent dans le texte.

Hors script parlé, pas de suite de phrases courtes juxtaposées ni de paragraphe réduit à un fragment : garde la variation de longueur de l'auteur.

Phrase par phrase, sur tout brouillon de l'assistant : une phrase de plus de 30 mots se coupe au point (P81), une virgule que la phrase ne réclame pas se retire (P82), et hors script parlé chaque phrase a son verbe conjugué (P83).

Un texte de référence, une politique ou une fiche technique garde une voix neutre, sans opinion ni « je ».

Sans échantillon, vise un français du Québec clair et direct, au registre du fichier de type.

## Patrons communs aux deux langues

Aussi dans `patterns-en.md`, mêmes identifiants et mêmes sources.

### P40. Nominalisations

Niveau : mesure · Origine : recherche · Types : tous · Vérification : lecture

**Repère.** Phrases bâties sur des noms d'action (« la mise en place de »), pauvres en verbes. En français, ChatGPT surutilise les noms et sous-utilise verbes et pronoms.

**Correction.** Remplace le nom d'action par un verbe conjugué avec un sujet qui agit.

**Avant**
> La mise en place d'une automatisation permet l'optimisation de la gestion des demandes de nos clients.

**Après**
> Une automatisation améliore la gestion des demandes de nos clients.

**Faux positif.** Intitulés, champs de formulaire et titres se nomment en groupe nominal.

**Sources.** https://arxiv.org/html/2410.16107; https://arxiv.org/abs/2411.18382v1; https://www.letemps.ch/articles/chatgpt-a-son-propre-style-mais-pour-combien-de-temps; https://www.slate.fr/tech-internet/intelligence-artificielle-ia-chatbot-chatgpt-texte-litterature-internet-ecriture

### P42. Résidus de génération

Niveau : guide · Origine : recherche · Types : tous · Vérification : kill_list/structure

**Repère.** Trous de gabarit (« [Nom de l'entreprise] »), consigne adressée au modèle, « en tant qu'IA », utm_source=chatgpt.com dans un lien.

**Correction.** Supprime le trou ou signale-le dans Changements; ne le remplis jamais avec une valeur inventée. Retire la consigne, nettoie les liens.

**Avant**
> Merci de votre confiance, [Nom du client]. Rendez-vous le 2026-XX-XX. Sois plus détaillé et précis.

**Après**
> Merci de votre confiance.

Dans Changements : date du rendez-vous manquante (2026-XX-XX), à fournir par l'auteur.

**Faux positif.** Un gabarit livré comme tel, champs à remplir annoncés.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://next.ink/article/71730/comment-tenter-didentifier-textes-emanant-dintelligences-artificielles-generatives; https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/

### P43. Petits tableaux et titres vides

Niveau : guide · Origine : recherche · Types : article, page_web, formation · Vérification : lecture

**Repère.** Tableau de deux ou trois lignes qui tiendrait en une phrase; titre qui ne contient que d'autres titres.

**Correction.** Signale en audit ou dans Ce qui sonne encore IA; ne fusionne ni ne convertis un tableau sans l'accord de l'auteur. Un titre vide se signale aussi : n'ajoute aucune phrase dessous.

**Avant**
> | Option | Prix |
> |---|---|
> | De base | 49 $ par mois |

**Après**
> Tableau gardé tel quel. Puce de Ce qui sonne encore IA : tableau d'une seule rangée, une phrase suffirait; à convertir seulement avec l'accord de l'auteur.

**Faux positif.** Un tableau comparatif à plusieurs critères (protégé en AEO).

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA

### P44. Résumé en fin de section

Niveau : guide · Origine : recherche · Types : article, formation, chronique · Vérification : lecture

**Repère.** Section qui finit en reformulant son idée centrale (« En résumé, ... », « Bref, ... »).

**Correction.** Supprime le résumé; la section finit sur son dernier fait utile.

**Avant**
> Monter une soumission à la main prend 25 minutes, et 8 avec le gabarit. Bref, chronométrer vos soumissions révèle vos économies.

**Après**
> Monter une soumission à la main prend 25 minutes, et 8 avec le gabarit.

**Faux positif.** Le récapitulatif annoncé d'un module de formation.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr

### P45. Contenu répétitif

Niveau : mesure · Origine : recherche · Types : article, page_web · Vérification : lecture

**Repère.** Même idée redite ailleurs avec d'autres mots (47 % plus susceptible d'être généré, et indice que les lecteurs emploient à bon escient).

**Correction.** Garde la meilleure formulation là où elle sert et coupe les reprises.

**Avant**
> L'automatisation fait gagner du temps. Grâce à elle, votre équipe gagne des heures. Ce gain de temps change tout.

**Après**
> L'automatisation fait gagner des heures à votre équipe.

**Faux positif.** La FAQ AEO, qui reprend le corps exprès.

**Sources.** https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

### P46. Ouverture « Dans un monde où »

Niveau : blogue · Origine : recherche · Types : article, page_web, publicite, chronique · Vérification : kill_list/ouvertures

**Repère.** Ouverture interchangeable sur l'époque : « Dans un monde où », « Dans le monde actuel ».

**Correction.** Commence par le fait, le chiffre ou la situation précise du lecteur.

**Avant**
> Dans un monde où la technologie évolue à un rythme effréné, la gestion des courriels est devenue un enjeu crucial pour les PME.

**Après**
> La gestion des courriels est devenue un enjeu pour les PME.

**Faux positif.** Une ouverture datée et propre au sujet.

**Sources.** https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/; https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content; https://textcortex.com/fr/post/%C3%A9diter-contenu-ia; https://seranking.com/fr/blog/bon-prompt-chatgpt/

### P67. Hésitations mécaniques

Niveau : blogue · Origine : recherche · Types : chronique · Vérification : lecture

**Repère.** « euh », « vous savez », « hum » semés à intervalles réguliers dans un script écrit.

**Correction.** Retire-les; l'animateur hésitera de lui-même au tournage.

**Avant**
> Alors, euh... vous savez, ces relances, hum, ça prend du temps.

**Après**
> Ces relances prennent du temps.

**Faux positif.** La transcription fidèle d'une vraie conversation.

**Sources.** https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/

### P68. Phrase trop longue pour une respiration

Niveau : guide · Origine : recherche · Types : chronique · Vérification : long_sentence

**Repère.** Dans un texte dit, phrase à plusieurs subordonnées en « qui », « que », « parce que », ou allongée de participes et d'imparfaits.

**Correction.** Coupe en phrases d'une idée, au présent, qu'on dit d'un souffle.

**Avant**
> L'entreprise, qui recevait des demandes que personne ne triait parce que tout arrivait dans la même boîte, perdait des heures.

**Après**
> Toutes les demandes arrivent dans la même boîte. Elles restent sans tri. L'entreprise perd des heures.

**Faux positif.** Une phrase longue qui se dit bien, vérifiée à voix haute.

**Sources.** https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice; https://pedagogie.ac-toulouse.fr/emi/node/1198

### P69. Ton enjoué et éloge du sujet

Niveau : blogue · Origine : recherche · Types : chronique, publicite · Vérification : lecture

**Repère.** Enthousiasme constant et éloge du sujet : « absolument passionnant », « tout simplement remarquable ».

**Correction.** Retire l'éloge; laisse le résultat chiffré déjà présent faire l'effet.

**Avant**
> C'est absolument passionnant : ce projet est tout simplement remarquable! La première année, les relances ont fait rentrer 4 800 $ de factures en retard.

**Après**
> La première année, les relances ont fait rentrer 4 800 $ de factures en retard.

**Faux positif.** Une réaction sincère et précise, une fois, sur un résultat qui la mérite.

**Sources.** https://www.scientificamerican.com/podcast/episode/how-tools-like-notebooklm-create-ai-generated-podcasts; https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/

### P70. Appel à l'action générique

Niveau : blogue · Origine : recherche · Types : chronique, publicite · Vérification : lecture

**Repère.** « Abonnez-vous pour plus de contenu! », « N'oubliez pas de liker » en fin de script ou de publication.

**Correction.** Remplace par une action liée au sujet seulement si elle figure déjà dans le texte ou dans les règles de la série; sinon, coupe. Un CTA protégé se signale en Conflit et ne se remplace pas.

**Avant**
> Faites le même calcul avec vos propres relances cette semaine. Et n'oubliez pas de vous abonner pour plus de contenu!

**Après**
> Faites le même calcul avec vos propres relances cette semaine.

**Faux positif.** Un rappel prévu par les règles de la série.

**Sources.** https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026

### P71. Titre à trous

Niveau : blogue · Origine : recherche · Types : publicite, page_web · Vérification : lecture

**Repère.** Titre interchangeable du type « La solution propulsée par l'IA pour les PME modernes ».

**Correction.** Dis ce que l'offre livre, à qui, et en combien de temps ou à quel prix, avec les seuls faits déjà présents sur la page.

**Avant**
> La solution propulsée par l'IA pour les PME modernes
> Le service trie vos courriels avant 8 h. Installation en une semaine.

**Après**
> Vos courriels triés avant 8 h, installé en une semaine
> Le service trie vos courriels avant 8 h. Installation en une semaine.

**Faux positif.** Un titre de marque déjà établi.

**Sources.** https://superdesign.dev/blog/fix-generic-ai-landing-page

### P72. Slogans en fragments et impératifs empilés

Niveau : blogue · Origine : recherche · Types : publicite · Vérification : exclamation

**Repère.** Fragments vrais de n'importe quel produit et impératifs empilés avec points d'exclamation.

**Correction.** Remplace la série par le gain chiffré seulement si le chiffre figure déjà dans le texte; sinon, coupe la série et garde un seul impératif. L'impératif va au seul bouton d'appel à l'action; un CTA protégé se signale en Conflit et ne se remplace pas.

**Avant**
> Dix heures de saisie de moins par mois. Gagnez du temps. Travaillez mieux. Grandissez plus vite. N'attendez plus!

**Après**
> Dix heures de saisie de moins par mois.

**Faux positif.** Un seul impératif clair, ou le bouton prédéfini de la plateforme.

**Sources.** https://superdesign.dev/blog/fix-generic-ai-landing-page; https://arxiv.org/html/2601.04925v1; https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features

### P73. Formule aspirationnelle creuse

Niveau : blogue · Origine : recherche · Types : publicite, page_web · Vérification : lecture

**Repère.** « Libérez votre potentiel », « Imaginez un avenir où », « ce qui compte vraiment » : du slogan au lieu d'un message.

**Correction.** Remplace la promesse par le résultat concret déjà présent dans le texte.

**Avant**
> Imaginez un avenir où votre équipe libère tout son potentiel et arrête de recopier les bons de commande à la main.

**Après**
> Votre équipe arrête de recopier les bons de commande à la main.

**Faux positif.** Une projection chiffrée et datée (« dans six mois, le logiciel enverra vos relances »).

**Sources.** https://www.eesel.ai/blog/ai-ad-copy-generator; https://www.eesel.ai/fr/blog/generateur-de-texte-publicitaire-ia; https://arxiv.org/html/2512.03373v1

### P74. Distracteurs invraisemblables

Niveau : mesure · Origine : recherche · Types : formation · Vérification : lecture

**Repère.** Questions à choix multiples dont les mauvaises réponses ne tentent personne (« 5 minutes », « 1 million de minutes »).

**Correction.** Signale le distracteur invraisemblable (audit ou Ce qui sonne encore IA) et propose en note une piste fondée sur une erreur réelle d'apprenant (chiffre d'avant, étape oubliée). Ne modifie ni la question ni les réponses : énoncés et bonnes réponses sont protégés (`type-formation.md`).

**Avant**
> Combien d'heures le gabarit fait-il gagner par mois? a) 15 heures b) 5 minutes c) 1 million de minutes

**Après**
> Question inchangée. Note : b) et c) sont invraisemblables; piste à soumettre à l'auteur : un distracteur tiré du temps mesuré avant le gabarit.

**Faux positif.** Une question de mise en route, exprès très simple, en début de module.

**Sources.** https://arxiv.org/html/2404.02124; https://elearningindustry.com/why-pedagogy-should-drive-ai-course-generation-not-the-other-way-around

## Patrons propres au français

### P47. Reformulation de la question

Niveau : mesure · Origine : recherche · Types : article, formation · Vérification : lecture

**Repère.** Réponse qui reprend la question puis annonce une liste (« Voici quelques explications possibles : »).

**Correction.** Réponds dans la première phrase, puis donne les raisons.

**Avant**
> Il peut y avoir plusieurs raisons pour lesquelles vos soumissions tardent. Voici quelques explications possibles : la principale est que chaque prix est recopié à la main depuis le catalogue.

**Après**
> Vos soumissions tardent surtout parce que chaque prix est recopié à la main depuis le catalogue.

**Faux positif.** Un H2 en question suivi de la réponse directe : structure AEO voulue.

**Sources.** https://ar5iv.labs.arxiv.org/html/2306.05871

### P48. Clôture de dissertation

Niveau : guide · Origine : recherche · Types : article, page_web, formation · Vérification : kill_list/clotures

**Repère.** « En conclusion », « En résumé », « En somme », « Au final » suivis d'un résumé; conclusion « vague et creuse, de portée générale ».

**Correction.** Termine sur une action concrète ou sur le dernier fait utile, sans résumer.

**Avant**
> En conclusion, l'automatisation du tri des courriels représente une solution incontournable pour gagner en efficacité.

**Après**
> Automatiser le tri des courriels fait gagner en efficacité.

**Faux positif.** Un renvoi précis vers un professionnel quand le sujet l'exige (fiscalité, droit).

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA; https://ar5iv.labs.arxiv.org/html/2306.05871

### P49. Restes de conversation et flatterie

Niveau : mesure · Origine : recherche · Types : tous · Vérification : lecture

**Repère.** « C'est une excellente question », « Bien sûr! », « J'espère que cela vous aidera », « N'hésitez pas à me demander » dans un texte publié.

**Correction.** Supprime la formule sans la remplacer par une autre politesse.

**Avant**
> C'est une excellente question! Voici un aperçu : la facturation automatisée envoie chaque facture le jour où le travail est terminé. J'espère que cela vous aidera.

**Après**
> La facturation automatisée envoie chaque facture le jour où le travail est terminé.

**Faux positif.** Une réponse à un vrai client peut remercier et offrir de l'aide.

**Sources.** https://ar5iv.labs.arxiv.org/html/2306.05871; https://www.pangram.com/fr/signs-of-ai-writing

### P50. Connecteurs et formules de liaison lourds

Niveau : blogue · Origine : recherche · Types : tous · Vérification : kill_list/formules

**Repère.** « Il est important de noter que », « en outre », « par ailleurs », « dans cette optique », « notamment » en série. Non mesuré en français : l'accumulation alourdit.

**Correction.** Supprime la formule d'annonce. Garde un connecteur seulement s'il marque une vraie relation logique.

**Avant**
> Il est important de noter que, par ailleurs, cette méthode permet de gagner du temps et, en outre, de réduire les erreurs.

**Après**
> Cette méthode fait gagner du temps. Elle réduit aussi les erreurs.

**Faux positif.** Un « cependant » ou un « par ailleurs » isolé, surtout en registre soutenu.

**Sources.** https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/

### P51. Vocabulaire gonflé en français

Niveau : mesure · Origine : recherche · Types : tous · Vérification : kill_list/vocabulaire

**Repère.** Mots mesurés comme surutilisés dans la presse générée (captiver, palpable, habilement, innovant, nécessité); adjectifs perçus, non mesurés (crucial, essentiel, fondamental, indispensable).

**Correction.** Remplace l'adjectif par le fait déjà présent dans le texte qui justifie l'importance; sinon, supprime-le.

**Avant**
> Cet outil innovant offre une expérience captivante et joue un rôle crucial : il classe vos courriels en trois dossiers.

**Après**
> L'outil classe vos courriels en trois dossiers.

**Faux positif.** « Essentiel » ou « important » une fois, au sens propre. Ne traque pas mot à mot.

**Sources.** https://arxiv.org/html/2605.25358; https://www.it-connect.fr/comment-detecter-un-texte-genere-par-ia-nous-avons-teste-plusieurs-outils/

### P52. Calques de l'anglais

Niveau : guide · Origine : recherche · Types : tous · Vérification : lecture

**Repère.** Emprunts sémantiques et syntaxiques : « adresser un problème », « faire du sens », « supporter », « définitivement », « réaliser », « les prochaines trois semaines ».

**Correction.** Régler, être logique, appuyer, certainement, se rendre compte, les trois prochaines semaines.

**Avant**
> Nous allons adresser ce problème dans les prochaines trois semaines, ce qui fait du sens pour votre équipe.

**Après**
> On va régler ce problème d'ici trois semaines. C'est logique pour votre équipe.

**Faux positif.** Un calque de l'oral québécois propre à l'auteur, dans un script parlé.

**Sources.** https://vitrinelinguistique.oqlf.gouv.qc.ca/25444/les-emprunts-a-langlais/typologie-des-emprunts; https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr

### P53. Annonces et survols en français

Niveau : blogue · Origine : recherche · Types : article, chronique, formation · Vérification : lecture

**Repère.** « Voici ce qu'il faut savoir », « Plongez dans », « Aujourd'hui, nous allons voir trois choses ».

**Correction.** Supprime l'annonce et montre tout de suite.

**Avant**
> Aujourd'hui, nous allons voir trois choses : le coût réel, la solution et les résultats. Une PME passait 14 heures par mois à relancer des factures.

**Après**
> Une PME passait 14 heures par mois à relancer des factures.

**Faux positif.** Les objectifs d'apprentissage en tête d'un module.

**Sources.** https://www.pangram.com/fr/signs-of-ai-writing; https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/

### P54. Tiret cadratin en français

Niveau : guide · Origine : recherche · Types : tous · Vérification : dash

**Repère.** Tiret cadratin ou demi-cadratin en incise ou devant une chute (45 contre 5 par 10 000 mots selon Pangram, langue non précisée).

**Correction.** Virgules, parenthèses, deux-points ou phrase à part. Aucun tiret en sortie.

**Avant**
> Les chiffres parlent d'eux-mêmes — 40 heures par mois.

**Après**
> Les chiffres le montrent : 40 heures par mois.

**Faux positif.** L'OQLF admet le tiret pour mettre un passage en valeur; chez un autre auteur, sa présence ne prouve rien.

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8392388/tiret-cadratin; https://www.pangram.com/fr/signs-of-ai-writing

### P55. Point-virgule et deux-points en série

Niveau : blogue · Origine : recherche · Types : chronique, article · Vérification : lecture

**Repère.** Phrases enchaînées par des points-virgules. À l'oral, point-virgule et deux-points ne s'entendent pas.

**Correction.** Coupe en phrases d'une idée, terminées par un point.

**Avant**
> L'entreprise envoyait 140 relances par mois; chaque relance prenait 6 minutes; cela représente 14 heures par mois.

**Après**
> L'entreprise envoyait 140 relances par mois. Une relance prenait 6 minutes. Ça fait 14 heures par mois.

**Faux positif.** Le point-virgule bien employé dans un texte écrit; le soupçon vient d'un blogue.

**Sources.** https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/; https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/

### P56. Typographie non québécoise ou incohérente

Niveau : guide · Origine : recherche · Types : tous · Vérification : typography_fr, curly_quotes

**Repère.** Espace avant « ; ! ? », dollar à gauche, point décimal, mélange d'apostrophes droites et courbes.

**Correction.** Applique l'OQLF (section Particularités québécoises) avec une seule sorte d'apostrophe.

**Avant**
> Notre offre est simple ; elle est efficace ; écrivez-nous ! Tarif : $49.99

**Après**
> Notre offre est simple et efficace. Écrivez-nous! Tarif : 49,99 $

**Faux positif.** L'usage de France n'est pas un signe d'IA; l'OQLF tolère l'absence d'espace insécable sur les réseaux sociaux.

**Sources.** https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

### P57. Mise en forme de clavardage

Niveau : mesure · Origine : recherche · Types : page_web, publicite, article, formation · Vérification : kill_list/ponctuation, bold_density, inline_header_list, emoji

**Repère.** Gras en double astérisque, puces là où une phrase suffit, flèches et coches en tête de ligne (9 à 167 fois plus fréquents chez l'IA selon Pangram, langue non précisée).

**Correction.** Remets en prose ce qui se lit comme une phrase; garde le gras sur un ou deux chiffres au plus.

**Avant**
> ✅ **Gain de temps** → vos courriels sont triés
> ✅ **Moins d'erreurs** → plus rien ne se perd

**Après**
> Vos courriels sont triés, et plus rien ne se perd.

**Faux positif.** Une liste d'étapes en formation, un tableau comparatif en article.

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing

### P58. Majuscules superflues dans les titres

Niveau : guide · Origine : recherche · Types : article, page_web, formation · Vérification : title_case

**Repère.** Majuscule à chaque mot d'un titre, calque de la casse de titre anglaise.

**Correction.** Majuscule au premier mot et aux noms propres seulement.

**Avant**
> ## Combien Coûte Vraiment Le Traitement Manuel Des Factures ?

**Après**
> ## Combien coûte le traitement manuel des factures?

**Faux positif.** Noms propres, sigles, titres d'œuvres.

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style

### P59. Plan gabarit

Niveau : guide · Origine : recherche · Types : page_web, formation, article · Vérification : lecture

**Repère.** Sections qui comptent toutes un à trois paragraphes, intertitres en question en série hors FAQ, plan qui se répète.

**Correction.** Laisse la longueur suivre le contenu. Signale en audit ou dans Ce qui sonne encore IA les sections qui se répètent; ne fusionne ni ne convertis sans l'accord de l'auteur. Un intertitre en question hors FAQ peut devenir un groupe nominal, un titre pour un titre.

**Avant**
> ## Qu'est-ce que le tri automatisé?
> ## Pourquoi le tri automatisé?
> ## Comment fonctionne le tri automatisé?

**Après**
> ## Ce que fait le tri automatisé
> ## Les raisons d'automatiser le tri
> ## Le fonctionnement du tri automatisé

**Faux positif.** Les H2 en question d'un article AEO, suivis d'une réponse directe.

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

### P60. Langue de bois et phrases creuses

Niveau : guide · Origine : recherche · Types : page_web, article, publicite · Vérification : lecture

**Repère.** Phrase qu'on collerait dans n'importe quel texte : « une solution incontournable », « au cœur de nos priorités ».

**Correction.** Remplace par le fait déjà présent dans le texte qui chiffre ou situe le problème; sans fait, coupe.

**Avant**
> La gestion des factures représente un défi majeur pour les entreprises d'aujourd'hui : une PME qui reçoit 400 factures par mois y consacre environ 40 heures de saisie.

**Après**
> Une PME qui reçoit 400 factures par mois y consacre environ 40 heures de saisie.

**Faux positif.** Une prose institutionnelle québécoise neutre et épicène.

**Sources.** https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.letemps.ch/articles/chatgpt-a-son-propre-style-mais-pour-combien-de-temps

### P61. Style impersonnel et consensuel

Niveau : mesure · Origine : recherche · Types : article, page_web, chronique · Vérification : hedging_stack

**Repère.** Impersonnel et conditionnels en série, aucun « je pense » ni « je recommande », plan qui nuance tout sans trancher.

**Correction.** Prends position à la première personne seulement si le « je » et l'avis figurent déjà dans la source : ce que l'auteur recommande et pourquoi. Sinon, retire les conditionnels empilés sans trancher à sa place.

**Avant**
> Il pourrait être pertinent d'envisager plusieurs options, chacune présentant des avantages et des inconvénients. Je recommanderais peut-être l'option deux, qui coûterait un peu plus cher, mais qui pourrait régler le problème.

**Après**
> Plusieurs options ont des avantages et des inconvénients. Je recommande l'option deux : elle coûte un peu plus cher, mais elle devrait régler le problème.

**Faux positif.** Une politique, une fiche technique, un document de référence : le neutre y est la bonne voix.

**Sources.** https://ar5iv.labs.arxiv.org/html/2306.05871; https://arxiv.org/abs/2411.18382v1

### P62. Aucun détail propre au lecteur

Niveau : blogue · Origine : recherche · Types : formation, article, page_web · Vérification : lecture

**Repère.** Ni province, ni secteur, ni taille d'entreprise, ni vécu de l'équipe; exercice sur « une tâche de votre choix ».

**Correction.** N'accepte que le détail qui figure déjà dans le texte ou dans les consignes de l'auteur (loi visée, outil réel); sinon, signale le manque.

**Avant**
> Plus haut, le module montre la saisie des factures. Exercice : choisissez une tâche de votre choix et mesurez-la pendant cinq jours.

**Après**
> Plus haut, le module montre la saisie des factures. Exercice : reprenez cette saisie et chronométrez-la pendant cinq jours.

**Faux positif.** N'invente jamais un détail local pour faire vrai.

**Sources.** https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/; https://360learning.com/fr/blog/generation-contenus-formation-ia/

### P63. « Non seulement X, mais aussi Y »

Niveau : mesure · Origine : recherche · Types : tous · Vérification : not_x_but_y

**Repère.** « non seulement... mais aussi », « ce n'est pas X, c'est Y » (trois fois plus fréquent selon Pangram, chiffre repris de l'anglais), « Il n'y a pas de X. Il y a Y. », et le titre en opposition elliptique (« X, pas Y »). Règle maison du skill, sans mesure propre : en titre ou dans la dernière phrase d'une section, la tournure sonne comme une chute fabriquée, et le script la classe alors en `error`.

**Correction.** Deux phrases simples, ou seulement le fait qui compte; en chute, dis de quoi la réponse dépend, en phrase affirmative; un titre prend un groupe nominal descriptif.

**Avant**
> Cette solution permet non seulement de gagner du temps, mais aussi d'améliorer la satisfaction client.

**Après**
> Cette solution fait gagner du temps. Elle améliore aussi la satisfaction client.

**Faux positif.** Une addition vraiment surprenante, une fois.

**Sources.** https://www.pangram.com/fr/signs-of-ai-writing; https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/

### P64. Triades en français

Niveau : mesure · Origine : recherche · Types : publicite, page_web, formation · Vérification : triad, staccato

**Repère.** Regroupements par trois répétés, surtout en fragments (« Concret. Pratique. Efficace. ») vrais de n'importe quelle offre.

**Correction.** Garde l'élément propre au sujet et appuie-le d'un fait.

**Avant**
> Un atelier de trois heures, concret, pratique et efficace, où chaque participant automatise une de ses propres tâches.

**Après**
> Un atelier de trois heures où chaque participant automatise une de ses propres tâches.

**Faux positif.** Trois éléments réels et distincts (trois étapes, trois prix).

**Sources.** https://www.pangram.com/fr/signs-of-ai-writing; https://superdesign.dev/blog/fix-generic-ai-landing-page

### P65. Participe présent en fin de phrase

Niveau : blogue · Origine : recherche · Types : article, page_web, chronique · Vérification : lecture

**Repère.** Phrase qui finit par un participe présent ajoutant une conséquence (« ..., permettant ainsi de réduire les erreurs »).

**Correction.** Fais-en une phrase avec sujet et verbe conjugué, ou coupe.

**Avant**
> Le logiciel trie les courriels entrants, permettant ainsi à votre équipe de se concentrer sur l'essentiel.

**Après**
> Le logiciel trie les courriels entrants. Votre équipe peut ainsi se concentrer sur l'essentiel.

**Faux positif.** Un participe qui décrit une action réelle et simultanée.

**Sources.** https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://pedagogie.ac-toulouse.fr/emi/node/1198

### P66. Verbes passe-partout (permettre, offrir, assurer)

Niveau : blogue · Origine : recherche · Types : page_web, publicite, formation · Vérification : lecture

**Repère.** « permettre de », « offrir », « assurer », « favoriser » comme verbes vides, avec un sujet abstrait.

**Correction.** Sujet qui agit, verbe d'action : « nous analysons », « je vous remets », « le script classe ».

**Avant**
> Notre service vous offre un accompagnement personnalisé et permet d'assurer la réussite de votre projet.

**Après**
> Nous vous accompagnons de façon personnalisée jusqu'à la réussite de votre projet.

**Faux positif.** « Permettre » au sens d'autoriser (« la loi permet »).

**Sources.** https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/; https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Règles maison de la 3.1 (P81 à P83)

Règles du skill sur la forme des phrases, ajoutées en 3.1.0. Elles ne viennent pas de la recherche, et leurs exemples sont fabriqués. Les numéros P75 à P80 ne sont pas publiés.

### P81. Phrase trop longue à l'écrit

Niveau : maison · Origine : maison · Types : tous · Vérification : long_sentence

**Repère.** Phrase de plus de 30 mots (25 en publicité) qui empile une condition, une incise et une conséquence. En script parlé, voir P68.

**Correction.** Une idée par phrase. Coupe au point, là où l'idée change, et garde le lien logique dans la phrase suivante (reprise du sujet, « ensuite », « dans ce cas »). Le résultat est fait de phrases complètes, jamais d'un chapelet de fragments (P83, P64).

**Avant**
> Quand une facture fournisseur arrive par courriel, le système la lit, en extrait le fournisseur, la date et le montant, la compare au bon de commande, puis prépare l'écriture comptable, que le responsable des comptes approuve avant le paiement.

**Après**
> Quand une facture fournisseur arrive par courriel, le système la lit et en extrait le fournisseur, la date et le montant. Il la compare au bon de commande et prépare l'écriture comptable. Le responsable des comptes l'approuve avant le paiement.

**Faux positif.** Une énumération que le lecteur doit voir d'un bloc, une clause contractuelle déjà approuvée (élément protégé), une citation.

**Sources.** Règle maison du skill, 3.1.0

### P82. Virgules sans fonction

Niveau : maison · Origine : maison · Types : tous · Vérification : comma_load

**Repère.** Virgule posée par habitude : avant « et », « ou » ou « puis » entre deux éléments courts, après un complément bref en tête de phrase, autour d'un mot qui n'est pas une incise. Plus de trois virgules dans une phrase : la phrase porte trop d'incises.

**Correction.** Relis la phrase sans la virgule. Si le sens tient, retire-la. Si la virgule encadre une incise, donne à l'incise sa propre phrase ou retire son emballage. Garde la virgule d'une énumération, celle qui suit une longue subordonnée en tête de phrase et celle que la grammaire exige.

**Avant**
> À la page 3, vous cochez les choix retenus, puis, une fois le document relu, vous signez, juste en dessous.

**Après**
> Vous cochez les choix retenus à la page 3. Vous signez juste en dessous une fois le document relu.

**Faux positif.** L'énumération simple (« le client, la date, les heures et les pièces »), la virgule décimale, la virgule d'une adresse ou d'une date.

**Sources.** Règle maison du skill, 3.1.0

### P83. Phrase sans verbe conjugué

Niveau : maison · Origine : maison · Types : article, page_web, formation, general · Vérification : verbless

**Repère.** Groupe nominal laissé en phrase par une coupe, ou écrit pour l'effet : « Dix heures par mois, sans engagement. », « Pas de surprise. », « Résultat immédiat. » La passe elle-même la crée souvent : un tic retiré emporte le verbe.

**Correction.** Donne à la phrase un sujet et un verbe conjugué, ou rattache le fragment à sa voisine. N'invente rien : le verbe dit ce que le texte dit déjà.

**Avant**
> Dix heures d'accompagnement sur un mois, sans engagement pour la suite.

**Après**
> Le forfait compte dix heures d'accompagnement sur un mois, sans engagement pour la suite.

**Faux positif.** Titres, intitulés, puces, étiquettes en gras (« **Délais.** »), lignes « étiquette : valeur », formules de politesse, réponse brève d'une FAQ suivie de la réponse complète (« Oui, selon les outils retenus. »), phrase nominale voulue d'un script parlé ou d'une publicité (constat en `info`). Le constat `verbless` est une heuristique : il manque des cas et se trompe parfois, la lecture phrase par phrase fait foi.

**Sources.** Règle maison du skill, 3.1.0

## Particularités québécoises et typographie

Ce sont des normes, pas des indices d'IA : applique-les à toute sortie en français (P56, constat `typography_fr`), sans conclure qu'un texte qui suit l'usage de France est généré.

**Espacement, nombres (OQLF).** Espace insécable avant le deux-points, aucune espace avant « ; ! ? », espaces insécables à l'intérieur des « », virgule décimale, « 1 300 $ » (dollar à droite, espace insécable, milliers séparés par une espace insécable). Absence d'espace insécable tolérée sur les réseaux sociaux. Heures en « 10 h 04 » (règle du skill). Source : https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles

**Guillemets et apostrophes.** Guillemets « » en français; les guillemets anglais sont signalés (`curly_quotes`). Apostrophe courbe acceptée si elle est constante; le mélange est relevé par Wikipédia (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative). Aucune source ne dit que les guillemets droits, seuls, trahissent l'IA.

**Courriel.** « courriel », jamais « e-mail », « email » ou « mail ». Règle de style du skill; la fiche de la Banque de dépannage linguistique n'a pas été vérifiée, ne cite pas de source. Lexique propre à l'auteur : `voix-auteur.md`, s'il existe.

**Calques de l'anglais.** L'OQLF distingue l'emprunt sémantique (« réaliser » pour se rendre compte) et l'emprunt syntaxique (« les prochaines trois semaines ») : https://vitrinelinguistique.oqlf.gouv.qc.ca/25444/les-emprunts-a-langlais/typologie-des-emprunts. Elle ne les relie pas à l'IA; seul un skill communautaire le fait (niveau blogue). Corrige-les pour la langue (P52).

**Casse et tiret.** Majuscule au premier mot des titres seulement (P58). L'OQLF admet le tiret cadratin pour mettre un passage en valeur (https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8392388/tiret-cadratin) : son retrait est une règle de style du skill, pas une preuve (P54).

**Ancrage.** Aucune mesure des tics d'IA en français québécois n'existe (premiers modèles québécois : https://arxiv.org/abs/2510.22747). L'absence de détail local (P62) reste un repère de lecture.

## Ce qu'il ne faut pas signaler

Faux positifs en français. Laisse-les, ou corrige-les pour une autre raison (norme, clarté) dite dans « Changements ».

1. **Registre soutenu.** Un « cependant » ou un « néanmoins » isolé est du français écrit normal; seule l'accumulation alourdit (P50).
2. **Français administratif.** Politique, avis, fiche technique : tournures impersonnelles et groupes nominaux y sont la bonne voix (P61, P40). Une prose institutionnelle équilibrée et épicène n'est pas de l'IA (https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr, blogue).
3. **Traductions.** Les traducteurs automatiques produisent des défauts proches de ceux des modèles (Wikipédia, lien plus haut, guide), et l'exactitude des détecteurs chute d'environ 20 % sur un texte traduit (https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00146-z, mesure). Corrige les calques sans conclure à l'IA.
4. **Texte poli ou révisé.** Les faux positifs vont de 0 % à 100 % selon le détecteur sur les mêmes manuscrits révisés (https://arxiv.org/html/2608.26710, mesure).
5. **Texte à gabarit ou court.** Listes d'étapes, FAQ, tableaux comparatifs (jusqu'à 33,4 % de faux positifs sur des recettes : https://arxiv.org/html/2405.07940, mesure); textes de moins de 300 mots, comme une publicité (https://www.turnitin.ca/blog/new-research-turnitin-s-ai-detector-shows-no-statistically-significant-bias-against-english-language-learners, mesure).
6. **Vocabulaire simple.** 61,22 % de faux positifs sur des textes de personnes qui écrivent dans leur langue seconde (https://arxiv.org/html/2304.02819v3, mesure). Ne remplace pas un mot simple par un mot rare.
7. **Vouvoiement.** Norme des documents remis au client; jamais de « tu » pour faire humain, et un seul registre par document.
8. **« On » et « je » d'expert.** L'absence de jugement personnel est le trait observé chez ChatGPT en français (https://ar5iv.labs.arxiv.org/html/2306.05871, mesure); garde le « je recommande ». N'ajoute jamais un « je » absent de la source, artefact connu des humaniseurs (https://arxiv.org/html/2501.03437, mesure).
9. **Termes techniques anglais du B2B québécois.** CRM, OCR, API : pas des calques au sens de l'OQLF. Le remplacement par synonyme crée des « expressions torturées » (https://arxiv.org/html/2402.03370, mesure).
10. **Phrases courtes voulues.** Une phrase brève qui porte un chiffre fait partie du rythme. Le tic est le découpage systématique (source DAMAGE plus haut) et le staccato (P64). À l'écrit, la phrase brève garde son verbe (P83).
11. **Répétitions voulues à l'oral.** Redire le chiffre clé aide l'auditeur d'une chronique; la FAQ AEO reprend le corps exprès (P45).
12. **Une seule tournure impersonnelle, un tic isolé.** « Aucun indice isolé ne permet de démasquer un texte rédigé par une IA » (https://www.pangram.com/fr/signs-of-ai-writing, blogue).
13. **Tiret ou espace avant « ; ! ? » chez un autre auteur.** Corrige-les selon les règles du skill sans les présenter comme des signes d'IA (https://leclaireur.fnac.com/article/612805-laffaire-tiret-cadratin-signe-ponctuation-symbole-ia/, blogue).

## Signes d'écriture humaine à préserver

Devant ces signes, laisse la prose tranquille.

- **Détail précis et difficile à inventer** : délai exact, outil réellement employé, citation étrange.
- **Tension non résolue** : « c'est surtout une bonne idée, mais quelque chose me dérange ».
- **Référence datée** : loi, fait ou expression rattachés à une année.
- **Choix défendable** : une coupe ou un mot que l'auteur sait justifier.
- **Variété de longueur** des phrases (à mesurer sur l'échantillon de l'auteur).
- **Aparté ou autocorrection** entre parenthèses.
- **Ancrage québécois** : la Loi 25, une réalité de PME d'ici, l'oral québécois d'un script (« cette boîte-là »). N'en invente jamais (P62).

Ne fabrique jamais d'humanité : aucune faute insérée, virgule qui soude deux phrases, synonyme rare, montée de registre, espace bricolée, phrase qui change le contenu ou source inventée (https://arxiv.org/html/2501.03437, mesure; https://www.pangram.com/blog/humanizers-aug-25, blogue).
