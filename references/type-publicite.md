# Type : Publicité LinkedIn ou Meta et publication sociale courte

Annonces LinkedIn, Facebook et Instagram, et publications sociales (posts, légendes, descriptions YouTube, premier commentaire). Script : `--type publicite` (alias `pub`). Indices de structure : texte court avec mots-clics, CTA ou plateforme nommée. Mode en conversation : `interactif`. En pipeline : un skill de publication qui produit les posts d'un article ou d'une vidéo, ou une passe de révision d'un profil ou d'une bio (section 7). Du fichier de langue, lis l'index et les patrons de la section 5 seulement.

## 1. Éléments protégés

1. Le CTA et le bouton prédéfini : la plateforme les fixe, LinkedIn exige un CTA clair.
2. Mentions légales et petits caractères : ne les retire jamais (Normes de la publicité).
3. Les chiffres, identiques à la source (article ou page d'origine).
4. Le mot-clé déclencheur et le renvoi au premier commentaire, au vouvoiement.
5. Liens courts et « Lien en bio » (vrai seulement si la bio mène à la page).
6. Les variantes A/B (4 à 5 par campagne, selon LinkedIn), gardées séparées.
7. Les longueurs de plateforme (section 9) : court par contrainte n'est pas un tic; ne rallonge pas.
8. Mots-clics et émojis voulus, 10 au plus sur LinkedIn (limite officielle).
9. La voix du compte : « on » pour une page d'entreprise, « je » pour un profil personnel, vouvoiement du lecteur.
10. Les textes fournis par l'auteur : publiés tels quels.
11. Un témoignage cité : au caractère près, exception déclarée `quote`.

## 2. Structures légitimes à ne pas signaler

- Impératif du CTA, CTA répété ou explicite (neutralise P70 et P72 pour cette ligne).
- Variantes proches (neutralise P45 entre variantes).
- Fragment court isolé (neutralise P31 et P72 tant qu'il ne revient pas partout).
- Ton promotionnel assumé : seul le vocabulaire répété trahit (neutralise P04 et P69 hors grappe).
- Thèse dès la première phrase, avant « voir plus » (neutralise P47 et P53).
- Blocs d'une ou deux lignes séparés par une ligne vide, à condition que chaque bloc porte un fait complet (neutralise P31); une suite de fragments d'une phrase n'est pas un bloc, c'est P72.
- Puces « • » en texte brut sous un intitulé nominal suivi d'un deux-points (neutralise P16 et P57).
- Question rhétorique : non documentée comme tic; ne la signale pas par défaut (neutralise P33).
- Mots-clics en fin de publication Instagram (neutralise P18 et P57 pour cette ligne).

## 3. Tics propres au type

- Texte générique, collable sous n'importe quel logo; chiffre, rabais ou fonctionnalité inventés. https://www.eesel.ai/blog/ai-ad-copy-generator
- « Libérez votre potentiel » et formules du même moule. https://www.eesel.ai/fr/blog/generateur-de-texte-publicitaire-ia
- Poli en surface, sans substance (« AI slop »). https://news.linkedin.com/2026/keeping-conversations-real-on-linkedin
- Slogan aspirationnel plutôt que message direct. https://arxiv.org/html/2512.03373v1
- Émoji en tête de chaque ligne ou puce. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Variantes qui commencent toutes par le même verbe, avec « ! » et émojis. https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features
- Tirets partout, « Ce n'est pas X, c'est Y ». https://storeytime.beehiiv.com/p/anti-ai-copywriting-prompts
- Superlatifs empilés, impératifs hors du CTA (mesuré surtout en anglais). https://arxiv.org/html/2601.04925v1
- Fragments collés (« Rapide. Simple. ») partout; fourchette ronde non mesurée. https://pasqualepillitteri.it/fr/news/11196/nouveau-em-dash-9-signes-ecriture-ia
- En tête d'un post personnel, formule d'annonce (« Petit partage. ») ou crédibilité revendiquée (« après 20 ans dans le métier »); phrase personnelle inventée (demande-la à l'auteur). Règle maison du skill.
- Accroche sans fait : le chiffre ou le bénéfice concret n'arrive qu'après le pli « voir plus » (150 caractères sur LinkedIn, section 9); point d'exclamation hors du CTA; texte haché en phrases d'une ligne après le retrait des slogans. Observation maison (évaluation du skill, 2026-11-01).

## 4. Registre

Écrit vivant, aucune locution parlée; « je » pour un profil personnel, « on » pour une page d'entreprise; vouvoiement. Thèse dans la première phrase, blocs d'une ou deux lignes séparés par une ligne vide, puces « • » en texte brut. Un profil de voix (`voix-auteur.md`) ou un échantillon de l'auteur l'emporte sur ce registre par défaut.

## 5. Patrons prioritaires

(fr) : patterns-fr.md seulement; (en) : patterns-en.md seulement; sinon les deux.

- P54 Tiret cadratin en français (fr); P14 Em dashes (and en dashes): cut them (en)
- P51 Vocabulaire gonflé en français (fr); P07 Overused "AI vocabulary" words (en)
- P63 « Non seulement X, mais aussi Y », en chute ou en titre compris (fr); P09 Negative parallelisms and tailing negations (en)
- P64 Triades en français (fr); P10 Rule of three overuse (en)
- P57 Mise en forme de clavardage (fr); P18 Emojis (en)
- P40 Nominalisations
- P04 Promotional and advertisement-like language (en)
- P56 Typographie non québécoise ou incohérente (fr)
- P72 Slogans en fragments et impératifs empilés
- P73 Formule aspirationnelle creuse
- P71 Titre à trous
- P70 Appel à l'action générique
- P66 Verbes passe-partout (permettre, offrir, assurer) (fr)
- P81 Phrase trop longue à l'écrit, P82 Virgules sans fonction; P83 Phrase sans verbe conjugué, signalée sans être fautive (fr)

## 6. Seuils du script pour ce type

| Seuil | publicite |
|---|---|
| Densité vocabulaire, `warning` au-delà (pour 1 000 mots) | fr 6, en 8 |
| Triades, `warning` au-delà (pour 1 000 mots) | 6 |
| Staccato : phrases consécutives de 3 mots ou moins | 3, `info` |
| CV minimal des phrases (si 12 phrases ou plus) | 0,30 |
| Phrase longue, mots | 25, `info` |
| Virgules dans une phrase, au-delà de | 3, `info` |
| Phrase sans verbe conjugué (français) | `info` |
| Gras non numérique, `warning` au-delà (pour 1 000 mots) | tout gras `warning` |
| Listes à intitulé en gras | `warning` |
| Émojis | plus de 10 : `error`; 3 lignes ou plus qui commencent par un émoji : `warning` |
| `!` : `warning` à partir de | 3 |
| Longueur par section (caractères) | plus de 3 000 dans une section : `warning` (maximum LinkedIn) |

Ces seuils sont ceux de verif_humanizer.py; en cas d'écart, le script fait foi. Les 3 000 caractères valent par section (plateforme ou variante), jamais pour le total du fichier.

## 7. Ce que les pipelines attendent

- **Posts d'un article ou d'une vidéo** (`type=publicite`, `pipeline`) : zéro tiret, pas de vocabulaire IA; voix du compte (page au « on », profil personnel au « je », sans gras); Instagram avec « Lien en bio » seulement si la bio mène à la page. Chiffres égaux à l'article; une formulation retirée de l'article pendant la révision est retirée aussi des textes de campagne; lien court. Ce que l'assistant compose se montre à l'auteur en citation avant son accord.
- **Profil ou bio** (après une passe de révision de fond) : humanizer en dernier et sur toute phrase ajoutée; dictée appliquée à la lettre.
- **Règles de forme** : vouvoiement; aucun lien externe dans le corps d'un post LinkedIn si la stratégie de l'auteur le prévoit; jamais de retour forcé.

## 8. Liste de contrôle

- [ ] Aucun tiret cadratin ni demi-cadratin?
- [ ] Chaque champ tient-il dans la longueur recommandée (section 9)?
- [ ] CTA, mot-clé déclencheur et mentions légales intacts?
- [ ] Chiffres identiques à la source?
- [ ] Un fait ou un cas propre à l'auteur plutôt qu'une promesse générique?
- [ ] Aucun émoji en tête de ligne, total dans la limite?
- [ ] Impératifs et superlatifs limités au CTA, et aucun point d'exclamation?
- [ ] Le fait chiffré ou le bénéfice concret tient-il dans les 150 premiers caractères (LinkedIn) ou avant le pli de la plateforme (section 9)?
- [ ] Les slogans retirés ont-ils laissé un texte qui se lit d'une traite, sans phrase de remplissage (règle dure 10)?
- [ ] Variantes séparées, sans même premier mot?
- [ ] Le post personnel commence-t-il par le fait, sans formule d'annonce?
- [ ] Vouvoiement, et voix (« on » ou « je ») du compte?
- [ ] Rien d'inventé (phrase personnelle, chiffre)?
- [ ] « Lien en bio » seulement si la bio mène à la page?
- [ ] Texte brut, sans gras ni Markdown, pour LinkedIn et Facebook?
- [ ] Aucune phrase de plus de 25 mots ni virgule sans fonction, et chaque phrase sans verbe est-elle voulue?

## 9. Limites de caractères par plateforme

| Plateforme | Champ | Recommandé | Maximum | Source |
|---|---|---|---|---|
| LinkedIn, image unique | Texte d'introduction | 150, tout compris | 3 000, 10 émojis | [1] |
| LinkedIn, image unique | Titre | 70 | 200 | [1] |
| LinkedIn, image unique | Description | 100 ou 70; retenir 70 | 300 | [1], [2] |
| LinkedIn, carrousel | Texte d'introduction | 150 | 255 | [1] |
| Meta, fil Facebook | Texte principal | 50 à 150 | non indiqué | [3] |
| Meta, fil Facebook | Titre | 27 | non indiqué | [3] |
| Meta, fil Instagram | Texte principal | 125 | non indiqué | [4] |
| Meta, fil Instagram | Titre et mots-clics | titre de 40 | 30 mots-clics | [4] |
| Meta, Marketplace | Texte, titre, description | 125, 40 et 30 | non indiqué | [5] |

[1] https://www.linkedin.com/help/lms/answer/a426534
[2] https://business.linkedin.com/advertise/ads/sponsored-content/single-image-ads-specs
[3] https://www.facebook.com/business/ads-guide/image/facebook-feed
[4] https://www.facebook.com/business/ads-guide/update/image/instagram-feed
[5] https://www.facebook.com/business/ads-guide/update/image/facebook-marketplace

- Valeurs Meta : recommandations selon l'objectif et le placement, pas des plafonds.
- Aucune page Meta lue ne donne de longueur de description hors Marketplace.
- La description LinkedIn s'affiche rarement : le message n'en dépend jamais.

Compte les caractères de chaque champ après la passe; signale tout dépassement de la zone recommandée dans « Changements ». Ne coupe jamais un CTA ni une mention légale pour tenir la limite.

## 10. Exemple court

Exemple fictif, abrégé (paire `evals/corpus/publicite/fr-02-atelier-ia-facebook`).

**Avant**
> Texte principal : Dans un paysage numérique en constante évolution, la maîtrise de l'IA est devenue essentielle — et même cruciale — pour vos équipes ! Notre atelier innovant favorise la mise en place d'une démarche d'appropriation des outils. Concret. Pratique. Efficace. 3 heures, groupes de 8 personnes, $2400.00 par groupe, soit $300.00 par personne. Obtenez votre place dès maintenant ! Profitez-en !

**Après**
> Texte principal : Un atelier de 3 heures pour apprendre à votre équipe à se servir des outils d'IA. Groupes de 8 personnes, 2 400 $ par groupe, soit 300 $ par personne. Obtenez votre place dès maintenant!

Corrigés : P46, P51, P54, P66, P40, P64, P72, P56. Gardés : chiffres, CTA (seul « Profitez-en! » sort), bouton « S'inscrire ».
