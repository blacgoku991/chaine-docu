VERDICT : KO

# Fact-check — Free Mobile, 2012 : casser quoi, au juste ? — script v3 — 7 octobre 2026

Passe 3 : re-vérification après révision. Le « Journal des révisions » du script v3 a été comparé, correction par correction, à la revue de la passe 2, puis au texte même du script (pas seulement au journal).

## Résumé
- Affirmations vérifiées : 214 (✅ 207, ⚠️ 7, ❌ 0). 68 ont été vérifiées à cette passe. Les 146 autres, validées à une passe précédente, ont le même extrait en v3 et sont reprises telles quelles. Trois de ces dernières (c15, c45, c118) passent en ⚠️ à cause du contrôle juridique de cette passe.
- Mode de vérification : les pages sources n'ont pas pu être ouvertes (WebFetch bloqué). Chaque affirmation est vérifiée contre le dossier (research.md et sources.md, lui-même vérifié en trois passes par recherches). Les affirmations clés sont en plus recoupées par des recherches restreintes au domaine de la source. On ne lit alors que les résumés de résultats, pas les pages.
- Passe 2 : les 21 corrections sont toutes appliquées dans la v3 (voir « Suivi des corrections de la passe 2 »). Deux d'entre elles contenaient une erreur de la revue elle-même, corrigée ici :
  - la correction 11 faisait dire au tribunal un motif (« saisie qui n'aurait pas dû être autorisée ») absent du dossier → correction 3 ;
  - la raison de la correction 12 parlait des « services d'accès audiovisuels », mais son texte de remplacement a perdu « d'accès » → correction 5.
- Corrections retenues : 6, qui modifient 10 extraits. Elles reprennent 3 remarques des vérificateurs des faits (c116, c128, c188) et les 3 remarques juridiques. Le visuel c138, jugé conforme par son vérificateur, est aligné sur c116 (même motif, même absence dans le dossier). Aucune remarque n'a été écartée.
- Juridique : 3 remarques, toutes retenues (corrections 1, 2 et 4). Aucun conseil financier. Aucun VISUEL d'un type interdit.
- Déjà vu : RAS. C'est le premier épisode de la chaîne, il n'y a aucun épisode précédent à comparer.
- Longueur : 2 291 mots aujourd'hui (~15,3 min). Une fois les 6 corrections appliquées, 2 282 mots (~15,2 min), toujours dans la fourchette de 1 800 à 2 300. Comptage fait avec `pipeline/narration.py`, sur le script et sur une copie corrigée.
- Format : l'accroche fait 73 mots (~29 s). La promesse est posée (« casser quoi : les prix, les concurrents, ou le marché lui-même ? », plus la pièce de juin 2026) et tenue (sections 8 et 9). Aucun tag ne manque.
- Pourquoi KO : 6 corrections restent à appliquer. Aucune n'est un rejet. Trois sont juridiques (insinuations ou formulations trop fortes visant des personnes nommées), deux corrigent un périmètre ou un motif que les sources ne portent pas, et une corrige une étiquette de frise trompeuse.

## Corrections à appliquer

Chaque extrait a été contrôlé : il apparaît une seule fois, tel quel, dans `script.md` v3. Les 10 remplacements ont été appliqués sur une copie, et le texte obtenu compte 2 282 mots selon `pipeline/narration.py`.

**Section 2 — La scène et ses témoins**

1. Section 2, « Sur scène, selon Puremédias, Xavier Niel traite les clients des opérateurs de « pigeons ». [S241][S70] » → « Pendant la présentation, selon Puremédias, Xavier Niel traite les clients des opérateurs de « pigeons ». [S241][S70] ». Raisons (juridique) :
   - le script prête à une personne réelle nommée une remarque péjorative, et « sur scène » laisse entendre qu'il l'a prononcée lui-même, en direct ;
   - les sections détaillées du dossier écrivent « pendant la présentation » (chronologie 2012-01-10) ou « pendant cette présentation » (6.3) et préviennent que la réplique a pu venir du faux documentaire projeté pendant la keynote (6.3, 8.2, à vérifier sur la vidéo). Seul le résumé d'angle (research.md, l. 25) dit « sur scène » : le dossier ne soutient donc pas la formule sans réserve, et la remarque ne peut pas être écartée ;
   - un résumé d'Edcom (contrôle juridique) décrit un film parodique de lancement qui prêtait aux patrons concurrents le fait de traiter leurs clients en « pigeons » ou en « vaches à lait », ce qui rend l'hypothèse du film plausible ;
   - « pendant la présentation » est vrai dans les deux hypothèses.

   Garder l'attribution à Puremédias et n'ajouter aucune citation directe. +1 mot. [S241][S70]

**Section 3 — Rembobinage**

2. Section 3, « Attention : rien dans notre dossier ne dit que ces pratiques duraient en 2011. [S160] » → « Attention : les pratiques sanctionnées datent de 1997 à 2003, pas de 2011. [S160] ». Raison (juridique) : la fin de la section 2 (« un détail surprend : Sosh et B&You […] existaient déjà avant Free ») enchaîne directement sur « Jusqu'à un mot : Yalta » et sur l'entente sanctionnée. On comprend qu'Orange et Bouygues auraient pu se coordonner de nouveau en 2011, ce qu'aucune décision n'établit. La phrase actuelle limite le démenti à « notre dossier » et laisse donc le soupçon ouvert. La nouvelle phrase le ferme avec un fait sourcé : selon le communiqué du Conseil de la concurrence, les deux pratiques sanctionnées couvrent 1997-2003 (échanges d'informations) et 2000-2002 (stabilisation des parts de marché) (research.md, chronologie et 6.12 « Deux pratiques, deux périodes »). Cette correction complète la correction 5 de la passe 2, qui laissait cette phrase telle quelle. −1 mot selon `narration.py` (le contrôle juridique estimait 0). [S160]

**Section 6 — Contre-expertise**

3. Section 6, motif du jugement Deffains. Cette correction fusionne c116 et c138 :
   - narration : « Mais le tribunal de grande instance de Paris juge ensuite, toujours selon la presse, que cette saisie n'aurait pas dû être autorisée, et déboute Free Mobile. [S287][S288] » → « Mais le tribunal de grande instance de Paris déboute ensuite Free Mobile. [S287][S288] » ;
   - VISUEL section 6 : « second carton « TGI de Paris, selon la presse : saisie qui n'aurait pas dû être autorisée, Free Mobile débouté (appel : non trouvé) » [S287][S288] » → « second carton « TGI de Paris : Free Mobile débouté (appel : non trouvé) » [S287][S288] ».

   Raisons :
   - le débouté est un fait validé du dossier (chronologie 2012-06, chiffres clés, 6.16), recoupé à cette passe sur frenchweb.fr et clubic.com ;
   - le motif prêté au tribunal ne figure nulle part dans research.md, ni en 6.16 ni en Zones d'ombre (8.4 dit seulement que la nature exacte de la procédure n'a pas été lue). Il venait du texte de la correction 11 de la passe 2 ;
   - selon les résumés de presse, le tribunal a jugé que Free Mobile « ne justifiait d'aucun intérêt légitime » à chercher des preuves dans les systèmes informatiques de Bruno Deffains. « N'aurait pas dû être autorisée » est une interprétation juridique de ce motif, pas sa formulation, à propos d'une décision non lue qui concerne une personne privée nommée.

   Garder la phrase précédente (« Selon la presse, Free Mobile engage une procédure… »), toujours sans lieu ni guillemets. −14 mots.
   Variante possible, mais seulement après avoir ajouté le motif à research.md 6.16 (voir Compléments) : « Mais le tribunal de grande instance de Paris déboute ensuite Free Mobile : selon la presse, l'opérateur ne justifiait d'aucun intérêt légitime à chercher des preuves dans ses systèmes informatiques. [S287][S288] ». [S287][S288]
4. Section 6, transition après la projection (juridique) :
   - narration : « Reste que c'était une projection. [S287] Qu'a-t-on constaté ? » → « Reste que c'était une projection. [S287] Chez les opérateurs seuls, qu'a-t-on constaté ? » ;
   - VISUEL section 6 : « la courbe à points de la série 7.1 X (emplois directs chez les opérateurs, Arcep, milliers : » → « la courbe à points de la série 7.1 X, légendée « emploi direct des opérateurs seulement » (Arcep, milliers : » ;
   - VISUEL section 6 : « aucune légende « effet Free » [S194][S276][S277][S274] ; » → « aucune légende « effet Free », jamais le carton « −55 000 » sur l'échelle de cette courbe [S194][S276][S277][S274] ; ».

   Raisons :
   - juste après le rappel que Free Mobile a perdu contre Bruno Deffains, « Reste que » et « Qu'a-t-on constaté ? » annoncent une réfutation. Elle repose ensuite sur la seule série de l'Arcep sur l'emploi direct des opérateurs [S194][S276] ;
   - rien n'établit que la projection de 55 000 destructions nettes porte sur ce périmètre. Le détail non vérifié d'Univers Freebox (research.md 8.4) y compte surtout des emplois chez les partenaires (35 200 et 15 800, contre 10 600 chez les opérateurs mobiles) ;
   - le spectateur conclut que l'économiste s'est trompé, ce qu'aucune source ne dit, et le récit épouse au passage la position de la partie déboutée.

   +4 mots. [S287][S194]
5. Section 6, périmètre de la hausse de TVA (c128) :
   - narration : « une hausse de TVA sur les services audiovisuels, non répercutée » → « une hausse de TVA sur les services d'accès audiovisuels, non répercutée » ;
   - VISUEL section 6 : « hausse de TVA sur les services audiovisuels non répercutée » → « hausse de TVA sur les services d'accès audiovisuels non répercutée ».

   Raison : l'Arcep parle des « services d'accès audiovisuels », pas de tous les services audiovisuels. Ce sont les termes du dossier (chronologie 2011, 6.16) et de l'observatoire du T4 2012 vu sur arcep.fr [S273]. L'explication par la TVA est confirmée dans [S157]. Tags inchangés. +1 mot. [S157][S273]

**Section 8 — Dernière pièce**

6. VISUEL section 8, « « 05/04/2014 : SFR → Numericable » [S20] » → « « 05/04/2014 : Vivendi accepte l'offre de Numericable pour SFR » [S20] ». Raisons :
   - une flèche « SFR → Numericable » datée du 5 avril 2014 laisse croire que SFR change de mains ce jour-là ;
   - selon la décision 14-DCC-160 (même URL que S20, recherche sur autoritedelaconcurrence.fr), le 5 avril 2014 Vivendi accepte l'offre de Numericable du 4 avril et les parties signent un accord d'exclusivité. Le contrat d'acquisition date du 20 juin 2014, l'autorisation du 30 octobre 2014 et la réalisation du 27 novembre 2014 ;
   - la narration dit déjà juste (« accord le 5 avril 2014 ») et le dossier prévient : « Ne pas confondre le choix du 14 mars et l'accord du 5 avril » (6.8).

   Ligne VISUEL seulement : aucun effet sur le nombre de mots. [S20]

**Effet sur la longueur** : 2 291 → 2 282 mots (~15,2 min), dans la fourchette, avec 18 mots de marge. Les repères de temps de la section 6 et des suivantes sont à recalculer.

## Compléments pour `sources.md` et `research.md`

Obligatoires (pour éviter qu'une prochaine version réintroduise les formulations corrigées) :
- **research.md, l. 25 (angle 1)** : « sur scène, selon Puremédias » → « pendant la présentation, selon Puremédias », pour aligner le résumé d'angle sur la chronologie 2012-01-10 et sur 6.3 (correction 1).
- **research.md, 7.1 Y (l. 745)** : « TVA sur les services audiovisuels » → « TVA sur les services d'accès audiovisuels » (correction 5). La chronologie 2011 et 6.16 sont déjà justes.
- **research.md, 6.16** : reporter depuis 8.4 la saisie de documents informatiques, avec la consigne « à attribuer à la presse », sans lieu [S287][S288][S289][S356] (c115). Si le scénariste veut la variante de la correction 3, y ajouter aussi : « selon la presse, le tribunal juge que Free Mobile ne justifiait d'aucun intérêt légitime à chercher des preuves dans les systèmes informatiques de Bruno Deffains » [S287][S288] (résumés de clubic.com et frenchweb.fr, fact-check passe 3).

Pour le documentaliste (non bloquants pour le script) :
- research.md 8.4 : la date du jugement Deffains serait proche du début de mars 2013, d'après deux résultats vus par le contrôle juridique (S355, WebManagerCenter du 4 mars 2013 ; universfreebox.com, article 19951). À confirmer avant tout usage.
- research.md 8.2 : le film parodique de lancement est décrit dans https://www.edcom.fr/23682-free-condamne-a-verser-25-million-d-euros-pour-denigrement-face-a-bouygues-telecom.html (astreinte de 100 000 € par infraction dans le même article).
- research.md 6.16 : aligner les pourcentages sur la fiche S284, soit 50 / 32 / 18 % pour la version publiée et 51 / 31 / 18 % pour la version de 2019 (c148, c149, c197).
- Les 40 destinations (c12) : lire la page LinuxFr avant toute mention « vers les fixes ».
- Bouygues en 2014 (c107) : un article de Next titré « Bouygues confirme de nouveaux licenciements et attaque vivement Free » (https://next.ink/23234/88003-bouygues-confirme-nouveaux-licenciements-et-attaque-vivement-free/) n'a pas été lu. À lire avant toute formulation sur la position de Bouygues en 2014.
- URL vues dans les résultats, utilisables comme compléments :
  - souscriptions à 9 h 30 (c16) : https://www.generation-nt.com/free-mobile-inscriptions-forfaits-mobiles-actualite-1524681.html ;
  - appel de Free dans l'affaire du dénigrement (c80) : https://www.universfreebox.com/article/19884/Diffamation-ou-denigrement-Les-raisons-de-l-appel-de-Free-contre-la-plainte-de-Bouygues-Telecom ;
  - date de l'étude de l'UFC (c139) : https://www.webmanagercenter.com/2014/04/29/149511/4eme-operateur-mobile-7-milliards-de-gain-de-pouvoir-d-achat-pour-les-consommateurs/ et https://www.arcep.fr/actualites/la-revue-de-presse/2014/avril/les-titres-de-la-presse-du-mercredi-30-avril-2014.html ;
  - fréquences cédées en 2014 (c163) : https://www.telecoms.com/spectrum/bouygues-to-sell-network-and-spectrum-to-free-if-sfr-deal-goes-through ;
  - S341, forme longue (c158) : https://www.universfreebox.com/article/20701/Free-aurait-envoye-une-proposition-de-rachat-a-Martin-Bouygues-qui-prefererait-crever-que-de-vendre-a-Free ;
  - S297, variante d'URL en /wp-content/ (c168) : https://www.bouygues.com/wp-content/uploads/2025/10/cp_bouygues-telecom_free-groupe-iliad_orange_141025_fr.pdf.

Suggestions non bloquantes, qui ne comptent pas comme corrections :
- VISUEL section 5 : ajouter [S82] à la barre « Free Mobile : 2,61 millions au 31/03/2012, selon Iliad » (c108).
- VISUEL section 9 : le stock « rue, écrans de smartphones » devrait suivre la consigne de la section 2, soit « sans visage identifiable ni logo ou application de marque à l'écran ».
- Section 2 : les « syndicats CFE-CGC et UNSA » sont probablement ceux de France Télécom-Orange (research.md 8.2, non validé). Ne rien ajouter tant que ce n'est pas vérifié.
- Rythme : la phrase de 35 mots de la section 9 (« …imposées par le régulateur, et aucun document financier… ») peut être coupée en deux, et celle de 37 mots de la section 7 (50 / 32 / 18 %) allégée.
- Packaging : le titre de travail « Comment Free a cassé le marché du mobile » affirme ce que le script nuance (« en partie », « non »). L'agent packaging ne doit pas le présenter comme un constat.

## Suivi des corrections de la passe 2

Les 21 corrections de la passe 2 ont été vérifiées une à une dans le texte v3, pas seulement dans le Journal des révisions.

| Passe 2 | Objet | Dans la v3 | Remarque |
|---|---|---|---|
| 1 | Empreinte : beat « paradoxe du réseau » | ✅ appliquée | |
| 2 | Empreinte : signatures = compteur + bandeau ; verdict rangé dans la structure | ✅ appliquée | |
| 3 | VISUEL S2 : « cadrées sans visage », « aucune personne réelle identifiable » | ✅ appliquée | |
| 4 | « les syndicats CFE-CGC et UNSA écrivent à l'Arcep » + VISUEL J+16 | ✅ appliquée | Confirmée à cette passe (c30, résumé quasi littéral de S234). |
| 5 | « un détail surprend » ; « Pour comprendre ce marché » | ✅ appliquée | Complétée par la correction 2 : la phrase-garde est remplacée. |
| 6 | Tampon « Décision 05-D-65 » tagué [S158][S159] | ✅ appliquée | |
| 7 | VISUEL S4 : prépayées sans retrait, « catégories à ne pas additionner » | ✅ appliquée | |
| 8 | Phrase « pigeon / racket » supprimée | ✅ appliquée | La formule « Sur scène » est traitée à part (correction 1). |
| 9 | « rien ne dit que ces abonnés viennent tous des historiques » | ✅ appliquée | |
| 10 | Encart SFR daté « 2 278 M€ (2011) → 1 600 M€ (2012) » | ✅ appliquée | |
| 11 | Procédure Deffains : attribution, tags, carton | ✅ appliquée | Le motif « n'aurait pas dû être autorisée », proposé par la passe 2, est retiré par la correction 3. |
| 12 | TVA et offres « en prévision du quatrième opérateur » + VISUEL | ✅ appliquée | Le texte de remplacement de la passe 2 avait perdu « d'accès » : correction 5. |
| 13 | VISUEL S6 : « trous de 2014 à 2016 signalés » | ✅ appliquée | |
| 14 | VISUEL S6 : « environ 3,6 en 2016, calcul d'après l'Arcep » | ✅ appliquée | |
| 15 | VISUEL S8 : « en numéraire », « accord conditionnel » | ✅ appliquée | |
| 16 | VISUEL S8 : « offre non engageante… (actifs visés) ; rejetée mi-octobre » | ✅ appliquée | |
| 17 | VISUEL S8 : « prix réparti à environ 42 / 31 / 27 % » | ✅ appliquée | |
| 18 | VISUEL S8 : « clients que Free reprendrait… peuvent inclure le fixe » | ✅ appliquée | |
| 19 | VISUEL S8 : courbe « selon iliad », « DOM compris », tags | ✅ appliquée | |
| 20 | S9 : « que nous avons pu vérifier ne relie explicitement » | ✅ appliquée | |
| 21 | S9 : « parmi d'autres explications » | ✅ appliquée | |

Compléments obligatoires de la passe 2 : fiches S355 et S356 mises à jour dans `sources.md` ✅ ; research.md chronologie 2011, 2012-01-26, 6.16 et 6.19 ✅ ; 7.1 Y seulement en partie (« services audiovisuels » sans « d'accès », voir Compléments). Les deux suggestions non bloquantes de la passe 2 (« manifestent contre le plan », façade sans enseigne) sont appliquées.

## Détail des vérifications

Légende : « Dossier » signifie vérifié contre research.md et sources.md. « Dossier + recherche (domaine) » signifie recoupé en plus par une recherche restreinte au domaine indiqué (résumés de résultats, pages non ouvertes). « Passe 2 : » signifie que l'affirmation, validée à une passe précédente, a le même extrait en v3 ; le mode indiqué est alors celui de cette passe. « ⚠️ juridique » signale un fait conforme au dossier dont la formulation pose un problème juridique retenu.

| # | Section | Affirmation | Source | Statut | Mode de vérif. | Commentaire |
|---|---|---|---|---|---|---|
| c1 | 1 | « 10 janvier 2012, 8 h 30 » | S11, S12, S239 | ✅ | Dossier + recherche (generation-nt.com) | Keynote le 10/01/2012 à 8 h 30, en direct sur live.free.fr. L'heure est portée par S11 ; S12 et S239 portent la date et l'offre. |
| c2 | 1 | « Xavier Niel présente un forfait illimité, sans engagement, à 19,99 euros par mois. » | S11, S12, S239 | ✅ | Dossier + recherche (generation-nt.com, linuxfr.org) | 19,99 € sans engagement (15,99 € pour les abonnés Free). « Illimité » est l'intitulé commercial ; les 3 Go sont précisés en section 2. |
| c3 | 1 | « En six jours, Orange baisse l'illimité de Sosh de 39,90 à 24,90 euros » | S10, S13, S14 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com, edcom.fr) | Nouvelle grille Sosh en vigueur le 12/01/2012. Les six jours vont du 10 au 16 janvier. |
| c4 | 1 | « et B&You, chez Bouygues, s'aligne à 19,99. » | S10, S13, S14 | ✅ | Dossier + recherche (edcom.fr) | Forfait « 24/24 & Internet 3 Go » à 19,99 € à partir du 16/01/2012 (S14). |
| c5 | 1 | « La dernière, datée de juin 2026, retourne toute l'histoire. » | S311 | ✅ | Passe 2 : dossier + recherche (bouygues.com) | Communiqué du 6 juin 2026. Le rachat n'est pas présenté comme fait ; la section 8 rappelle qu'il s'agit d'un projet. |
| c6 | 1 (VISUEL) | « Sosh illimité 39,90 € → 24,90 € (12/01) » | S10, S13 | ✅ | Dossier + recherche (lesmobiles.com) | 12/01 = entrée en vigueur. Même offre (1 Go) aux deux prix. Le 24,90 € n'apparaît pas dans le résumé, mais il est porté par trois sources du dossier ; aucune contradiction. |
| c7 | 1 (VISUEL) | « B&You → 19,99 € (16/01) » | S14 | ✅ | Dossier + recherche (edcom.fr) | Date et prix confirmés. Aucun prix de départ affiché, donc rien de trompeur. |
| c8 | 2 | « 8 h 30, au siège d'Iliad : la présentation commence, en direct sur internet. » | S11, S58 | ✅ | Passe 2 : dossier + recherche (generation-nt.com) | Siège d'Iliad (la Mutualité n'est pas confirmée, 8.2). Direct sur live.free.fr. |
| c9 | 2 | « Deux forfaits sans engagement. » | S239, S2 | ✅ | Passe 2 : dossier + recherche (generation-nt.com) | |
| c10 | 2 | « 60 minutes et 60 SMS pour 2 euros » | S239, S240 | ✅ | Dossier + recherche (linuxfr.org, generation-nt.com) | |
| c11 | 2 | « gratuit pour les abonnés Freebox » | S239, S240 | ✅ | Dossier + recherche (linuxfr.org, generation-nt.com) | Prix réservé aux abonnés Freebox, pas une offre autonome : la formule respecte cette réserve. |
| c12 | 2 | « appels, y compris vers 40 destinations » | S239, S242, S240 | ✅ | Dossier + recherche (linuxfr.org, generation-nt.com) | Formule validée par le dossier (8.2), sans « internationales » ni « fixes et mobiles ». Lire LinuxFr avant toute mention « vers les fixes ». |
| c13 | 2 | « SMS, MMS, plus 3 gigas d'internet, pour 19,99 euros » | S239, S242, S240 | ✅ | Dossier + recherche (linuxfr.org, generation-nt.com) | « 3 Go » et non « internet illimité », comme l'exige 8.2. |
| c14 | 2 | « ou 15,99 avec une Freebox » | S239, S242, S240 | ✅ | Dossier + recherche (linuxfr.org, generation-nt.com) | 15,99 € (ni 16 € ni « 19,90 € moins 2 € »). |
| c15 | 2 | « Sur scène, selon Puremédias, Xavier Niel traite les clients des opérateurs de « pigeons ». » | S241, S70 | ⚠️ juridique | Passe 2 : dossier + recherche (ozap.com) ; contrôle juridique passe 3 (edcom.fr) | Attribution à Puremédias correcte. Mais « sur scène » va plus loin que les sections détaillées du dossier (« pendant la présentation »), qui signalent que la réplique a pu venir du faux documentaire projeté pendant la keynote (6.3, 8.2) → correction 1. |
| c16 | 2 | « 9 h 30 : les souscriptions ouvrent. » | S11, S60 | ✅ | Passe 2 : dossier + recherche (generation-nt.com) | URL complémentaire dans « Compléments ». |
| c17 | 2 | « Dès le 12 janvier, la portabilité des numéros sature » | S77 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Communiqué de l'Arcep au GIE EGP. |
| c18 | 2 | « environ 40 000 portages par jour, la capacité maximale du système » | S77 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Capacité saturée, pas la demande : réserve reprise par le VISUEL (c32). |
| c19 | 2 | « contre 12 000 en moyenne en 2011 » | S77 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c20 | 2 | « SFR réplique aussi, ce même mois, avec un forfait Red à 24,90 euros » | S24, S68, S69 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com, lyoncapitale.fr, edcom.fr) | « Réplique » justifié par le titre de S24 (« pour contrer Free Mobile »). |
| c21 | 2 | « illimité sauf l'internet : 1 giga, bloqué au-delà » | S24, S68, S69 | ✅ | Passe 2 : dossier + recherche (mêmes domaines) | Une recharge payante existait (hors dossier) ; la phrase reste exacte. |
| c22 | 2 | « En janvier, Arnaud Montebourg, alors député, salue l'offre sur Twitter » | S332, S333 | ✅ | Passe 2 : dossier + recherche (universfreebox.com, next.ink) | Jour non établi dans le dossier : « En janvier » reste prudent. |
| c23 | 2 | « « Xavier Niel vient de faire avec son nouveau forfait illimité plus pour le pouvoir d'achat des Français que Nicolas Sarkozy en 5 ans » » | S332, S333 | ✅ | Passe 2 : dossier + recherche (universfreebox.com, next.ink) | Mot pour mot (Citations vérifiées n° 4). Carton texte, sans capture du tweet. |
| c24 | 2 | « selon la presse spécialisée, le directeur général de Bouygues Telecom, Olivier Roussat » | S65, S66 | ✅ | Dossier + recherche (generation-nt.com, universfreebox.com) | Propos rapportés par deux sources, entretien au JDD non lu : l'attribution « selon la presse spécialisée » est exacte. |
| c25 | 2 | « juge l'offre à 2 euros scandaleuse, et celle à 19,99 inadaptée » | S65, S66 | ✅ | Dossier + recherche (generation-nt.com, universfreebox.com) | Discours indirect, sans guillemets. Opinion attribuée d'un concurrent, pas une accusation de la chaîne. |
| c26 | 2 | « Environ deux semaines après le lancement » | S70, S71 | ✅ | Passe 2 : dossier + recherche (ozap.com, alloforfait.fr) | Délai porté par Puremédias (dossier) ; le résumé ne le contredit pas. |
| c27 | 2 | « le PDG de France Télécom-Orange, Stéphane Richard » | S70, S71 | ✅ | Passe 2 : dossier + recherche (ozap.com, alloforfait.fr) | |
| c28 | 2 | « dénonce à propos de cette présentation un « show indigne » » | S70, S71 | ✅ | Passe 2 : dossier + recherche (ozap.com, alloforfait.fr) | Deux mots seulement (Citations vérifiées n° 1) ; la phrase longue, vue en traduction seulement, n'est pas reprise. |
| c29 | 2 | « Le 25 janvier, devant les députés, Xavier Niel affirme que Free a déjà 1 000 antennes actives. » | S200, S27 | ✅ | Passe 2 : dossier (recherche ozap.com non aboutie) | Chiffre de l'opérateur, attribué ; deux sources au dossier. |
| c30 | 2 | « Le 26 janvier, les syndicats CFE-CGC et UNSA écrivent à l'Arcep pour demander une enquête sur la couverture de Free Mobile. » | S26, S234 | ✅ | Dossier + recherche (arcep.fr) | Correction 4 de la passe 2 appliquée. Résumé quasi littéral de S234 : « In a letter dated 26 January ». Date de la lettre, pas de sa réception. |
| c31 | 2 | « Sosh et B&You, les deux offres qui ripostent, existaient déjà avant que Free Mobile ne vende son premier forfait. » | S9, S10 | ✅ | Passe 2 : dossier | B&You le 18/07/2011, Sosh le 06/10/2011. Aucune causalité ajoutée. |
| c32 | 2 (VISUEL) | « la demande réelle a pu être plus forte » | S77 | ✅ | Dossier | Mise en garde imposée par 7.1 G, au conditionnel, déduite de « capacité maximale ». |
| c33 | 2 (VISUEL) | « Stéphane Richard, JDD, fin janvier 2012 » | S70 | ✅ | Dossier | Formule autorisée par le dossier (6.3) ; seuls les deux mots s'affichent. |
| c34 | 2 (VISUEL) | « tweet, janvier 2012 » | S332, S333 | ✅ | Dossier | Pas de jour (non établi) ; pas de capture. |
| c35 | 3 | « Jusqu'à un mot : Yalta. » | S160, S166 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Mot attribué au Conseil deux phrases plus loin. |
| c36 | 3 | « Le 30 novembre 2005, le Conseil de la concurrence sanctionne Orange France, SFR et Bouygues Télécom pour entente » | S158, S159 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Décision 05-D-65 ; « Conseil » et non « Autorité » pour 2005. |
| c37 | 3 | « 534 millions d'euros d'amendes au total » | S158, S159 | ✅ | Passe 2 : dossier | 256 + 220 + 58 = 534, recoupé à cette passe (c57). |
| c38 | 3 | « Selon le Conseil, des documents évoquaient la « pacification » du marché et un « Yalta » des parts de marché. » | S160, S166 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Guillemets sur ces deux mots seulement, comme le permet 6.12. |
| c39 | 3 | « De 1997 à 2003, les trois échangent des informations confidentielles » | S160, S162 | ✅ | Dossier + recherche (autoritedelaconcurrence.fr ; WebManagerCenter 2006) | Période distincte de celle de 2000-2002, et traitée à part. |
| c40 | 3 | « notamment le nombre de leurs nouveaux abonnés et celui de leurs résiliations » | S160, S162 | ✅ | Dossier + recherche (autoritedelaconcurrence.fr) | « Notamment », sans périodicité, comme le demande 6.12. |
| c41 | 3 | « Et de 2000 à 2002, ils s'entendent pour stabiliser leurs parts de marché. » | S160, S158 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | |
| c42 | 3 | « Après six ans et demi de recours » | S162, S169, S173 | ✅ | Passe 2 : dossier (calcul) | Du 30/11/2005 au 30/05/2012 : 6 ans et 6 mois. |
| c43 | 3 | « la justice clôt définitivement l'affaire en mai 2012, amendes confirmées » | S162, S169, S173 | ✅ | Passe 2 : dossier | Formule prescrite par 6.12 ; issue de la procédure donnée. |
| c44 | 3 | « 141 jours après le lancement de Free Mobile, d'après notre calcul » | S162, S169, S173 | ✅ | Passe 2 : dossier (calcul refait) | 10/01/2012 → 30/05/2012 = 141 jours (année bissextile). |
| c45 | 3 | « Attention : rien dans notre dossier ne dit que ces pratiques duraient en 2011. » | S160 | ⚠️ juridique | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) ; contrôle juridique passe 3 | Exact, mais le démenti, limité à « notre dossier », laisse ouvert le soupçon créé par la juxtaposition (Sosh et B&You → « Yalta ») → correction 2, phrase factuelle sur les périodes sanctionnées. |
| c46 | 3 | « En 2011, justement, le marché bouge déjà. » | S9, S10 | ✅ | Passe 2 : dossier | Transition appuyée sur les deux lancements de 2011. |
| c47 | 3 | « Le 18 juillet, Bouygues Telecom lance B&You » | S9, S53 | ✅ | Dossier + recherche (lesmobiles.com, universfreebox.com) | « On July 18, 2011, Bouygues Telecom launched… » (résumé de S9). |
| c48 | 3 | « sa marque en ligne sans engagement, à partir de 24,90 euros » | S9, S53 | ✅ | Dossier + recherche (lesmobiles.com, universfreebox.com) | Titre de S9. 24,90 € sans 3G, 36,90 € avec : « à partir de » est exact. |
| c49 | 3 | « Le 6 octobre, Orange lance Sosh » | S10, S55 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com) | |
| c50 | 3 | « avec un illimité à 39,90 euros » | S10, S55 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com) | Forfait 24/7 à 39,90 €, 1 Go. |
| c51 | 3 | « en 2002, il lançait une offre ADSL à 29,99 euros par mois » | S3, S4 | ✅ | Passe 2 : dossier + recherche (universfreebox.com) | « Offre ADSL », pas « triple play » (6.11). |
| c52 | 3 | « quand ses concurrents demandaient près du double, selon Univers Freebox » | S3, S4 | ✅ | Passe 2 : dossier + recherche (universfreebox.com) | Attribution imposée par le dossier (site proche de Free). |
| c53 | 3 | « En décembre 2009, quand Free Mobile décroche la quatrième licence » | S8, S25, S50 | ✅ | Passe 2 : dossier | Décision de l'Arcep n° 2009-1067 du 17/12/2009. |
| c54 | 3 | « Xavier Niel promet, selon la presse spécialisée, de diviser par deux la facture mobile des ménages » | S8, S25, S50 | ✅ | Passe 2 : dossier + recherche (generation-nt.com) | Discours indirect, sans guillemets (8.6). |
| c55 | 3 (VISUEL) | « communiqué du 1er décembre 2005 » | S160, S166 | ✅ | Dossier + recherche (autoritedelaconcurrence.fr) | « Selon le Conseil de la concurrence », deux mots isolés. |
| c56 | 3 (VISUEL) | « Décision 05-D-65 » | S158, S159 | ✅ | Dossier + recherche (autoritedelaconcurrence.fr) | Tag ajouté en v3 (correction 6 de la passe 2). |
| c57 | 3 (VISUEL) | « Orange France 256 / SFR 220 / Bouygues Télécom 58 M€ » | S160, S158, S159 | ✅ | Dossier + recherche (autoritedelaconcurrence.fr ; WebManagerCenter 2006) | Frise annotée, sans barres ni parts de marché (7.2). |
| c58 | 3 (VISUEL) | « 30/05/2012 : affaire close, amendes confirmées » | S162 | ✅ | Dossier (recherche journaldugeek.com, webmanagercenter.com non aboutie) | Deux sources datées du 30/05/2012 par leur URL (S162, S169). Ne dit pas « condamnations définitives le 30 mai ». Aucune contradiction. |
| c59 | 3 (VISUEL) | « bande « échanges d'informations confidentielles, 1997-2003 », bande « stabilisation des parts de marché, 2000-2002 » » | S160, S158, S159 | ✅ | Dossier | Deux périodes sur deux bandes distinctes, comme l'exige 6.12. |
| c60 | 4 | « Le 23 mai 2013, l'Arcep publie son indice des prix mobiles pour l'année 2012. » | S16, S100 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c61 | 4 | « moins 11,4 % en moyenne sur un an, pour les services mobiles grand public en métropole » | S16 | ✅ | Dossier + recherche (arcep.fr) | Même chiffre, même périmètre, même année. |
| c62 | 4 | « de 2006 à 2010, l'indice de l'Arcep baissait de 2,9 % par an en moyenne » | S61 | ✅ | Dossier + recherche (en.arcep.fr) | Comparaison « avant / après », méthodes différentes signalées. |
| c63 | 4 | « Méthodes et périmètres diffèrent, mais l'écart est net. » | S61, S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Pas de causalité affirmée. |
| c64 | 4 | « Sur les forfaits sans téléphone, la baisse atteint même 28,4 %. » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Forfaits sans terminal. |
| c65 | 4 | « Sur ce segment, l'Arcep relie la baisse à l'arrivée du quatrième opérateur, Free Mobile » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Causalité portée par la source, pour ce seul segment. |
| c66 | 4 | « qui ne vend que des offres sans téléphone subventionné » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c67 | 4 | « Pour l'ensemble, le régulateur attribue la baisse en partie à la pression du quatrième opérateur. » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | « En partie », pas « largement ». |
| c68 | 4 | « Iliad revendique pour Free Mobile 5,2 millions d'abonnés fin 2012 » | S15, S11 | ✅ | Dossier | Chiffre et attribution dans le titre de S15. |
| c69 | 4 | « moins d'un an après le lancement » | S15, S11 | ✅ | Passe 2 : dossier (calcul) | 356 jours. |
| c70 | 4 | « L'indice moyen, lui, ne montre pas une division par deux. » | S16, S25 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | −11,4 % en moyenne, −28,4 % au mieux. |
| c71 | 4 | « Une chose est sûre : les prix ont baissé. » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c72 | 4 | « Et une baisse de prix, quelqu'un la paie. » | — | ✅ | Passe 2 : dossier | Transition générique, qui ne vise personne et que le script nuance ensuite. |
| c73 | 4 (VISUEL) | « 2010 : −3,4 » | S61 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Pas placé à côté de −12,4 % (8.1). |
| c74 | 4 (VISUEL) | « ensemble des forfaits post-payés −12,6 » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Forfaits bloqués compris. |
| c75 | 4 (VISUEL) | « cartes prépayées −8 » | S16 | ✅ | Dossier + recherche (arcep.fr) | Placé sans retrait, au niveau des post-payés (correction 7 de la passe 2 appliquée). |
| c76 | 4 (VISUEL) | « 2,6 / 3,6 / 4,4 / 5,2 millions d'abonnés (fin de trimestre 2012) » | S81, S85, S86, S15 | ✅ | Passe 2 : dossier | « Selon Iliad », sans point « 0 ». |
| c77 | 5 | « Le 22 février 2013, en première instance, le tribunal de commerce de Paris condamne Free Mobile » | S94, S95 | ✅ | Passe 2 : dossier + recherche (universfreebox.com, next.ink) | « En première instance » ; issue de l'appel dite inconnue. |
| c78 | 5 | « à verser 25 millions d'euros à Bouygues Telecom pour dénigrement » | S94, S95 | ✅ | Passe 2 : dossier + recherche (universfreebox.com, next.ink) | |
| c79 | 5 | « Mais Bouygues Telecom est condamné lui aussi pour dénigrement, à verser 5 millions à Free. » | S95, S96 | ✅ | Passe 2 : dossier + recherche (franceinfo.fr, universfreebox.com) | Même jugement de première instance. |
| c80 | 5 | « Free fait appel ; l'issue, nous ne l'avons pas trouvée. » | S95 | ✅ | Passe 2 : dossier + recherche (domaines S94 à S99) | Appel confirmé, aucun arrêt trouvé. URL complémentaire dans « Compléments ». |
| c81 | 5 | « Sur ces 25 millions, 15 réparent, en première instance, une perte de clientèle de Bouygues Telecom. » | S97, S99 | ✅ | Passe 2 : dossier + recherche (universfreebox.com) | 15 M€ perte de clientèle, 10 M€ image. |
| c82 | 5 | « au premier trimestre 2012, en solde net, Orange perd 615 000 clients mobiles en France, selon ses chiffres » | S249 | ✅ | Dossier + recherche (lesmobiles.com, confirmation indirecte) | Chiffre d'Orange, attribué ; solde net, parc total. |
| c83 | 5 | « SFR, environ 620 000, selon la presse. » | S257, S258, S259, S260 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com) | 274 000 forfaits et parc de 20,843 M confirmés ; « environ » et « selon la presse » respectent la réserve. |
| c84 | 5 | « Bouygues Telecom, 379 000. » | S253 | ✅ | Passe 2 : dossier | Source primaire ; −381 000 abandonné. |
| c85 | 5 | « Environ 1,6 million à eux trois, d'après notre calcul. » | S249, S257, S253 | ✅ | Passe 2 : dossier (calcul) | 615 + 620 + 379 = 1 614 milliers. |
| c86 | 5 | « Free Mobile, lui, revendique 2,6 millions d'abonnés fin mars. » | S81 | ✅ | Passe 2 : dossier | Chiffre d'Iliad, attribué. |
| c87 | 5 | « le parc total a grossi de 860 000 cartes » | S84 | ✅ | Dossier + recherche (arcep.fr) | Hausse qui comprend aussi des cartes MtoM et internet. |
| c88 | 5 | « rien ne dit que ces abonnés viennent tous des historiques » | S84 | ✅ | Dossier | Correction 9 de la passe 2 appliquée ; garde-fou du dossier (6.15, 7.1 Q). |
| c89 | 5 | « L'Arcep vérifie : au 31 janvier 2012, son réseau propre couvre 28 % de la population métropolitaine » | S26, S234 | ✅ | Dossier + recherche (arcep.fr) | Hors itinérance. |
| c90 | 5 | « avec 735 sites » | S26, S234 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Sites ouverts commercialement. |
| c91 | 5 | « pour une obligation de 27 % » | S26, S234 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c92 | 5 | « Conforme, avec un point de marge. » | S26 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Conformité constatée par le régulateur. |
| c93 | 5 | « Des sites, pas des antennes : les deux chiffres ne comptent pas la même chose. » | S26, S27 | ✅ | Passe 2 : dossier | Nuance de 6.5, sans conclure à une contradiction. |
| c94 | 5 | « Pour le reste, Free Mobile passe par le réseau d'Orange, grâce à un contrat d'itinérance prévu pour six ans. » | S29, S28 | ✅ | Passe 2 : dossier | Durée validée (8.1). |
| c95 | 5 | « Au premier trimestre 2012, Orange perd ces 615 000 clients tout en louant son réseau à son nouveau concurrent. » | S249, S29 | ✅ | Passe 2 : dossier | Paradoxe formulé en 6.7, sans causalité. |
| c96 | 5 | « Chez Bouygues Telecom, l'EBITDA, un indicateur de rentabilité, recule de 29 % en 2012, à 908 millions d'euros. » | S261, S262 | ✅ | Passe 2 : dossier + recherche (bouygues.com) | 908 / 1 272 = −28,6 %. |
| c97 | 5 | « Bouygues parle de turbulences du marché mobile. » | S253 | ✅ | Passe 2 : dossier | Discours indirect, mot attesté. |
| c98 | 5 | « Chez SFR, selon Vivendi, un autre indicateur, l'EBITA, perd près de 30 %, d'après notre calcul. » | S265, S266 | ✅ | Passe 2 : dossier + recherche (vivendi.com) | −29,8 %. |
| c99 | 5 | « Juillet 2012, Bouygues Telecom : 556 départs volontaires. » | S17, S219 | ✅ | Passe 2 : dossier + recherche (lesmobiles.com) | Annonce, pas départs constatés. |
| c100 | 5 | « Fin novembre, SFR : 856 suppressions nettes. » | S18, S87 | ✅ | Passe 2 : dossier | Titre de S18. |
| c101 | 5 | « Juin 2014, Bouygues Telecom encore : 1 516 suppressions prévues » | S113, S343, S345 | ✅ | Passe 2 : dossier + recherche (next.ink) | |
| c102 | 5 | « ramenées à 1 404 fin septembre » | S113, S343, S345 | ✅ | Passe 2 : dossier + recherche (next.ink) | Même plan, chiffre révisé. |
| c103 | 5 | « Des annonces de natures différentes, qu'on n'additionne pas. » | S17, S18, S113 | ✅ | Passe 2 : dossier | Réserve de 7.1 O. |
| c104 | 5 | « Sur France 5, fin 2012, le PDG de SFR, Stéphane Roussel » | S88, S89 | ✅ | Dossier + recherche (ozap.com) | Jour non établi : « fin 2012 ». |
| c105 | 5 | « défend le caractère volontaire de son plan : « On n'envoie personne à Pôle emploi » » | S88, S89 | ✅ | Dossier + recherche (ozap.com) | Mot pour mot, bonne personne, bon contexte. |
| c106 | 5 | « Les syndicats de SFR, eux, manifestent contre le plan. » | S91, S87 | ✅ | Dossier | Titres de S91 et S87. |
| c107 | 5 | « Dans les documents financiers que nous avons pu vérifier, aucun de ces plans n'est relié explicitement à Free. » | S253, S262, S268 | ✅ | Passe 2 : dossier | Constat borné et assumé comme limite. Article de Next de 2014 non lu : voir « Compléments ». |
| c108 | 5 (VISUEL) | « Free Mobile : 2,61 millions au 31/03/2012, selon Iliad » | S81 | ✅ | Dossier + recherche (ozap.com) | 2,6 millions confirmé ; décimale portée par le dossier. Suggestion : ajouter [S82]. |
| c109 | 5 (VISUEL) | « 1 272 (2011) / 908 (2012) » | S261, S262 | ✅ | Passe 2 : dossier + recherche (bouygues.com) | EBITDA, séparé de l'EBITA de SFR. |
| c110 | 5 (VISUEL) | « SFR, EBITA selon Vivendi : 2 278 M€ (2011) → 1 600 M€ (2012) » | S265 | ✅ | Dossier + recherche (vivendi.com) | Valeur 2011 désormais recoupée. |
| c111 | 5 (VISUEL) | « Tribunal de commerce de Paris, 22/02/2013, première instance » | S95, S96 | ✅ | Dossier | Sous-titre « Free fait appel ; issue non trouvée » : procédure avec son statut. |
| c112 | 6 | « Juin 2012 : dans Les Échos, Bruno Deffains » | S287, S288 | ✅ | Dossier + recherche (frenchweb.fr, clubic.com) | Date et support confirmés. |
| c113 | 6 | « professeur d'économie à Panthéon-Assas » | S287, S288 | ✅ | Dossier + recherche (frenchweb.fr, clubic.com) | |
| c114 | 6 | « estime que Free Mobile pourrait provoquer la destruction nette de 55 000 emplois en deux ans » | S287, S288 | ✅ | Passe 2 : dossier + recherche (frenchweb.fr, clubic.com) | Conditionnel, attribué à l'auteur ; seul le 55 000 est retenu ; aucun commanditaire nommé. |
| c115 | 6 | « Selon la presse, Free Mobile engage une procédure contre lui et obtient une saisie de documents informatiques. » | S287, S288, S289, S356 | ✅ | Dossier + recherche (clubic.com, frenchweb.fr) | Saisie en 8.4 seulement, avec la consigne « à attribuer à la presse », respectée ; lieu absent. Documentaliste : reporter la saisie en 6.16. |
| c116 | 6 | « Mais le tribunal de grande instance de Paris juge ensuite, toujours selon la presse, que cette saisie n'aurait pas dû être autorisée, et déboute Free Mobile. » | S287, S288 | ⚠️ | Dossier + recherche (clubic.com, frenchweb.fr) | Débouté validé (6.16). Le motif prêté au tribunal est absent de research.md, et la formule est une interprétation juridique (la presse dit « aucun intérêt légitime ») d'une décision non lue : remarque non écartable → correction 3. |
| c117 | 6 | « D'un éventuel appel, nous n'avons pas trouvé trace. » | S287, S288, S289, S356 | ✅ | Passe 2 : dossier + recherche (frenchweb.fr, clubic.com, webmanagercenter.com, universfreebox.com) | Constat d'absence borné ; issue en première instance donnée. |
| c118 | 6 | « Reste que c'était une projection. » (suivi de « Qu'a-t-on constaté ? ») | S287 | ⚠️ juridique | Passe 2 : dossier ; contrôle juridique passe 3 | Fait exact. Mais l'enchaînement oppose la projection, dont le périmètre n'est pas établi (partenaires compris selon 8.4, non vérifié), à la seule série de l'emploi direct des opérateurs : réfutation implicite d'une personne nommée → correction 4. |
| c119 | 6 | « Selon l'Arcep, les opérateurs emploient 129 000 personnes fin 2012 » | S194 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c120 | 6 | « un effectif stable sur un an » | S194 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | +0,1 %. |
| c121 | 6 | « Ensuite, l'emploi direct recule de 3 000 à 4 000 postes par an » | S276, S274 | ✅ | Passe 2 : dossier | Formule de l'Arcep, recoupée à cette passe sur la page S276 (c133). |
| c122 | 6 | « jusqu'à 105 000 fin 2019 » | S276, S274 | ✅ | Passe 2 : dossier | |
| c123 | 6 | « Mais rien de ce que nous avons lu chez l'Arcep n'attribue cette baisse à Free. » | S276, S274 | ✅ | Passe 2 : dossier | Constat borné, conforme à 6.14, 6.16 et 7.1 X. |
| c124 | 6 | « L'investissement mobile, lui, ne s'effondre pas » | S192 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c125 | 6 | « selon l'Arcep, de 2004 à 2014, il reste relativement stable, entre 2 et 2,5 milliards d'euros par an » | S192 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c126 | 6 | « Les revenus des services mobiles baissent bien, d'une année sur l'autre, pendant vingt-deux trimestres d'affilée, jusqu'au troisième trimestre 2016. » | S196 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Pas « jusqu'à fin 2016 ». |
| c127 | 6 | « Mais selon l'Arcep, la chute avait commencé dès 2011 » | S157, S273 | ✅ | Dossier + recherche (arcep.fr) | En baisse depuis le T2 2011 (S273). |
| c128 | 6 | « en partie à cause d'une hausse de TVA sur les services audiovisuels, non répercutée, et d'offres moins chères lancées en prévision du quatrième opérateur » | S157, S273 | ⚠️ | Dossier + recherche (arcep.fr) | Périmètre élargi : l'Arcep parle des services d'accès audiovisuels. Erreur venue du texte de remplacement de la correction 12 de la passe 2 → correction 5. Le volet « offres en prévision du quatrième opérateur » reste porté par le dossier (S273). |
| c129 | 6 | « Puis les revenus repartent à la hausse, fin 2016. » | S196 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | T4 2016. |
| c130 | 6 | « Les opérateurs eux-mêmes citent aussi une autre cause : les baisses de tarifs de terminaison d'appel et d'interconnexion imposées par le régulateur. » | S270, S268, S261 | ✅ | Passe 2 : dossier | Tient sur S268 et S261 ; Orange n'est pas nommé. |
| c131 | 6 | « En décembre 2014, l'Arcep reprend d'ailleurs un entretien de son président aux Échos » | S183 | ✅ | Passe 2 : dossier | Entretien du 18/12/2014. |
| c132 | 6 | « « L'arrivée de Free a été un changement important, mais prévisible » » | S183 | ✅ | Dossier | Titre de la page de l'Arcep, mot pour mot ; présenté comme titre, pas prêté à Silicani. |
| c133 | 6 (VISUEL) | « 129 en 2012, 125 en 2013, 112,7 en 2017, 109 en 2018 « provisoire », 105 en 2019 » | S194, S276, S277, S274 | ✅ | Dossier + recherche (arcep.fr) | 112 700 au 31/12/2017 confirmé, avec la tendance. La légende de périmètre est ajoutée par la correction 4. |
| c134 | 6 (VISUEL) | « 4,7 en 2011, 4,2 en 2012, environ 3,6 en 2016, calcul d'après l'Arcep » | S157, S273, S196 | ✅ | Dossier + recherche (arcep.fr) | 4,2 Md€ HT au T4 2012 confirmé ; calcul signalé. |
| c135 | 6 (VISUEL) | « 22 trimestres de baisse sur un an, du T2 2011 au T3 2016 » | S157, S273, S196 | ✅ | Dossier + recherche (arcep.fr) | 3 + 16 + 3 = 22. Le +1,8 % (résumé) contre +1,7 % (dossier) n'est pas cité. |
| c136 | 6 (VISUEL) | « baisse commencée dès le T2 2011 » | S157, S273 | ✅ | Dossier + recherche (arcep.fr, indirecte) | |
| c137 | 6 (VISUEL) | « investissement mobile seul : 2,0 à 2,5 Md€ par an, 2004-2014 (Arcep, rapport de 2015) » | S192 | ✅ | Dossier + recherche (arcep.fr) | Rapport du 3 décembre 2015. |
| c138 | 6 (VISUEL) | « TGI de Paris, selon la presse : saisie qui n'aurait pas dû être autorisée, Free Mobile débouté (appel : non trouvé) » | S287, S288 | ⚠️ | Dossier + recherche (frenchweb.fr, clubic.com) | Le vérificateur le juge fidèle, mais constate lui-même que le motif est absent de research.md (il venait de la correction 11 de la passe 2). Aligné sur c116, retenu → correction 3. |
| c139 | 7 | « Le 29 avril 2014, l'UFC-Que Choisir publie son bilan. » | S281 | ✅ | Passe 2 : dossier + recherche (webmanagercenter.com ; revue de presse de l'Arcep) | URL complémentaires dans « Compléments ». |
| c140 | 7 | « L'association est partie prenante : elle était plaignante dans l'affaire de l'entente. » | S167, S163 | ✅ | Passe 2 : dossier | Mise en garde voulue par le dossier, sans qualification péjorative. |
| c141 | 7 | « l'arrivée du quatrième opérateur a fait baisser la facture mobile mensuelle moyenne de 30 % » | S281 | ✅ | Dossier + recherche (quechoisir.org) | Causalité attribuée (« Selon l'UFC »), pas affirmée par la chaîne. |
| c142 | 7 | « fait économiser près de 7 milliards d'euros aux utilisateurs en 2012 et 2013 » | S281 | ✅ | Dossier + recherche (quechoisir.org) | 6,83 Md€. |
| c143 | 7 | « Pas une division par deux, mais près d'un tiers. » | S281, S25 | ✅ | Passe 2 : dossier | 30 % ≈ un tiers. |
| c144 | 7 | « En 2021, trois économistes publient une autre mesure dans l'American Economic Review. » | S283 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | AER vol. 111, n° 11. |
| c145 | 7 | « Selon la version de leur étude présentée en 2019, l'entrée de Free Mobile a augmenté le surplus des consommateurs » | S285 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | Causalité du modèle, attribuée. |
| c146 | 7 | « d'environ 4,6 milliards d'euros sur 2012-2014 » | S285 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | |
| c147 | 7 | « Autre concept que l'économie de l'UFC : on n'additionne pas les deux. » | S285, S281 | ✅ | Passe 2 : dossier | Précaution de méthode (6.16, 8.4). |
| c148 | 7 | « Selon la version publiée, 50 % du gain des clients viennent de la variété apportée par Free Mobile » | S284 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | 50 % (publié) ; 51 % = version 2019. |
| c149 | 7 | « 32 % des marques de combat des opérateurs en place » | S284 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | |
| c150 | 7 | « et seulement 18 % environ de la concurrence accrue sur les prix » | S284 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | |
| c151 | 7 | « Ces marques de combat, selon la présentation de l'étude : Sosh, Red et B&You. » | S284 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | La page les date de 2012 ; le script ne reprend pas cette date. |
| c152 | 7 | « Sosh et B&You existaient même avant Free. » | S9, S10 | ✅ | Passe 2 : dossier | « Free » = Free Mobile, sans ambiguïté dans le contexte. |
| c153 | 7 | « selon la version de 2019, les opérateurs ont subi de fortes pertes » | S285 | ✅ | Passe 2 : dossier (recherche aeaweb.org concordante) | |
| c154 | 7 | « le gain total brut pour la collectivité retombe à environ 2,2 milliards » | S285 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | 3,7 % des ventes. |
| c155 | 7 | « Selon ces économistes, les clients ont gagné et les opérateurs ont perdu. » | S283, S285 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | Au niveau agrégé ; pas de collusion évoquée. |
| c156 | 7 (VISUEL) | « 6,83 Md€ économisés en 2012-2013 » | S281 | ✅ | Passe 2 : dossier + recherche (quechoisir.org) | Carte légendée « association partie prenante », non additionnée. |
| c157 | 7 (VISUEL) | « Bourreau, Sun, Verboven, version présentée en 2019 » | S285 | ✅ | Dossier | Version signalée, comme le conseille le dossier. |
| c158 | 8 | « Avril 2013 : l'hebdomadaire Marianne rapporte que Free aurait proposé de racheter Bouygues Telecom. » | S340, S341 | ✅ | Passe 2 : dossier + recherche (next.ink, universfreebox.com) | Conditionnel, attribué à Marianne. |
| c159 | 8 | « Toujours selon Marianne, un proche de Martin Bouygues, resté anonyme, affirme que celui-ci « préférerait crever » plutôt que de vendre à Free. » | S340, S341 | ✅ | Passe 2 : dossier + recherche (next.ink, universfreebox.com) | Deux mots entre guillemets ; jamais prêté à Martin Bouygues lui-même. |
| c160 | 8 | « Mars 2014 : Bouygues veut racheter SFR, et offre 10,5, puis 11,3 milliards d'euros en numéraire. » | S103, S110 | ✅ | Passe 2 : dossier + recherche (telecoms.com) | 11,3 Md€ n'est pas présenté comme l'offre finale. |
| c161 | 8 | « Un accord prévoit que, si Bouygues l'emporte, Free Mobile reprendra le réseau mobile de Bouygues Telecom » | S35, S105 | ✅ | Passe 2 : dossier + recherche (telecompaper.com, iphonesoft.fr) | Condition dite. |
| c162 | 8 | « environ 15 000 sites » | S35, S105 | ✅ | Passe 2 : dossier + recherche (telecompaper.com) | |
| c163 | 8 | « et des fréquences, pour 1,8 milliard » | S35, S105 | ✅ | Passe 2 : dossier + recherche (telecompaper.com, telecoms.com) | |
| c164 | 8 | « Dès 2014, Free figure donc dans un scénario de retour à trois opérateurs. » | S19, S35 | ✅ | Passe 2 : dossier | Synthèse prudente. |
| c165 | 8 | « Mais Vivendi choisit Numericable : accord le 5 avril 2014. » | S20 | ✅ | Passe 2 : dossier ; recoupé à cette passe via c188 (autoritedelaconcurrence.fr) | Le 5 avril : offre acceptée et accord d'exclusivité. |
| c166 | 8 | « En 2016, Orange et Bouygues négocient à leur tour. » | S21, S119 | ✅ | Passe 2 : dossier + recherche (journaldugeek.com) | |
| c167 | 8 | « Le 1er avril, Bouygues y met fin. » | S21, S120 | ✅ | Passe 2 : dossier + recherche (journaldugeek.com) | |
| c168 | 8 | « Puis, en octobre 2025, les rivaux s'allient. » | S297 | ✅ | Passe 2 : dossier + recherche (bouygues.com) | Offre conjointe du 14/10/2025. |
| c169 | 8 | « Bouygues Telecom, Free et Orange font une offre commune, non engageante, de 17 milliards d'euros de valeur d'entreprise » | S297, S299, S22 | ✅ | Dossier + recherche (iliad.fr, bouygues.com, corporate.bouyguestelecom.fr) | S22 porte le lien Altice France / SFR de la même phrase. |
| c170 | 8 | « pour une grande partie des activités d'Altice en France, propriétaire de SFR » | S297, S299, S22 | ✅ | Dossier + recherche (iliad.fr, corporate.bouyguestelecom.fr, orange.com) | Titre exact des communiqués. |
| c171 | 8 | « Altice refuse. » | S301 | ✅ | Passe 2 : dossier | Jour du rejet non donné. |
| c172 | 8 | « En avril 2026, nouvelle offre, et négociations exclusives. » | S136, S304 | ✅ | Passe 2 : dossier + recherche (orange.com, bouygues.com) | 20,35 Md€, exclusivité jusqu'au 15/05/2026. |
| c173 | 8 | « le 6 juin 2026, les trois annoncent la signature d'un protocole d'accord avec Altice France en vue d'acquérir SFR » | S311, S312, S313 | ✅ | Dossier + recherche (bouygues.com, orange.com, titres) | Formule « annoncent la signature » conforme ; projet rappelé ensuite. |
| c174 | 8 | « 20,35 milliards d'euros de valeur d'entreprise pour les actifs concernés, sous réserve d'ajustements » | S311, S312, S313 | ✅ | Passe 2 : dossier + recherche (corporate.bouyguestelecom.fr) | |
| c175 | 8 | « Plus de 8 millions de clients, selon iliad » | S23, S312 | ✅ | Passe 2 : dossier + recherche (corporate.bouyguestelecom.fr) | Attribué ; « clients » et non « abonnés » ; non additionné. |
| c176 | 8 | « dont toute la base de RED by SFR, 6 millions » | S23, S312 | ✅ | Passe 2 : dossier + recherche (corporate.bouyguestelecom.fr) | |
| c177 | 8 | « C'est le nom du forfait que SFR opposait à Free Mobile en janvier 2012. » | S24 | ✅ | Passe 2 : dossier | Titre de S24. |
| c178 | 8 | « Le perturbateur absorberait la riposte : ça, c'est notre lecture, pas celle des communiqués. » | S24, S312 | ✅ | Passe 2 : dossier | Lecture éditoriale signalée, au conditionnel. |
| c179 | 8 | « Le nouveau venu de 2012 compte, fin juin 2026, 15,8 millions d'abonnés mobiles, selon iliad » | S319, S322 | ✅ | Passe 2 : dossier + recherche (iliad.fr) | Derniers chiffres publiés au 7 octobre 2026. |
| c180 | 8 | « près d'une carte SIM sur cinq, d'après notre calcul » | S319, S322 | ✅ | Passe 2 : dossier (calcul) | 15,8 / 84,7 = 18,7 % ; pas présenté comme une part de marché. |
| c181 | 8 | « Et il cosigne un projet qui ferait passer le marché de quatre à trois opérateurs de réseau. » | S312, S139 | ✅ | Passe 2 : dossier | Conditionnel, « projet ». |
| c182 | 8 | « Mais au 7 octobre 2026, ce n'est qu'un projet. » | S315, S312 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Aucune décision possible avant ce délai. |
| c183 | 8 | « Le 15 juillet, la Commission européenne a renvoyé à l'Autorité de la concurrence l'examen de la part d'iliad. » | S315 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | |
| c184 | 8 | « L'Autorité examinera en parallèle les trois opérations, distinctes mais liées » | S315 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | « Concomitantly ». |
| c185 | 8 | « pendant au moins dix-huit mois » | S315 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Pas de date de fin, ni dans la narration ni dans le VISUEL. |
| c186 | 8 (VISUEL) | « 14/10/2025 : offre non engageante de 17 Md€ de valeur d'entreprise (actifs visés) ; rejetée mi-octobre » | S297, S299, S301 | ✅ | Dossier + recherche (iliad.fr, bouygues.com, corporate.bouyguestelecom.fr) | Correction 16 de la passe 2 appliquée ; prise d'acte du rejet le 15/10/2025. |
| c187 | 8 (VISUEL) | « 17/04/2026 : négociations exclusives ; prix réparti à environ 42 % Bouygues Telecom / 31 % Free / 27 % Orange » | S136, S304 | ✅ | Dossier + recherche (bouygues.com, orange.com) | Clé d'avril 2026, distincte de celle d'octobre 2025. |
| c188 | 8 (VISUEL) | « 05/04/2014 : SFR → Numericable » | S20 | ⚠️ | Dossier + recherche (autoritedelaconcurrence.fr) | Le 5 avril est l'acceptation de l'offre, pas le transfert (autorisation le 30/10/2014, réalisation le 27/11/2014) → correction 6. |
| c189 | 8 (VISUEL) | « 01/04/2016 : fin des négociations Orange-Bouygues » | S21 | ✅ | Dossier + recherche (bouygues.com) | Communiqué de Bouygues du 1er avril 2016. |
| c190 | 8 (VISUEL) | « RED by SFR 6,0 / grand public SFR 1,6 / TPE 0,4 million » | S312, S23 | ✅ | Dossier + recherche (iliad.fr, corporate.bouyguestelecom.fr) | Projet, attribué. |
| c191 | 8 (VISUEL) | « peuvent inclure le fixe » | S312, S23 | ✅ | Dossier | Correction 18 de la passe 2 appliquée. |
| c192 | 8 (VISUEL) | « environ 15,5 fin 2024 et 15,8 au 30/06/2026 » | S131, S319 | ✅ | Dossier + recherche (iliad.fr) | Points 2025 et 31/03/2026 non validés, donc omis ; trou signalé. |
| c193 | 8 (VISUEL) | « périmètre des trois opérations examinées » | S315 | ✅ | Dossier | Formule de 7.4. |
| c194 | 9 | « Les prix : oui, en partie. » | S16 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | Verdict éditorial annoncé, fidèle à « en partie ». |
| c195 | 9 | « Moins 11,4 % en 2012, contre moins 2,9 % par an de 2006 à 2010. » | S16, S61 | ✅ | Passe 2 : dossier | Comparaison avant / après ; réserve de méthode dite en section 4. |
| c196 | 9 | « Mais l'Arcep n'attribue la baisse qu'en partie au quatrième opérateur » | S16, S284 | ✅ | Passe 2 : dossier | Discours indirect, sans exagération. |
| c197 | 9 | « selon l'étude publiée en 2021, 32 % du gain des clients vient des marques de combat des opérateurs en place » | S16, S284 | ✅ | Passe 2 : dossier + recherche (aeaweb.org) | 32 % = version publiée. |
| c198 | 9 | « Les concurrents : secoués, pas cassés. » | — | ✅ | Passe 2 : dossier | Verdict éditorial annoncé, étayé ensuite. |
| c199 | 9 | « Les comptes de Bouygues Telecom et de SFR plongent en 2012 » | S262, S265, S253 | ✅ | Passe 2 : dossier | Indicateurs en recul d'environ 30 % ; aucune causalité affirmée. |
| c200 | 9 | « et Bouygues parle de turbulences » | S262, S265, S253 | ✅ | Passe 2 : dossier | Mot de S253, discours indirect. |
| c201 | 9 | « Mais les trois historiques invoquent aussi, avant comme après 2012, les baisses de tarifs imposées par le régulateur » | S270, S268, S261, S253, S262 | ✅ | Passe 2 : dossier + recherche (sec.gov, non concluante) | Validé en 6.15. |
| c202 | 9 | « aucun document financier que nous avons pu vérifier ne relie explicitement un plan social à Free » | S270, S268, S261, S253, S262 | ✅ | Dossier + recherche (bouygues.com) | Correction 20 de la passe 2 appliquée ; constat borné. |
| c203 | 9 | « Les trois sont toujours là en 2026. » | S311 | ✅ | Passe 2 : dossier | |
| c204 | 9 | « L'un d'eux est même à vendre. » | S311 | ✅ | Passe 2 : dossier | Projet rappelé juste après. |
| c205 | 9 | « Le marché : non. » | — | ✅ | Passe 2 : dossier | Verdict éditorial annoncé, étayé par S192, S196, S139, S311 et S315. |
| c206 | 9 | « L'investissement mobile ne s'effondre pas, les revenus repartent fin 2016 » | S192, S196, S139 | ✅ | Passe 2 : dossier + recherche (arcep.fr) | |
| c207 | 9 | « le marché fonctionne avec quatre opérateurs de réseau depuis 2012 » | S192, S196, S139 | ✅ | Passe 2 : dossier | |
| c208 | 9 | « Jusqu'au projet de 2026, qui le ramènerait à trois, avec Free parmi les acheteurs. » | S311, S139, S315 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Conditionnel, « projet ». |
| c209 | 9 | « Selon l'UFC-Que Choisir, SFR et RED by SFR annoncent en 2026 des hausses de prix à la plupart de leurs abonnés » | S326, S327 | ✅ | Passe 2 : dossier + recherche (quechoisir.org) | |
| c210 | 9 | « après une relance des hausses chez Orange » | S326, S327 | ✅ | Passe 2 : dossier + recherche (quechoisir.org) | |
| c211 | 9 | « L'association y voit, parmi d'autres explications, un lien possible avec la vente de SFR ; c'est son analyse, pas un fait établi. » | S326 | ✅ | Dossier + recherche (quechoisir.org) | Correction 21 de la passe 2 appliquée ; analyse attribuée. |
| c212 | 9 | « En 2012, on se demandait ce que change un quatrième opérateur. » | S184 | ✅ | Passe 2 : dossier | Questions non prêtées à Silicani. |
| c213 | 9 | « Le communiqué d'iliad, lui, affirme : « Free restera Free ». » | S23 | ✅ | Passe 2 : dossier + recherche (iliad.fr) | Attribué au communiqué (Citations vérifiées n° 7). |
| c214 | 9 | « Un autre tourne désormais, à l'Autorité de la concurrence. » | S315 | ✅ | Passe 2 : dossier + recherche (autoritedelaconcurrence.fr) | Métaphore ; aucune date de fin. |

## Juridique et règles

Remarques du contrôle juridique (passe 3), toutes retenues :
1. **« Sur scène… « pigeons » »** (section 2) : une remarque péjorative est prêtée à une personne réelle nommée, avec une précision (« sur scène ») que les sections détaillées du dossier ne portent pas. Le dossier prévient lui-même que la réplique a pu venir du faux documentaire projeté pendant la keynote (6.3, 8.2). Le résumé d'angle (l. 25) dit bien « sur scène », mais il contredit les sections détaillées : il ne suffit pas pour écarter la remarque. **Retenue → correction 1.** La passe 2 avait déjà retenu par prudence une remarque sur les « pigeons » (phrase « racket » supprimée).
2. **Insinuation par juxtaposition** (fin de la section 2, début de la section 3) : malgré « un détail surprend » (correction 5 de la passe 2), l'enchaînement Sosh et B&You → « Yalta » → entente continue de suggérer une coordination en 2011, et la phrase-garde ne fait que limiter le démenti à « notre dossier ». **Retenue → correction 2**, qui remplace la phrase-garde par les périodes sanctionnées [S160]. Facultatif, à mots constants : le scénariste peut rappeler d'un mot l'explication de l'Arcep (offres moins chères lancées « en prévision du quatrième opérateur » [S157][S273], déjà en section 6).
3. **Réfutation implicite de Bruno Deffains** (section 6) : la projection, faite par une personne privée nommée, est opposée à une série dont rien ne dit qu'elle a le même périmètre. **Retenue → correction 4.**

S'y ajoute un point mixte, faits et juridique : le motif du jugement Deffains (c116, c138) paraphrase une décision non lue qui concerne une personne privée → correction 3.

Points conformes :
- **Conseil financier** : aucun. Le script ne parle jamais de l'action Iliad ni de bourse. « Valeur d'entreprise » ne désigne que le montant des opérations.
- **Procédures et issues** :
  - entente de 2005 : amendes confirmées, affaire close en mai 2012 ;
  - dénigrement (tribunal de commerce, 22/02/2013) : première instance, condamnations dans les deux sens, appel de Free, « issue non trouvée ». Le contrôle juridique ne trouve pas non plus d'arrêt d'appel (edcom.fr 23682 ; universfreebox.com 19884) ;
  - procédure Deffains : saisie attribuée à la presse, débouté de Free Mobile, appel non trouvé ; après la correction 3, plus aucun motif non sourcé ;
  - examen par l'Autorité de la concurrence : présenté comme un projet au 7 octobre 2026.
- **Attributions** :
  - citations : Montebourg (tweet, carton texte), Roussat (« selon la presse spécialisée »), Richard (« show indigne », deux mots), Roussel, « préférerait crever » (source anonyme rapportée par Marianne, attribution dans la phrase ; aucun démenti trouvé : ozap.com 446733, next.ink 30637, universfreebox.com 20701), « Free restera Free » (communiqué d'iliad) ;
  - l'UFC est présentée comme partie prenante, et son analyse sur la vente de SFR comme la sienne ;
  - les lectures de la rédaction sont signalées (« Notre lecture », « d'après notre calcul », « c'est notre lecture, pas celle des communiqués »).
- **VISUEL** : aucun type interdit. Pas d'extrait de la keynote, d'un JT ou de France 5, pas de capture de tweet, pas d'image IA réaliste ni de photo de presse. Seulement des illustrations en aplats, des graphiques, frises et cartes générés en code, et du stock sous licence commerciale, sans personne identifiable.
- **Vie privée** : le domicile de Bruno Deffains (Nancy) n'est jamais cité, et le soupçon d'un commanditaire concurrent n'est pas repris. Cela doit rester ainsi, y compris dans les VISUEL.
- **Ton** : équilibré, les deux camps sont représentés. La pique de Montebourg contre Nicolas Sarkozy est une citation publique, attribuée, d'un élu, et contrebalancée par Roussat et Richard.

## Déjà vu

- **Épisodes précédents** : aucun. `state/episodes.json` ne contient que `free-mobile`, c'est-à-dire cet épisode, et son champ `structure` vaut `null`. C'est le premier épisode de la chaîne : il n'y a rien à comparer, ni type de récit associé à un type d'accroche, ni séquence de beats, ni tournures recyclées. **RAS.**
- **Empreinte** : présente et complète (type, accroche, séquence, pourquoi cette structure, dispositifs de signature). Les corrections 1 et 2 de la passe 2 sont appliquées. La séquence suit l'ordre réel des sections 1 à 9. L'ADSL de 2002 (rembobinage) et la procédure Deffains (contre-expertise) n'y figurent pas, mais ce sont des sous-éléments, pas des beats. Une fois le script validé, le producteur devra copier cette empreinte dans le champ `structure` de `episodes.json`, qui sert aux prochains contrôles de déjà-vu.
- **Tournures propres à cet épisode, à ne pas recycler** : « On rouvre le dossier, pièce par pièce » ; « d'après notre calcul » (à varier d'un épisode à l'autre) ; « c'est notre lecture, pas… » ; « on n'additionne pas » ; « Souvenez-vous : » ; « Voilà le retournement » ; « Le rebondissement est dans le détail » ; l'appel final « Le prochain dossier, dites-nous en commentaire lequel ouvrir », qui pousse vers le même format.

## Format

- **Longueur** : 2 291 mots aujourd'hui (~15,3 min) et 2 282 mots une fois les corrections appliquées (~15,2 min), dans la fourchette de 1 800 à 2 300 (`python pipeline/narration.py`, sans titres, tags, lignes VISUEL, Journal ni Empreinte). Il restera 18 mots de marge. La durée dépasse un peu la cible de 12 à 15 min de CLAUDE.md, mais la règle du fact-check porte sur le nombre de mots : non bloquant.
- **Accroche** : 73 mots, soit environ 29 s à 150 mots par minute, donc moins de 30 s. La question à trois sens (« casser quoi : les prix, les concurrents, ou le marché lui-même ? ») arrive vers le 50e mot, avec le teaser de juin 2026.
- **Promesse** : posée et tenue. Le verdict en trois lignes et la question inversée sont en section 9, la pièce de juin 2026 en section 8 (« Voilà le retournement »), le ÷2 est mesuré (« Gardez ce chiffre » en section 3, −30 % en section 7), et la question du réseau, posée en section 2, trouve son paradoxe en section 5.
- **Tags** : les 126 tags distincts du script existent tous dans `sources.md` (S1 à S356, sans trou ni doublon), et S355 n'est plus utilisée. Aucune phrase factuelle de la narration n'est sans tag : les phrases non taguées sont des questions, des transitions ou des verdicts annoncés comme éditoriaux, suivis de phrases taguées. Les quelques dates affichées sans tag dans les VISUEL (« 10.01.2012 — 08:30 », compteur J+2 / J+15 / J+16, carton « au 7 octobre 2026 : un projet ») sont taguées dans la narration de la même section.
- **VISUEL** : une ligne par section (9 sur 9).
- **Rythme** : une relance toutes les 30 à 90 s environ, 13,3 mots par phrase en moyenne. Deux phrases longues peuvent être allégées (voir les suggestions).
