from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from otp.level.LevelSpec import LevelSpec
from direct.distributed.ClockDelta import *
from toontown.coghq.FactoryBase import FactoryBase
from toontown.toonbase import ToontownGlobals
from toontown.coghq import FactorySpecs

class DistributedLevelAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLevelAI')

    def __init__(self, air, zoneId, entranceId, avIds):
        DistributedObjectAI.__init__(self, air)
        FactoryBase.__init__(self)

        self.levelZoneId = zoneId
        self.entranceId = entranceId
        self.avIdList = avIds

    def generate(self, factorySpec=None):
        DistributedObjectAI.generate(self)

        if not factorySpec:
            return
        
        self.factoryId = simbase.factory.getFactoryId()
        self.factorySpec = factorySpec
        self.zoneIds = self.factorySpec.getAllEntIdsFromAllScenarios()
        self.setFactoryId(self.factoryId)
        self.d_setZoneIds(self.zoneIds)
        self.d_setStartTimestamp(self.getTimestamp())
        self.factoryFilename = self.factorySpec.getFilename()
        FactorySpecs.CogSpecModules[self.factoryId] = self.factoryFilename

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def setFactoryId(self, factoryId):
        FactoryBase.setFactoryId(self, factoryId)

    def getTimestamp(self):
        return globalClockDelta.getRealNetworkTime(bits=32)

    def getLevelZoneId(self):
        return self.levelZoneId

    def getPlayerIds(self):
        return self.avIdList

    def getEntranceId(self):
        return self.entranceId

    def d_setZoneIds(self, zoneIds):
        self.sendUpdate('setZoneIds', [
            zoneIds])

    def d_setStartTimestamp(self, timestamp):
        self.sendUpdate('setStartTimestamp', [
            timestamp])

    def setOuch(self, penalty):
        pass

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
