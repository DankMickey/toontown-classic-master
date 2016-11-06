from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedPartyGateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyGateAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def getZoneId(self):
        return self.zoneId

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getPartyList(self, sender):
        avId = self.air.getAvatarIdFromSender()
        if avId not in self.air.doId2do:
            return

        self.d_listAllPublicParties(avId,
            self.air.partyManager.getPartyList())

    def d_listAllPublicParties(self, avId, publicPartyInfo):
        self.sendUpdateToAvatarId(avId, 'listAllPublicParties', [
            publicPartyInfo])

    def partyChoiceRequest(self, avId, doneStatus0, doneStatus1):
        pass

    def d_partyRequestDenied(self, reason):
        pass

    def d_setParty(self, publicPartyInfo):
        pass

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
