#include "global.h"
#include "caps.h"
#include "difficulty.h"
#include "event_data.h"
#include "test/test.h"

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
