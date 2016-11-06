from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from DistributedStatuaryAI import DistributedStatuaryAI

class DistributedChangingStatuaryAI(DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedChangingStatuaryAI')

    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel
        
    def getGrowthLevel(self):
        if not self.growthLevel:
            return None
        return self.growthLevel