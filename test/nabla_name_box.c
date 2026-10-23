#include "global.h"
#include "field_message_box.h"
#include "field_name_box.h"
#include "string_util.h"
#include "test/test.h"

TEST("Nabla: the name that starts a message goes to the name box")
{
    u8 message[64];
    const u8 *text = NULL, *speaker = NULL, *shown = NULL;

    PARAMETRIZE { text = COMPOUND_STRING("STEVEN: Hi!"); speaker = COMPOUND_STRING("STEVEN"); shown = COMPOUND_STRING("Hi!"); }
    PARAMETRIZE { text = COMPOUND_STRING("PROF. BIRCH: Hi!"); speaker = COMPOUND_STRING("PROF. BIRCH"); shown = COMPOUND_STRING("Hi!"); }
    PARAMETRIZE { text = COMPOUND_STRING("PIERRE : Salut !"); speaker = COMPOUND_STRING("PIERRE"); shown = COMPOUND_STRING("Salut !"); }
    PARAMETRIZE { text = COMPOUND_STRING("DAD: Hi!"); speaker = COMPOUND_STRING("NORMAN"); shown = COMPOUND_STRING("Hi!"); }
    PARAMETRIZE { text = COMPOUND_STRING("TATE: Hi!\pLIZA: Hi!"); speaker = NULL; shown = COMPOUND_STRING("TATE: Hi!\pLIZA: Hi!"); }
    PARAMETRIZE { text = COMPOUND_STRING("ERROR 404: Hi!"); speaker = NULL; shown = COMPOUND_STRING("ERROR 404: Hi!"); }
    PARAMETRIZE { text = COMPOUND_STRING("Obtained the TM!"); speaker = NULL; shown = COMPOUND_STRING("Obtained the TM!"); }

    gSpeakerName = NULL;
    StringCopy(message, text);
    TryTakeSpeakerFromMessage(message);
    if (speaker == NULL)
        EXPECT(gSpeakerName == NULL);
    else
        EXPECT_EQ(StringCompare(gSpeakerName, speaker), 0);
    EXPECT_EQ(StringCompare(message, shown), 0);
}

TEST("Nabla: a message without a name after a named one has no name box, unless the script gave one")
{
    u8 message[64];
    const u8 *scriptSpeaker = COMPOUND_STRING("WALLY");

    gSpeakerName = NULL;
    StringCopy(message, COMPOUND_STRING("STEVEN: Hi!"));
    TryTakeSpeakerFromMessage(message);
    StringCopy(message, COMPOUND_STRING("STEVEN used the DEVON SCOPE."));
    TryTakeSpeakerFromMessage(message);
    EXPECT(gSpeakerName == NULL);

    gSpeakerName = scriptSpeaker;
    StringCopy(message, COMPOUND_STRING("Hi!"));
    TryTakeSpeakerFromMessage(message);
    EXPECT(gSpeakerName == scriptSpeaker);
    gSpeakerName = NULL;
}
