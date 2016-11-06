from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyJukeboxActivityBaseAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyJukeboxActivityBaseAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        
    def setNextSong(self):
        pass
        
    def setSongPlaying(self):
        pass
        
    def queuedSongsRequest(self):
        pass
        
    def queuedSongsResponse(self):
        pass
        
    def setSongInQueue(self):
        pass

    def moveHostSongToTopRequest(self):
        pass
        
    def moveHostSongToTop(self):
        pass