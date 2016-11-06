from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class MagicWordManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('MagicWordManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def setMagicWord(self, magicWord, avId, zoneId):
        if avId not in self.air.doId2do:
            return

        if avId == self.air.getAvatarIdFromSender():
            self.sendUpdateToAvatarId(avId, 'setMagicWord', [
                magicWord, 
                avId, 
                zoneId])

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
