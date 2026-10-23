#include "global.h"
#include "pokemon.h"
#include "wild_encounter.h"
#include "test/test.h"
#include "constants/nabla.h"

TEST("Nabla: wild Pokémon evolve with their level, and from level 40 for the other evolutions")
{
    struct Pokemon mon;
    enum Species species = SPECIES_NONE, evolution = SPECIES_NONE;
    u32 level = 0, gender = MON_MALE;

    PARAMETRIZE { species = SPECIES_CHARMANDER; level = 15; evolution = SPECIES_NONE; }
    PARAMETRIZE { species = SPECIES_CHARMANDER; level = 16; evolution = SPECIES_CHARMELEON; }
    PARAMETRIZE { species = SPECIES_ONIX; level = NABLA_OTHER_EVOLUTIONS_LEVEL - 1; evolution = SPECIES_NONE; }
    PARAMETRIZE { species = SPECIES_ONIX; level = NABLA_OTHER_EVOLUTIONS_LEVEL; evolution = SPECIES_STEELIX; }
    PARAMETRIZE { species = SPECIES_MACHOKE; level = NABLA_OTHER_EVOLUTIONS_LEVEL; evolution = SPECIES_MACHAMP; }
    PARAMETRIZE { species = SPECIES_GOLBAT; level = NABLA_OTHER_EVOLUTIONS_LEVEL; evolution = SPECIES_CROBAT; }
    PARAMETRIZE { species = SPECIES_COMBEE; level = NABLA_OTHER_EVOLUTIONS_LEVEL; gender = MON_MALE; evolution = SPECIES_NONE; }
    PARAMETRIZE { species = SPECIES_COMBEE; level = 21; gender = MON_FEMALE; evolution = SPECIES_VESPIQUEN; }

    CreateMon(&mon, species, level, GetMonPersonality(species, gender, NATURE_HARDY, RANDOM_UNOWN_LETTER), OTID_STRUCT_PLAYER_ID);
    EXPECT_EQ(GetNablaWildEvolution(&mon), evolution);
}
