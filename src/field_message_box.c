#include "global.h"
#include "menu.h"
#include "string_util.h"
#include "task.h"
#include "text.h"
#include "match_call.h"
#include "field_message_box.h"
#include "text_window.h"
#include "script.h"
#include "field_name_box.h"

static EWRAM_DATA u8 sFieldMessageBoxMode = 0;
EWRAM_DATA u8 gWalkAwayFromSignpostTimer = 0;

static void ExpandStringAndStartDrawFieldMessage(const u8 *, bool32);
static void StartDrawFieldMessage(void);

void InitFieldMessageBox(void)
{
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
    gTextFlags.canABSpeedUpPrint = FALSE;
    gTextFlags.useAlternateDownArrow = FALSE;
    gTextFlags.autoScroll = FALSE;
    gTextFlags.forceMidTextSpeed = FALSE;
}

#define tState data[0]

static void Task_DrawFieldMessage(u8 taskId)
{
    struct Task *task = &gTasks[taskId];

    switch (task->tState)
    {
    case 0:
        if (gMsgIsSignPost)
            LoadSignPostWindowFrameGfx();
        else
            LoadMessageBoxAndBorderGfx();
        task->tState++;
        break;
    case 1:
    {
        u32 nameboxWinId = GetNameboxWindowId();
        DrawDialogueFrame(0, TRUE);
        if (nameboxWinId != WINDOW_NONE)
            DrawNamebox(nameboxWinId, NAME_BOX_BASE_TILE_NUM - NAME_BOX_BASE_TILES_TOTAL, TRUE);
        task->tState++;
        break;
    }
    case 2:
        if (RunTextPrintersAndIsPrinter0Active() != TRUE)
        {
            sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
            DestroyTask(taskId);
        }
    }
}

#undef tState

static void CreateTask_DrawFieldMessage(void)
{
    CreateTask(Task_DrawFieldMessage, 0x50);
}

static void DestroyTask_DrawFieldMessage(void)
{
    u8 taskId = FindTaskIdByFunc(Task_DrawFieldMessage);
    if (taskId != TASK_NONE)
        DestroyTask(taskId);
}

bool8 ShowFieldMessage(const u8 *str)
{
    if (sFieldMessageBoxMode != FIELD_MESSAGE_BOX_HIDDEN)
        return FALSE;
    ExpandStringAndStartDrawFieldMessage(str, TRUE);
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_NORMAL;
    return TRUE;
}

static void Task_HidePokenavMessageWhenDone(u8 taskId)
{
    if (!IsMatchCallTaskActive())
    {
        sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
        DestroyTask(taskId);
    }
}

bool8 ShowPokenavFieldMessage(const u8 *str)
{
    if (sFieldMessageBoxMode != FIELD_MESSAGE_BOX_HIDDEN)
        return FALSE;
    StringExpandPlaceholders(gStringVar4, str);
    CreateTask(Task_HidePokenavMessageWhenDone, 0);
    StartMatchCallFromScript(str);
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_NORMAL;
    return TRUE;
}

bool8 ShowFieldAutoScrollMessage(const u8 *str)
{
    if (sFieldMessageBoxMode != FIELD_MESSAGE_BOX_HIDDEN)
        return FALSE;
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_AUTO_SCROLL;
    ExpandStringAndStartDrawFieldMessage(str, FALSE);
    return TRUE;
}

static bool8 UNUSED ForceShowFieldAutoScrollMessage(const u8 *str)
{
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_AUTO_SCROLL;
    ExpandStringAndStartDrawFieldMessage(str, TRUE);
    return TRUE;
}

// Same as ShowFieldMessage, but instead of accepting a
// string arg it just prints whats already in gStringVar4
bool8 ShowFieldMessageFromBuffer(void)
{
    if (sFieldMessageBoxMode != FIELD_MESSAGE_BOX_HIDDEN)
        return FALSE;
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_NORMAL;
    StartDrawFieldMessage();
    return TRUE;
}

// Pokémon Nabla: a message that starts with the name of who speaks ("STEVEN: Hi!") shows this name in the
// name box instead, unless several people speak in it. The original texts stay as they are.
#define MESSAGE_SPEAKER_MAX_LENGTH 12

static EWRAM_DATA u8 sMessageSpeaker[MESSAGE_SPEAKER_MAX_LENGTH + 1] = {0};

// Names shown in the name box under another name than in the texts
static const struct { const u8 *inText; const u8 *shown; } sMessageSpeakerAliases[] =
{
    {COMPOUND_STRING("DAD"), COMPOUND_STRING("NORMAN")},
};

// Length of the name that starts the message (capital letters, spaces, periods, "&"), followed by ": "
// or " : "; 0 if there is none
static u32 GetMessageSpeakerLength(const u8 *str)
{
    if (str[0] < CHAR_A || str[0] > CHAR_Z)
        return 0;
    for (u32 i = 1; i <= MESSAGE_SPEAKER_MAX_LENGTH; i++)
    {
        if (str[i] == CHAR_COLON || (str[i] == CHAR_SPACE && str[i + 1] == CHAR_COLON))
            return str[i + (str[i] == CHAR_SPACE) + 1] == CHAR_SPACE ? i : 0;
        if ((str[i] < CHAR_A || str[i] > CHAR_Z) && str[i] != CHAR_SPACE && str[i] != CHAR_PERIOD && str[i] != CHAR_AMPERSAND)
            return 0;
    }
    return 0;
}

void TryTakeSpeakerFromMessage(u8 *str)
{
    u8 speaker[MESSAGE_SPEAKER_MAX_LENGTH + 1];
    u32 length = GetMessageSpeakerLength(str);
    bool32 isAutomatic = (gSpeakerName == sMessageSpeaker);

    for (u32 i = 0; length != 0 && str[i] != EOS; i++)
    {
        if (str[i] == CHAR_PROMPT_CLEAR && GetMessageSpeakerLength(&str[i + 1]) != 0)
            length = 0;
    }
    if (length == 0)
    {
        // A message without a name after a named one: narration
        if (isAutomatic)
            gSpeakerName = NULL;
        return;
    }

    StringCopyN(speaker, str, length);
    speaker[length] = EOS;
    for (u32 i = 0; i < ARRAY_COUNT(sMessageSpeakerAliases); i++)
    {
        if (StringCompare(speaker, sMessageSpeakerAliases[i].inText) == 0)
            StringCopy(speaker, sMessageSpeakerAliases[i].shown);
    }
    // A name given by the script or by the trainer's data comes first
    if (gSpeakerName != NULL && !isAutomatic && StringCompare(gSpeakerName, speaker) != 0)
        return;

    StringCopy(sMessageSpeaker, speaker);
    gSpeakerName = sMessageSpeaker;
    length += (str[length] == CHAR_SPACE) + 2;
    for (u32 i = 0; ; i++)
    {
        str[i] = str[i + length];
        if (str[i] == EOS)
            break;
    }
}

static void ExpandStringAndStartDrawFieldMessage(const u8 *str, bool32 allowSkippingDelayWithButtonPress)
{
    StringExpandPlaceholders(gStringVar4, str);
    TryTakeSpeakerFromMessage(gStringVar4);
    TrySpawnNamebox(gStringVar4, NAME_BOX_BASE_TILE_NUM);
    AddTextPrinterForMessage(allowSkippingDelayWithButtonPress);
    CreateTask_DrawFieldMessage();
}

static void StartDrawFieldMessage(void)
{
    AddTextPrinterForMessage(TRUE);
    CreateTask_DrawFieldMessage();
}

void HideFieldMessageBox(void)
{
    DestroyTask_DrawFieldMessage();
    ClearDialogWindowAndFrame(0, TRUE);
    DestroyNamebox();
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
}

u8 GetFieldMessageBoxMode(void)
{
    return sFieldMessageBoxMode;
}

bool8 IsFieldMessageBoxHidden(void)
{
    if (sFieldMessageBoxMode == FIELD_MESSAGE_BOX_HIDDEN)
        return TRUE;
    return FALSE;
}

static void UNUSED ReplaceFieldMessageWithFrame(void)
{
    DestroyTask_DrawFieldMessage();
    DrawStdWindowFrame(0, TRUE);
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
}

void StopFieldMessage(void)
{
    DestroyTask_DrawFieldMessage();
    sFieldMessageBoxMode = FIELD_MESSAGE_BOX_HIDDEN;
}
