# ROADMAP — Pokémon Nabla

Base : pokeemerald-expansion 1.17.2 (master, non taguée). Chaque étape = un commit, build vert, validation avant la suivante.

Légende — **Type** : `config` (réglage natif), `data` (tables, trainers), `map` (cartes), `script` (événements), `code` (C).
**ROM** : 🎮 = produit une ROM testable avec un changement visible.
**Risque** : 🟢 faible · 🟡 moyen · 🔴 élevé / coûteux.

Vue d'ensemble :

| Phase | Contenu | Dépend de |
|---|---|---|
| 0 | Fondations : docs, patch BPS, crédits | — |
| 1 | Réglages natifs (config) | 0 |
| 2 | Systèmes : menu de départ, difficulté, level caps, style de combat | 1 |
| 3 | Monde et objets : suiveurs, CS en objets clés, événement Latios + Méga | 2 |
| 4 | Contenu et équilibrage : Dex national, équipes Normal/Difficile | 2, 3 |
| 5 | Interface | 1 |
| 6 | **Monde étendu : nouvelles zones et ajouts narratifs** | 4 (6.1 peut être avancée) |
| 7 | Post-game | 6 |
| 8 | Release 1.0 | tout |

---

## 1. Correspondance VISION.md ↔ expansion

Les décisions de `PROGRESS.md` priment sur VISION.md (ex. : Nuzlocke retiré, 2 difficultés).

| Point de VISION.md | Couverture | Détail |
|---|---|---|
| Mécaniques modernes (dégâts Gen 5+, Fée, split phys/spé, talents récents) | ✅ déjà actif | Toutes les options `battle.h` sont à `GEN_LATEST`, Gen 1-9 activées |
| Méga-Évolution | ⚙️ config + script | `P_MEGA_EVOLUTIONS` = TRUE, mais il faut le **Méga-Bracelet** dans le sac (jamais donné dans Émeraude) et placer les Méga-Gemmes |
| Combats sauvages en double (faible proba) | ✅ config | `WE_DOUBLE_WILD_CHANCE` (actuellement 0) + `WE_DOUBLE_WILD_REQUIRE_2_MONS` |
| 2 difficultés au choix | ⚙️ natif partiel | `B_VAR_DIFFICULTY` + `setdifficulty` + variantes de trainers dans `trainers.party`. Il faut le menu de choix et **écrire les équipes « Difficile »** |
| Level caps activables | ⚙️ config + code léger | `caps.h` gère les caps par badge ; il manque l'interrupteur on/off (quelques lignes dans `src/caps.c`) |
| Nuzlocke | ⛔ retiré | Décision du 2026-10-12 |
| Style de combat Choix / Défini | ✅ déjà là | Option vanilla |
| « Choix à l'aveugle » | ❌ code | Variante du mode Choix qui ne révèle pas le Pokémon adverse. L'option tient sur 1 bit en sauvegarde → à élargir |
| Randomizer (plus tard) | ❌ code | Hors première version |
| IA forte pour Champions / Conseil 4 / rival / boss | ✅ natif | Flags d'IA par trainer + équipes complètes (objets, natures, EV, talents) dans `trainers.party` |
| Dex national Gen 1-9 | ✅ déjà actif | Tout est activé. **À concevoir** : où trouver ces espèces (tables de rencontres) |
| Évolutions par échange remplacées | ✅ presque natif | Chaque évolution par échange a déjà une alternative : **Fil de Liaison** ou objet utilisé depuis le sac. Seuls Carabing/Escargaume restent à traiter. Il faut surtout rendre ces objets **trouvables** |
| Course en intérieur | ✅ déjà actif | `OW_RUNNING_INDOORS` = GEN_LATEST |
| Texte rapide / instantané | 🛠️ code léger | La vitesse instantanée existe dans le moteur mais pas dans le menu Options → ajoutée en 1.2 |
| Multi Exp moderne | ✅ config | `I_EXP_SHARE_ITEM` ≥ GEN_6 : le Multi Exp (donné par M. Rochard) devient un objet clé qui couvre toute l'équipe |
| CT réutilisables | ✅ config | `I_REUSABLE_TMS` |
| CS en objets clés | ❌ code | Rien de natif. Voir étape 3.2 |
| Affichage IV / EV | ✅ config | `P_SUMMARY_SCREEN_IV_EV_INFO` |
| Aromates, Capsules Talent, Bonbons Exp. | 🛠️ data | Les objets existent ; à placer sur les maps et dans les boutiques |
| Pokémon qui suivent | ⚙️ config + tests | `OW_FOLLOWERS_ENABLED`. Sprites présents (1 324 overworld). Des cinématiques peuvent devoir cacher le suiveur |
| Cycle jour/nuit | ✅ déjà actif | `OW_ENABLE_DNS` = TRUE, horloge RTC réelle (décision) |
| Dernière Ball utilisée | ✅ déjà actif | `B_LAST_USED_BALL` = TRUE (bouton R) |
| Poison sans dégâts hors combat | ✅ déjà actif | `OW_POISON_DAMAGE` = GEN_LATEST |
| Gel = Brûlure spéciale | ✅ config | `B_USE_FROSTBITE` : la Gelure (Légendes Arceus) fait exactement ça |
| Ajouts narratifs | 🛠️ script | Phase 6 ; le premier (événement Latios) arrive dès l'étape 3.4 |
| Nouvelles zones | 🛠️ map | Phase 6 (tilesets existants, Porymap) |
| Ligue rejouable / Conseil 4 renforcé | 🛠️ data + script | Phase 7 |
| Défense du titre | ❌ script (+ code léger) | Phase 7 |
| Tous les légendaires capturables | 🛠️ script + map | Phase 7 |
| Système façon Flûte Éon | ❌ script + code | Phase 7 — s'accroche naturellement à l'événement Latios (3.4) |
| Nom au-dessus des dialogues | ✅ natif | `name_box.h` + macros de script |
| Résumé enrichi | ✅ config | IV/EV, renommer, réapprendre des capacités depuis le résumé |
| Patch BPS | 🛠️ outillage | Flips + ROM Émeraude US propre (SHA1 `f3ae0881…07b7`) |
| Crédits RHH | 🛠️ docs | Demandé par expansion : « please credit RHH (Rom Hacking Hideout) », version optionnelle. Étape 0.2 |

---

## Phase 0 — Fondations

### 0.1 Documents de projet
- `CLAUDE.md`, `ROADMAP.md`, `PROGRESS.md`. · ROM : non.

### 0.2 Distribution et crédits
- **Fait** :
  - script qui lance `make release` puis produit un `.bps` à partir d'une ROM Émeraude US propre (rangée hors du repo, SHA1 vérifié) ;
  - `README.md` remplacé par la présentation de Nabla, avec une section **Crédits** : « Built on pokeemerald-expansion 1.17.2 by RHH (Rom Hacking Hideout) » + lien vers la liste des contributeurs (`CREDITS.md`, conservé tel quel). Cette section accueillera aussi toute ressource communautaire utilisée ;
  - intro RHH désactivée (`EXPANSION_INTRO` = FALSE) — le crédit est repris dans le README, les notes de version et, en phase 8, le générique de fin.
- **Vérif** : patcher une ROM propre donne un SHA1 identique au build ; le jeu démarre sur mGBA sans l'intro RHH.
- 🎮 · 🟢 · **Bloquant** : la ROM de base.

---

## Phase 1 — Réglages natifs (config uniquement)

### 1.1 Combat moderne
- `B_USE_FROSTBITE` = TRUE, affichage des types et de l'efficacité en combat, autres ajustements à valider ensemble.
- **Vérif** : combat debug, Laser Glace → Gelure.
- 🎮 · 🟢

### 1.2 Qualité de vie
- CT réutilisables, Multi Exp Gen 6+, IV/EV dans le résumé, vitesse de texte Moyen / Rapide / Instantané.
- **Vérif** : quickstart + menu debug : utiliser une CT deux fois, ouvrir le résumé, changer la vitesse du texte.
- 🎮 · 🟢 · ⚠️ Certaines options changent le format de sauvegarde : on les fixe **avant** toute bêta publique.

### 1.3 Combats sauvages en double
- Probabilité proposée : **8 %**, seulement avec 2 Pokémon valides.
- **Vérif** : forcer via flag de debug, puis jouer quelques rencontres.
- 🎮 · 🟢

### 1.4 Jour/nuit
- Garder la vraie horloge (RTC). Vérifier la teinte et la cohérence des événements horaires.
- **Vérif** : changer l'heure via debug ; test sur mGBA et VBA-M.
- 🎮 · 🟢

---

## Phase 2 — Systèmes de jeu

### 2.1 Menu de début de partie
- **Type** : script (`dynmultichoice` natif) + flags/vars dédiés.
- Après le discours de Birch : **difficulté** (Normal / Difficile) et **level caps** (oui / non). Choix définitifs pour la partie.
- **Vérif** : nouvelle partie, vérifier flags/vars via debug.
- 🎮 · 🟢

### 2.2 Level caps
- **Type** : config + code léger. Cap par badge (`LEVEL_CAP_FLAG_LIST`), désactivé si l'option est sur « non » ; Super Bonbon bloqué au cap.
- **Valeurs définies à la main par toi** dans `src/caps.c` (on met des valeurs provisoires en attendant).
- **Vérif** : debug : au cap → pas d'XP ; badge obtenu → cap relevé ; option « non » → aucun cap.
- 🎮 · 🟢

### 2.3 Évolutions par échange
- **Type** : data. Carabing ↔ Escargaume passent au Fil de Liaison ; placement du Fil de Liaison et des objets d'évolution (Peau Métal, Écaille Draco, Protecteur…) sur les maps ou en boutique.
- **Vérif** : debug : Kadabra + Fil de Liaison → Alakazam ; Carabing + Fil de Liaison → Lançargot.
- 🎮 · 🟢

### 2.4 Style de combat « Choix à l'aveugle »
- **Type** : code. 3ᵉ valeur dans le menu Options, message « L'adversaire va envoyer un Pokémon. Changer ? » sans nom.
- **Vérif** : combat dresseur dans les 3 modes.
- 🎮 · 🟡

### 2.5 Branchement de la difficulté
- **Type** : config + script. `B_VAR_DIFFICULTY` relié au choix 2.1. Les équipes « Difficile » sont écrites en phase 4.
- **Vérif** : un dresseur de test change d'équipe selon la difficulté.
- 🎮 · 🟢

---

## Phase 3 — Monde et objets

### 3.1 Pokémon qui suivent
- **Type** : config + correctifs de scripts.
- **Vérif** : parcourir les cinématiques clés (Team Aqua/Magma, Mont Chimnée, Pilier Céleste, Musée…) via sauvegardes debug.
- 🎮 · 🟡 — bugs visuels possibles en cinématique ; corrigés au fil de l'eau.

### 3.2 CS en objets clés
- **Type** : code + script. Chaque CS devient un **objet clé** obtenu au même moment de l'histoire ; l'action de terrain marche si objet + badge, sans Pokémon qui connaît l'attaque. Les CS restent des CT normales pour qui veut l'attaque en combat.
- **Vérif** : parcours Coupe / Éclate-Roc / Force / Surf / Cascade / Plongée / Flash / Vol sans aucun Pokémon compatible.
- 🎮 · 🟡

### 3.3 Objets de progression
- **Type** : data. Aromates, Capsules Talent, Bonbons Exp. sur les maps et dans quelques boutiques (selon les badges).
- **Vérif** : parcours debug ; liste des emplacements dans PROGRESS.md.
- 🎮 · 🟢

### 3.4 Événement Latios et Méga-Évolution *(1er ajout narratif)*
- **Type** : script + data. Inspiré de ROSA : déclenché **après le 5ᵉ badge** (Norman — le joueur obtient Surf juste après, ce qui ouvre l'est de la Route 118), Steven sur la Route 118 ; Latios apparaît et demande de l'aide ; Île du Sud ; combat en duo avec Steven contre un Admin + un Sbire (le partenaire de combat est natif) ; Latios rejoint l'équipe avec son Latiosite et Steven donne le **Méga-Bracelet**. Puis placement des autres Méga-Gemmes.
- Points à trancher dans la mini-conception : comment rejoindre l'Île du Sud sans le vol en 3D, quelle équipe (Aqua ou Magma), et comment ça s'articule avec le Latios/Latias post-game d'Émeraude (choix à la TV, Passe Éon).
- **Vérif** : jouer la scène depuis une sauvegarde debug à 5 badges ; Méga-Évolution en combat.
- 🎮 · 🟡

---

## Phase 4 — Contenu et équilibrage

### 4.1 Répartition du Dex national
- **Type** : data. Intégrer les espèces Gen 1-9 dans les rencontres de Hoenn en gardant l'identité de chaque zone (espèces de Hoenn toujours majoritaires). Les nouvelles zones (phase 6) accueilleront une bonne partie du reste.
- **Vérif** : tableau de répartition relu par toi avant intégration, **zone par zone**, par tranches de badges.
- 🎮 · 🔴

### 4.2 Équipes des dresseurs importants
- **Type** : data. Champions, Conseil 4, rival, boss Aqua/Magma : équipes Normal et Difficile (objets, natures, EV, talents, IA).
- **Vérif** : combats test dans les deux modes.
- 🎮 · 🔴

### 4.3 Calibrage des level caps et des dresseurs normaux
- 🎮 · 🟡

---

## Phase 5 — Interface

### 5.1 Name box sur les personnages importants, ajustements du résumé
- **Type** : script + config. Minimal.
- 🎮 · 🟢

---

## Phase 6 — Monde étendu : nouvelles zones et ajouts narratifs

### 6.1 Chaîne de création de maps
- **Fait** : réglage de Porymap (installé par toi), conventions de nommage (`Nabla_*`), petit script d'aperçu qui rend une map en PNG (pour relire mes maps sans ouvrir Porymap), puis une première **petite zone réelle** créée par Claude (tilesets existants) avec PNJ, texte et rencontres, accessible d'abord via le menu debug. Elle sert de test : on juge le rendu avant de décider qui dessine quoi.
- **Vérif** : warp debug vers la zone, rien de cassé ailleurs.
- 🎮 · 🟡 — ne dépend que de la phase 0 : on peut l'avancer si tu veux commencer à dessiner tôt.

### 6.2 Plan du monde étendu
- **Fait** : un document `docs/nabla/world.md` qui liste chaque nouvelle zone (rôle, accès, moment du jeu, rencontres, liens avec l'histoire, **dessinée par toi ou par Claude**) et chaque ajout narratif (scène, personnages, déclencheur).
- Deux familles de zones : **quelques zones facultatives pendant l'aventure** et **des zones nouvelles en post-game**.
- **Vérif** : validé par toi avant toute construction. Nécessite tes idées.
- ROM : non · 🟢

### 6.3 et suivantes — Construction zone par zone et scène par scène
- Une zone ou une scène = une étape = un commit, testable.
- Règle : les maps d'origine ne sont touchées que pour **ajouter une entrée** (porte, grotte, connexion), jamais pour retirer quelque chose.
- 🎮 · 🔴 (volume)

---

## Phase 7 — Post-game

| Étape | Contenu | Risque |
|---|---|---|
| 7.1 | Conseil 4 renforcé après la 1ʳᵉ victoire (rematch) | 🟡 |
| 7.2 | Défense du titre (challengers à la Ligue) | 🟡 |
| 7.3 | Légendaires et fabuleux capturables — d'abord ceux qui ont une place logique, puis le reste dans les zones de la phase 6 | 🔴 |
| 7.4 | Système « Flûte Éon » : îles mirages débloquées sous conditions, introduit par Latios | 🔴 |

Chaque étape fera l'objet d'une mini-conception validée avant de commencer.

## Phase 8 — Release 1.0
Build release, patch BPS, tests sur plusieurs émulateurs (mGBA, VBA-M, un émulateur mobile), crédit RHH dans le générique de fin, notes de version. 🟢

## Plus tard
Randomizer, formes inventées (sprites à fournir), traduction française, Parc Safari, Zone de Combat.

---

## Risques transverses

- **Sauvegarde** : nouvelles options = nouvelles données en sauvegarde. On fige le format avant toute bêta publique.
- **Mises à jour upstream** : on suit `upstream/master` de temps en temps (une étape dédiée à chaque merge). Modifier les configs en place, sans dupliquer, limite les conflits. En cas de conflit sur `README.md`, garder le nôtre.
- **Espace ROM** : 79,7 % utilisés avec tout le Dex. Suffisant pour maps et scripts ; à surveiller avec musique ou graphismes ajoutés.
- **Horloge** : la vraie horloge marche sur mGBA et VBA-M ; certains émulateurs plus anciens ne la gèrent pas (le jeu tourne, mais sans jour/nuit fiable). À signaler dans les notes de version.
