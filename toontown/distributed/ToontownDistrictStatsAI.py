from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class ToontownDistrictStatsAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDistrictStatsAI')

    def __init__(self, air, districtId):
        DistributedObjectAI.__init__(self, air)
        self.districtId = districtId
        self.avatarCount = 0
        self.newAvatarCount = 0

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def gettoontownDistrictId(self):
        return self.districtId

    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

    def d_setAvatarCount(self, avatarCount):
        self.sendUpdate('setAvatarCount', [
            avatarCount])

    def b_setAvatarCount(self, avatarCount):
        self.setAvatarCount(avatarCount)
        self.d_setAvatarCount(avatarCount)

    def getAvatarCount(self):
        return self.avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    def d_setNewAvatarCount(self, newAvatarCount):
        self.sendUpdate('setNewAvatarCount', [
            newAvatarCount])

    def b_setNewAvatarCount(self, newAvatarCount):
        self.setNewAvatarCount(newAvatarCount)
        self.d_setNewAvatarCount(newAvatarCount)

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def setStats(self, avatarCount, newAvatarCount):
        self.b_setAvatarCount(avatarCount)
        self.b_setNewAvatarCount(newAvatarCount)

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)