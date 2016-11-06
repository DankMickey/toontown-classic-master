from toontown.safezone.DistributedPartyGateAI import DistributedPartyGateAI
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

class PartyManagerAI:

    def __init__(self, air):
        self.air = air
        self.partyGates = { }

    def createPartyGateInZone(self, zoneId):
        for partyGateId in self.partyGates:
            if self.partyGates[partyGateId].getZoneId() == zoneId:
                return

        if ZoneUtil.isCogHQZone(zoneId):
            return

        if zoneId == ToontownGlobals.OutdoorZone:
            return
            
        if zoneId == ToontownGlobals.GoofySpeedway:
            return
            
        if zoneId == ToontownGlobals.GolfZone:
            return
            
        if zoneId == ToontownGlobals.Tutorial:
            return
            
        if zoneId == ToontownGlobals.PartyHood:
            return
        
        partyGate = DistributedPartyGateAI(self.air)
        partyGate.generateWithRequired(zoneId)
        self.partyGates[partyGate.doId] = partyGate