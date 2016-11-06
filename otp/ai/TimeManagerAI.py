from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from pandac.PandaModules import *
import time

class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getTimestamp(self):
        return int(globalClockDelta.getRealNetworkTime(bits=32))

    def requestServerTime(self, context):
        avatarID = self.air.getAvatarIdFromSender()

        self.sendUpdateToAvatarId(avatarID, 'serverTime', [
            context, 
            self.getTimestamp(), 
            int(time.time())])

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
