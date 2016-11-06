from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from direct.distributed.ClockDelta import *
from pandac.PandaModules import *
import time

class DistributedEstateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEstateAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.estateType = 0
        self.rentalType = 0
        self.clouds = 0
        
        self.decoreData = [ ]

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def getEstateType(self):
        return self.estateType

    def getDawnTime(self):
        return globalClockDelta.getRealNetworkTime(
            bits=32)

    def getDecorData(self):
        return self.decoreData

    def getLastEpochTimeStamp(self):
        return globalClockDelta.getRealNetworkTime(
            bits=32)

    def getRentalTimeStamp(self):
        return globalClockDelta.getRealNetworkTime(
            bits=32)

    def getRentalType(self):
        return self.rentalType

    def setClouds(self, clouds):
        self.clouds = clouds

    def d_setClouds(self, clouds):
        self.sendUpdate('setClouds', [
            clouds])

    def b_setClouds(self, clouds):
        self.setClouds(clouds)
        self.d_setClouds(clouds)

    def getClouds(self):
        return self.clouds

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
