#include "global.h"
#include "event_data.h"
#include "nabla_white_rock.h"
#include "pokemon.h"
#include "test/test.h"

TEST("Nabla: the white rock of Mossdeep City changes the form of Deoxys")
{
    enum Species species = SPECIES_NONE, form = SPECIES_NONE;

    PARAMETRIZE { species = SPECIES_DEOXYS_NORMAL; form = SPECIES_DEOXYS_ATTACK; }
    PARAMETRIZE { species = SPECIES_DEOXYS_SPEED; form = SPECIES_DEOXYS_NORMAL; }
    PARAMETRIZE { species = SPECIES_WOBBUFFET; form = SPECIES_WOBBUFFET; }

    ZeroPlayerPartyMons();
    CreateMon(&gParties[B_TRAINER_PLAYER][0], species, 50, 0, OTID_STRUCT_PLAYER_ID);
    gSpecialVar_0x8004 = 0;
    EXPECT_EQ(NablaWhiteRock_HasFormChangeMon(), species != SPECIES_WOBBUFFET);
    EXPECT_EQ(NablaWhiteRock_TryFormChange(), species != SPECIES_WOBBUFFET);
    EXPECT_EQ(GetMonData(&gParties[B_TRAINER_PLAYER][0], MON_DATA_SPECIES), form);
}
