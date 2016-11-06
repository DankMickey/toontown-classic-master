from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.ai import DistributedBlackCatMgrAI
from toontown.building import FADoorCodes
from toontown.building.HQBuildingAI import HQBuildingAI
from toontown.quest import Quests
from toontown.suit.DistributedTutorialSuitAI import DistributedTutorialSuitAI
from toontown.toon import NPCToons
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import ToontownGlobals
from toontown.building.DistributedTutorialInteriorAI import DistributedTutorialInteriorAI
from toontown.dnaparser.DNAParser import *
from toontown.building.DistributedBuildingMgrAI import DistributedBuildingMgrAI
from toontown.building import FADoorCodes, DoorTypes
from toontown.building.DistributedDoorAI import DistributedDoorAI

class TutorialManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def requestTutorial(self):
        self.generateTutorial()
        
    def rejectTutorial(self):
        pass

    def loadTutorialDoors(self, branchZone, streetZone, shopZone, hqZone):
        self.air.dnaStoreMap[branchZone] = DNAStorage()
        self.air.loadDNAFileAI(self.air.dnaStoreMap[branchZone], 'phase_3.5/dna/tutorial_street.dna')

        self.outsideDoor0 = DistributedDoorAI(self.air, 2, DoorTypes.EXT_STANDARD, doorIndex = 1)
        self.outsideDoor1 = DistributedDoorAI(self.air, 2, DoorTypes.EXT_STANDARD, doorIndex = 2)
        self.insideDoor0 = DistributedDoorAI(self.air, 1, DoorTypes.INT_STANDARD, doorIndex = 1)
        self.insideDoor1 = DistributedDoorAI(self.air, 1, DoorTypes.INT_STANDARD, doorIndex = 2)
        self.outsideDoor0.setOtherDoor(self.insideDoor0)
        self.outsideDoor1.setOtherDoor(self.insideDoor1)
        self.insideDoor0.setOtherDoor(self.outsideDoor0)
        self.insideDoor1.setOtherDoor(self.outsideDoor1)
        self.outsideDoor0.zoneId = streetZone
        self.outsideDoor1.zoneId = streetZone
        self.insideDoor0.zoneId = shopZone
        self.insideDoor1.zoneId = shopZone
        self.outsideDoor0.generateWithRequired(streetZone)
        self.outsideDoor1.generateWithRequired(streetZone)
        self.insideDoor0.generateWithRequired(shopZone)
        self.insideDoor1.generateWithRequired(shopZone)
        self.outsideDoor0.sendUpdate('setDoorIndex', [
            self.outsideDoor0.getDoorIndex()])
        self.outsideDoor1.sendUpdate('setDoorIndex', [
            self.outsideDoor1.getDoorIndex()])
        self.insideDoor0.sendUpdate('setDoorIndex', [
            self.insideDoor0.getDoorIndex()])
        self.insideDoor1.sendUpdate('setDoorIndex', [
            self.insideDoor1.getDoorIndex()])

    def generateTutorial(self):
        (branchZone, streetZone, shopZone, hqZone) = (ToontownGlobals.Tutorial, self.air.allocateZone(), self.air.allocateZone(), self.air.allocateZone())

        self.shopInterior = DistributedTutorialInteriorAI(self.air, shopZone, 1, 0)
        self.shopInterior.generateWithRequired(shopZone)

        self.loadTutorialDoors(branchZone, streetZone, shopZone, hqZone)
        avId = self.air.getAvatarIdFromSender()
        self.d_enterTutorial(avId, branchZone, streetZone, shopZone, hqZone)

    def d_enterTutorial(self, avId, branchZone, streetZone, shopZone, hqZone):
        self.sendUpdateToAvatarId(avId, 'enterTutorial', [
            branchZone, 
            streetZone, 
            shopZone, 
            hqZone])

    def requestSkipTutorial(self):
        avId = self.air.getAvatarIdFromSender()
        self.d_skipTutorialResponse(avId, 1)

        def handleTutorialSkipped(av):
            av.b_setTutorialAck(1)
            av.b_setQuests([[110, 1, 1000, 100, 1]])
            av.b_setQuestHistory([101])
            av.b_setRewardHistory(1, [])

        self.accept('generate-%d' % avId, handleTutorialSkipped)

    def d_skipTutorialResponse(self, avId, allOk):
        self.sendUpdateToAvatarId(avId, 'skipTutorialResponse', [
            allOk])

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)