from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

class DistributedGardenBoxAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGardenBoxAI')
        
    def setTypeIndex(self, index):
        self.index = index
        
    def getTypeIndex(self):
        return self.index