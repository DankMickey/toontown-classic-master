# File: D (Python 2.4)

import DistributedBarrelBaseAI
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class DistributedHealBarrelAI(DistributedBarrelBaseAI.DistributedBarrelBaseAI):
    
    def __init__(self, level, entId):
        x = 0
        y = 0
        z = 0
        h = 0
        DistributedBarrelBaseAI.DistributedBarrelBaseAI.__init__(self, level, entId)

    
    def d_setGrab(self, avId):
        self.notify.debug('d_setGrab %s' % avId)
        self.sendUpdate('setGrab', [
            avId])
        av = self.air.doId2do.get(avId)
        if av:
            av.toonUp(self.getRewardPerGrab())
        


