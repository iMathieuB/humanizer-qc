# Type : Page web de service, page d'offre ou étude de cas

Page de service, d'offre ou étude de cas, FR ou EN. Script : `--type page_web` (alias `page`, `page_service`). Indices de structure : sections d'offre, prix et CTA unique. Mode en conversation : interactif; en pipeline : un skill de publication de page ou d'étude de cas, ou une révision de page déjà publiée (section 7). Du fichier de langue, lis l'index et les patrons de la section 5 seulement.

## 1. Éléments protégés

1. Le H1 formulé comme un problème ou un bénéfice, jamais comme le nom du produit : gabarit de l'auteur.
2. L'ordre des sections du gabarit de page : H1 et H2 symétriques entre FR et EN.
3. La section d'objection : c'est la partie qui vend.
4. L'unique lien, celui du CTA, et son URL exacte (absolue en EN) : un lien relatif en EN mène à la page FR.
5. Le prix forfaitaire, « sans abonnement » et la phrase sur les frais d'outils tiers non revendus, quand le gabarit les prévoit.
6. Les drapeaux [NEEDS SOURCE] et tout chiffre de performance : aucun chiffre sans source.
7. Le témoignage attribué, au caractère près, orthographe seulement, tiret compris (exception déclarée `quote`) : prime sur toute règle de style.
8. L'attribution des chiffres déclarés par le client (« selon le propriétaire ») : un chiffre déclaré n'est pas mesuré.
9. Les liens externes en HTML (`target="_blank"`, `rel="noopener noreferrer"`) et internes en Markdown : comparés octet pour octet.
10. La mention *Translated from French* sous la signature EN d'un témoignage traduit.
11. Le front matter YAML, metaTitle de 60 caractères au plus, metaDesc de 155 : lu par le script d'injection.
12. Le gras sur les points clés, les phrases courtes en rafale et les énumérations, quand ils font partie de la voix de l'auteur.
13. Le H2 en question en position 2, son bloc de définition autoportant et l'ancrage local (« PME québécoise ») : SEO, GEO et AEO.
14. Les mentions légales, conditions et petits caractères : jamais retirés.
15. Les attributs du produit ou du service (IA, intégrations, garantie, pilote, délai) et les puces de bénéfices : l'emballage part (« grâce à une IA de pointe »), l'attribut reste (« l'assistant lit chaque courriel entrant »), et une liste reste une liste (règle dure 2).
16. La FAQ AEO : le moteur extrait sa première phrase.

## 2. Structures légitimes à ne pas signaler

- Gras sur les points clés, phrases courtes en rafale et énumérations, quand l'auteur les emploie (neutralise P15, P57 et P13).
- Puces, intertitres et gras qui aident le balayage (Nielsen Norman Group; neutralise P16 et P57).
- Tableau de trois offres ou paliers réels (neutralise P43, P64 et P10).
- CTA impératif, même répété (neutralise P70 et P72 pour le CTA).
- Le « vous » qui s'adresse au dirigeant lecteur (neutralise P61).
- Question en H2 pour traiter une objection, et FAQ (neutralise P47).
- Prix forfaitaire en clair, « sans abonnement », et ton promotionnel en soi : le vocabulaire répété trahit, pas la promotion (neutralise P04 et P69 hors grappe).
- Espace avant le deux-points, correcte au Québec (neutralise P56).
- Ordre de sections du gabarit de l'auteur (neutralise P59 et P35).
- Tiret dans un témoignage attribué (neutralise P54 et P14, exception `quote`).

## 3. Tics propres au type

- Bénéfices vrais de tout produit (« Gagnez du temps. Travaillez mieux. »); titre à trous (« La solution IA de [X] pour les [Y] modernes »); trois cartes à émoji vides de faits. https://superdesign.dev/blog/fix-generic-ai-landing-page
- Formules promotionnelles répétées même sur un ton neutre; verbe marketing (« offre », « propose »); émoji en tête de titre ou de puce. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Verbes passe-partout (permettre, garantir, assurer, offrir, favoriser), adjectifs crucial, essentiel; deux adjectifs enchaînés; aucun détail local. À pondérer (blogue d'agence). https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/
- Statistique, rabais ou fonctionnalité que l'entreprise n'offre pas. https://www.eesel.ai/blog/ai-ad-copy-generator
- Langage marketing gonflé au lieu de faits. https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/
- Fragment sans sujet; aphorisme fabriqué en deux propositions symétriques; annonce de la règle de trois (« Trois conséquences pratiques »); inflation de sens; formule d'autorité (« le calcul est simple : »); parallélisme négatif et chute fabriquée en fin de section. Règle maison du skill.
- Même tournure d'ouverture d'une page à l'autre (« consiste à », « means having »). Règle maison du skill.
- Locution parlée dans un H2 ou un intitulé (« et ce que ça coûte » au lieu de « et à quel prix »); réponse de FAQ qui ne répond pas dans sa première phrase. Règle maison du skill.
- Pointe contre un absent non nommé (« ce qu'aucun autre outil ne vous dira ») ou posture de vendeur annoncée : décris ce que fait l'offre. Règle maison du skill.
- « solutions sur mesure », « accompagnement personnalisé », « Découvrez », « Révolutionnez ». Hypothèse non sourcée, ne pas traiter comme établie.

## 4. Registre

Écrit vivant et simple, sans locution parlée dans un titre, un intitulé, une cellule ou une FAQ. H1 et H2 de vente porteurs d'un verbe fort et d'un résultat (document de lecture). Un seul registre par page, vouvoiement partout si le corps vouvoie, CTA compris. Un profil de voix (`voix-auteur.md`) ou un échantillon de l'auteur l'emporte sur ce registre par défaut.

## 5. Patrons prioritaires

(fr) : patterns-fr.md seulement; (en) : patterns-en.md seulement; sinon les deux.

- P54 Tiret cadratin en français (fr); P14 Em dashes (and en dashes): cut them (en)
- P51 Vocabulaire gonflé en français (fr); P07 Overused "AI vocabulary" words (en)
- P63 « Non seulement X, mais aussi Y », en chute ou en titre compris (fr); P09 Negative parallelisms and tailing negations (en)
- P64 Triades en français (fr); P10 Rule of three overuse (en)
- P40 Nominalisations
- P57 Mise en forme de clavardage (fr); P18 Emojis (en)
- P04 Promotional and advertisement-like language (en)
- P60 Langue de bois et phrases creuses (fr)
- P66 Verbes passe-partout (permettre, offrir, assurer) (fr)
- P62 Aucun détail propre au lecteur (fr)
- P71 Titre à trous
- P73 Formule aspirationnelle creuse
- P13 Passive voice and subjectless fragments (en)
- P81 Phrase trop longue à l'écrit, P82 Virgules sans fonction, P83 Phrase sans verbe conjugué (fr); P81 et P82 (en)

## 6. Seuils du script pour ce type

| Seuil | page_web |
|---|---|
| Densité vocabulaire, `warning` au-delà (pour 1 000 mots) | fr 6, en 8 |
| Triades, `warning` au-delà (pour 1 000 mots) | 4 |
| Staccato : phrases consécutives de 3 mots ou moins | 3, `info` |
| CV minimal des phrases (si 12 phrases ou plus) | 0,30 |
| Phrase longue, mots | 30, `warning` |
| Virgules dans une phrase, au-delà de | 3, `warning` |
| Phrase sans verbe conjugué (français) | `info` |
| Gras non numérique, `warning` au-delà (pour 1 000 mots) | 8 |
| Listes à intitulé en gras | `info` |
| Émojis | chaque émoji `warning` |
| `!` : `warning` à partir de | 2 |
| Longueur par section (caractères) | aucun |

Ces seuils sont ceux de verif_humanizer.py; en cas d'écart, le script fait foi.

## 7. Ce que les pipelines attendent

- **Publication d'une page de service**, FR et EN, avant l'injection. Reste conservateur; vise fragments sans sujet, aphorismes, annonces de la règle de trois, formules d'autorité et chutes fabriquées. Script : zéro tiret, zéro guillemet courbe, H1 et H2 symétriques FR et EN, un seul lien. Chiffre de performance invérifiable : [NEEDS SOURCE] visible, ou il saute.
- **Publication d'une étude de cas client**, FR et EN, avant l'injection, toujours avec `exceptions=quote`. Mêmes cibles, plus l'inflation de sens. Contrôle : témoignage intact au caractère près, aucun chiffre interdit réintroduit. Structure gardée : Contexte, Problème, Solution, Résultats en puces qualitatives, témoignage en blockquote, « Ce que ça veut dire pour votre entreprise », CTA.
- **Révision d'une page déjà publiée** : `passages=` sur la prose ajoutée; varie une ouverture qui revient d'une page à l'autre; aucun chiffre nouveau; ne réécris pas ce qui fonctionne ni les H1 du gabarit.
- **Passe de révision de fond** : humanizer passe après elle, en dernier, sans défaire ses décisions.

## 8. Liste de contrôle

- [ ] Aucun tiret cadratin ni demi-cadratin, hors citation de témoignage?
- [ ] Aucun guillemet courbe anglais, et les guillemets français sont-ils « »?
- [ ] Le témoignage est-il identique au caractère près, sauf l'orthographe?
- [ ] La page garde-t-elle un seul lien, celui du CTA, avec son URL exacte?
- [ ] Le prix, « sans abonnement » et la phrase sur les frais tiers sont-ils intacts?
- [ ] Chiffres et drapeaux [NEEDS SOURCE] sont-ils identiques à l'entrée, sans chiffre nouveau?
- [ ] Les H1 et H2 sont-ils ceux de l'entrée, symétriques entre FR et EN?
- [ ] Le gras des points clés et les phrases courtes sont-ils conservés?
- [ ] Chaque bénéfice est-il propre à ce service?
- [ ] Aucun fragment sans sujet, aphorisme ni chute fabriquée en fin de section?
- [ ] Aucune annonce de la règle de trois ni formule d'autorité?
- [ ] Chaque réponse de FAQ répond-elle dans sa première phrase?
- [ ] Aucune locution parlée dans un titre, un intitulé ou une cellule?
- [ ] Chaque paragraphe tient-il sur une ligne, et leur nombre est-il inchangé?
- [ ] Aucune phrase de plus de 30 mots, aucune virgule sans fonction, un verbe conjugué dans chaque phrase du corps?

## 9. Exemple court

Exemple fictif, abrégé (paire `evals/corpus/page_web/fr-02-tri-courriels`).

**Avant**
> Il est important de noter que la gestion des courriels représente aujourd'hui un défi majeur pour les entreprises. Gagnez du temps. Travaillez mieux. Grandissez plus vite. L'agent classe chaque courriel dans l'une de quatre catégories et prépare des brouillons de réponse. Par ailleurs, aucun courriel n'est envoyé sans votre approbation.

**Après**
> L'agent classe chaque courriel dans l'une de quatre catégories et prépare des brouillons de réponse. Il n'envoie aucun courriel sans votre approbation.

Corrigés : formule de liaison et connecteur (P50), langue de bois (P60), bénéfices interchangeables, retirés pour leur contenu et non leur forme (P72).
