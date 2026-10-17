# PROGRESS — Pokémon Nabla

## État actuel

- **Base** : pokeemerald-expansion **1.17.2** (master, commit non tagué, `git describe` = `expansion/1.17.1-11-g87cc74b5ec`).
- **Build** : ✅ `make` passe sur macOS (devkitARM). ROM utilisée à 79,7 % (26,7 Mo / 32 Mo), EWRAM 86 %, IWRAM 87 %.
- **Jeu** : expansion + Gelure, Neige à la place de la Grêle, sans affection, types adverses affichés ; CT réutilisables, Multi Exp moderne, IV/EV chiffrés, texte instantané, 8 % de combats sauvages en double ; sans l'intro RHH.
- **Étape en cours** : phase 4. 4.1a faite ; 4.1b-1 (Safari moderne + Kanto) terminée, en attente de ton test. Prochaine : 4.1b-2 (déblocage des régions).
- **Sauvegarde** : SaveBlock1 = 15 044 octets en jeu (828 libres sur 15 872). Les sauvegardes faites avant le 2026-10-13 (agrandissement du sac) ne sont plus compatibles.

## Journal

### Session 1 — 2026-10-12
- Lecture de VISION.md, build vérifié, exploration des configs `include/config/`.
- Créé : `CLAUDE.md` (règles permanentes), `ROADMAP.md` (correspondance VISION ↔ expansion + phases), `PROGRESS.md`.
- Constats :
  - Déjà actifs par défaut : mécaniques Gen 9, Dex Gen 1-9 complet, Méga activée (mais Anneau Méga jamais donné), course en intérieur, poison sans dégâts hors combat, jour/nuit (DNS), dernière Ball utilisée, option texte « Instant ».
  - Réglables en config : Gelure (`B_USE_FROSTBITE`), doubles sauvages, level caps, CT réutilisables, Multi Exp moderne, IV/EV, followers, name box.
  - Évolutions par échange : alternatives par objet déjà présentes (Fil de Liaison…), sauf Carabing/Escargaume.
  - À coder : Nuzlocke, Choix à l'aveugle, CS sans slot, menu de début de partie.
  - Ressources libres : 381 flags `FLAG_UNUSED_*`, 29 vars `VAR_UNUSED_*`.
- Note technique : le shell de Claude doit exporter `DEVKITPRO`/`DEVKITARM` avant `make` (voir CLAUDE.md).
- Retours sur la roadmap intégrés : Nuzlocke retiré, 2 difficultés, phase 6 « Monde étendu » (nouvelles zones + ajouts narratifs) créée, post-game devient la phase 7, événement Latios/Méga-Bracelet façon ROSA en 3.4, crédits RHH en 0.2.

### Session 2 — 2026-10-12
- Étape 0.2 :
  - ROM de base vérifiée (SHA1 Émeraude US correct), rangée dans `../rom/`.
  - Flips compilé depuis les sources officielles (Alcaro/Flips) dans `../tools/flips`.
  - `make_bps.sh` : build release → patch `build/pokemon_nabla.bps` (16,8 Mo) → ré-application et comparaison SHA1 ✅.
  - `README.md` remplacé : présentation de Nabla, comment jouer, crédits RHH (pokeemerald-expansion 1.17.2) + pret.
  - `EXPANSION_INTRO` = FALSE ; code de l'intro absent de la ROM (vérifié dans les symboles).
  - **À tester par toi** : appliquer le patch sur la ROM propre, le jeu démarre sur l'écran de copyright puis l'intro Game Freak, sans la scène RHH.

- Étape 0.2 validée par l'utilisateur (le jeu se lance normalement).
- Étape 1.1 — combat moderne (`include/config/battle.h`) :
  - `B_USE_FROSTBITE` = TRUE : la Gelure remplace le Gel (VISION).
  - `B_AFFECTION_MECHANICS` = FALSE : plus d'effets d'affection en combat (comme Gen 9).
  - `B_PREFERRED_ICE_WEATHER` = SNOW : Grêle et Alerte Neige donnent la Neige (comme Gen 9).
  - `B_SHOW_TYPES` = SEEN : types de l'adversaire affichés si l'espèce a déjà été vue (même règle que l'efficacité).
  - Inchangé car déjà moderne : tout le reste de `battle.h` est à `GEN_LATEST` ; Dynamax, Téracristal et Capacités Z restent inaccessibles (leurs objets ne sont jamais donnés).
  - Tests : 0 échec ; 33 tests ignorés, tous parce qu'ils supposent la Grêle (attendu). Référence avant changement : 5 417 réussis, 0 échec.

- Étape 1.1 validée par l'utilisateur (types affichés correctement).
- Étape 1.2 — qualité de vie :
  - `I_REUSABLE_TMS` = TRUE : les CT ne s'usent plus ; les boutiques ne vendent une CT que si on ne l'a pas déjà (natif).
  - Multi Exp moderne : `I_EXP_SHARE_ITEM` = GEN_LATEST + flag `FLAG_NABLA_EXP_SHARE` (ex-`FLAG_UNUSED_0x020`). Le Multi Exp donné par M. Rochard devient un objet clé à activer/désactiver depuis le Sac (désactivé à la réception, comportement natif).
  - Résumé : page Stats → IV → EV avec valeurs chiffrées, et libellé de la page qui change (`P_SUMMARY_SCREEN_IV_EV_*`).
  - Vitesse du texte : le menu Options propose MID / FAST / INSTANT (SLOW retiré), FAST par défaut (`src/option_menu.c`, `src/new_game.c`). Une ancienne sauvegarde en SLOW s'affiche en MID.
  - Laissés tels quels (déjà présents dans expansion) : réapprendre des capacités et renommer depuis le résumé.
  - Correction : la roadmap disait à tort que « Instantané » existait déjà dans le menu.
  - Tests : 0 échec, mêmes 33 tests ignorés (Grêle) ; 1 test de l'ancien Multi Exp Gen 5 n'est plus compilé (attendu).
- Étape 1.2 validée par l'utilisateur.
- Étape 1.3 — combats sauvages en double : `WE_DOUBLE_WILD_CHANCE` = 8, `WE_DOUBLE_WILD_REQUIRE_2_MONS` = TRUE (jamais de double avec un seul Pokémon valide). Concerne les herbes et le Surf, pas la pêche ni le Parc Safari. Capture impossible tant que deux Pokémon sauvages sont sur le terrain (comportement Gen 5+, natif). Tests : 0 échec.
- Étape 1.5 — évolutions dans le résumé (demande de l'utilisateur) :
  - Rien de natif dans le résumé ; le Pokédex HGSS d'expansion sait déjà décrire chaque méthode d'évolution. Ce code a été extrait dans une fonction partagée `BufferEvolutionMethodText` (`src/pokedex_plus_hgss.c`), utilisée par le Pokédex HGSS et par le résumé.
  - Page INFO : invite « START EVOLUTION » en haut à droite (même emplacement que « START RELEARN » sur les pages d'attaques) ; START fait défiler mémo → évolutions (3 par page, la 4ᵉ ligne débordait) → mémo. Rien pour les Œufs. « Does not evolve. » si aucune évolution.
  - ⚠️ Merge upstream : l'extraction ré-indente ~290 lignes de `pokedex_plus_hgss.c` ; un conflit est probable si upstream modifie ces textes (résolution : garder notre fonction et y reporter leur changement).
  - Tests : 0 échec.
- Étape 1.5 validée par l'utilisateur après passage à 3 évolutions par page.
- Étape 1.4 — jour/nuit :
  - Config déjà correcte : `OW_ENABLE_DNS` = TRUE, vraie horloge, plages horaires Gen 9.
  - Éclairages nocturnes restaurés (accord de l'utilisateur) : patch inverse du commit expansion `a5b079d833` (93 fichiers : objets lumière sur les maps de villes, palettes `.pal`/`.pla`, tilesets, `headers.h`, correctif des Lavaridge old ladies). Appliqué sans conflit avant toute modification de map.
  - Heure du jeu = heure de l'appareil (horloge de l'émulateur) + décalage choisi à la pendule de la chambre au début. Expansion (PR #7860) ouvre cette pendule sur l'heure de l'appareil (Émeraude démarrait à 10:00) : valider sans toucher = heure réelle. Scène d'origine conservée, aucun code à changer.
  - Build OK. Pas de `make check` : seules des données de maps/tilesets ont changé.
- Étape 1.4 validée par l'utilisateur.
- Nouvelle règle : avant chaque étape, Claude présente le plan et attend le feu vert (CLAUDE.md).
- Étape 2.1 — menu de début de partie :
  - Déclenché dans le camion arrêté, quand le joueur marche vers la sortie (une ligne `call` ajoutée en tête de `InsideOfTruck_EventScript_SetIntroFlags`, demande de l'utilisateur).
  - Difficulté : `VAR_NABLA_DIFFICULTY` (ex-`VAR_UNUSED_0x404E`) branchée sur `B_VAR_DIFFICULTY`, réglée par `setdifficulty`. Un dresseur sans équipe Difficile garde son équipe Normale (natif). L'ancienne étape 2.5 est absorbée.
  - Level caps : `FLAG_NABLA_LEVEL_CAPS` (ex-`FLAG_UNUSED_0x021`), sans effet avant 2.2.
  - Premiers fichiers Nabla : `data/scripts/nabla/new_game_options.inc`, `data/text/nabla/new_game_options.inc`. Largeur des lignes vérifiée (≤ 201 px sur 208).
  - Tests : 0 échec.
- Étape 2.1 validée par l'utilisateur.
- Étape 2.2 — level caps :
  - `B_EXP_CAP_TYPE` = HARD, `B_LEVEL_CAP_TYPE` = FLAG_LIST, `B_RARE_CANDY_CAP` = TRUE, `B_LEVEL_CAP_EXP_UP` = FALSE (choix de l'utilisateur).
  - `GetCurrentLevelCap` (`src/caps.c`) renvoie `MAX_LEVEL` si `FLAG_NABLA_LEVEL_CAPS` n'est pas posé.
  - Valeurs (= Pokémon le plus fort de chaque Champion d'Émeraude) : 15, 19, 24, 29, 31, 33, 42, 46, puis 58 jusqu'au titre de Maître, aucun cap ensuite. Modifiables dans `sLevelCapFlagMap`.
  - Effets natifs du cap : plus d'XP en combat, Super Bonbon refusé, Bonbons Exp. et Pension plafonnés.
  - Tests : 0 échec.
- Étape 2.2 validée par l'utilisateur.
- Étape 2.3 — évolutions par échange :
  - Carabing/Escargaume : `EVO_ITEM ITEM_LINKING_CORD` ajouté (l'échange reste possible) dans `gen_5_families.h`.
  - Fil de Liaison ajouté à la fin des listes des 11 Boutiques Pokémon de Hoenn, visible seulement à partir de 3 badges (`ShopCriteriaByThreeBadges` dans `src/shop_criteria.c`, champ `.shopCriteriaFunc` de l'objet).
  - Nouveau vendeur (sprite d'employé de Boutique) au 3ᵉ étage du Centre Commercial de Nénucrique, derrière le comptoir entre les deux vendeuses (case 9,2) : Fil de Liaison, Roche Royale, Peau Métal, Écaille Draco, Améliorator, CD Douteux, Protecteur, Électriseur, Magmariseur, Tissu Fauche, Dent/Écaille Océan, Bel'Écaille, Sachet Senteur, Chantibonbon. Script et texte dans `data/scripts/nabla/` et `data/text/nabla/evolution_items.inc`.
  - Prix natifs d'expansion (Fil de Liaison 8 000, Roche Royale 10 000, la plupart 2 000-4 000) : à ajuster si trop chers.
  - Tests : 0 échec.
- Étape 2.3 : l'utilisateur ne s'est pas prononcé sur le prix du Fil de Liaison (question ouverte).
- Étape 2.4 — style « Choix à l'aveugle » :
  - `OPTIONS_BATTLE_STYLE_BLIND` (= 2) ; `optionsBattleStyle` passe à 2 bits dans SaveBlock2 (pris sur le padding, taille inchangée ; les options Animations/Style peuvent se décaler une fois sur les anciennes sauvegardes).
  - Menu Options : SHIFT / SET / BLIND. Script `BattleScript_FaintedMon…` : en BLIND, nouveau message `STRINGID_ENEMYABOUTTOSWITCHPKMNBLIND` sans le nom du Pokémon (le hack d'Illusion n'est pas activé dans ce cas).
- Ajouts demandés par l'utilisateur (même lot de tests) :
  - Combat : `STRINGID_PKMNATLEVELCAP` « X can't gain Exp. Points past the level cap! » au lieu de « gained 0 Exp. Points ».
  - Super Bonbon / Bonbons Exp. au cap : « X can't level up past the level cap! » (`gText_PkmnCantLevelPastCap`), seulement si un vrai cap (< 100) est atteint.
  - Sac : `FREE_MYSTERY_EVENT_BUFFERS` = TRUE (1 104 octets ; distributions e-Reader/câble impossibles sur émulateur) ; poches Objets 60, Objets rares 50, Poké Balls 30, Baies 70, CT 64 (inchangé).
  - Sac : flèche haut sur la 1ʳᵉ ligne → dernière ligne, flèche bas sur la dernière → première (`src/item_menu.c`).
  - `test/save.c` : taille SaveBlock1 mise à jour (14 916 dans le build de test) ; ce test sert désormais de garde-fou de compatibilité.
  - Tests : 0 échec après mise à jour de `test/save.c`.
- Étape 2.4 et ajouts validés par l'utilisateur.
- Étape 3.1 — Pokémon qui suivent :
  - `OW_FOLLOWERS_ENABLED` = TRUE ; autres options laissées par défaut (Ball d'origine, rebond, gros sprites cachés en intérieur, retour dans la Ball si un PNJ le percute).
  - Pas de flag permanent réservé : pour corriger une cinématique, `FLAG_TEMP_HIDE_FOLLOWER` ou `hidefollower` (natifs).
  - Coût : ROM 79,67 % (+0,01 pt), EWRAM inchangée. Tests : 0 échec.
  - Bugs de cinématique à corriger au fil des signalements (liste ci-dessous).
- Étape 3.1 : premiers tests OK selon l'utilisateur.
- Étape 3.2 — CS sans slot :
  - `PlayerHasHMForFieldMove` (`src/field_move.c`) : vrai si la CS correspondante (ITEM_HM01-08) est dans le Sac.
  - `checkfieldmove` (`src/scrcmd.c`) : si aucun Pokémon ne connaît l'attaque mais que la CS est possédée, le premier Pokémon non-Œuf est choisi (il fait l'animation, c'est le suiveur).
  - `PartyHasMonWithSurf` : vrai si la CS Surf est possédée. Cascade et Plongée passent par `checkfieldmove`.
  - Menu de l'équipe : Vol et Flash ajoutés à chaque Pokémon non-Œuf si la CS est possédée et débloquée, sans doublon et en gardant la place pour Échanger/Objet/Retour (8 actions max).
  - `P_CAN_FORGET_HIDDEN_MOVE` = TRUE.
  - Choix : la CS elle-même sert d'« objet clé » (pas de nouveaux objets ni d'icônes).
- Course automatique (demande de l'utilisateur, menu défilant choisi par lui) :
  - Menu Options défilant : 7 lignes visibles, flèches de défilement natives (`AddScrollIndicatorArrowPairParameterized`), objets autorisés dans la fenêtre (WINOUT_OBJ).
  - Nouvelle ligne RUNNING : HOLD / AUTO, stockée dans `optionsAutoRun` (1 bit du padding de SaveBlock2, taille inchangée).
  - `field_player_avatar.c` : on court si « B tenu » est différent de « AUTO ».
- Tests : 0 échec.
- Étape 3.2 et course automatique validées par l'utilisateur.
- Étape 3.3 — objets de progression (exigence : facilement modifiable plus tard) :
  - Badges requis en boutique centralisés dans `sShopItemBadgeRequirements` (`src/shop_criteria.c`) ; `ShopCriteriaByThreeBadges` remplacé par `ShopCriteriaByBadgeRequirement` (Fil de Liaison 3, Bonbon Exp. S 2, M 4, L 6).
  - Bonbons Exp. S/M/L ajoutés aux 11 Boutiques Pokémon ; 21 Aromates + Capsule Talent ajoutés à la vendeuse « vitamines » du 3ᵉ étage de Nénucrique.
  - 27 objets cachés placés avec `dev_scripts/nabla/hidden_item_spots.py` (outil réutilisable : cases accessibles à pied, sans CS, coins/culs-de-sac ; les objets de la map comptent comme obstacles). Flags `FLAG_NABLA_HIDDEN_ITEM_*` = anciens `FLAG_UNUSED_0x264`-`0x27E`.
  - Liste complète et procédure d'ajout : `docs/nabla/items.md`.
  - Tests : 0 échec.
- Boutiques à la moderne (demande de l'utilisateur) :
  - Les 11 Boutiques Pokémon de Hoenn vendent la même liste `Nabla_Pokemart_Items` (anciennes listes par ville et leurs variantes supprimées).
  - Paliers dans `sShopItemRequirements` (badges + flag optionnel), vérifiés dans `TryBuildDynamicShopItemList` pour toutes les boutiques normales. Chaque palier = nombre de badges à l'arrivée dans la ville qui vendait l'article dans Émeraude (Chrono/Bis Ball : 1 badge, rencontre de l'employé Devon). Poké Ball : flag `FLAG_ADVENTURE_STARTED`, comme à Rosalia.
  - Plus de `.shopCriteriaFunc` dans `items.h` : une seule source de vérité.
- Étape 3.4 — événement Latios (plan validé par l'utilisateur) :
  - Flags `FLAG_NABLA_HIDE_ROUTE118_STEVEN/LATIOS`, `FLAG_NABLA_HIDE_SOUTHERN_ISLAND_EVENT/LATIOS`, `FLAG_NABLA_LATIOS_EVENT_ACTIVE`, `FLAG_NABLA_RECEIVED_LATIOS` (ex-`FLAG_UNUSED_0x280`-`0x285`). Les flags « hide » sont recalculés à chaque chargement de map (OnTransition), donc rien à initialiser en début de partie.
  - Route 118 : une ligne `call` ajoutée dans `Route118_OnTransition`, deux objets (Steven, Latios). Île du Sud (intérieur) : une ligne `call` dans `OnTransition`, une table ON_FRAME ajoutée, quatre objets (Steven, Matt, Sbire, Latios). Matt utilise le sprite de membre Aqua, comme dans Émeraude.
  - Combat : `multi_2_vs_2` comme à Algatia (choix de 3 Pokémon), `TRAINER_NABLA_MATT_SOUTHERN_ISLAND` / `TRAINER_NABLA_GRUNT_SOUTHERN_ISLAND` (855-856, Normal + Difficile), partenaire `PARTNER_STEVEN_SOUTHERN_ISLAND` (Airmure 32, Métang 33). Défaite : retour au Centre Pokémon, Steven réapparaît sur la Route 118 pour réessayer.
  - Récompense : Latios Nv. 30 tenant le Latiosite (`givemon`, gestion équipe pleine → PC, surnom), Méga-Bracelet (`ITEM_MEGA_RING` renommé « Mega Bracelet »).
  - Post-game : `players_house.inc` saute la question « rouge ou bleu ? » si Latios a été reçu, et Latias erre.
  - Retour utilisateur : déclenchement déplacé dans la scène d'origine de Steven (Route 118, cases 43-45, 11), comme dans ROSA. Après son dialogue, au lieu de partir, Latios arrive (`goto_if_unset FLAG_NABLA_RECEIVED_LATIOS` ajouté dans `Route118_EventScript_StevenTrigger`). Steven de la plage supprimé, `FLAG_NABLA_HIDE_ROUTE118_STEVEN` rendu (redevenu `FLAG_UNUSED_0x280`). Défaite : `VAR_ROUTE118_STATE` remis à 0 et Steven réaffiché, la scène se rejoue. Retour de l'île en (44, 11).
  - Bug rencontré en test : la sauvegarde de l'utilisateur, faite sur la Route 118 avec l'ancienne version, gardait l'ancienne liste d'objets (23 au lieu de 22) ; `addobject` faisait apparaître l'ancien Steven au lieu de Latios. Corrigé en recopiant la liste depuis la ROM dans la sauvegarde ; règle « objets ajoutés en fin de liste uniquement » ajoutée à CLAUDE.md. À rappeler dans les notes de version : sauvegarder dans un Centre Pokémon avant de mettre à jour le patch.
  - Bug expansion corrigé : dans un combat en duo lancé par script (Île du Sud, et Algatia en vanilla), la sélection des 3 Pokémon était ignorée si le combat précédent était sauvage. `AreMultiPartiesFullTeams` (`src/battle_util.c`) lisait les drapeaux du combat précédent ; ils ne sont plus consultés qu'en combat (`gMain.inBattle`). Tests : 0 échec. Correctif à proposer à expansion.
  - Cas limite non géré : équipe ET PC pleins au moment du don (message natif « plus de place », l'événement reste bloqué sur l'île).
  - Tests : 0 échec.
- Étape 3.4 validée par l'utilisateur (événement complet, sélection d'équipe corrigée).
- Étape 3.5 — Méga-Gemmes (choix de l'utilisateur) :
  - Objets sauvages : 177 espèces/formes non légendaires des lignées Méga portent leur Méga-Gemme en objet rare (5 % / 20 %). Charizard/Raichu → gemme X ; Absol/Carchacrok/Lucario → gemme de base ; Tarsal/Kirlia → Gardevoirite ; Stalgamin → Oniglalite. Ancien objet rare → objet commun si libre (46 cas), sinon retiré (Morceau d'Étoile de Stari/Staross, Baie Sitrus de Nanméouïe).
  - 17 Méga-Gemmes de Hoenn au sol, visibles (Poké Balls ajoutées en fin de liste d'objets, flags `FLAG_NABLA_ITEM_*` ex-`FLAG_UNUSED_0x280`-`0x290`).
  - Route 120 : Steven donne aussi la Méga-Gemme du starter (`VAR_STARTER_MON`), une ligne `call` ajoutée après le Scope Devon.
  - Vendeur au 4ᵉ étage de Nénucrique (entre les deux vendeuses de CT) : les 65 autres Méga-Gemmes non légendaires (starters, X/Y/Z, autres régions), prix fixé à 5 000 ₽ (0 par défaut dans expansion).
  - Légendaires (Mewtwo X/Y, Latias, Diancie, Zygarde, Heatran, Darkrai, Zeraora, Magearna) : à traiter avec les légendaires.
  - Retours utilisateur : don de Steven et vendeur validés.
    - Gardevoirite introuvable : elle était collée à la Potion d'origine de la Route 102 (enclos en bas à gauche). L'outil exclut maintenant les cases à 2 pas ou moins d'un objet ; Gardevoirite déplacée en (16, 2), et 6 autres Méga-Gemmes collées à un objet replacées (dont celle de la Grotte Tréfonds, à côté d'un rocher à pousser).
    - Corde Sortie gratuite : objet rare réutilisable (expansion, Gen 8+), prix fixé à 1 000 ₽ (achat unique, choix de l'utilisateur).
    - Gardevoirite toujours invisible : son flag 0x280 avait servi à cacher le Steven de la plage (ancienne version de l'événement Latios), et la sauvegarde de l'utilisateur l'avait posé. Corrigé dans la sauvegarde (flag effacé + liste d'objets de la Route 102 recopiée) ; règle « ne jamais réattribuer un flag Nabla libéré » ajoutée à CLAUDE.md.
    - `dev_scripts/nabla/list_items.py` génère les tableaux de `docs/nabla/items.md` depuis les maps.
  - Outil `hidden_item_spots.py` amélioré : exclut les ponts (altitude 15) et l'altitude 0 quand le sol de la map est ailleurs ; deux objets cachés de la 3.3 déplacés (Bonbon Exp. S Route 110, Aromate Assuré Route 118).
- Étape 3.5 validée par l'utilisateur.
- Phase 4.1 refondue (choix de l'utilisateur) : pas de répartition des 420 lignées sur les routes. Les routes restent proches d'Émeraude (retouches par l'utilisateur) ; un **Safari par région** rend le reste capturable.
  - Safari : Hoenn exclu ; régions permanentes Kanto, Johto, Sinnoh, Unys, Kalos, Alola, Galar(+Hisui), Paldea (26 à 66 lignées chacune) ; zones spéciales après la Ligue : Starters (toutes régions), Zone Zéro (Paradoxes), Ultra-Espace (Ultra-Chimères). Niveaux qui suivent les badges (niveau des routes voisines au déblocage → 60-70 après la Ligue).
  - Règles du Safari d'Émeraude : 500 pas, 30 Safari Balls, POKéBLOC / S'APPROCHER (équivalents de l'Appât et de la Pierre de RF/VF, qui a 600 pas).
- Étape 4.1a — jour/nuit : `OW_TIMES_OF_DAY` = GEN_7 (matin 6-10 h, jour 10-17 h, soir 17-18 h, nuit 18-6 h) et `OW_TIME_OF_DAY_ENCOUNTERS` = TRUE. Les tables existantes servent de repli à toute heure. Tests : 0 échec.
- Fil de Liaison : 4 000 ₽, comme les autres objets d'évolution (demande de l'utilisateur).
- Étape 4.1b-1 — Safari moderne (choix de l'utilisateur : comme ROSA) :
  - Plus de mode Safari : entrée gratuite, pas de Safari Balls ni de limite de pas, vrais combats avec ses Poké Balls (doubles sauvages possibles). Script d'entrée réécrit (Pokébloc, 500 ₽, balls, `EnterSafariMode` retirés) ; textes Nabla pour l'entrée, l'info et la sortie (`data/text/nabla/safari_zone.inc`).
  - `VAR_NABLA_SAFARI_REGION` (ex-`VAR_UNUSED_0x4083`), constantes `NABLA_SAFARI_REGION_*` (`include/constants/nabla.h`). Pour l'instant Kanto est imposé à l'entrée ; remise à zéro à la sortie.
  - `src/wild_encounter.c` : dans le Safari, `GetCurrentMapWildMonHeaderId` saute à la table de la région (même principe que la Grotte Altérée) ; niveaux selon les badges (27-31 à 6 badges, 33-37, 40-45, 60-70 Maître) ; évolution dynamique par `GetEvolutionTargetSpecies` (niveau, sexe, heure… ; pas les évolutions par objet ou échange).
  - Tables de Kanto (71 Pokémon) générées par `dev_scripts/nabla/safari_tables.py` : lignées dont le premier membre est de Kanto (bébés plus récents exclus, évolutions inter-générations exclues), par type et par puissance ; relecture : `docs/nabla/safari.md`. Tables d'origine strictement inchangées.
  - Tests : 0 échec.

## Bugs connus

| Lieu | Symptôme | Statut |
|---|---|---|

## Décisions prises

| Date | Décision |
|---|---|
| 2026-10-12 | Docs de projet en français, code et commits en anglais. |
| 2026-10-12 | Nouveaux textes regroupés dans `data/text/nabla/` (scripts) et un fichier dédié (C). |
| 2026-10-12 | **Nuzlocke retiré** du projet. |
| 2026-10-12 | **2 difficultés** : Normal / Difficile, choisies en début de partie. |
| 2026-10-12 | **Level caps activables** en début de partie ; valeurs définies à la main par l'utilisateur. |
| 2026-10-12 | **CS → objets clés** obtenus aux mêmes moments de l'histoire, sans Pokémon qui connaît l'attaque. |
| 2026-10-12 | **Vraie horloge (RTC)** pour le jour/nuit. |
| 2026-10-12 | **Intro RHH retirée** ; crédit RHH dans le README, les notes de version et le générique de fin. |
| 2026-10-12 | **Nouvelles zones** : quelques zones facultatives pendant l'aventure + des zones nouvelles en post-game. Maps dessinées par l'utilisateur (Porymap) **et** par Claude. |
| 2026-10-12 | En-tête de ROM inchangé (titre `POKEMON EMER`, code `BPEE`) : les émulateurs s'en servent pour détecter la sauvegarde et l'horloge. |
| 2026-10-12 | README public en anglais (le jeu est en anglais d'abord). |
| 2026-10-12 | Combat : Gelure, Neige à la place de la Grêle, affection désactivée, types adverses affichés pour les espèces vues. |
| 2026-10-12 | QoL : CT réutilisables, Multi Exp Gen 6+ (on/off), IV/EV en valeurs chiffrées, texte MID / FAST / INSTANT (FAST par défaut). |
| 2026-10-12 | Les cases non cochées de VISION.md = « je te laisse choisir » : Claude tranche les petits réglages et les signale ; les choix qui changent l'expérience de jeu restent soumis à l'utilisateur. |
| 2026-10-13 | Éclairages nocturnes de Hoenn restaurés (patch officiel d'expansion). |
| 2026-10-13 | Mémoire des Événements Mystère libérée pour agrandir le sac ; les sauvegardes de test antérieures sont abandonnées. |
| 2026-10-13 | Level caps : cap dur, sans bonus d'XP ; valeurs = as des Champions, modifiables dans `src/caps.c`. |
| 2026-10-13 | Menu de début de partie dans le camion arrêté, juste avant la sortie ; choix définitifs. |
| 2026-10-12 | **Méga-Bracelet** donné comme dans ROSA : événement Latios après le **5ᵉ badge**, Île du Sud, combat en duo avec Steven. |

## Questions ouvertes

- Conception du Safari par région (voir message du 2026-10-17).

