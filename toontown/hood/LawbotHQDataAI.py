from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.coghq import DistributedLawOfficeElevatorExtAI
from toontown.building import DistributedCJElevatorAI
from toontown.suit import DistributedLawbotBossAI
from toontown.building import FADoorCodes
from toontown.building import DistributedBoardingPartyAI

class LawbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('LawbotHqDataAI')
    
    def __init__(self, air, zoneId = None):
        hoodId = ToontownGlobals.LawbotHQ
        if zoneId == None:
            zoneId = hoodId
        
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        
    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        mins = ToontownGlobals.FactoryLaffMinimums[1]
        
        self.testElev0 = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.officeMgr, ToontownGlobals.LawbotStageIntA, 0, antiShuffle = 0, minLaff = mins[0])
        self.testElev0.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
        self.addDistObj(self.testElev0)
        
        self.testElev1 = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.officeMgr, ToontownGlobals.LawbotStageIntB, 1, antiShuffle = 0, minLaff = mins[1])
        self.testElev1.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
        self.addDistObj(self.testElev1)
        
        self.testElev2 = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.officeMgr, ToontownGlobals.LawbotStageIntC, 2, antiShuffle = 0, minLaff = mins[2])
        self.testElev2.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
        self.addDistObj(self.testElev2)
        
        self.testElev3 = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.officeMgr, ToontownGlobals.LawbotStageIntD, 3, antiShuffle = 0, minLaff = mins[2])
        self.testElev3.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
        self.addDistObj(self.testElev3)
        
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedLawbotBossAI.DistributedLawbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedCJElevatorAI.DistributedCJElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.LawbotLobby, antiShuffle = 1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyElevator)
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [
                self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.LawbotLobby)
            
        destinationZone = ToontownGlobals.LawbotLobby
        extDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 1, DoorTypes.EXT_COGHQ, destinationZone, doorIndex = 1, lockValue = FADoorCodes.LB_DISGUISE_INCOMPLETE)
        extDoor1 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, ToontownGlobals.LawbotOfficeExt, doorIndex = 0, lockValue = FADoorCodes.LB_DISGUISE_INCOMPLETE)
        extDoorList = [
            extDoor0,
            extDoor1]
        intDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 1, DoorTypes.INT_COGHQ, ToontownGlobals.LawbotHQ, doorIndex = 1)
        intDoor0.setOtherDoor(extDoor0)
        intDoor0.zoneId = ToontownGlobals.LawbotLobby
        intDoor1 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, ToontownGlobals.LawbotHQ, doorIndex = 0)
        intDoor1.setOtherDoor(extDoor1)
        intDoor1.zoneId = ToontownGlobals.LawbotOfficeExt
        
        for extDoor in extDoorList:
            extDoor.setOtherDoor(intDoor0)
            extDoor.zoneId = ToontownGlobals.LawbotHQ
            extDoor.generateWithRequired(ToontownGlobals.LawbotHQ)
            extDoor.sendUpdate('setDoorIndex', [
                extDoor.getDoorIndex()])
            self.addDistObj(extDoor)
        
        intDoor0.generateWithRequired(ToontownGlobals.LawbotLobby)
        intDoor0.sendUpdate('setDoorIndex', [
            intDoor0.getDoorIndex()])
        self.addDistObj(intDoor0)
        
        intDoor1.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
        intDoor1.sendUpdate('setDoorIndex', [
            intDoor1.getDoorIndex()])
        self.addDistObj(intDoor1)