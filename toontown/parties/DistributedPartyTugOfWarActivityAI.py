from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyTugOfWarActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyTugOfWarActivityAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def reportKeyRateForce(self):
        pass
        
    def reportFallIn(self):
        pass
        
    def setToonsPlaying(self):
        pass
        
    def updateToonKeyRate(self):
        pass
        
    def updateToonPositions(self):
        pass