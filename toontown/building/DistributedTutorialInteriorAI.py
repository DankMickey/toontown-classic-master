from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedTutorialInteriorAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialInteriorAI')

    def __init__(self, air, zoneId, block, tutorialNpcId):
        DistributedObjectAI.__init__(self, air)
        self.zoneId = zoneId
        self.block = block
        self.tutorialNpcId = tutorialNpcId

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getZoneIdAndBlock(self):
        return [self.zoneId, self.block]

    def getTutorialNpcId(self):
        return self.tutorialNpcId

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
