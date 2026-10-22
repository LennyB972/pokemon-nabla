# Équipes des dresseurs importants

Fiche de travail de l'étape 4.2. C'est l'utilisateur qui compose les équipes ; Claude les intègre au jeu (`src/data/trainers.party`), complète les détails techniques et vérifie.

## Règles

- **Mode Normal** : équipes de l'utilisateur, niveaux proches de ceux d'origine (un peu relevés). **6 Pokémon à partir de la 6ᵉ arène.**
- **Méga-Évolution à partir de la 6ᵉ arène, dans les deux modes** : un seul Pokémon méga-évolutif par équipe, qui tient sa Méga-Gemme (`Altaria @ Altarianite`).
- **Mode Difficile** : **même équipe** qu'en Normal, avec des niveaux plus hauts. Règle automatique pour **tous les dresseurs adverses** : niveau × 1,1 arrondi à l'entier inférieur, et au moins +1 (57 → 62, 9 → 10). Les sets pourront changer plus tard. Exception : un dresseur qui a sa propre équipe Difficile (`Difficulty: Hard` dans `trainers.party`) l'utilise telle quelle.
- **Talents** : le meilleur en compétitif (sets de référence Smogon / Coupcritique), choisi par Claude quand il n'est pas précisé.
- **Level caps** : niveau du Pokémon le plus fort de chaque Champion (`src/caps.c`) ; en Difficile, même règle des +10 %.

## Comment écrire une équipe

Au **format Pokémon Showdown** (noms anglais), le format du fichier des dresseurs du jeu. Le plus simple : le constructeur d'équipes de Showdown (play.pokemonshowdown.com/teambuilder), puis *Export*, et coller le texte dans la case « Normal » du Champion (ou dans le chat). Pour chaque Pokémon :

```
Altaria @ Altarianite
Ability: Natural Cure
Level: 33
- Dragon Breath
- Aerial Ace
- Dragon Dance
- Earthquake
```

- Le niveau est obligatoire ; le reste est facultatif. Si les IV manquent, Claude reprend ceux des équipes d'origine (plus élevés pour le Pokémon le plus fort) ; Showdown n'écrit pas les IV parfaits.
- La ligne `Items:` de l'équipe d'origine liste les objets de soin que le Champion utilise en combat (Potions…) : à garder, changer ou supprimer en Normal ; aucun en Difficile.
- Si une case reste vide, l'équipe d'origine est gardée.

## Pokémon méga-évolutifs (hors légendaires) pour les arènes 6 à 8

- **Vol (Alizée)** : Aerodactyl, Altaria, Charizard X et Y, Clefable, Dragonite, Gyarados, Hawlucha, Pidgeot, Pinsir, Salamence, Skarmory, Staraptor.
- **Psy (Lévy & Tatia)** : Alakazam, Chimecho, Delphox, Gallade, Gardevoir, Malamar, Medicham, Meowstic, Metagross, Slowbro, Starmie.
- **Eau (Juan)** : Barbaracle, Blastoise, Feraligatr, Golisopod, Greninja, Gyarados, Sharpedo, Slowbro, Starmie, Swampert, Tatsugiri.

(Le Pokémon ou sa Méga-Évolution a le type de l'arène. Le nom de la Méga-Gemme est celui de Showdown : Altarianite, Metagrossite, Swampertite…)

## Roxanne — Mérouville (Roche)

- Niveau maximal : **16** (level cap du badge ; 15 dans Émeraude).
- Objets de soin d'origine : Potion / Potion.

**Équipe d'origine**

```
Geodude
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Tackle
- Defense Curl
- Rock Throw
- Rock Tomb

Geodude
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Tackle
- Defense Curl
- Rock Throw
- Rock Tomb

Nosepass @ Oran Berry
Level: 15
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Block
- Harden
- Tackle
- Rock Tomb
```

**Normal** (dans le jeu)

```
Geodude @ Berry Juice
Ability: Sturdy
Level: 13
IVs: 1 HP / 24 Atk / 24 Def / 12 SpA / 24 SpD / 24 Spe
- Defense Curl
- Rollout
- Sand Tomb

Anorith
Ability: Battle Armor
Level: 14
IVs: 31 HP / 24 Atk / 24 Def / 12 SpA / 24 SpD / 24 Spe
- Bug Bite
- Harden
- Metal Claw
- Rock Throw

Nosepass @ Berry Juice
Ability: Sturdy
Level: 16
IVs: 31 HP / 24 Atk / 31 Def / 24 SpA / 31 SpD / 24 Spe
- Block
- Harden
- Thunder Wave
- Rock Tomb
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Bastien (Brawly) — Myokara (Combat)

- Niveau maximal : **20** (level cap du badge ; 19 dans Émeraude).
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Machop
Level: 16
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Karate Chop
- Low Kick
- Seismic Toss
- Bulk Up

Meditite
Level: 16
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Focus Punch
- Light Screen
- Reflect
- Bulk Up

Makuhita @ Sitrus Berry
Level: 19
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Arm Thrust
- Vital Throw
- Reversal
- Bulk Up
```

**Normal** (dans le jeu)

```
Meditite
Ability: Pure Power
Level: 16
IVs: 24 HP / 24 Atk / 24 Def / 12 SpA / 24 SpD / 24 Spe
- Karate Chop
- Light Screen
- Reflect
- Bulk Up

Makuhita @ Sitrus Berry
Ability: Thick Fat
Level: 18
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Arm Thrust
- Bullet Punch
- Fake Out
- Bulk Up

Flamigo @ Lum Berry
Ability: Scrappy
Level: 20
IVs: 16 HP / 16 Atk / 16 Def / 16 SpA / 16 SpD / 16 Spe
- Focus Energy
- Peck
- Double Kick
- Detect
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Voltère (Wattson) — Lavandia (Électrik)

- Niveau maximal : **27** (level cap du badge ; 24 dans Émeraude).
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Voltorb
Level: 20
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Rollout
- Spark
- Self Destruct
- Shock Wave

Electrike
Level: 20
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Shock Wave
- Leer
- Quick Attack
- Howl

Magneton
Level: 22
IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe
- Supersonic
- Shock Wave
- Thunder Wave
- Sonic Boom

Manectric @ Sitrus Berry
Level: 24
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Quick Attack
- Thunder Wave
- Shock Wave
- Howl
```

**Normal** (dans le jeu)

```
Emolga
Ability: Motor Drive
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Acrobatics
- Spark
- Charge
- Volt Switch

Dedenne @ Sitrus Berry
Ability: Cheek Pouch
Level: 25
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Parabolic Charge
- Draining Kiss
- Volt Switch
- Thunder Wave

Magneton
Ability: Magnet Pull
Level: 25
IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe
- Volt Switch
- Shock Wave
- Thunder Wave
- Mirror Shot

Manectric @ Sitrus Berry
Ability: Lightning Rod
Level: 27
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Charge
- Thunder Wave
- Volt Switch
- Signal Beam
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Adriane (Flannery) — Vermilava (Feu)

- Niveau maximal : **34** (level cap du badge ; 29 dans Émeraude).
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Numel
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Overheat
- Take Down
- Magnitude
- Sunny Day

Slugma
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Overheat
- Smog
- Light Screen
- Sunny Day

Camerupt
Level: 26
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Overheat
- Tackle
- Sunny Day
- Attract

Torkoal @ White Herb
Level: 29
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Overheat
- Sunny Day
- Body Slam
- Attract
```

**Normal** (dans le jeu)

```
Scovillain
Ability: Chlorophyll
Level: 30
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Sunny Day
- Solar Beam
- Overheat
- Growth

Camerupt @ Sitrus Berry
Ability: Solid Rock
Level: 30
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Yawn
- Lava Plume
- Earth Power
- Attract

Salazzle
Ability: Corrosion
Level: 33
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Toxic
- Sludge Bomb
- Flamethrower
- Toxic Spikes

Arcanine-Hisui @ Sitrus Berry
Ability: Rock Head
Level: 33
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Flare Blitz
- Rock Slide
- Extreme Speed
- Crunch

Rotom-Heat @ Leftovers
Ability: Levitate
Level: 34
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Overheat
- Thunder Shock
- Will-O-Wisp
- Hex
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Norman — Clémenti-Ville (Normal)

- Niveau maximal : **35** (level cap du badge ; 31 dans Émeraude).
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Spinda
Level: 27
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Teeter Dance
- Psybeam
- Facade
- Encore

Vigoroth
Level: 27
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Slash
- Facade
- Encore
- Feint Attack

Linoone
Level: 29
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Slash
- Belly Drum
- Facade
- Headbutt

Slaking @ Sitrus Berry
Level: 31
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Counter
- Yawn
- Facade
- Feint Attack
```

**Normal** (dans le jeu)

```
Wigglytuff
Ability: Competitive
Level: 33
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Stealth Rock
- Light Screen
- Reflect
- Psychic

Obstagoon @ Chople Berry
Ability: Guts
Level: 33
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Obstruct
- Night Slash
- Shadow Claw
- Retaliate

Maushold @ Wide Lens
Ability: Technician
Level: 34
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Population Bomb
- Bite
- Tidy Up
- Encore

Slaking @ Life Orb
Ability: Truant
Level: 34
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Counter
- Yawn
- Giga Impact
- Earthquake

Zoroark-Hisui @ Focus Sash
Ability: Illusion
Level: 35
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Focus Blast
- Nasty Plot
- Hyper Voice
- Shadow Ball
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Alizée (Winona) — Cimetronelle (Vol)

- Niveau maximal : **41** (level cap du badge ; 33 dans Émeraude) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Swablu
Level: 29
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Perish Song
- Mirror Move
- Safeguard
- Aerial Ace

Tropius
Level: 29
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Sunny Day
- Aerial Ace
- Solar Beam
- Synthesis

Pelipper
Level: 30
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Water Gun
- Supersonic
- Protect
- Aerial Ace

Skarmory
Level: 31
IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe
- Sand Attack
- Fury Attack
- Steel Wing
- Aerial Ace

Altaria @ Oran Berry
Level: 33
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Dragon Breath
- Dragon Dance
- Aerial Ace
```

**Normal** (dans le jeu)

```
Altaria @ Sitrus Berry
Ability: Natural Cure
Level: 37
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Roost
- Dragon Dance
- Sky Attack

Iron Jugulis @ Booster Energy
Ability: Quark Drive
Level: 38
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earth Power
- Hurricane
- Dark Pulse
- Taunt

Tornadus-Therian @ Assault Vest
Ability: Regenerator
Level: 38
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Hurricane
- U-turn
- Heat Wave
- Focus Blast

Corviknight @ Rocky Helmet
Ability: Pressure
Level: 39
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Roost
- Defog
- U-turn
- Brave Bird

Shaymin-Sky @ Life Orb
Ability: Serene Grace
Level: 40
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Air Slash
- Seed Flare
- Earth Power
- Dazzling Gleam

Aerodactyl @ Aerodactylite
Ability: Unnerve
Level: 41
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Stone Edge
- Earthquake
- Roost
- Ice Fang
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Lévy & Tatia (Tate & Liza) — Algatia (Psy, combat en duo)

- Niveau maximal : **51** (level cap du badge ; 42 dans Émeraude) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion / Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Claydol
Level: 41
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Earthquake
- Ancient Power
- Psychic
- Light Screen

Xatu
Level: 41
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Psychic
- Sunny Day
- Confuse Ray
- Calm Mind

Lunatone @ Sitrus Berry
Level: 42
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Light Screen
- Psychic
- Hypnosis
- Calm Mind

Solrock @ Sitrus Berry
Level: 42
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Sunny Day
- Solar Beam
- Psychic
- Flamethrower
```

**Normal** (dans le jeu)

```
Gardevoir @ Choice Scarf
Ability: Trace
Level: 46
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Moonblast
- Psychic Noise
- Trick
- Sacred Fire

Gallade @ Choice Band
Ability: Sharpness
Level: 46
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Psycho Cut
- Sacred Sword
- Leaf Blade
- Shadow Sneak

Jirachi @ Leftovers
Ability: Serene Grace
Level: 47
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Iron Head
- U-turn
- Wish
- Body Slam

Iron Boulder @ Booster Energy
Ability: Quark Drive
Level: 47
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Mighty Cleave
- Close Combat
- Earthquake
- Zen Headbutt

Metagross @ Weakness Policy
Ability: Clear Body
Level: 50
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Heavy Slam
- Knock Off
- Bullet Punch

Alakazam @ Alakazite
Ability: Magic Guard
Level: 51
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Psychic
- Focus Blast
- Shadow Ball
- Calm Mind
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Juan — Atalanopolis (Eau)

- Niveau maximal : **59** (level cap du badge ; 46 dans Émeraude) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Luvdisc
Level: 41
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Water Pulse
- Attract
- Sweet Kiss
- Flail

Whiscash
Level: 41
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Rain Dance
- Water Pulse
- Amnesia
- Earthquake

Sealeo
Level: 43
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Encore
- Body Slam
- Aurora Beam
- Water Pulse

Crawdaunt
Level: 43
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Water Pulse
- Crabhammer
- Taunt
- Leer

Kingdra @ Chesto Berry
Level: 46
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Water Pulse
- Double Team
- Ice Beam
- Rest
```

**Normal** (dans le jeu)

```
Pelipper @ Damp Rock
Ability: Drizzle
Level: 55
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Hurricane
- U-turn
- Roost
- Weather Ball

Kingdra @ Choice Specs
Ability: Swift Swim
Level: 55
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Surf
- Draco Meteor
- Hydro Pump
- Hurricane

Urshifu-Rapid-Strike @ Choice Scarf
Ability: Unseen Fist
Level: 56
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Surging Strikes
- Close Combat
- Aqua Jet
- U-turn

Volcanion @ Heavy-Duty Boots
Ability: Water Absorb
Level: 56
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Steam Eruption
- Flamethrower
- Earth Power
- Taunt

Tapu Fini @ Leftovers
Ability: Misty Surge
Level: 57
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Scald
- Moonblast
- Defog
- Draining Kiss

Greninja @ Greninjite
Ability: Protean
Level: 59
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Dark Pulse
- Hydro Pump
- Ice Beam
- Gunk Shot
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

# Conseil 4 et Maître (4.2b)

- **Règles** : comme les Champions de la 6ᵉ arène et plus : 6 Pokémon et une Méga-Évolution par équipe, dans les deux modes (proposition, libre à toi de faire autrement). Niveaux à relever : Juan est désormais au niveau 59.
- **Level cap** : un seul cap après le 8ᵉ badge (Route Victoire et Ligue), au niveau du Pokémon le plus fort de Marc : **72** (`src/caps.c`, 79 en Difficile).
- **Formes Originelles** : le jeu suit la génération 9, où les Orbes ne changent plus la forme. Dialga, Palkia et Giratina Originels tiennent donc Adamant Crystal, Lustrous Globe et Griseous Core (même bonus que les Orbes).
- **Difficile** : même équipe, niveaux +10 % (règle automatique).

## Pokémon méga-évolutifs (hors légendaires) par type

- **Ténèbres (Damien)** : Absol, Absol Z, Greninja, Gyarados, Houndoom, Malamar, Sableye, Scrafty, Sharpedo, Tyranitar.
- **Spectre (Spectra)** : Absol Z, Banette, Chandelure, Froslass, Gengar, Golurk, Sableye.
- **Glace (Glacia)** : Abomasnow, Baxcalibur, Crabominable, Froslass, Glalie.
- **Dragon (Aragon)** : Altaria, Ampharos, Baxcalibur, Charizard X, Dragalge, Dragonite, Drampa, Feraligatr, Garchomp, Garchomp Z, Salamence, Sceptile, Tatsugiri.
- **Eau (Marc)** : Barbaracle, Blastoise, Feraligatr, Golisopod, Greninja, Gyarados, Sharpedo, Slowbro, Starmie, Swampert, Tatsugiri.

(Le Pokémon ou sa Méga-Évolution a le type du dresseur. Nom de la Méga-Gemme : celui de Showdown, ex. Absolite, Banettite, Glalitite, Salamencite, Gyaradosite. « Z » = Méga-Évolutions de Légendes Z-A : Absolite Z, Garchompite Z.)

## Damien (Sidney) (Ténèbres)

- Niveaux d'origine : 46-49 (5 Pokémon).
- Objets de soin d'origine : Full Restore / Full Restore.

**Équipe d'origine**

```
Mightyena
Level: 46
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Roar
- Double Edge
- Sand Attack
- Crunch

Shiftry
Level: 48
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Torment
- Double Team
- Swagger
- Extrasensory

Cacturne
Level: 46
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Leech Seed
- Feint Attack
- Needle Arm
- Cotton Spore

Crawdaunt
Level: 48
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Surf
- Swords Dance
- Strength
- Facade

Absol @ Sitrus Berry
Level: 49
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Aerial Ace
- Rock Slide
- Swords Dance
- Slash
```

**Normal** (dans le jeu)

```
Meowscarada @ Choice Band
Ability: Protean
Level: 66
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Knock Off
- U-turn
- Triple Axel
- Flower Trick

Moltres-Galar @ Heavy-Duty Boots
Ability: Berserk
Level: 66
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Nasty Plot
- Air Slash
- Fiery Wrath
- U-turn

Hoopa-Unbound @ Choice Band
Ability: Magician
Level: 66
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Drain Punch
- Hyperspace Fury
- Knock Off
- Zen Headbutt

Darkrai @ Life Orb
Ability: Bad Dreams
Level: 66
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Dark Void
- Dream Eater
- Dark Pulse
- Sludge Bomb

Kingambit @ Leftovers
Ability: Supreme Overlord
Level: 66
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Sucker Punch
- Iron Head
- Swords Dance
- Kowtow Cleave

Absol @ Absolite Z
Ability: Super Luck
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Night Slash
- Shadow Claw
- Swords Dance
- Close Combat
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Spectra (Phoebe) (Spectre)

- Niveaux d'origine : 48-51 (5 Pokémon).
- Objets de soin d'origine : Full Restore / Full Restore.

**Équipe d'origine**

```
Dusclops
Level: 48
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Shadow Punch
- Confuse Ray
- Curse
- Protect

Banette
Level: 49
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Shadow Ball
- Grudge
- Will O Wisp
- Feint Attack

Sableye
Level: 50
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Shadow Ball
- Double Team
- Night Shade
- Feint Attack

Banette
Level: 49
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Shadow Ball
- Psychic
- Thunderbolt
- Facade

Dusclops @ Sitrus Berry
Level: 51
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Shadow Ball
- Ice Beam
- Rock Slide
- Earthquake
```

**Normal** (dans le jeu)

```
Marshadow @ Life Orb
Ability: Technician
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Shadow Sneak
- Close Combat
- Spectral Thief
- Ice Punch

Aegislash @ Weakness Policy
Ability: Stance Change
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- King's Shield
- Iron Head
- Shadow Sneak
- Shadow Ball

Flutter Mane @ Booster Energy
Ability: Protosynthesis
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 30 SpD / 31 Spe
- Moonblast
- Shadow Ball
- Power Gem
- Sacred Fire

Dragapult @ Choice Specs
Ability: Infiltrator
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Draco Meteor
- U-turn
- Flamethrower
- Shadow Ball

Giratina-Origin @ Griseous Core
Ability: Levitate
Level: 67
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Poltergeist
- Dragon Tail
- Will-O-Wisp
- Defog

Chandelure @ Chandelurite
Ability: Flash Fire
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Overheat
- Shadow Ball
- Flamethrower
- Energy Ball
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Glacia (Glace)

- Niveaux d'origine : 50-53 (5 Pokémon).
- Objets de soin d'origine : Full Restore / Full Restore.

**Équipe d'origine**

```
Sealeo
Level: 50
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Encore
- Body Slam
- Hail
- Ice Ball

Glalie
Level: 50
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Light Screen
- Crunch
- Icy Wind
- Ice Beam

Sealeo
Level: 52
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Attract
- Double Edge
- Hail
- Blizzard

Glalie
Level: 52
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Shadow Ball
- Explosion
- Hail
- Ice Beam

Walrein @ Sitrus Berry
Level: 53
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Surf
- Body Slam
- Ice Beam
- Sheer Cold
```

**Normal** (dans le jeu)

```
Ninetales-Alola @ Light Clay
Ability: Snow Warning
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Aurora Veil
- Moonblast
- Freeze Dry
- Encore

Chien-Pao @ Focus Sash
Ability: Sword of Ruin
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Sucker Punch
- Sacred Sword
- Icicle Crash
- Ice Shard

Mamoswine @ Life Orb
Ability: Thick Fat
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Icicle Crash
- Ice Shard
- Stealth Rock

Kyurem-White @ Choice Scarf
Ability: Turboblaze
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Draco Meteor
- Freeze Dry
- Earth Power
- Fusion Flare

Kyurem-Black @ Loaded Dice
Ability: Teravolt
Level: 68
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Icicle Spear
- Scale Shot
- Dragon Dance
- Fusion Bolt

Froslass @ Froslassite
Ability: Cursed Body
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Blizzard
- Shadow Ball
- Aurora Veil
- Nasty Plot
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Aragon (Drake) (Dragon)

- Niveaux d'origine : 52-55 (5 Pokémon).
- Objets de soin d'origine : Full Restore / Full Restore.

**Équipe d'origine**

```
Shelgon
Level: 52
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Rock Tomb
- Dragon Claw
- Protect
- Double Edge

Altaria
Level: 54
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Double Edge
- Dragon Breath
- Dragon Dance
- Aerial Ace

Kingdra
Level: 53
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Smokescreen
- Dragon Dance
- Surf
- Body Slam

Flygon
Level: 53
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Flamethrower
- Crunch
- Dragon Breath
- Earthquake

Salamence @ Sitrus Berry
Level: 55
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Flamethrower
- Dragon Claw
- Rock Slide
- Crunch
```

**Normal** (dans le jeu)

```
Garchomp @ Rocky Helmet
Ability: Rough Skin
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Dragon Tail
- Stealth Rock
- Spikes

Hydreigon @ Choice Specs
Ability: Levitate
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Dark Pulse
- Draco Meteor
- Nasty Plot
- U-turn

Naganadel @ Focus Sash
Ability: Beast Boost
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Sludge Bomb
- Draco Meteor
- Tailwind
- Heat Wave

Palkia-Origin @ Lustrous Globe
Ability: Pressure
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Hydro Pump
- Draco Meteor
- Thunder
- Fire Blast

Dialga-Origin @ Adamant Crystal
Ability: Pressure
Level: 69
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Draco Meteor
- Flash Cannon
- Earth Power
- Ice Beam

Salamence @ Salamencite
Ability: Intimidate
Level: 70
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Dragon Dance
- Earthquake
- Roost
- Double-Edge
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).

## Marc (Wallace), Maître (Eau)

- Niveaux d'origine : 55-58 (6 Pokémon).
- Objets de soin d'origine : Full Restore / Full Restore / Full Restore / Full Restore.

**Équipe d'origine**

```
Wailord
Level: 57
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Rain Dance
- Water Spout
- Double Edge
- Blizzard

Tentacruel
Level: 55
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Toxic
- Hydro Pump
- Sludge Bomb
- Ice Beam

Ludicolo
Level: 56
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Giga Drain
- Surf
- Leech Seed
- Double Team

Whiscash
Level: 56
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Surf
- Amnesia
- Hyper Beam

Gyarados
Level: 56
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Dragon Dance
- Earthquake
- Hyper Beam
- Surf

Milotic @ Sitrus Berry
Level: 58
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Recover
- Surf
- Ice Beam
- Toxic
```

**Normal** (dans le jeu)

```
Kyogre @ Blue Orb
Ability: Drizzle
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Ice Beam
- Thunder
- Origin Pulse
- Calm Mind

Zygarde-50-Power-Construct @ Leftovers
Ability: Power Construct
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Thousand Arrows
- Coil
- Glare
- Substitute

Miraidon @ Choice Scarf
Ability: Hadron Engine
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Draco Meteor
- Volt Switch
- Dazzling Gleam
- Electro Drift

Arceus @ Silk Scarf
Ability: Multitype
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Extreme Speed
- Earthquake
- Recover
- Judgment

Calyrex-Shadow @ Choice Specs
Ability: As One Shadow Rider
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Psyshock
- Trick
- Astral Barrage
- Draining Kiss

Magearna @ Magearnite
Ability: Soul-Heart
Level: 72
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Shift Gear
- Volt Switch
- Stored Power
- Fleur Cannon
```

**Difficile** : même équipe, niveaux +10 % (règle automatique).
