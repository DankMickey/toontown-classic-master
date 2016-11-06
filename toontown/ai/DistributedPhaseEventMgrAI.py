from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedPhaseEventMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPhaseEventMgrAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)

    def delete(self):
        DistributedObjectAI.delete(self)
        
    def setNumPhases(self, todo1):
        pass

    def setIsRunning(self, todo1):
        pass

    def setCurPhase(self, todo1):
        pass
        
    def setDates(self, todo1):
        pass