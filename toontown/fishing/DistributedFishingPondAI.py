from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedFishingPondAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingPondAI')

    def __init__(self, air, area):
        DistributedObjectAI.__init__(self, air)
        self.area = area
        self.doId2do = { }
        self.spots = { }

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
    
    def addTarget(self, target):
        if not target:
            return 
        if target.getDoId() not in self.doId2do:
            self.doId2do[target.getDoId()] = target
        else:
            self.notify.warning('A fishing target requested add with doId: %d, but already exists in the doId2do' % target.getDoId())
    
    def removeTarget(self, target):
        if not target:
            return
        if target.getDoId() in self.doId2do:
            del self.doId2do[target.getDoId()]
        else:
            self.notify.warning('A fishing target request delete with doId: %d, but wasn\'t in the doId2do!' % target.getDoId())
    
    def hitTarget(self, targetDoId):
        pass
    
    def getArea(self):
        return self.area
        
    def addSpot(self, spot):
        self.spots[spot.doId] = spot

    def hasToon(self, avId):
        for spot in self.spots:
            if self.spots[spot].avId == avId:
                return self.spots[spot]
        return

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
