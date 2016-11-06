from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

class WelcomeValleyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('WelcomeValleyManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)
        self.valleyZoneId = self.air.allocateZone(True)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getNewZoneId(self, origZoneId):
        if origZoneId == ToontownGlobals.WelcomeValleyToken:
            # going to welcome valley zone.
            return self.valleyZoneId

        return origZoneId

    def requestZoneIdMessage(self, origZoneId, context):
        self.d_requestZoneIdResponse(self.air.getAvatarIdFromSender(), self.getNewZoneId(origZoneId), context)

    def toonSetZone(self, doId, newZoneId):
        if doId != self.air.getAvatarIdFromSender():
            return # Got an invalid doId.

        do = self.air.doId2do[doId]
        if not do:
            simbase.air.writeServerEvent('suspicious', self.air.getAvatarIdFromSender(), 'a non-existant toon requested requestZoneIdResponse!')
            return

        if do.zoneId == newZoneId:
            # no zone change!
            return

        # this is only used for setting a new zoneId not a parentId!
        self.air.sendSetZone(do, newZoneId)

    def d_requestZoneIdResponse(self, doId, zoneId, context):
        if doId not in self.air.doId2do:
            return # Got a non-existant doId.

        do = self.air.doId2do[doId]
        if not do:
            simbase.air.writeServerEvent('suspicious', self.air.getAvatarIdFromSender(), 'a non-existant toon requested requestZoneIdResponse!')
            return

        # Now send a request zoneId response.
        self.sendUpdateToAvatarId(doId, 'requestZoneIdResponse', [
            zoneId, context])

    def disable(self):
        DistributedObjectAI.disable(self)
        self.air.deallocateZone(self.valleyZoneId, True)

    def delete(self):
        DistributedObjectAI.delete(self)
