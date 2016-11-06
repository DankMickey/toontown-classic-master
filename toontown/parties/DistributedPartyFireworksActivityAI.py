from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyFireworksActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyFireworksActivityAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def setEventId(self):
        pass
        
    def setShowStyle(self):
        pass