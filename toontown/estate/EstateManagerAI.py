from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.estate.DistributedEstateAI import DistributedEstateAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals

class EstateManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('EstateManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)
        self.zone2owner = { }
        self.owner2zone = { }

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def d_startAprilFools(self, avatarId):
        self.sendUpdateToAvatarId(avatarId, 'startAprilFools', [
            ])

    def d_stopAprilFools(self, avatarId):
        self.sendUpdateToAvatarId(avatarId, 'stopAprilFools', [
            ])

    def getOwnerFromZone(self, zoneId):
        if zoneId not in self.zone2owner:
            return None

        return self.zone2owner[zoneId]

    def getEstateZones(self, avId):
        if avId not in self.owner2zone:
            return None

        return [self.owner2zone[avId]]

    def getEstateZone(self, sender, name):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.air.doId2do:
            return

        if avId in self.owner2zone:
            return

        estateZone = self.air.allocateZone()
        self.d_setEstateZone(avId, estateZone)

        self.zone2owner[estateZone] = avId
        self.owner2zone[avId] = estateZone

        # generate estate objects.
        self.generateEstateZone(estateZone)

        if simbase.air.wantAprilFools:
            self.d_startAprilFools(avId)

    def generateEstateZone(self, estateZone):
        self.estate = DistributedEstateAI(self.air)
        self.estate.generateWithRequired(estateZone)
        
    def exitEstate(self):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.air.doId2do:
            return
        
        if avId not in self.owner2zone:
            return

        self.air.deallocateZone(self.owner2zone[avId])

        del self.zone2owner[self.owner2zone[avId]]
        del self.owner2zone[avId]

        if simbase.air.wantAprilFools:
            self.d_stopAprilFools(avId)

    def d_setEstateZone(self, ownerId, zoneId):
        self.sendUpdateToAvatarId(ownerId, 'setEstateZone', [
            ownerId, zoneId])

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
