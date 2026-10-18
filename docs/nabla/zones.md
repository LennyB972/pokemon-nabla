# Zones ajoutées par Nabla

## Liste

| Zone | Map | Accès | Carte de la région | Contenu |
|---|---|---|---|---|
| WEST BEACH (Plage de l'Ouest) | `NablaWestBeach` (30 × 26) | Route 115 : bande de sable vers l'ouest au sud de la route (connexion est ↔ ouest, sans Surf) | case du bas de la route 115 (`MAPSEC_NABLA_WEST_BEACH`) | v1 : île de sable, carré de hautes herbes (pas encore de Pokémon) |

## Créer une zone

1. **Map** : Porymap, *File → New Map*. Nom préfixé `Nabla` (ex. `NablaWestBeach`), groupe `gMapGroup_Nabla`. Porymap l'ajoute à la fin du groupe : les numéros des maps existantes ne bougent pas (les sauvegardes les retiennent).
2. **Script de la map** : vérifier que `data/maps/<Map>/scripts.inc` est inclus dans `data/event_scripts.s` **avant** le bloc `.if IS_FRLG` (sinon : « undefined reference to `<Map>_MapScripts` »).
3. **Liaison** :
   - connexion (passage continu) : onglet *Connections*, case *Mirror to Connecting Maps*, puis *Save All* ;
   - warp (porte, grotte) : un événement *Warp* dans chaque map, chacun pointant vers le numéro du warp d'arrivée.
   - Une map d'origine ne se modifie que pour ajouter le passage.
4. **Nom et carte de la région** : nouvelle section ajoutée **à la fin** de `src/data/region_map/region_map_sections.json` (les numéros de sections sont gardés dans les Pokémon comme lieu de rencontre), case(s) dans `src/data/region_map/region_map_layout.h` (ou *Tools → Region Map Editor*), puis la section dans le champ *Location* du Header de la map.
5. **Vérifier** : `python3 dev_scripts/nabla/render_map.py <Map> image.png --grid` pour une image de la map, build, test en jeu ; rencontres sauvages → relancer `dev_scripts/nabla/coverage.py`.
