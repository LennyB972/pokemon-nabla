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

# Rival et Timmy (4.2c)

- **Rival (Brendan ou Flora)** : une équipe par combat, **les mêmes pour Brendan et Flora**. Le rival prend le starter qui a l'avantage sur le tien (Arcko → Poussifeu, Poussifeu → Gobou, Gobou → Arcko) : écris une ligne **`STARTER`** à sa place, Claude génère les 3 versions.
- **`STARTER`** : écris seulement son niveau (et un objet si tu veux) :

```
STARTER @ Sitrus Berry
Level: 31
```

  Claude choisit le stade d'évolution selon le niveau (évolution aux niveaux 16 et 36 pour les trois lignées), le meilleur talent et 4 capacités apprises par niveau jusqu'à ce niveau, variées (attaque du type, couverture, soutien). `STARTER @ Mega` donne la Méga-Gemme de la lignée (Jungkite, Braségalite, Laggronite : Sceptilite, Blazikenite, Swampertite), à partir de la 6ᵉ arène.
- **Level cap** au moment du combat : indiqué pour chaque combat.
- **Difficile** : même équipe, niveaux +10 % (règle automatique).
- **Combats finaux** (rival à Nénucrique, Timmy sur la Route Victoire et ses revanches) : sets inspirés des sets compétitifs, avec des capacités des jeux officiels qui ne s'apprennent pas forcément par les CT d'Émeraude (U-turn, Volt Switch…). Ailleurs, capacités apprises par niveau jusqu'au niveau du Pokémon.
- **Timmy dans la Forêt Émeraude** : nouveau dresseur `TRAINER_NABLA_WALLY_EMERALD_FOREST` (857), branché quand la zone sera construite.

## Rival — combats d'origine

| Combat | Si tu as pris Arcko | Si tu as pris Poussifeu | Si tu as pris Gobou |
|---|---|---|---|
| Route 103 | Torchic 5 | Mudkip 5 | Treecko 5 |
| Mérouville | Lotad 13, Torchic 15 | Torkoal 13, Mudkip 15 | Wingull 13, Treecko 15 |
| Route 110 | Wingull 18, Lombre 18, Combusken 20 | Lombre 18, Slugma 18, Marshtomp 20 | Wingull 18, Slugma 18, Grovyle 20 |
| Route 119 | Pelipper 29, Lombre 29, Combusken 31 | Lombre 29, Slugma 29, Marshtomp 31 | Slugma 29, Lombre 29, Grovyle 31 |
| Nénucrique | Tropius 31, Pelipper 32, Ludicolo 32, Combusken 34 | Tropius 31, Ludicolo 32, Slugma 32, Marshtomp 34 | Tropius 31, Slugma 32, Pelipper 32, Grovyle 34 |

## Rival — Route 103, au tout début (avant le 1er badge)

- Level cap à ce moment : **16**.
- Objets de soin d'origine : aucun.

**Normal** (dans le jeu ; les mêmes pour Brendan et Flora)

```
# STARTER, si tu as pris Arcko :
Torchic
Ability: Speed Boost
Level: 5
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe
- Scratch
- Growl
- Ember

# STARTER, si tu as pris Poussifeu :
Mudkip
Ability: Torrent
Level: 5
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe
- Tackle
- Growl
- Water Gun

# STARTER, si tu as pris Gobou :
Treecko
Ability: Overgrow
Level: 5
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe
- Pound
- Leer
- Leafage
```

## Rival — Mérouville, après le 1er badge

- Level cap à ce moment : **20**.
- Objets de soin d'origine : aucun.

**Normal** (dans le jeu ; les mêmes pour Brendan et Flora)

```
Taillow
Ability: Guts
Level: 17
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
- Wing Attack
- Quick Attack
- Double Team
- Growl

Aron
Ability: Sturdy
Level: 17
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
- Metal Claw
- Rock Tomb
- Headbutt
- Harden

# STARTER, si tu as pris Arcko :
Combusken
Ability: Speed Boost
Level: 18
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Double Kick
- Flame Charge
- Aerial Ace
- Detect

# STARTER, si tu as pris Poussifeu :
Marshtomp
Ability: Torrent
Level: 18
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Mud Shot
- Water Pulse
- Rock Throw
- Protect

# STARTER, si tu as pris Gobou :
Grovyle
Ability: Overgrow
Level: 18
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Mega Drain
- Assurance
- Quick Attack
- Detect
```

## Rival — Route 110, après le 2ᵉ badge

- Level cap à ce moment : **27**.
- Objets de soin d'origine : aucun.

**Normal** (dans le jeu ; les mêmes pour Brendan et Flora)

```
Swellow @ Sitrus Berry
Ability: Guts
Level: 22
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Aerial Ace
- Quick Attack
- Double Team
- Growl

Aron @ Leftovers
Ability: Sturdy
Level: 22
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Metal Claw
- Rock Tomb
- Headbutt
- Protect

Trapinch
Ability: Arena Trap
Level: 22
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
- Bulldoze
- Bite
- Astonish
- Sand Attack

# STARTER, si tu as pris Arcko :
Combusken
Ability: Speed Boost
Level: 23
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Flame Charge
- Double Kick
- Slash
- Detect

# STARTER, si tu as pris Poussifeu :
Marshtomp
Ability: Torrent
Level: 23
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Mud Shot
- Water Pulse
- Rock Slide
- Protect

# STARTER, si tu as pris Gobou :
Grovyle
Ability: Overgrow
Level: 23
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Giga Drain
- Assurance
- Quick Attack
- Detect
```

## Rival — Route 119, après le 5ᵉ badge

- Level cap à ce moment : **41**.
- Objets de soin d'origine : aucun.

**Normal** (dans le jeu ; les mêmes pour Brendan et Flora)

```
Swellow @ Sitrus Berry
Ability: Guts
Level: 35
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Brave Bird
- Quick Attack
- Agility
- Double Team

Vibrava @ Soft Sand
Ability: Levitate
Level: 35
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Dig
- Dragon Breath
- Bug Buzz
- Screech

Lairon @ Leftovers
Ability: Sturdy
Level: 35
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Iron Head
- Rock Slide
- Protect
- Roar

Snorunt
Ability: Inner Focus
Level: 35
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Frost Breath
- Bite
- Ice Shard
- Protect

Latias
Ability: Levitate
Level: 33
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Dragon Breath
- Confusion
- Recover
- Charm

# STARTER, si tu as pris Arcko :
Blaziken
Ability: Speed Boost
Level: 36
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Blaze Kick
- Double Kick
- Bounce
- Detect

# STARTER, si tu as pris Poussifeu :
Swampert
Ability: Torrent
Level: 36
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Surf
- Earthquake
- Rock Slide
- Protect

# STARTER, si tu as pris Gobou :
Sceptile
Ability: Overgrow
Level: 36
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Leaf Blade
- X-Scissor
- Quick Attack
- Detect
```

## Rival — Nénucrique, après le 6ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **51**.
- Objets de soin d'origine : aucun.

**Normal** (dans le jeu ; les mêmes pour Brendan et Flora)

```
Swellow @ Sitrus Berry
Ability: Guts
Level: 43
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Brave Bird
- Facade
- Quick Attack
- U-turn

Flygon @ Soft Sand
Ability: Levitate
Level: 45
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Earthquake
- Dragon Claw
- U-turn
- Fire Punch

Aggron @ Leftovers
Ability: Rock Head
Level: 45
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Head Smash
- Heavy Slam
- Earthquake
- Stealth Rock

Glalie @ Never-Melt Ice
Ability: Inner Focus
Level: 45
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Freeze-Dry
- Ice Shard
- Crunch
- Earthquake

Latias @ Soul Dew
Ability: Levitate
Level: 43
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Draco Meteor
- Psyshock
- Calm Mind
- Recover

# STARTER, si tu as pris Arcko :
Blaziken @ Blazikenite
Ability: Speed Boost
Level: 46
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Protect
- Flare Blitz
- Close Combat
- Swords Dance

# STARTER, si tu as pris Poussifeu :
Swampert @ Swampertite
Ability: Torrent
Level: 46
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Rain Dance
- Waterfall
- Earthquake
- Ice Punch

# STARTER, si tu as pris Gobou :
Sceptile @ Sceptilite
Ability: Overgrow
Level: 46
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Leaf Storm
- Dragon Pulse
- Focus Blast
- Earthquake
```

## Timmy — Lavandia, devant l'arène, avant le 3ᵉ badge

- Level cap à ce moment : **27**.
- Objets de soin d'origine : aucun.

**Équipe d'origine**

```
Ralts
Level: 16
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
```

**Normal** (dans le jeu)

```
Magneton
Ability: Magnet Pull
Level: 24
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
- Spark
- Gyro Ball
- Thunder Wave
- Supersonic

Swablu
Ability: Natural Cure
Level: 24
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
- Dragon Breath
- Disarming Voice
- Round
- Safeguard

Kirlia
Ability: Trace
Level: 25
IVs: 3 HP / 3 Atk / 3 Def / 3 SpA / 3 SpD / 3 Spe
- Psybeam
- Draining Kiss
- Hypnosis
- Life Dew
```

## Timmy — Forêt Emeraude, avant le 7ᵉ badge

- Level cap à ce moment : **51**.

**Normal** (dans le jeu)

```
Magnezone
Ability: Magnet Pull
Level: 41
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Discharge
- Flash Cannon
- Tri Attack
- Thunder Wave

Altaria
Ability: Natural Cure
Level: 41
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Dragon Pulse
- Moonblast
- Cotton Guard
- Sing

Larvesta
Ability: Flame Body
Level: 41
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Flame Wheel
- Leech Life
- Flame Charge
- Screech

Celebi
Ability: Natural Cure
Level: 40
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Magical Leaf
- Confusion
- Ancient Power
- Life Dew

Gallade
Ability: Sharpness
Level: 43
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Psycho Cut
- Sacred Sword
- Night Slash
- Swords Dance
```

## Timmy — Route Victoire, avant la Ligue

- Level cap à ce moment : **72**.
- Objets de soin d'origine : Full Restore / Full Restore.

**Équipe d'origine**

```
Altaria
Level: 44
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Aerial Ace
- Safeguard
- Dragon Breath
- Dragon Dance

Delcatty
Level: 43
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Sing
- Assist
- Charm
- Feint Attack

Roselia
Level: 44
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Magical Leaf
- Leech Seed
- Giga Drain
- Toxic

Magneton
Level: 41
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Supersonic
- Thunderbolt
- Tri Attack
- Screech

Gardevoir
Level: 45
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Double Team
- Calm Mind
- Psychic
- Future Sight
```

**Normal** (dans le jeu)

```
Magnezone @ Magnet
Ability: Magnet Pull
Level: 65
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Thunderbolt
- Flash Cannon
- Volt Switch
- Thunder Wave

Altaria @ Lum Berry
Ability: Natural Cure
Level: 65
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Dragon Dance
- Dragon Claw
- Earthquake
- Roost

Volcarona @ Leftovers
Ability: Flame Body
Level: 65
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Quiver Dance
- Fiery Dance
- Bug Buzz
- Roost

Celebi @ Miracle Seed
Ability: Natural Cure
Level: 65
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Nasty Plot
- Giga Drain
- Psychic
- Earth Power

Ceruledge @ Life Orb
Ability: Flash Fire
Level: 65
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
- Bitter Blade
- Poltergeist
- Swords Dance
- Shadow Sneak

Gallade @ Galladite
Ability: Sharpness
Level: 66
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Swords Dance
- Sacred Sword
- Psycho Cut
- Night Slash
```

## Timmy — revanches (après la Ligue, Route Victoire)

Même équipe et mêmes sets que sur la Route Victoire, tous les Pokémon au niveau **80** (1ʳᵉ revanche), **90** (2ᵉ), puis **100** (3ᵉ et suivantes). `TRAINER_WALLY_VR_2` à `VR_5`.

# Team Aqua et Team Magma (4.2d)

- **Nombre de Pokémon** : au choix de l'utilisateur, combat par combat.
- **Combats en duo** (Île du Sud, Centre Spatial) : **3 Pokémon par dresseur**, Pierre Rochard compris ; le joueur choisit 3 de ses Pokémon avant le combat.
- **Méga-Évolution** : à partir de la 6ᵉ arène (combats du Repaire Magma et après). En duo, chaque dresseur peut méga-évoluer une fois. Méga-Gemmes liées aux équipes d'origine : Cameruptite (Camérupt), Sharpedonite (Sharpedo), Houndoominite (Démolosse) ; pour Pierre : Metagrossite (Métalosse), Aggronite (Galeking), Skarmorite (Airmure).
- **Capacités laissées vides** : 4 capacités apprises par niveau jusqu'au niveau du Pokémon, variées ; pour le **dernier combat** de chaque personnage (Tabitha et Max au Centre Spatial, Matt au Repaire Aqua, Shelly et Arthur à la Grotte du Fond Marin, Pierre au Centre Spatial), sets inspirés des sets compétitifs, comme pour la 4.2c.
- **Level cap** au moment du combat : indiqué pour chaque combat.
- **Difficile** : même équipe, niveaux +10 % (règle automatique). Pierre Rochard est un allié : son équipe ne change pas en Difficile.
- Les sbires (dresseurs ordinaires) seront relevés avec les autres dresseurs en 4.3, sauf le sbire de l'Île du Sud, qui fait équipe avec Matt.

## Combats d'origine, dans l'ordre de l'histoire

| # | Combat | Moment | Level cap | Équipe d'origine | N° |
|---|---|---|---|---|---|
| 1 | Tabitha, Mont Chimnée | après le 3ᵉ badge | 34 | Numel 18, Poochyena 20, Numel 22, Zubat 22 | 597 |
| 2 | Max (Maxie), Mont Chimnée, juste après Tabitha | après le 3ᵉ badge | 34 | Mightyena 24, Zubat 24, Camerupt 25 | 602 |
| 3 | Matt et un sbire contre toi et Pierre, Île du Sud (événement Latios) | après le 5ᵉ badge | 41 | Matt : Mightyena 31, Golbat 31, Sharpedo 32. Sbire : Carvanha 29, Wailmer 29. Pierre : Skarmory 32, Metang 33 | 855 + 856 |
| 4 | Shelly, Institut Météo | après le 5ᵉ badge | 41 | Carvanha 28, Mightyena 28 | 32 |
| 5 | Tabitha, Repaire Magma | après le 6ᵉ badge | 51 | Numel 26, Mightyena 28, Zubat 30, Camerupt 33 | 732 |
| 6 | Max, Repaire Magma, après Tabitha | après le 6ᵉ badge | 51 | Mightyena 37, Crobat 38, Camerupt 39 | 601 |
| 7 | Matt, Repaire Aqua | après le 6ᵉ badge | 51 | Mightyena 34, Golbat 34 | 30 |
| 8 | Max et Tabitha contre toi et Pierre, Centre Spatial | après le 7ᵉ badge | 59 | Max : Mightyena 42, Crobat 43, Camerupt 44. Tabitha : Camerupt 36, Mightyena 38, Golbat 40. Pierre : Metang 42, Skarmory 43, Aggron 44 | 734 + 514 |
| 9 | Shelly, Grotte du Fond Marin | après le 7ᵉ badge | 59 | Sharpedo 37, Mightyena 37 | 33 |
| 10 | Arthur (Archie), Grotte du Fond Marin | après le 7ᵉ badge | 59 | Mightyena 41, Crobat 41, Sharpedo 43 | 34 |

Repères dans la nouvelle courbe : rival Route 119 à 35-36 (cap 41) ; rival Nénucrique à 43-46 et Timmy dans la Forêt Émeraude à 40-43 (cap 51).

## Tabitha — Mont Chimnée, après le 3ᵉ badge

- Level cap à ce moment : **34**. Combat juste avant celui de Max, sans Centre Pokémon entre les deux.
- Objets de soin d'origine : aucun.

**Équipe d'origine**

```
Numel
Level: 18
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Poochyena
Level: 20
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Numel
Level: 22
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Zubat
Level: 22
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
```

**Normal** (à remplir)

```

```

## Max (Maxie) — Mont Chimnée, après le 3ᵉ badge

- Level cap à ce moment : **34**.
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Mightyena
Level: 24
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Zubat
Level: 24
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Camerupt
Level: 25
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
```

**Normal** (à remplir)

```

```

## Île du Sud — Matt et un sbire contre toi et Pierre Rochard, après le 5ᵉ badge (événement Latios)

- Level cap à ce moment : **41**.
- Combat en duo : **3 Pokémon par dresseur** (le joueur en choisit 3).
- Objets de soin : aucun.
- Équipes actuelles : celles de l'événement Latios (étape 3.4). Matt et le sbire ont aussi une équipe Difficile faite à la main à l'époque (sets différents) : à décider avec l'utilisateur (garder, ou la retirer pour appliquer la règle des +10 %).

### Matt (`TRAINER_NABLA_MATT_SOUTHERN_ISLAND`, 855)

**Équipe actuelle (Normal)**

```
Mightyena
Level: 31
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Golbat
Level: 31
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Sharpedo
Level: 32
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
```

**Normal** (à remplir)

```

```

### Sbire de la Team Aqua (`TRAINER_NABLA_GRUNT_SOUTHERN_ISLAND`, 856)

**Équipe actuelle (Normal)**

```
Carvanha
Level: 29
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe

Wailmer
Level: 29
IVs: 0 HP / 0 Atk / 0 Def / 0 SpA / 0 SpD / 0 Spe
```

**Normal** (à remplir)

```

```

### Pierre Rochard, allié (`PARTNER_STEVEN_SOUTHERN_ISLAND`)

**Équipe actuelle**

```
Skarmory
Level: 32
Impish Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Steel Wing
- Aerial Ace
- Spikes
- Protect

Metang
Level: 33
Adamant Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Metal Claw
- Zen Headbutt
- Bullet Punch
- Take Down
```

**Équipe** (à remplir, 3 Pokémon)

```

```

## Shelly — Institut Météo (Route 119), après le 5ᵉ badge

- Level cap à ce moment : **41**.
- Objets de soin d'origine : aucun.

**Équipe d'origine**

```
Carvanha
Level: 28
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Mightyena
Level: 28
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
```

**Normal** (à remplir)

```

```

## Tabitha — Repaire Magma, après le 6ᵉ badge

- Level cap à ce moment : **51**. Combat juste avant celui de Max.
- Objets de soin d'origine : aucun.

**Équipe d'origine**

```
Numel
Level: 26
IVs: 9 HP / 9 Atk / 9 Def / 9 SpA / 9 SpD / 9 Spe

Mightyena
Level: 28
IVs: 9 HP / 9 Atk / 9 Def / 9 SpA / 9 SpD / 9 Spe

Zubat
Level: 30
IVs: 9 HP / 9 Atk / 9 Def / 9 SpA / 9 SpD / 9 Spe

Camerupt
Level: 33
IVs: 9 HP / 9 Atk / 9 Def / 9 SpA / 9 SpD / 9 Spe
```

**Normal** (à remplir)

```

```

## Max (Maxie) — Repaire Magma, après le 6ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **51**.
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Mightyena
Level: 37
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Crobat
Level: 38
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Camerupt
Level: 39
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
```

**Normal** (à remplir)

```

```

## Matt — Repaire Aqua (Nénucrique), après le 6ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **51**.
- Objets de soin d'origine : Super Potion.

**Équipe d'origine**

```
Mightyena
Level: 34
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe

Golbat
Level: 34
IVs: 6 HP / 6 Atk / 6 Def / 6 SpA / 6 SpD / 6 Spe
```

**Normal** (à remplir)

```

```

## Centre Spatial (Algatia) — Max et Tabitha contre toi et Pierre Rochard, après le 7ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **59**.
- Combat en duo : **3 Pokémon par dresseur** (le joueur en choisit 3).
- Objets de soin d'origine : aucun.

### Max (`TRAINER_MAXIE_MOSSDEEP`, 734)

**Équipe d'origine**

```
Mightyena
Level: 42
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Crobat
Level: 43
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Camerupt
Level: 44
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
```

**Normal** (à remplir, 3 Pokémon)

```

```

### Tabitha (`TRAINER_TABITHA_MOSSDEEP`, 514)

**Équipe d'origine**

```
Camerupt
Level: 36
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe

Mightyena
Level: 38
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe

Golbat
Level: 40
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
```

**Normal** (à remplir, 3 Pokémon)

```

```

### Pierre Rochard, allié (`PARTNER_STEVEN`)

**Équipe d'origine**

```
Metang
Level: 42
Brave Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Light Screen
- Psychic
- Reflect
- Metal Claw

Skarmory
Level: 43
Impish Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Toxic
- Aerial Ace
- Protect
- Steel Wing

Aggron
Level: 44
Adamant Nature
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Thunder
- Protect
- Solar Beam
- Dragon Claw
```

**Équipe** (à remplir, 3 Pokémon)

```

```

## Shelly — Grotte du Fond Marin, après le 7ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **59**. Combat avant celui d'Arthur, dans la même grotte.
- Objets de soin d'origine : aucun.

**Équipe d'origine**

```
Sharpedo
Level: 37
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe

Mightyena
Level: 37
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
```

**Normal** (à remplir)

```

```

## Arthur (Archie) — Grotte du Fond Marin, après le 7ᵉ badge (Méga-Évolution possible)

- Level cap à ce moment : **59**.
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Mightyena
Level: 41
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Crobat
Level: 41
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe

Sharpedo
Level: 43
IVs: 18 HP / 18 Atk / 18 Def / 18 SpA / 18 SpD / 18 Spe
```

**Normal** (à remplir)

```

```
