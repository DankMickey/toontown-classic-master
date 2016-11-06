from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
from otp.uberdog.SpeedchatRelayUD import SpeedchatRelayUD

class TTSpeedchatRelayUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTSpeedchatRelayUD')