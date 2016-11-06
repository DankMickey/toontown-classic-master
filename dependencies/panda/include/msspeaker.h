#ifndef MSSPEAKER_H
#define MSSPEAKER_H

#include "mss.h"


typedef enum
{
   MSS_SPEAKER_FRONT_LEFT            = 0,     // Speaker order indexes correspond to 
   MSS_SPEAKER_FRONT_RIGHT           = 1,     // bitmasks in PSDK's ksmedia.h
   MSS_SPEAKER_FRONT_CENTER          = 2,     // Also see microsoft.com/whdc/device/audio/multichaud.mspx
   MSS_SPEAKER_LOW_FREQUENCY         = 3,
   MSS_SPEAKER_BACK_LEFT             = 4,
   MSS_SPEAKER_BACK_RIGHT            = 5,
   MSS_SPEAKER_FRONT_LEFT_OF_CENTER  = 6,
   MSS_SPEAKER_FRONT_RIGHT_OF_CENTER = 7,
   MSS_SPEAKER_BACK_CENTER           = 8,
   MSS_SPEAKER_SIDE_LEFT             = 9,
   MSS_SPEAKER_SIDE_RIGHT            = 10,
   MSS_SPEAKER_TOP_CENTER            = 11,
   MSS_SPEAKER_TOP_FRONT_LEFT        = 12,
   MSS_SPEAKER_TOP_FRONT_CENTER      = 13,
   MSS_SPEAKER_TOP_FRONT_RIGHT       = 14,
   MSS_SPEAKER_TOP_BACK_LEFT         = 15,
   MSS_SPEAKER_TOP_BACK_CENTER       = 16,
   MSS_SPEAKER_TOP_BACK_RIGHT        = 17,
   MSS_SPEAKER_MAX_INDEX             = 17
}
MSS_SPEAKER;

#endif