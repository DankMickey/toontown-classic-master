from toontown.fishing import FishGlobals
from toontown.fishing import FishingTargetGlobals
from toontown.fishing.FishBase import FishBase
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.fishing import DistributedFishingPondAI
from toontown.fishing import DistributedFishingTargetAI
from toontown.safezone import DistributedFishingSpotAI

class FishManagerAI:

    def __init__(self, air):
        self.air = air
        self.doId2do = {}
        self.pond = None
    
    def cleanup(self):
        for pondDoId in self.doId2do:
            self.doId2do[pondDoId].delete()
            del self.doId2do[pondDoId]
        
        for fishingSpot in self.doId2do:
            self.doId2do[fishingSpot].delete()
            del self.doId2do[fishingSpot]
        
    def createPondInZone(self, zoneId):
        for pondDoId in self.doId2do:
            if self.doId2do[pondDoId].getArea() == zoneId:
                self.air.notify.warning('Tried to generate a pond but an existing pond is already generated in zone: %d with doId: %d' % (zoneId, self.doId2do[pondDoId].getDoId()))
                return
        
        pond = DistributedFishingPondAI.DistributedFishingPondAI(self.air, zoneId)
        pond.generateWithRequired(zoneId)
        self.doId2do[pond.getDoId()] = pond
        self.pond = pond
        
        for i in range(FishingTargetGlobals.getNumTargets(zoneId)):
            fishingTarget = DistributedFishingTargetAI.DistributedFishingTargetAI(self.air)
            fishingTarget.setPondDoId(pond.doId)
            fishingTarget.generateWithRequired(pond.zoneId)
        
                        
    def createSpotsInZone(self, zoneId, dnaData):
        for zone in self.air.zoneTable[zoneId]:
            if ZoneUtil.isCogHQZone(zone):
                return
            if zone[0] == ToontownGlobals.OutdoorZone:
                return
            if zone[0] == ToontownGlobals.GoofySpeedway:
                return
            if not dnaData:
                print(':FishManagerAI: Failed to find dnaData for zone %d!' %zone[0])
                break
            for i in range(0, 4):
                for x in range(dnaData.getNumChildren()):
                    posSpot = dnaData.at(x)
                    if 'fishing_spot_' in posSpot.getName():
                        print(':FishManagerAI: Creating Fishing Spot at %d!' %zone[0])
                        fishingSpot = DistributedFishingSpotAI.DistributedFishingSpotAI(self.air)
                        x, y, z = posSpot.getPos()
                        h, p, r = posSpot.getHpr()
                        fishingSpot.generateWithRequired(self.pond.zoneId)
                        fishingSpot.doId = fishingSpot.getDoId()
                        fishingSpot.b_setPosHpr(x, y, z, h, p, r)
                        fishingSpot.b_setPondDoId(self.pond.doId)
                        self.doId2do[fishingSpot.getDoId()] = fishingSpot