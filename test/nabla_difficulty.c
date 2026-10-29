#include "global.h"
#include "battle_setup.h"
#include "caps.h"
#include "data.h"
#include "difficulty.h"
#include "event_data.h"
#include "malloc.h"
#include "test/test.h"
#include "constants/trainers.h"

TEST("Nabla: Hard mode raises levels by 10%, rounded down, at least one level")
{
    u32 level = 0, normal = 0, hard = 0;

    PARAMETRIZE { level = 5; normal = 5; hard = 6; }
    PARAMETRIZE { level = 9; normal = 9; hard = 10; }
    PARAMETRIZE { level = 16; normal = 16; hard = 17; }
    PARAMETRIZE { level = 57; normal = 57; hard = 62; }
    PARAMETRIZE { level = 100; normal = 100; hard = 100; }

    SetCurrentDifficultyLevel(DIFFICULTY_NORMAL);
    EXPECT_EQ(GetDifficultyLevel(level), normal);
    SetCurrentDifficultyLevel(DIFFICULTY_HARD);
    EXPECT_EQ(GetDifficultyLevel(level), hard);
    SetCurrentDifficultyLevel(DIFFICULTY_NORMAL);
}

TEST("Nabla: level caps follow the difficulty")
{
    u32 difficulty = DIFFICULTY_NORMAL, cap = 0;

    PARAMETRIZE { difficulty = DIFFICULTY_NORMAL; cap = 16; }
    PARAMETRIZE { difficulty = DIFFICULTY_HARD; cap = 17; }

    FlagSet(FLAG_NABLA_LEVEL_CAPS);
    SetCurrentDifficultyLevel(difficulty);
    EXPECT_EQ(GetCurrentLevelCap(), cap);
    SetCurrentDifficultyLevel(DIFFICULTY_NORMAL);
}

TEST("Nabla: the Elite Four and the Champion are level 100 once the player is the Champion")
{
    u32 trainerClass = TRAINER_CLASS_ELITE_FOUR, isChampion = FALSE, level = 0;
    struct Trainer trainer;
    struct Pokemon *party = Alloc(PARTY_SIZE * sizeof(struct Pokemon));

    PARAMETRIZE { trainerClass = TRAINER_CLASS_ELITE_FOUR; isChampion = FALSE; level = 5; }
    PARAMETRIZE { trainerClass = TRAINER_CLASS_ELITE_FOUR; isChampion = TRUE; level = MAX_LEVEL; }
    PARAMETRIZE { trainerClass = TRAINER_CLASS_CHAMPION; isChampion = TRUE; level = MAX_LEVEL; }
    PARAMETRIZE { trainerClass = TRAINER_CLASS_RIVAL; isChampion = TRUE; level = 5; }

    memcpy(&trainer, GetTrainerStructFromId(1), sizeof(trainer));
    trainer.trainerClass = trainerClass;
    if (isChampion)
        FlagSet(FLAG_IS_CHAMPION);
    CreateNPCTrainerPartyFromTrainer(party, &trainer);
    EXPECT_EQ(GetMonData(&party[0], MON_DATA_LEVEL), level);
    FlagClear(FLAG_IS_CHAMPION);
    Free(party);
}
