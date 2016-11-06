from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyCannonActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyCannonActivityAI')

    def __init__(self, air, parent, activityP):
        DistributedPartyActivityAI.__init__(self, air, parent, activityP)
        self.air = air
        self.cloudColors = {}
        self.cloudsHit = {}

    def setMovie(self):
        pass
        
    def setLanded(self):
        pass
        
    def setCannonWillFire(self):
        pass
        
    def cloudsColorRequest(self):
        avId = self.air.getAvatarIdFromSender()
        self.d_cloudsColorResponse(avId)
        
    def d_cloudsColorResponse(self, avId):
        self.sendUpdateToAvatarId(avId, 'cloudsColorResponse', [self.cloudColors.values()])
        
    def requestCloudHit(self, cloudId, r, g, b):
        avId = self.air.getAvatarIdFromSender()
        if not avId in self.toonsPlaying:
            return
        self.cloudColors[cloudId] = [cloudId, r, g, b]
        self.d_setCloudHit(avId, cloudId, r, g, b)
        
    def d_setCloudHit(self, avId, cloudId, r, g, b):
        self.sendUpdate('setCloudHit', [cloudId, r, g, b])
        self.cloudsHit[avId] += 1
        
    def setToonTrajectoryAi(self, launchTime, x, y, z, h, p, r, vx, vy, vz):
        self.sendUpdate('setToonTrajectory', [self.air.getAvatarIdFromSender(), launchTime, x, y, z, h, p, r, vx, vy, vz])
        
    def updateToonTrajectoryStartVelAi(self):
        pass
 