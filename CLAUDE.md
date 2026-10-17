# Pokémon Nabla — règles du projet

Romhack de Pokémon Émeraude basé sur pokeemerald-expansion (RHH).
- Cahier des charges : `VISION.md`. Plan : `ROADMAP.md`. État et décisions : `PROGRESS.md`.
- Lire `PROGRESS.md` en début de session pour savoir où on en est. Ses décisions priment sur VISION.md.

## Règles permanentes

- **Philosophie** : améliorer Émeraude sans le dénaturer. On ajoute plutôt qu'on remplace : l'histoire et les maps d'origine restent intactes.
- **Natif d'abord** : avant d'écrire du code, vérifier si expansion propose déjà la fonctionnalité (`include/config/*.h`, `docs/tutorials/`, macros de script). Toujours préférer la solution native.
- **Build vert** : le jeu doit compiler à la fin de chaque étape.
- **Un commit par étape**, message clair en anglais, puis `git push origin master`.
- **Annonce** : avant d'entamer une étape, présenter à l'utilisateur ce qui va y être fait (quoi, où, comment on vérifie) et attendre son feu vert.
- **Validation** : ne passer à l'étape suivante qu'après validation de l'utilisateur. Si une décision n'est pas couverte par `VISION.md` ou `PROGRESS.md`, demander plutôt que supposer.
- **Suivi** : mettre à jour `PROGRESS.md` à la fin de chaque étape et de chaque session.
- **Textes** : regrouper tous les nouveaux textes du jeu pour faciliter une future traduction française (voir « Conventions » ci-dessous).
- **Code** : minimal, propre, cohérent avec le style du repo (`docs/STYLEGUIDE.md`). Pas d'échafaudage inutile.
- **Jamais de ROM (`.gba`) ni de fichiers de build dans un commit.**
- **Communication** : en français, avec des recommandations franches et une conclusion claire.

## Environnement

- macOS. Le shell de Claude ne charge pas `~/.zshrc` : exporter la toolchain avant `make` :
  `export DEVKITPRO=/opt/devkitpro DEVKITARM=/opt/devkitpro/devkitARM`
- Build : `make -j$(sysctl -n hw.ncpu)` → `pokeemerald.gba`. Build de distribution : `make release`.
- Remotes : `origin` = LennyB972/pokemon-nabla (notre fork), `upstream` = rh-hideout/pokeemerald-expansion.
- ROM Émeraude US propre (base du patch BPS, hors repo) : `../rom/emerald_us.gba`. Flips (compilé depuis les sources) : `../tools/flips`.
- Patch : `./make_bps.sh` → build release + `build/pokemon_nabla.bps`, vérifié par ré-application.
- Tests automatiques : `make check` (~8 min, à lancer après chaque changement de config ou de code de combat). Attendu : 0 `FAIL`. Les `ASSUMPTION_FAIL` sont des tests ignorés parce qu'une de nos options contredit leur hypothèse (ex. Grêle → Neige) : à vérifier, mais normaux.
- Sauvegarde : `test/save.c` contient les tailles de nos blocs de sauvegarde. Si un test « is backwards compatible » échoue, c'est qu'un changement casse les sauvegardes : vérifier qu'il est voulu, puis mettre à jour la taille (et le signaler).
- Test headless : `tools/mgba/mgba-rom-test-mac` n'a pas de Lua (pas de captures d'écran) ; les tests visuels se font par l'utilisateur.
- Distribution : patch BPS jouable sur n'importe quel émulateur (et doit tourner sous Windows comme macOS).

## Conventions

- **Config** : les réglages se font dans `include/config/*.h`. Toujours modifier la valeur existante plutôt que dupliquer un define, pour que les merges upstream restent simples.
- **Flags / vars** : prendre dans les `FLAG_UNUSED_*` / `VAR_UNUSED_*` et les renommer avec un nom explicite (ex. `FLAG_NABLA_LEVEL_CAPS`). Les vars libres sont rares (~29) : les économiser. Un flag ou une var Nabla qui ne sert plus n'est **jamais réattribué** (des sauvegardes peuvent l'avoir posé) : le garder avec un commentaire « retired » et en prendre un autre.
- **Textes nouveaux** :
  - scripts : textes dans `data/text/nabla/*.inc` et scripts dans `data/scripts/nabla/*.inc` (un fichier par thème, inclus en fin de `data/event_scripts.s`), labels préfixés `Nabla_Text_` / `Nabla_EventScript_` ;
  - textes C : regroupés dans un fichier dédié plutôt que dispersés.
  - exception : un libellé qui modifie une interface existante reste à côté des textes d'origine de cette interface (ex. options du menu dans `src/option_menu.c`).
  - Ne pas réécrire les textes d'origine sauf demande explicite.
- **Nouveau contenu** (maps, scripts, trainers) : préfixer ou regrouper sous « Nabla » pour qu'il soit identifiable face au contenu vanilla.
- **Jour/nuit** : dans un script en extérieur, utiliser `fadescreenswapbuffers` (pas `fadescreen`). Les lumières se posent avec des objets `OBJ_EVENT_GFX_LIGHT_SPRITE` et des fichiers `.pla` (voir `docs/tutorials/dns.md`). Ne pas appliquer le tutoriel « triple-layer metatiles » sans le correctif de l'issue expansion #7034.
- **Objets** : tout objet ajouté (boutique, objet caché) est listé dans `docs/nabla/items.md`, qui explique aussi comment en ajouter. Boutiques Pokémon : liste commune `Nabla_Pokemart_Items`, paliers de badges dans `sShopItemRequirements` (`src/shop_criteria.c`). Emplacements d'objets (cachés ou au sol) : `dev_scripts/nabla/hidden_item_spots.py` ; tableaux de la doc régénérés avec `dev_scripts/nabla/list_items.py`.
- **Safari par région** : tables générées par `dev_scripts/nabla/safari_tables.py <Région>` (insérées après la table d'origine de chaque zone, dans l'ordre de `include/constants/nabla.h`) ; relecture dans `docs/nabla/safari.md` (`--doc`). Une correction manuelle d'une table se fait dans `src/data/wild_encounters.json`, puis `--doc`.
- **Maps d'origine** : on n'y touche que pour ajouter (entrée vers une nouvelle zone, événement), jamais pour retirer.
- **Objets de map** : toujours ajouter les nouveaux objets à la fin de `object_events`, sans retirer ni réordonner les existants (pour un objet devenu inutile, le laisser caché par son flag). La sauvegarde garde la liste d'objets de la map où l'on se trouve : changer les numéros casse `addobject`/`removeobject` jusqu'au prochain changement de map.
- **Crédits** : pokeemerald-expansion doit être crédité (« RHH (Rom Hacking Hideout) », avec la version). Toute ressource communautaire utilisée est ajoutée à la section Crédits du `README.md` avec son auteur, au moment où on l'intègre.
- **Tests** : utiliser le menu debug (R + START) et le quickstart (SELECT à l'écran titre) pour vérifier ; les décrire dans `PROGRESS.md`.
