# État du projet — Pokémon Nabla (au 2026-10-22)

Point de reprise d'une nouvelle session. À lire en premier, puis `CLAUDE.md` (règles permanentes), `ROADMAP.md` (plan) et `PROGRESS.md` (journal détaillé et décisions datées).

## Prompt de reprise (à envoyer en début de session)

> Pokémon Nabla. Lis d'abord `ETAT_DU_PROJET.md`, puis `CLAUDE.md` et `PROGRESS.md`, et repars de là. 4.2c (rival et Timmy) et 4.2d (Team Aqua / Magma) intégrées, en attente de mon test. Prochaine : 4.3 (relever les niveaux de tous les dresseurs ordinaires, sbires compris, et des Pokémon sauvages), à me présenter avant de commencer.

## Où on en est
Romhack d'Émeraude sur pokeemerald-expansion 1.17.2 (RHH), distribué en patch BPS. Phases 0 à 3 terminées, phase 4 en cours :
- **4.1 (Pokémon sauvages)** : faite (jour/nuit, Safari par région, couverture : 984 / 984 espèces non légendaires obtenables).
- **4.2 (dresseurs importants)** : 4.2a Champions ✅, 4.2b Conseil 4 et Maître ✅, **4.2c rival et Timmy intégrée (à tester par l'utilisateur)**, **4.2d Team Aqua / Magma intégrée (à tester par l'utilisateur)**.
- En parallèle (phase 6) : première zone **WEST BEACH** v1 faite et validée ; plan du monde dans `docs/nabla/world.md`.

## Méthode de travail avec l'utilisateur
- Français avec l'utilisateur, recommandations franches et conclusion claire ; code, commits et textes du jeu en anglais (traduction française plus tard).
- **Avant chaque étape** : présenter ce qui va être fait (quoi, où, comment on vérifie), poser les questions de conception, **attendre son feu vert**. Ne pas décider à sa place ce qui n'est pas couvert par `VISION.md` / `PROGRESS.md`.
- **Fin d'étape** : build vert, `make check` si code C de combat/config touché (0 FAIL attendu), un commit en anglais (avec la ligne `Co-Authored-By`), `git push origin master`, mise à jour de `PROGRESS.md` (journal + décisions) et de ce fichier.
- L'utilisateur teste sur `pokeemerald.gba` (build debug) avec mGBA ; sa sauvegarde `pokeemerald.sav` est à la racine (jamais commitée). Il donne son retour (« ok », corrections), puis on passe à la suite. Toujours **recompiler la ROM** après des changements (y compris ses changements Porymap) avant qu'il teste.
- **Dresseurs** : c'est **l'utilisateur qui compose les équipes** (fiche `docs/nabla/trainers.md`, format Showdown). Claude intègre dans `src/data/trainers.party` et complète :
  - **talents** : le meilleur en compétitif (sets Smogon / Coupcritique ; Coupcritique ne donne pas les taux d'utilisation) ; vérifier qu'il est dans `.abilities` de l'espèce ;
  - **capacités absentes** : 4 capacités apprises par niveau jusqu'au niveau du Pokémon (`src/data/pokemon/level_up_learnsets/gen_9.h`, pré-évolutions comprises), variées (attaque du type, couverture, soutien ; jamais 4 attaques du même type) ; pour les **combats finaux** d'un personnage, sets compétitifs (capacités des jeux officiels permises même hors CT d'Émeraude) ;
  - **IV absents** : ceux des équipes d'origine du combat (plus élevés pour le Pokémon le plus fort) ; garder les IV écrits par l'utilisateur, même étranges (ils sont voulus : IV PV 1 du Racaillou de Roxanne, IV Déf. Spé. 30 du Flutter Mane) ;
  - **noms** : écrire à la Showdown (`Arcanine-Hisui`) ; corriger les noms français (Motisma → Rotom, Gallame → Gallade, Sulfura → Moltres, Psychock → Psyshock…) ; Méga-Gemmes au nom officiel (Alakazite, Froslassite, Absolite Z…) ; formes Originelles avec les objets de la génération 9 (Adamant Crystal, Lustrous Globe, Griseous Core) ;
  - **`STARTER`** (rival) : ligne remplacée par la lignée qui contre le starter du joueur, au stade de son niveau (évolutions 16 / 36), talent Speed Boost / Torrent / Overgrow ; `STARTER @ Mega` → Méga-Gemme de la lignée ; une seule équipe écrite = 3 versions × Brendan et Flora ;
  - objets de soin d'origine (`Items:`) et IA d'origine gardés ;
  - synchroniser la fiche avec ce qui est dans le jeu (blocs « Normal (dans le jeu) »).
- **Règles des équipes** (décisions de l'utilisateur) : niveaux d'origine un peu relevés ; 6 Pokémon et une Méga-Évolution à partir de la 6ᵉ arène (deux modes) ; **Difficile = mêmes équipes, niveaux × 1,1 arrondi à l'inférieur, au moins +1** (automatique, aussi pour les level caps et les partenaires comme Pierre) ; level caps = Pokémon le plus fort de chaque Champion ; un seul cap pour la Route Victoire et la Ligue (le plus fort de Marc). Les niveaux des Pokémon sauvages et des dresseurs ordinaires suivront plus tard (4.3).
- **Porymap** (l'utilisateur a Porymap 6.3.1) : il doit **fermer Porymap** avant que Claude modifie des maps, et le rouvrir après. Quand il a modifié quelque chose : vérifier `git diff`, **annuler les réécritures cosmétiques de Porymap** (`layouts.json`, `heal_locations.json`, `map.json`, `name_clone` dans `region_map_sections.json` : `git checkout` du fichier si le contenu est identique), garder ses vrais changements, vérifier (`render_map.py`, couverture si rencontres), recompiler, committer.
- L'utilisateur veut être tenu au courant pendant les longues tâches (messages courts d'avancement).

## Environnement et commandes
- `export DEVKITPRO=/opt/devkitpro DEVKITARM=/opt/devkitpro/devkitARM` puis `make -j$(sysctl -n hw.ncpu)` → `pokeemerald.gba`.
- `make check` (~8 min) ; référence : **0 FAIL**, 5 387 réussis, 33 `ASSUMPTION_FAIL` (Grêle → Neige, normal), 18 known failing, 9 expect failing, 421 TO_DO. `make check TESTS="Nabla"` : tests Nabla (`test/nabla_*.c`).
- Patch : `./make_bps.sh` (ROM propre `../rom/emerald_us.gba`, Flips `../tools/flips`).
- `test/save.c` : garde-fou des tailles de sauvegarde.
- Tester un dresseur : menu debug (R + START) → *Trainers… → Trainer 1* (numéro) → *Try Battle* (*Double Battle* pour un duo). Mode Difficile : *Flags & Vars → Set Var XYZ…* `0x404E` = 2 (Normal = 1). Maître de la Ligue : *Set Flag* `0x87F`. Argent : *Give → Max Money*.

## Ce qui est fait
| Étape | Contenu |
|---|---|
| 0 | Docs, patch BPS, README + crédits RHH, intro RHH retirée |
| 1 | Combat moderne (Gelure, Neige, pas d'affection, types affichés) ; QoL (CT réutilisables, Multi Exp Gen 6, IV/EV chiffrés, texte MID/FAST/INSTANT) ; doubles sauvages 8 % ; jour/nuit + éclairages ; évolutions dans le résumé (START sur la page INFO) |
| 2 | Menu du camion (difficulté Normal/Difficile, level caps on/off) ; level caps durs (`src/caps.c`) ; évolutions par échange (Fil de Liaison) ; style de combat SHIFT/SET/BLIND ; messages de level cap ; sac agrandi + défilement |
| 3 | Suiveurs ; CS sans les apprendre ; course automatique ; objets de progression et boutiques à paliers de badges ; événement Latios façon ROSA (Méga-Bracelet après le 5ᵉ badge) ; Méga-Gemmes (sauvages, sol, vendeur à Nénucrique 4ᵉ) |
| 4.1 | Jour/nuit 12 h/12 h + rencontres selon l'heure ; Safari moderne par région (8 régions à 30 000 ₽, zones spéciales STARTER ZONE / AREA ZERO / ULTRA SPACE à 100 000 ₽ après la Ligue, évolutions régionales dans la région du Safari, Beast Balls après la Ligue) ; couverture complète (`coverage.py`) : Pokémon de Hoenn manquants sur les routes, objets d'évolution à Nénucrique 3ᵉ, inscriptions des Ruines du Désert (Tutétékri) |
| 4.2a | 8 Champions (équipes de l'utilisateur, Méga dès Alizée) ; level caps 16/20/27/34/35/41/51/59 ; règle Difficile (+10 %) pour les dresseurs et les caps |
| 4.2b | Conseil 4 (66-70) et Marc (72) ; cap après le 8ᵉ badge : 72 |
| 4.2c | Rival (5 combats, `STARTER`, Méga à Nénucrique) ; Timmy à Lavandia, sur la Route Victoire (Méga-Gallame) et ses revanches 80/90/100/100 ; nouveau combat de Timmy dans la Forêt Émeraude (`TRAINER_NABLA_WALLY_EMERALD_FOREST`, 857), à brancher avec la zone |
| 4.2d | Team Aqua / Magma : 10 combats (Tabitha, Max, Matt, Shelly, Arthur ; Méga-Camérupt et Méga-Sharpedo), dont les duos de l'Île du Sud et du Centre Spatial avec les équipes de Pierre Rochard (Méga-Métalosse) ; en Difficile, les partenaires suivent aussi la règle des +10 % |
| 6 | WEST BEACH v1 (bande de sable au sud de la route 115 → île de sable, hautes herbes, flaques ; rencontres de test de l'utilisateur) ; outils et marche à suivre des zones |

## En attente côté utilisateur
- **Tester la 4.2c** : rival (IDs `TRAINER_{MAY,BRENDAN}_{ROUTE_103,RUSTBORO,ROUTE_110,ROUTE_119,LILYCOVE}_{TREECKO,TORCHIC,MUDKIP}`, suffixe = starter du joueur, numéros dans `include/constants/opponents.h`), Timmy (Lavandia 656, Route Victoire 519, Forêt 857, revanches `WALLY_VR_2`-`5`).
- **Tester la 4.2d** : *Trainers… → Trainer 1* (numéro) *→ Try Battle* : Tabitha 597 / 732, Max 602 / 601, Shelly 32 / 33, Matt 30, Arthur 34 ; Île du Sud : *Trainer 1* 855, *Trainer 2* 856, *Partner* 2, *Try Battle* ; Centre Spatial : *Utilities → Steven Multi*. En Difficile, vérifier que Pierre a aussi ses niveaux +10 %.
- Pas encore testé en jeu : inscriptions de Tutétékri (Route 111).
- Il retouchera lui-même routes et West Beach dans Porymap au fil de l'eau (et préviendra).

## Prochaines étapes (dans l'ordre)
1. **4.3 Calibrage** : relever les niveaux de **tous** les dresseurs ordinaires (sbires compris, demande de l'utilisateur : simple relèvement pour suivre la courbe) et des Pokémon sauvages ; ajustement des level caps après parties de test.
2. **Phase 5 Interface** : name box sur les personnages importants, ajustements du résumé.
3. **Phase 6 Zones** (`docs/nabla/world.md`) : Forêt Émeraude au sud du Mont Mémoria (scénario : après le Mont Mémoria, Timmy signale des activités suspectes ; ennemis ; Timmy obtient Celebi ; combat obligatoire — dresseur prêt) ; îles accessibles par Plongée (hors scénario) ; contenu de West Beach.
4. **Phase 7 Post-game** : Conseil 4 renforcé, défense du titre, légendaires via des îles mirages façon Flûte Éon (sans vol en 3D).
5. **Phase 8 Release 1.0**.
- À proposer un jour en amont (expansion) : correctif `AreMultiPartiesFullTeams` (`src/battle_util.c`).

## Repères techniques
- **Dresseurs** : `src/data/trainers.party` (format Showdown ; une version `Difficulty: Hard` faite à la main est utilisée telle quelle, sinon la règle +10 % s'applique : `GetDifficultyTrainerMonLevel` dans `src/battle_setup.c`, `FillPartnerParty` dans `src/battle_partner.c` pour les partenaires, formule `GetDifficultyLevel` dans `src/caps.c`). Partenaires (Pierre) : `src/data/battle_partners.party`. Nouveaux dresseurs : `include/constants/opponents.h` (`TRAINER_NABLA_*` 855-857, `TRAINERS_COUNT_EMERALD` 858 ; place pour 6 de plus avant `MAX_TRAINERS_COUNT_EMERALD` 864). IDs : Champions 265-272, Conseil 4 261-264, Marc 335. Fiche : `docs/nabla/trainers.md`.
- **Safari** : `VAR_NABLA_SAFARI_REGION` (0x4083) ; `include/constants/nabla.h` ; `src/nabla_safari_zone.c` (régions, prix, specials, niveaux, `IsPlayerInEvolutionRegion`) ; `src/wild_encounter.c` (table de la région) ; scripts `data/scripts/nabla/safari_zone.inc` ; générateur `dev_scripts/nabla/safari_tables.py` (+ `docs/nabla/safari.md`).
- **Zones** : groupe de maps `gMapGroup_Nabla`, maps `Nabla*`, scripts inclus avant `.if IS_FRLG` dans `data/event_scripts.s`, sections de carte ajoutées en fin de `region_map_sections.json` ; `docs/nabla/zones.md` ; image d'une map : `python3 dev_scripts/nabla/render_map.py <Map> out.png --grid` (les blocs animés y sont gris).
- **Flags Nabla** : 0x20 Multi Exp, 0x21 level caps, 0x22-0x28 régions du Safari, 0x29-0x2B zones spéciales, 0x264-0x27E objets cachés, 0x280 et 0x286-0x295 Méga-Gemmes au sol, 0x281-0x285 événement Latios. **Vars** : `VAR_NABLA_DIFFICULTY` 0x404E (1 Normal, 2 Difficile), `VAR_NABLA_SAFARI_REGION` 0x4083.
- **Outils** (`dev_scripts/nabla/`) : `hidden_item_spots.py`, `list_items.py`, `safari_tables.py`, `coverage.py` (à relancer après tout changement de rencontres/cadeaux/objets ; objectif 984 / 984), `render_map.py`.
- **Docs de référence** (`docs/nabla/`) : `items.md`, `safari.md`, `couverture.md`, `zones.md`, `world.md`, `trainers.md`.
- **Fichiers d'expansion modifiés** (attention aux merges upstream ; `pokedex_plus_hgss.c` le plus risqué) : `src/{battle_message,battle_partner,battle_script_commands,battle_setup,battle_util,caps,field_move,field_player_avatar,item_menu,new_game,option_menu,party_menu,pokedex_plus_hgss,pokemon,pokemon_summary_screen,scrcmd,shop_criteria,strings,wild_encounter}.c`, `data/specials.inc`, `data/event_scripts.s`, `src/data/{items.h,trainers.party,battle_partners.party,wild_encounters.json}`, `src/data/pokemon/species_info/gen_*_families.h`, `src/data/pokemon/level_up_learnsets/gen_9.h`, `src/data/region_map/*`, `data/maps/{map_groups.json}`, `data/layouts/layouts.json`, `include/{global.h,caps.h,field_move.h,pokedex_plus_hgss.h,strings.h}`, `include/constants/{flags,vars,global,opponents,battle_partner,battle_string_ids}.h`, `include/config/*.h`, `test/battle/{evolution_tracker,ability/ball_fetch}.c`, nombreuses maps et scripts.

## Pièges déjà rencontrés
- Ne jamais réattribuer un flag/var Nabla libéré (sauvegardes de l'utilisateur).
- Objets de map ajoutés en fin de liste uniquement (sinon `addobject` casse, cas de Latios).
- Ajouts dans des listes numérotées (maps, layouts, sections de carte, dresseurs) : toujours **à la fin**, les numéros sont gardés dans les sauvegardes et les Pokémon.
- `wild_encounters.json` contient aussi les tables de RFVF (labels `_FireRed`/`_LeafGreen`) : les ignorer dans les outils ; ne pas en parler à l'utilisateur, qui ne s'occupe que d'Émeraude.
- Tests d'expansion qui supposent un comportement que Nabla change : les adapter avec un commentaire « Pokémon Nabla » (Ball Fetch, Evolution Tracker).
- Placement d'objets : `hidden_item_spots.py`. Édition de la sauvegarde de l'utilisateur : possible (format Gen 3), toujours avec une copie avant ; copies hors repo : `../pokeemerald_backup_before_latios_edit.sav`, `../pokeemerald_backup_before_gardevoirite_fix.sav`.
