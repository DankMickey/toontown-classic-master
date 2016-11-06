from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from DistributedLawnDecorAI import DistributedLawnDecorAI

class DistributedPlantBaseAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPlantBaseAI')

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex
        
    def setWaterLevel(self, waterlevel):
        self.waterLevel = waterLevel
        
    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel
        
    def getTypeIndex(self):
        if not self.typeIndex:
            return None
        return self.typeIndex
        
    def getWaterLevel(self):
        if not self.waterLevel:
            return None
        return self.waterLevel
        
    def getGrowthLevel(self):
        if not self.growthLevel:
            return None
        return self.growthLevel
        
    def waterPlant(self):
        pass
        
    def waterPlantDone(self):
        pass