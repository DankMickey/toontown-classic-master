from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedKartPadAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartPadAI')

    def __init__(self, air, area):
        DistributedObjectAI.__init__(self, air)
        self.area = area
        self.startingBlocks = { }

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getArea(self):
        return self.area
    
    def addAvBlock(self, avId, startingBlock, paid):
        if avId not in self.air.doId2do:
            return False
		
        if avId in self.startingBlocks.keys():
            del self.startingBlocks[avId]
            return False
		
        self.startingBlocks[avId] = startingBlock
        return True
	
    def kartMovieDone(self):
        pass
    	
    def removeAvBlock(self, avId, startingBlock):
        if avId not in self.air.doId2do:
            return
		
        if avId not in self.startingBlocks.keys():
            return
		
        sb = self.startingBlocks[avId]
        if sb.getDoId() == startingBlock.getDoId():
            del self.startingBlocks[avId]

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
