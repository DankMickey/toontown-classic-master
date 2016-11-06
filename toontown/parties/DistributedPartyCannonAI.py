from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class DistributedPartyCannonAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyCannonAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.activityId = 0
        self.posHpr = [0, 0, 0, 0, 0, 0]
        self.avId = 0

    def setActivityDoId(self, actId):
        self.activityId = activityId

    def getActivityDoId(self):
        return self.activityId
        
    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = [x, y, z, h, p, r]

    def getPosHpr(self):
        return self.posHpr
        
    def requestEnter(self):
        if not self.avId or self.avId == 0:
            self.avId = self.air.getAvatarIdFromSender()
            self.setMovie(PartyGlobals.CANNON_MOVIE_LOAD, self.avId)
        
    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId == avId:
            self.d_setCannonExit(avId)
            self.avId = 0
        
    def setMovie(self, movie, avId):
        self.sendUpdate('setMovie', [movie, avId])
        
    def setCannonPosition(self, rot, angle):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.d_updateCannonPosition(avId, rot, angle)
        
    def setCannonLit(self):
        pass
    
    def setFired(self):
        pass
        
    def setLanded(self):
        pass
        
    def d_updateCannonPosition(self, avId, rot, angle):
        if avId == self.avId:
            self.sendUpdate('updateCannonPosition', [avId, rot, angle])
        
    def d_setCannonExit(self, avId):
        if self.avId == avId:
            self.sendUpdate('setCannonExit', [avId])
        
    def setTimeout(self):
        pass