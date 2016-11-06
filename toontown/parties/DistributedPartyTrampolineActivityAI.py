from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyTrampolineActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyTrampolineActivityAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def awardBeans(self):
        pass
        
    def setBestHeightInfo(self):
        pass
        
    def reportHeightInformation(self):
        pass
        
    def leaveTrampoline(self):
        pass
        
    def requestAnim(self):
        pass
        
    def requestAnimEcho(self):
        pass
        
    def removeBeans(self):
        pass
        
    def removeBeansEcho(self):
        pass