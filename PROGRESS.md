# PROGRESS — Pokémon Nabla

## État actuel

- **Base** : pokeemerald-expansion **1.17.2** (master, commit non tagué, `git describe` = `expansion/1.17.1-11-g87cc74b5ec`).
- **Build** : ✅ `make` passe sur macOS (devkitARM). ROM utilisée à 79,7 % (26,7 Mo / 32 Mo), EWRAM 86 %, IWRAM 87 %.
- **Jeu** : expansion + Gelure, Neige à la place de la Grêle, sans affection, types adverses affichés ; CT réutilisables, Multi Exp moderne, IV/EV chiffrés, texte instantané, 8 % de combats sauvages en double ; sans l'intro RHH.
- **Étape en cours** : phase 4. 4.1, 4.2a et 4.2b faites ; 4.2c (rival et Timmy) et **4.2d (Team Aqua / Magma, avec les équipes de Pierre Rochard)** intégrées, en attente du test de l'utilisateur. **4.3 (niveaux des dresseurs ordinaires et des sauvages)** faite. Phase 5 : **5.1 name box** faite et validée ; **5.2 (plusieurs objets d'un coup, menus en boucle)** faite, à tester ; 5.3 (vitamines et autres objets d'entraînement) en attente des valeurs de l'utilisateur. Phase 6 : WEST BEACH v1 validée ; plan du monde dans `docs/nabla/world.md`.
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
- Étape 4.1b-2 — déblocage des régions du Safari :
  - Comptoir : menu des régions ouvertes (+ « UNLOCK A REGION » tant qu'il en reste, + CANCEL). Le déblocage coûte 30 000 ₽ (`NABLA_SAFARI_REGION_PRICE`), dans n'importe quel ordre, définitif ; après un achat (ou un refus faute d'argent) on reste dans la liste des régions à acheter, B revient au menu des régions. Plus de question oui/non : le menu s'ouvre directement.
  - Flags `FLAG_NABLA_SAFARI_JOHTO` … `PALDEA` (0x22-0x28, jamais utilisés). Kanto n'a pas de flag (toujours ouvert).
  - `src/nabla_safari_zone.c` : liste des régions (nom, flag, régions d'évolution), specials du comptoir (`NablaSafariZone_*`, dans `data/specials.inc`), `InSafariZoneRegion` (déplacé depuis `src/wild_encounter.c`).
  - Évolutions régionales : les conditions `IF_REGION` / `IF_NOT_REGION` d'expansion utilisent la région du Safari visitée (`IsPlayerInEvolutionRegion`, `src/pokemon.c`). Ex. Pikachu + Pierre Foudre → Raichu d'Alola dans le Safari Alola ; Feurisson niv. 36 → Typhlosion de Hisui dans Galar & Hisui ; ailleurs, formes normales. Vaut aussi pour les sauvages du Safari (évolution dynamique). Test : `test/nabla_safari_zone.c`.
  - 7 régions générées (Johto 49, Sinnoh 35, Unys 66, Kalos 28, Alola 41, Galar & Hisui 56, Paldea 39 lignées), Kanto régénéré (71).
  - Générateur corrigé et complété :
    - types et stats écrits en macros (Rondoudou, Mélofée, Togepi, Motisma… n'avaient pas de type) et espèces construites par macros (Zarbi, Lépidonille, Flabébé, Couafarel, Météno manquaient) ;
    - Pikachu casquette d'Alola exclu ;
    - les non-Eau des groupes d'œufs Eau 1/2 (Minidraco, Delibird, Inkay…) vont aussi dans l'eau ;
    - les lignées à évolution régionale vivent aussi dans cette région (Pikachu, Noeunoeuf, Osselait en Alola ; Smogo, Mime Jr., Teddiursa, Chlorobule, Furaiglon, Grelaçon, Mucuscule en Galar & Hisui) ;
    - chaque table a un minimum de variété (6 espèces en herbes, 3 en surf/pêche, 2 sous les rochers), complétée avec les Pokémon les moins présents de la région (les plus faibles avant la Ligue, les plus forts après) ;
    - le surplus d'une région ne va plus que dans les zones post-Ligue. Les Pokémon Roche sont dans les herbes (ou l'eau) **et** sous les rochers.
  - À prévoir (4.1c) : Ursaring → Ursaking demande un Bloc de Tourbe (introuvable pour l'instant), comme d'autres évolutions de Galar/Hisui par objet.
  - Tests : 0 échec (5 382 réussis) + test Nabla.
  - Testé par l'utilisateur : refus sans argent, régions conservées après sauvegarde, Raichu d'Alola obtenu.
- Couverture (analyse du 2026-10-18, script provisoire) : 569 lignées (formes cosmétiques regroupées, formes régionales à part), 480 obtenables après la 4.1b-3. Manquent : 84 légendaires/fabuleux (phase 7) ; Arakdo, Méditikka, Mangriff, Séléroc (absents d'Émeraude) ; Paragruel (Bargantua à rayures blanches non capturable). Le second fossile est bien au Passage du Désert après la Ligue. Objets d'évolution introuvables : Pierres Aube, Nuit, Éclat, Glace ; objets de Galar/Hisui/Paldea (Galanoa, pommes, théières, armures, Obsidienne, Bloc de Tourbe, Emblème du Général, Métal Composite, pièces de Mordudor) ; Pierres Feu/Eau/Foudre/Plante en un seul exemplaire. → 4.1c.
- Étape 4.1b-3 — zones spéciales du Safari :
  - Après la Ligue (`FLAG_IS_CHAMPION`), la liste d'achat propose STARTER ZONE (27 starters, niveau 5), AREA ZERO (20 Paradoxes) et ULTRA SPACE (10 Ultra-Chimères, Mandrache par évolution) à 100 000 ₽ (`NABLA_SAFARI_SPECIAL_PRICE`). Flags `FLAG_NABLA_SAFARI_STARTERS` / `PARADOX` / `ULTRA_BEASTS` (0x29-0x2B).
  - `sSafariZoneRegions` : prix, texte du prix et condition « après la Ligue » par région ; specials `NablaSafariZone_CountRegionsForSale` et `NablaSafariZone_TryBuyRegion` (vérifie et retire l'argent). La confirmation affiche le prix de la région. `GetSafariZoneRegionWildLevel` déplacé dans `src/nabla_safari_zone.c` (niveau 5 dans la STARTER ZONE).
  - Message d'entrée : « Today's destination: … ! ».
  - Beast Ball : 1 000 ₽, dans la liste commune des Boutiques, visible une fois Maître (`sShopItemRequirements`).
  - Générateur : Mandrache n'est plus listé à part (il évolue de Vémini). Une zone sans Pokémon Eau ou Roche n'a pas de rencontre en surf/pêche ou sous les rochers (demande de l'utilisateur : starters Plante et Feu dans les herbes, Eau seulement dans l'eau ; Ultra-Chimères seulement dans les herbes et sous les rochers).
  - Tests : 3 tests Nabla (évolutions régionales, niveaux, vente des zones spéciales).
  - Testé par l'utilisateur : niveau 5 dans la STARTER ZONE, Beast Balls en Boutique après la Ligue.
- Étape 4.1c — couverture :
  - Outil `dev_scripts/nabla/coverage.py` → `docs/nabla/couverture.md` : espèce par espèce (formes cosmétiques regroupées), sources (rencontres d'Émeraude et du Safari, cadeaux, fixes, échanges, vagabond, œufs, évolutions avec objet trouvable, régions du Safari pour les formes régionales), objets d'évolution et où les trouver, évolutions à condition spéciale à vérifier en jeu. Ignore les tables de RFVF et les tables d'origine du Safari. Capacités vérifiées dans les capacités par niveau du jeu (`P_LVL_UP_LEARNSETS`).
  - Résultat : **984 / 984 espèces non légendaires obtenables**. Légendaires : 8 / 97 (phase 7).
  - Hoenn (comme dans Rubis/Saphir, emplacements en double convertis, aucune espèce retirée) : Arakdo route 102 (1 %, ex-Zigzaton) et route 117 (4 %, ex-Lumivole) ; Mangriff route 114 (4 %, ex-Séviper, qui garde 5 %) ; Méditikka à l'extérieur du Mont Mémoria (10 %, ex-Goupix qui garde 20 % ; pas à la Route Victoire, choix de l'utilisateur) ; Séléroc la nuit aux Chutes Météore (tables `_Night` des 5 salles où vit Solaroc, herbes et surf).
  - Bargantua à rayures blanches dans Galar & Hisui (`OTHER_REGIONAL_FORMS` du générateur) → Paragruel.
  - Vendeur d'objets d'évolution de Nénucrique : + 10 pierres, 7 Friandises, Galanoa, pommes, Théière Fêlée, Bol Médiocre, armures, Obsidienne, Bloc de Tourbe, Métal Composite, Pièces de Mordudor (10 ₽ au lieu de 400). Prix d'expansion (officiels).
  - Scalproie sauvages : tiennent toujours l'Emblème du Général (Scalpereur).
  - Capacités ajoutées (`level_up_learnsets/gen_9.h`) : Cerfrousse apprend Sprint Bouclier au niveau 21 (Légendes Arceus) → Cerbyllin ; Pomdramour apprend Dragon Cheer à l'évolution → Pomdorochi.
  - Générateur : Pikachu casquette rattaché à Kanto (forme cosmétique). Lecture des espèces factorisée (`species_entries`), réutilisée par l'outil.
  - Tutétékri : inscriptions anciennes gravées dans la paroi des Ruines du Désert (Route 111, de part et d'autre de l'entrée, à lire face au nord ; `data/scripts/nabla/ancient_tablet.inc`). Un Tutafeh de Galar ayant perdu au moins 49 PV y évolue (`tryspecialevo EVO_TRIGGER_TABLET_CURSE`), comme sous l'arche de pierre d'Épée/Bouclier. L'outil reconnaît les évolutions déclenchées par un script du jeu.
  - Testé par l'utilisateur : Méditikka, Arakdo, Séléroc, vendeur de Nénucrique.
  - Tests : 0 échec (5 385 réussis). Test d'expansion adapté : `test/battle/evolution_tracker.c` (le Scalproie sauvage « sans Emblème » tient une Pierre Stase, puisque les sauvages tiennent désormais toujours l'Emblème).

- Porymap 6.3.1 installé par l'utilisateur (version macOS Apple Silicon ; quarantaine retirée avec `xattr -dr com.apple.quarantine`). Ses fichiers `porymap.*.cfg` sont ignorés par git.
- Zone WEST BEACH v1 (Plage de l'Ouest, demande de l'utilisateur) :
  - Route 115 : bande de sable prolongée vers l'ouest au sud de la route (lignes 64-67 ; trois rochers dans l'eau retirés pour le passage), connexion à gauche vers la nouvelle map.
  - Map `NablaWestBeach` (30 × 26, tilesets General + Fallarbor comme la route 115, musique de la route 115), groupe `gMapGroup_Nabla` : île de sable entourée d'eau, carré de hautes herbes (bords sable/herbe de l'île Mirage), rochers dans l'eau. Pas encore de Pokémon ni de contenu.
  - Section `MAPSEC_NABLA_WEST_BEACH` (« WEST BEACH »), ajoutée en fin de liste ; sur la carte de la région, la case du bas de la route 115 (la route 115 est au bord gauche de la carte : pas de case libre plus à l'ouest).
  - Retouches de l'utilisateur dans Porymap : petite bosse de sable à la jonction, deux flaques d'eau peu profonde ; rencontres de test (herbes, surf, pêche).
  - Outil `dev_scripts/nabla/render_map.py` : image d'une map (ou d'un layout), avec grille et collisions, pour vérifier un dessin sans Porymap. Marche à suivre pour créer une zone : `docs/nabla/zones.md`.

- Étape 4.2a — Champions d'arène (équipes composées par l'utilisateur dans `docs/nabla/trainers.md`) :
  - Les 8 équipes Normal intégrées dans `src/data/trainers.party` (3 Pokémon pour Roxanne et Bastien, jusqu'à 6 dès Alizée ; Méga-Évolution dès la 6ᵉ arène : Méga-Ptéra, Méga-Alakazam, Méga-Amphinobi). Noms corrigés (Motisma → Rotom-Heat, Gallame → Gallade, Psycho Cut, Alakazite) ; formes écrites à la Showdown (`Arcanine-Hisui`). Talents choisis par Claude (meilleur talent compétitif), tous vérifiés valides. Objets de soin et IA d'origine gardés.
  - Level caps relevés au Pokémon le plus fort de chaque Champion : 16, 20, 27, 34, 35, 41, 51, 59 ; cap avant le Maître provisoirement à 59 (à fixer avec le Conseil 4, 4.2b).
  - Mode Difficile : les level caps suivent la même règle (`GetDifficultyLevel`, `src/caps.c` : 17 au lieu de 16… 64 au lieu de 59). Tests Nabla : `test/nabla_difficulty.c`.
  - Testé par l'utilisateur : trois combats en Difficile au bon niveau, combat double de Lévy & Tatia. L'IV PV de 1 du Racaillou de Roxanne est voulu.
  - Mode Difficile : règle automatique pour tous les dresseurs adverses (`GetDifficultyTrainerMonLevel`, `src/battle_setup.c`) : niveau × 1,1 arrondi à l'inférieur, au moins +1. Les partenaires (Steven) ne changent pas, et un dresseur qui a sa propre équipe Difficile (`Difficulty: Hard`, ex. événement Latios) l'utilise telle quelle. Trois tests d'expansion (`test/battle/trainer_control.c`) vérifient ce dernier point.

- Étape 4.2b — Conseil 4 et Maître (équipes de l'utilisateur) : Damien, Spectra, Glacia, Aragon (niveaux 66-70) et Marc (72), 6 Pokémon et une Méga-Évolution chacun (Méga-Absol Z, Méga-Lugulabre, Méga-Momartik, Méga-Drattak, Méga-Magearna ; Kyogre Primal avec l'Orbe Bleu). Noms corrigés (Moltres-Galar, Froslass/Froslassite, Miraidon, Calyrex-Shadow, Zygarde-50-Power-Construct, Poltergeist, Judgment, Psyshock) ; formes Originelles avec les objets de la génération 9 (Adamant Crystal, Lustrous Globe, Griseous Core ; Giratina mis en forme Originelle, comme son set). Talents vérifiés valides. Level cap après le 8ᵉ badge : 72.

- Étape 4.2c — rival et Timmy (équipes de l'utilisateur, capacités et talents choisis par Claude) :
  - Rival : 5 combats × 3 versions (selon le starter du joueur) × 2 (Brendan et Flora) = 30 équipes générées depuis une seule par combat ; `STARTER` remplacé par la lignée qui contre le starter du joueur, au stade du niveau (16/36), talent Speed Boost / Torrent / Overgrow ; Méga à Nénucrique (Jungkite, Braségalite, Laggronite). IV comme les équipes d'origine du combat.
  - Timmy : Lavandia (Magnéton, Tylton, Kirlia), Route Victoire (6 Pokémon, Méga-Gallame), revanches `VR_2` à `VR_5` aux niveaux 80, 90, 100, 100 (même équipe) ; nouveau combat dans la Forêt Émeraude : `TRAINER_NABLA_WALLY_EMERALD_FOREST` (857), à brancher avec la zone (scénario dans `docs/nabla/world.md`).
  - Capacités : apprises par niveau jusqu'au niveau du Pokémon (vérifié par script), variées ; combats finaux (rival à Nénucrique, Timmy sur la Route Victoire) : sets compétitifs, qui peuvent contenir des capacités hors CT d'Émeraude (U-turn, Volt Switch…).
- Étape 4.2d — Team Aqua / Magma (équipes de l'utilisateur, capacités, talents et objets des combats finaux choisis par Claude) :
  - 10 combats : Tabitha et Max au Mont Chimnée (27-33), Île du Sud (Matt 35, sbire 32-33, Pierre 34), Shelly à l'Institut Météo (35-36), Tabitha et Max au Repaire Magma (40-45, Méga-Camérupt), Matt au Repaire Aqua (43-45), Centre Spatial en duo (Max avec Méga-Camérupt, Tabitha avec Chartor Sécheresse, Pierre avec Méga-Métalosse, 50-52), Shelly (52) et Arthur (53-54, équipe pluie, Méga-Sharpedo) à la Grotte du Fond Marin.
  - Île du Sud : équipes de l'utilisateur (le sbire n'a que 2 Pokémon) ; les équipes Difficile faites à la main de Matt et du sbire sont retirées.
  - Capacités : par niveau jusqu'au niveau du Pokémon (vérifié par script), sans objet tenu ; dernier combat de chaque personnage (Matt au Repaire Aqua, Max et Tabitha au Centre Spatial, Shelly et Arthur à la Grotte, Pierre au Centre Spatial) : sets compétitifs avec objets. En duo, pas d'attaque qui touche le partenaire chez Pierre (pas de Séisme).
  - Mode Difficile : les partenaires (Pierre) suivent maintenant la même règle des +10 % que les adversaires (`FillPartnerParty`, `src/battle_partner.c`), sauf s'ils ont leur propre équipe Difficile.
- Étape 4.3 — niveaux des dresseurs ordinaires et des Pokémon sauvages :
  - `dev_scripts/nabla/scale_levels.py` : un facteur par étape de l'aventure (level cap Nabla ÷ Pokémon le plus fort du Champion d'origine : ×1,07, ×1,05, ×1,12, ×1,17, ×1,13, ×1,24, ×1,21, ×1,28 ; Route Victoire ×1,40, calée sur le Conseil 4) et l'étape de chaque map. Un dresseur prend l'étape de sa map ou celle de son niveau d'origine si elle est plus tardive (dresseurs en Surf, revanches) ; les sauvages commencent au plus tôt à l'obtention du Surf, d'Éclate-Roc ou de la canne. Le script repart toujours des niveaux d'origine (dresseurs d'expansion, tables sauvages de la 4.1) : relançable pour rééquilibrer. Relecture : `docs/nabla/levels.md`.
  - 728 dresseurs (premiers combats et revanches), 190 tables de sauvages, 4 Pokémon fixes (Voltorbe de New Mauville, Électrode du Repaire Aqua, Kecleon). Non touchés : dresseurs de la 4.2, revanches des Champions, post-game, Safari, zones Nabla, légendaires, cadeaux, Barpau (niveaux 20-25 à part). Exemples : Route 119 26 → 32, arène d'Algatia 36 → 44, Route Victoire 43-45 → 60-63.
  - Évolutions : 205 Pokémon de dresseurs évoluent quand le relèvement leur fait atteindre leur niveau d'évolution (un Pokémon d'origine qui pouvait déjà évoluer reste tel quel) ; les évolutions qui demandent plus qu'un niveau (échange, objet, bonheur, attaque connue…) se font au niveau 40 (`NABLA_OTHER_EVOLUTIONS_LEVEL`) : Stari → Staross, Machopeur → Mackogneur, Rosélia → Roserade, Magnéton → Magnézone… Les sauvages évoluent dans le jeu selon leur niveau (`GetNablaWildEvolution`, `src/wild_encounter.c`, partout et plus seulement au Safari), avec la même règle ; les conditions qui choisissent entre deux évolutions (sexe, nature, heure, région) sont gardées, et une évolution est tirée au hasard quand il y en a plusieurs. Test : `test/nabla_wild_evolution.c`.
  - Safari : niveaux 38-42 avec 6 badges, 48-52 avec 7, 53-57 avec 8, 68-72 après la Ligue (zone Starters toujours au niveau 5).
  - Couverture (`coverage.py`) : tient compte de l'évolution des sauvages selon le niveau de leur table ; 984 / 984.

- Étape 5.1 — name box :
  - Native d'expansion (`include/config/name_box.h`, `setspeaker`). `OW_NAME_BOX_NPC_TRAINER` activé : le nom du dresseur s'affiche sur sa réplique d'avant-combat.
  - Nom repris des textes : 830 textes d'Émeraude commencent par le nom de celui qui parle (« STEVEN: », « MOM: », « PROF. BIRCH: », « MR. BRINEY: »…). `TryTakeSpeakerFromMessage` (`src/field_message_box.c`) met ce nom dans la name box et l'enlève du texte affiché : majuscules, espaces, points et « & », 12 caractères au plus, suivis de « : » ou « : » (traduction française). Les textes d'origine ne changent pas. Un texte où plusieurs personnes parlent (Lévy et Tatia, ~130 textes) reste comme dans Émeraude ; un message sans nom après un message nommé (objet reçu, narration) n'a pas de name box. « DAD » s'affiche « NORMAN » (`sMessageSpeakerAliases`). Tests : `test/nabla_name_box.c`.
  - Réapprentissage des capacités d'œuf/tuteur déjà connues : abandonné (il faudrait les mémoriser pour chaque Pokémon, la sauvegarde n'a qu'une vingtaine de bits libres par Pokémon).
- Étape 5.2 — plusieurs objets d'un coup, menus en boucle :
  - Hors combat, après le choix du Pokémon, une boîte « ×01 » (↑↓ ±1, ←→ ±10, A, B) quand l'objet peut servir plusieurs fois de suite sur lui et qu'il y en a plusieurs dans le sac. Le maximum est le nombre d'utilisations qui ont un effet, essayées sur une copie du Pokémon (`GetItemUseMaxQuantity`, `src/party_menu.c`) : PV pleins, 252 EV / 510 au total, level cap ou niveau 100. Concerne les objets des fonctions `ItemUseCB_Medicine` (soins de PV, vitamines, plumes ; les soins de statut, Potion Max, Rappels n'ont qu'une utilisation utile, donc pas de boîte), `ItemUseCB_ReduceEV` (baies, quand l'EV baisse) et `ItemUseCB_RareCandy` (Super Bonbon, Bonbons Exp). La première utilisation est celle d'origine ; les suivantes s'y ajoutent (attaques de tous les niveaux franchis et évolution gérées par le code des Bonbons Exp). Bonbons Exp : le message donne l'expérience réellement gagnée. Texte : `gText_UseHowManyVar1s` (`src/strings.c`, à côté de « Toss out how many »). Test : `test/nabla_item_quantity.c`.
  - Menus en boucle partout : `Menu_ProcessInputNoWrap` et `Menu_ProcessInputNoWrapAround_other` (`src/menu.c`) bouclent comme les autres menus (ACHETER/VENDRE/QUITTER, OUI/NON, menus d'objet, choix des scripts quel que soit leur nombre) ; `ListMenu_ProcessInput` (`src/list_menu.c`) boucle sur un nouvel appui (articles des boutiques, comptoir du Safari, PC, listes des scripts ; garder la flèche enfoncée s'arrête au bout). La retouche propre au sac est retirée.

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
| 2026-10-17 | Safari moderne façon ROSA : entrée gratuite, vrais combats, pas de limite de pas ni de Safari Balls ; une région par visite, niveaux selon les badges (60-70 après la Ligue), évolution dynamique. Hoenn retiré du Safari. |
| 2026-10-17 | Régions du Safari : Kanto ouvert d'office, les 7 autres à 30 000 ₽ chacune, dans n'importe quel ordre ; zones spéciales (Starters, Paradoxes, Ultra-Chimères) à 100 000 ₽ après la Ligue ; **la zone Starters est au niveau 5**. |
| 2026-10-17 | Formes régionales : un Pokémon prend sa forme régionale en évoluant dans le Safari de la région (Raichu d'Alola en Alola, Typhlosion de Hisui en Galar & Hisui). |
| 2026-10-17 | Répartition du Safari : équilibrée selon la puissance (les plus faibles sont les plus communs), pas de Pokémon Roche uniquement sous les rochers, Pokémon aquatiques non-Eau aussi dans l'eau. |
| 2026-10-18 | Zones spéciales nommées STARTER ZONE, AREA ZERO, ULTRA SPACE. Beast Balls vendues 1 000 ₽ dans les Boutiques après la Ligue. |
| 2026-10-18 | Ordre : 4.1b-3, puis 4.1c qui comble la couverture (4 Pokémon de Hoenn ajoutés aux routes comme dans Rubis/Saphir, Bargantua blanc, objets d'évolution en vente). |
| 2026-10-18 | Starters du Safari : Plante et Feu dans les herbes, Eau seulement dans l'eau, rien sous les rochers. |
| 2026-10-18 | Couverture : objets d'évolution vendus aux prix officiels (Pièces de Mordudor à 10 ₽) ; Méditikka seulement au Mont Mémoria (pas à la Route Victoire). |
| 2026-10-19 | Équipes des dresseurs importants (4.2) : **l'utilisateur compose les équipes**, Claude les intègre et vérifie. Normal : équipes modifiables, niveaux d'origine, 6 Pokémon à partir de la 6ᵉ arène. Méga-Évolution à partir de la 6ᵉ arène dans les deux modes. Difficile : même composition, niveaux et/ou sets améliorés (sets proposés par Claude), pas d'objets de soin. Découpage : 4.2a Champions, 4.2b Conseil 4 et Maître, 4.2c rival et Timmy, 4.2d Aqua/Magma. |
| 2026-10-22 | Difficile = mêmes équipes, niveaux de tous les dresseurs adverses × 1,1 (arrondi inférieur, au moins +1) ; les sets pourront changer plus tard. Talents : le meilleur en compétitif. Level caps = Pokémon le plus fort de chaque Champion. Niveaux des sauvages et des autres dresseurs à adapter plus tard. |
| 2026-10-22 | En Difficile, les level caps suivent aussi la règle des +10 %. |
| 2026-10-22 | Rival : une équipe par combat (mêmes pour Brendan et Flora) avec une ligne `STARTER` ; Claude génère les 3 versions selon le starter du joueur. Timmy (Lavandia avant le 3ᵉ badge, Route Victoire avant la Ligue) traité avec le rival ; ses revanches au post-game. |
| 2026-10-22 | Un Pokémon de dresseur sans capacités dans la fiche : Claude lui donne 4 capacités apprises par niveau jusqu'à son niveau, variées (même logique que pour `STARTER`). |
| 2026-10-22 | Team Aqua / Magma (4.2d) : l'utilisateur choisit le nombre de Pokémon de chaque combat. Combats en duo (Île du Sud, Centre Spatial) : 3 Pokémon par dresseur, Pierre Rochard compris ; l'utilisateur compose aussi les équipes de Pierre. |
| 2026-10-22 | Île du Sud (événement Latios) : équipes composées par l'utilisateur ; les équipes Difficile faites à la main de Matt et du sbire sont retirées, la règle des +10 % s'applique. |
| 2026-10-23 | Mode Difficile : les partenaires (Pierre Rochard) ont aussi leurs niveaux +10 %, sinon ils seraient trop faibles face aux adversaires. Objets tenus : seulement dans les sets des combats finaux (et ceux écrits par l'utilisateur). |
| 2026-10-22 | 4.3 : les niveaux de **tous** les dresseurs ordinaires (sbires compris) seront relevés pour suivre la nouvelle courbe (simple relèvement de niveaux). |
| 2026-10-23 | 4.3 : un facteur par étape de l'aventure (level cap ÷ Champion d'origine), Route Victoire ×1,40 (calée sur le Conseil 4). Les Pokémon évoluent selon leur nouveau niveau, dresseurs comme sauvages ; évolutions par échange, objet (et les autres qui demandent plus qu'un niveau) au niveau 40. Pokémon fixes non légendaires relevés ; légendaires et cadeaux inchangés ; post-game plus tard (phase 7). |
| 2026-10-23 | Safari : niveaux autour de 40 avec 6 badges, 50 avec 7, 55 avec 8, 70 après la Ligue. |
| 2026-10-23 | Name box : nom automatique sur les répliques d'avant-combat des dresseurs et sur les textes qui commencent par « NOM: » (textes d'origine inchangés) ; père affiché « NORMAN ». Noms ajoutés à la main pour les dialogues sans nom : à décider après le test. Résumé inchangé. |
| 2026-10-23 | Plusieurs objets d'un coup (hors combat, quantité choisie, 1 par défaut, maximum = utilisations utiles) et menus en boucle partout : étape 5.2. Objets d'entraînement (vitamines…) : étape 5.3, valeurs à donner par l'utilisateur. |
| 2026-10-23 | Nouvelles zones (West Beach, Forêt Émeraude…) : niveaux calés sur les zones qui les entourent. Équilibrage fin (niveaux, puissance des équipes, sets) après la partie complète de l'utilisateur en v1. |

## Questions ouvertes

- Aucune pour l'instant.
