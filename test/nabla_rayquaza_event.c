#include "global.h"
#include "event_data.h"
#include "nabla_rayquaza_event.h"
#include "pokemon.h"
#include "pokemon_storage_system.h"
#include "test/test.h"

static void CreatePartyMon(u32 slot, enum Species species)
{
    CreateMon(&gParties[B_TRAINER_PLAYER][slot], species, 50, 0, OTID_STRUCT_PLAYER_ID);
}

static enum Species GetPartySpecies(u32 slot)
{
    return GetMonData(&gParties[B_TRAINER_PLAYER][slot], MON_DATA_SPECIES);
}

TEST("Nabla: the Rayquaza caught at Sky Pillar goes to the head of the party")
{
    ZeroPlayerPartyMons();
    CreatePartyMon(0, SPECIES_WOBBUFFET);
    CreatePartyMon(1, SPECIES_WYNAUT);
    CreatePartyMon(2, SPECIES_RAYQUAZA);
    EXPECT(NablaRayquazaEvent_PutRayquazaFirst());
    EXPECT_EQ(GetPartySpecies(0), SPECIES_RAYQUAZA);
    EXPECT_EQ(GetPartySpecies(1), SPECIES_WOBBUFFET);
    EXPECT_EQ(GetPartySpecies(2), SPECIES_WYNAUT);
}

TEST("Nabla: with a full party, the Rayquaza caught at Sky Pillar takes the place of a chosen Pokémon")
{
    struct Pokemon rayquaza;
    static const enum Species party[PARTY_SIZE] = {SPECIES_WOBBUFFET, SPECIES_WYNAUT, SPECIES_PIKACHU,
                                                   SPECIES_EEVEE, SPECIES_ZIGZAGOON, SPECIES_RALTS};

    ZeroPlayerPartyMons();
    for (u32 i = 0; i < PARTY_SIZE; i++)
        CreatePartyMon(i, party[i]);
    CreateMon(&rayquaza, SPECIES_RAYQUAZA, 65, 0, OTID_STRUCT_PLAYER_ID);
    SetBoxMonAt(0, 0, &rayquaza.box);
    EXPECT(!NablaRayquazaEvent_PutRayquazaFirst());
    gSpecialVar_0x8004 = 2;
    NablaRayquazaEvent_SwapRayquazaIntoParty();
    EXPECT_EQ(GetPartySpecies(0), SPECIES_RAYQUAZA);
    EXPECT_EQ(GetPartySpecies(1), SPECIES_WOBBUFFET);
    EXPECT_EQ(GetPartySpecies(2), SPECIES_WYNAUT);
    EXPECT_EQ(GetPartySpecies(3), SPECIES_EEVEE);
    EXPECT_EQ(GetBoxMonData(GetBoxedMonPtr(0, 0), MON_DATA_SPECIES), SPECIES_PIKACHU);
}

TEST("Nabla: the white rock of Mossdeep City changes the form of Deoxys")
{
    enum Species species = SPECIES_NONE, form = SPECIES_NONE;

    PARAMETRIZE { species = SPECIES_DEOXYS_NORMAL; form = SPECIES_DEOXYS_ATTACK; }
    PARAMETRIZE { species = SPECIES_DEOXYS_SPEED; form = SPECIES_DEOXYS_NORMAL; }
    PARAMETRIZE { species = SPECIES_WOBBUFFET; form = SPECIES_WOBBUFFET; }

    ZeroPlayerPartyMons();
    CreatePartyMon(0, species);
    gSpecialVar_0x8004 = 0;
    EXPECT_EQ(NablaWhiteRock_HasFormChangeMon(), species != SPECIES_WOBBUFFET);
    EXPECT_EQ(NablaWhiteRock_TryFormChange(), species != SPECIES_WOBBUFFET);
    EXPECT_EQ(GetPartySpecies(0), form);
}
