from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from toontown.fishing import FishingTargetGlobals
from toontown.fishing import FishGlobals

class DistributedFishingTargetAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingTargetAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.pondDoId = 0
        self.angle = 0
        self.radius = 0
        self.targetRadius = 0
        self.time = 0
        self.timeStamp = 0
        self.stateIndex = 0

    def generate(self):
        DistributedObjectAI.generate(self)
        if self.pondDoId in self.air.doId2do:
            self.pond = self.air.doId2do[self.pondDoId]
            self.pond.addTarget(self)
            self.centerPoint = FishingTargetGlobals.getTargetCenter(self.pond.getArea())
        else:
            self.pond = None
            self.air.notify.warning('Tried to add target to a non-existant pond with doId: %d!' % self.pondDoId)

    def getPondDoId(self):
        return self.pondDoId
        
    def setPondDoId(self, pondDoId):
        self.pondDoId = pondDoId
    
    def setState(self, stateIndex, angle, radius, time, timeStamp):
        self.angle = angle
        self.radius = radius
        self.time = time
        self.timeStamp = timeStamp
        self.stateIndex = stateIndex     

    def getState(self):
        return [0, self.angle, self.targetRadius, self.time, globalClockDelta.getRealNetworkTime()]

    def updateState(self):
        pass
	
    def disable(self):
        DistributedObjectAI.disable(self)
        
        if self.pond:
            self.pond.removeTarget(self)

    def delete(self):
        DistributedObjectAI.delete(self)
