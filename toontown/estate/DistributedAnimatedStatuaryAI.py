from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from DistributedStatuaryAI import DistributedStatuaryAI

class DistributedAnimatedStatuaryAI(DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedAnimatedStatuaryAI')


