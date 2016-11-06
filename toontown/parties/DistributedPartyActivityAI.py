from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyActivityAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyActivityAI')

    def __init__(self, air, doId, activityP):
        DistributedObjectAI.__init__(self, air)
        self.doId = doId
        x, y, h = activityP[1:]
        self.partyX = PartyUtils.convertDistanceFromPartyGrid(x, 0)
        self.partyY = PartyUtils.convertDistanceFromPartyGrid(y, 1)
        self.partyH = h * PartyGlobals.PartyGridHeadingConverter
        self.toonsActive = []
        self.toonsPlaying = []
        
    def getX(self):
        return self.partyX

    def getY(self):
        return self.partyY

    def getH(self):
        return self.partyH

    def getPartyDoId(self):
        return self.doId
        
    def setToonsPlaying(self):
        pass

    def toonJoinRequest(self):
        pass
        
    def toonExitRequest(self):
        pass

    def toonExitDemand(self):
        pass
        
    def toonReady(self):
        pass

    def joinRequestDenied(self, todo0):
        pass

    def exitRequestDenied(self, todo0):
        pass

    def setToonsPlaying(self, todo0):
        pass

    def setState(self, todo0, todo1):
        pass

    def showJellybeanReward(self, todo0, todo1, todo2):
        pass