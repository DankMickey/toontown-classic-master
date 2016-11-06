from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import PartyGlobals, PartyUtils
from direct.directnotify import DirectNotifyGlobal
import time

#Activity Imports
from toontown.parties.DistributedPartyCannonActivityAI import DistributedPartyCannonActivityAI
from toontown.parties.DistributedPartyCannonAI import DistributedPartyCannonAI

class DistributedPartyAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyAI')

    def __init__(self, air, hostId, zoneId, info):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.hostId = hostId
        self.zoneId = zoneId
        self.info = info
        self.activities = []
        self.avIdsAtParty = []
        self.partyState = 0 
        self.hostName = ''
        host = self.air.doId2do.get(self.hostId, None)
        PARTY_TIME_FORMAT = PartyGlobals.PARTY_TIME_FORMAT
        self.startedAt = time.strftime(PARTY_TIME_FORMAT)

        
    def setPartyClockInfo(self): 
        pass
    
    def setInviteeIds(self):
        pass
        
    def getPartyState(self):
        return self.partyState
        
    def b_setPartyState(self, partyState):
        self.partyState = partyState
        self.d_setPartyState(partyState)
        
    def d_setPartyState(self):
        self.sendUpdate('setPartyState', [partyState])
        
    def setPartyInfoTuple(self):
        pass
        
    def getAvIdsAtParty(self):
        return self.avIdsAtParty
        
    def b_setAvIdsAtParty(self, avIds):
        self.avIdsAtParty = avIds
        self.d_setAvIdsAtParty(avIds)
        
    def d_setAvIdsAtParty(self, avIds):
        self.sendUpdate('setAvIdsAtParty', [avIds])
        
    def b_setPartyStartedTime(self, startTime):
        self.startedAt = startTime
        self.d_setPartyStartedTime(startTime)
        
    def d_setPartyStartedTime(self, startTime):
        self.sendUpdate('setPartyStartedTime', [startTime])
    
    def getPartyStartedTime(self):
        return self.startedAt
        
    def b_setHostName(self, hostName):
        self.hostName = hostName
        self.d_setHostName(hostName)
        
    def d_setHostName(self, hostName):
        self.sendUpdate('setHostName', [hostName])
        
    def getHostName(self):
        if host:
            self.hostName = host.getName()
        return self.hostName
        
    def avIdEnteredParty(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId in self.avIdsAtParty:
            #We'll need more then a append but this is good for now.
            self.avIdsAtParty.append(avId)
            
    def avIdExitedParty(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.avIdsAtParty:
            #We'll need more then a remove but this is good for now.
            self.avIdsAtParty.remove(avId)