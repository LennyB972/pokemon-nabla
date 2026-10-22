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
| 2 | Systèmes : menu de départ (difficulté), level caps, échanges, style de combat | 1 |
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
- Garder la vraie horloge (RTC) et les plages horaires Gen 9 (matin 6 h-10 h, jour 10 h-19 h, soir 19 h-20 h, nuit 20 h-6 h).
- Restaurer les éclairages nocturnes de Hoenn fournis par expansion (annulation du commit `a5b079d833` : fenêtres, lampes, enseignes ; inclut le correctif d'ombre de Lavarise).
- **Vérif** : menu debug → Time Functions → Set time of day ; parcourir une ville de nuit.
- 🎮 · 🟢

### 1.5 Évolutions dans le résumé *(ajout demandé le 2026-10-12)*
- **Type** : code. Page INFO du résumé : START fait défiler l'encadré du mémo entre le mémo du dresseur et la liste des évolutions (espèce + méthode, 3 par page). Le texte des méthodes réutilise celui du Pokédex HGSS d'expansion (fonction partagée `BufferEvolutionMethodText`).
- **Vérif** : résumé d'un starter, d'Évoli (plusieurs pages), d'un Pokémon sans évolution, d'un Œuf.
- 🎮 · 🟢

---

## Phase 2 — Systèmes de jeu

### 2.1 Menu de début de partie ✅
- **Type** : script (`dynmultichoice`, `msgbox` natifs) + `VAR_NABLA_DIFFICULTY` / `FLAG_NABLA_LEVEL_CAPS`.
- Dans le camion arrêté, juste avant d'en sortir (script `InsideOfTruck_EventScript_SetIntroFlags`) : **difficulté** (Normal / Difficile) puis **level caps** (oui / non), récapitulatif et confirmation. Choix définitifs.
- La difficulté utilise le système natif (`B_VAR_DIFFICULTY` + `setdifficulty`) : cela couvre l'ancienne étape 2.5.
- 🎮 · 🟢

### 2.2 Level caps ✅
- **Type** : config + code léger. Cap dur par badge (`LEVEL_CAP_FLAG_LIST`), actif seulement si `FLAG_NABLA_LEVEL_CAPS` ; Super Bonbon et Bonbons Exp. bloqués au cap ; pas de bonus d'XP sous le cap.
- **Valeurs** : table `sLevelCapFlagMap` en tête de `src/caps.c` (une ligne par badge), à modifier librement.
- 🎮 · 🟢

### 2.3 Évolutions par échange ✅
- **Type** : data + script. Carabing ↔ Escargaume évoluent aussi avec le Fil de Liaison. Fil de Liaison vendu dans les 11 Boutiques Pokémon dès le 3ᵉ badge (critère natif `shopCriteriaFunc`). Nouveau vendeur au 3ᵉ étage du Centre Commercial de Nénucrique : tous les objets d'évolution par échange.
- 🎮 · 🟢

### 2.4 Style de combat « Choix à l'aveugle » ✅
- **Type** : code. Menu Options : SHIFT / SET / BLIND (`OPTIONS_BATTLE_STYLE_BLIND`, réglage sur 2 bits). En BLIND, la proposition de changer de Pokémon après un K.O. ne nomme pas le Pokémon adverse.
- 🎮 · 🟢

### 2.5 Petits ajouts demandés ✅
- Messages explicites au level cap (combat, Super Bonbon / Bonbons Exp.).
- Poches du sac agrandies (Objets 60, Objets rares 50, Poké Balls 30, Baies 70), mémoire des Événements Mystère libérée.
- Curseur du sac qui passe du haut au bas d'une poche (et inversement).
- 🎮 · 🟢

---

## Phase 3 — Monde et objets

### 3.1 Pokémon qui suivent ✅ (corrections au fil des tests)
- **Type** : config (`OW_FOLLOWERS_ENABLED`). Pour une cinématique qui pose problème : `setflag FLAG_TEMP_HIDE_FOLLOWER` (natif, remis à zéro au changement de map) ou `hidefollower`.
- **Vérif** : parties de test de l'utilisateur ; chaque bug signalé = une petite correction.
- 🎮 · 🟡

### 3.2 CS sans slot d'attaque ✅
- **Type** : code. Posséder la CS dans le Sac (+ badge) suffit : le premier Pokémon de l'équipe (hors Œuf) l'utilise sur le terrain. Coupe, Éclate-Roc, Force, Surf, Cascade, Plongée via A ; Vol et Flash proposés dans le menu de chaque Pokémon. Les attaques de CS peuvent être oubliées.
- 🎮 · 🟢

### 3.2 bis Course automatique ✅ *(ajout demandé)*
- Menu Options défilant (flèches) avec une ligne RUNNING : HOLD / AUTO. En AUTO, le joueur court par défaut et marche en tenant B.
- 🎮 · 🟢

### 3.3 Objets de progression ✅
- **Type** : data. 27 objets cachés (Bonbons Exp. XS→XL selon la progression, 8 Aromates, 3 Capsules Talent, 2 Patchs Talent en post-game) ; Bonbons Exp. S/M/L en Boutique selon les badges ; Aromates et Capsule Talent à Nénucrique. Référence : `docs/nabla/items.md`.
- 🎮 · 🟢

### 3.4 Événement Latios et Méga-Bracelet ✅
- **Type** : script + data. Pendant la scène d'origine de Steven sur la Route 118, au moment où il s'apprête à partir, Latios arrive et les emmène (fondu) à l'Île du Sud ; combat en duo avec Steven contre Matt et un Sbire Aqua (équipes Normal/Difficile) ; Latios Nv. 30 avec Latiosite rejoint l'équipe, Steven donne le Méga-Bracelet ; retour en fondu sur la Route 118. En post-game, l'Éon errant est toujours Latias.
- Fichiers : `data/scripts/nabla/latios_event.inc`, `data/text/nabla/latios_event.inc`.
- 🎮 · 🟡

### 3.5 Méga-Gemmes ✅
- **Type** : data + script. Méga-Gemmes en objet rare des Pokémon sauvages (lignées non légendaires) ; 17 Méga-Gemmes de Hoenn au sol (visibles) ; Steven donne celle du starter sur la Route 120 ; vendeur de 65 Méga-Gemmes à 5 000 ₽ au 4ᵉ étage de Nénucrique. Légendaires : plus tard. Référence : `docs/nabla/items.md`.
- 🎮 · 🟢

---

## Phase 4 — Contenu et équilibrage

### 4.1 Pokémon sauvages (refondue le 2026-10-17)
Constat : 420 lignées non légendaires existent, Hoenn en propose ~85. Plutôt que saturer les routes, le **Safari par région** rend tout capturable ; les routes restent proches d'Émeraude et l'utilisateur les retouche lui-même.

- **4.1a Jour/nuit 12 h / 12 h** ✅ — horaires Soleil/Lune (`OW_TIMES_OF_DAY` = GEN_7), tables de nuit possibles (`_Night`, éditables dans Porymap) ; sans table de nuit, une map garde ses rencontres.
- **4.1b Safari par région** — 4.1b-1 ✅ (Safari moderne + Kanto), 4.1b-2 ✅ (déblocage à 30 000 ₽ par région, dans n'importe quel ordre, + 7 régions + évolutions régionales dans la région du Safari), 4.1b-3 ✅ zones spéciales (100 000 ₽, après la Ligue) + Beast Balls après la Ligue. À l'entrée, choix d'une région (Kanto, Johto, Sinnoh, Unys, Kalos, Alola, Galar+Hisui, Paldea : permanentes) ; après la Ligue, zones spéciales : Starters (27 lignées, **niveau 5**), Zone Zéro (Paradoxes), Ultra-Espace (Ultra-Chimères). Niveaux selon les badges.
- **4.1c Couverture** ✅ (984 / 984 espèces non légendaires) — outil de rapport des lignées obtenables (routes, Safari, cadeaux) et manquantes, y compris les objets d'évolution introuvables ; puis combler : Arakdo, Méditikka, Mangriff, Séléroc sur les routes (comme dans Rubis/Saphir, Séléroc la nuit aux Chutes Météore), Bargantua à rayures blanches dans Galar & Hisui, pierres et objets d'évolution manquants en vente à Nénucrique.
- **4.1d Retouches des routes par l'utilisateur** — Porymap (onglet Wild Pokémon) ou listes appliquées par Claude.
- 🎮 · 🟡

### 4.2 Équipes des dresseurs importants
- **Type** : data. Champions, Conseil 4, rival, boss Aqua/Magma : équipes Normal et Difficile (objets, natures, EV, talents, IA). Compositions choisies par l'utilisateur (`docs/nabla/trainers.md`), Difficile = même composition avec niveaux et/ou sets améliorés ; Méga-Évolution à partir de la 6ᵉ arène.
- Sous-étapes : 4.2a Champions d'arène ✅ (+ règle Difficile : niveaux et level caps +10 %), 4.2b Conseil 4 et Maître ✅, 4.2c rival et Timmy ✅ (+ combat de Timmy dans la Forêt Émeraude, revanches 80/90/100), 4.2d Aqua/Magma ✅ (+ équipes de Pierre Rochard dans les deux combats en duo ; en Difficile, les partenaires suivent aussi la règle des +10 %).
- **Vérif** : combats test dans les deux modes.
- 🎮 · 🔴

### 4.3 Calibrage des level caps et des dresseurs normaux
- Relever les niveaux de tous les dresseurs ordinaires (sbires Aqua/Magma compris) et des Pokémon sauvages pour suivre la nouvelle courbe ; ajuster les level caps après des parties de test.
- 🎮 · 🟡

---

## Phase 5 — Interface

### 5.1 Name box sur les personnages importants, ajustements du résumé
- **Type** : script + config. Minimal.
- 🎮 · 🟢

---

## Phase 6 — Monde étendu : nouvelles zones et ajouts narratifs

### 6.1 Chaîne de création de maps ✅ (Porymap, `render_map.py`, `docs/nabla/zones.md`, première zone : WEST BEACH)
- **Fait** : réglage de Porymap (installé par toi), conventions de nommage (`Nabla_*`), petit script d'aperçu qui rend une map en PNG (pour relire mes maps sans ouvrir Porymap), puis une première **petite zone réelle** créée par Claude (tilesets existants) avec PNJ, texte et rencontres, accessible d'abord via le menu debug. Elle sert de test : on juge le rendu avant de décider qui dessine quoi.
- **Vérif** : warp debug vers la zone, rien de cassé ailleurs.
- 🎮 · 🟡 — ne dépend que de la phase 0 : on peut l'avancer si tu veux commencer à dessiner tôt.

### 6.2 Plan du monde étendu (en cours : `docs/nabla/world.md`)
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
