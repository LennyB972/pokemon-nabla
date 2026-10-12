# Pokémon Nabla — règles du projet

Romhack de Pokémon Émeraude basé sur pokeemerald-expansion (RHH).
- Cahier des charges : `VISION.md`. Plan : `ROADMAP.md`. État et décisions : `PROGRESS.md`.
- Lire `PROGRESS.md` en début de session pour savoir où on en est. Ses décisions priment sur VISION.md.

## Règles permanentes

- **Philosophie** : améliorer Émeraude sans le dénaturer. On ajoute plutôt qu'on remplace : l'histoire et les maps d'origine restent intactes.
- **Natif d'abord** : avant d'écrire du code, vérifier si expansion propose déjà la fonctionnalité (`include/config/*.h`, `docs/tutorials/`, macros de script). Toujours préférer la solution native.
- **Build vert** : le jeu doit compiler à la fin de chaque étape.
- **Un commit par étape**, message clair en anglais, puis `git push origin master`.
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
- ROM Émeraude US propre (base du patch BPS, hors repo) : `~/Documents/pokemon/nabla/rom/emerald_us.gba`.
- Distribution : patch BPS jouable sur n'importe quel émulateur (et doit tourner sous Windows comme macOS).

## Conventions

- **Config** : les réglages se font dans `include/config/*.h`. Toujours modifier la valeur existante plutôt que dupliquer un define, pour que les merges upstream restent simples.
- **Flags / vars** : prendre dans les `FLAG_UNUSED_*` / `VAR_UNUSED_*` et les renommer avec un nom explicite (ex. `FLAG_NABLA_LEVEL_CAPS`). Les vars libres sont rares (~29) : les économiser.
- **Textes nouveaux** :
  - scripts : `data/text/nabla/*.inc` (un fichier par thème), labels préfixés `gText_Nabla_` ou `Nabla_Text_` ;
  - textes C : regroupés dans un fichier dédié plutôt que dispersés.
  - Ne pas réécrire les textes d'origine sauf demande explicite.
- **Nouveau contenu** (maps, scripts, trainers) : préfixer ou regrouper sous « Nabla » pour qu'il soit identifiable face au contenu vanilla.
- **Maps d'origine** : on n'y touche que pour ajouter (entrée vers une nouvelle zone, événement), jamais pour retirer.
- **Crédits** : pokeemerald-expansion doit être crédité (« RHH (Rom Hacking Hideout) », avec la version). Toute ressource communautaire utilisée est ajoutée à la section Crédits du `README.md` avec son auteur, au moment où on l'intègre.
- **Tests** : utiliser le menu debug (R + START) et le quickstart (SELECT à l'écran titre) pour vérifier ; les décrire dans `PROGRESS.md`.
