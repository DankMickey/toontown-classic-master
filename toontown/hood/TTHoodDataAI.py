# File: T (Python 2.4)

from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.safezone import DistributedTrolleyAI
from toontown.safezone import TTTreasurePlannerAI
from toontown.classicchars import DistributedMickeyAI
from toontown.building import DistributedDoorAI
from toontown.building import DoorTypes
from toontown.safezone import ButterflyGlobals
from direct.task import Task

class TTHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTHoodDataAI')
    
    def __init__(self, air, zoneId = None):
        hoodId = ToontownGlobals.ToontownCentral
        if zoneId == None:
            zoneId = hoodId
        
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)

    
    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.addDistObj(trolley)
        self.trolley = trolley
        self.treasurePlanner = TTTreasurePlannerAI.TTTreasurePlannerAI(self.zoneId)
        self.treasurePlanner.start()
        self.classicChar = DistributedMickeyAI.DistributedMickeyAI(self.air)
        self.classicChar.generateWithRequired(self.zoneId)
        self.classicChar.start()
        self.addDistObj(self.classicChar)
        self.createButterflies(ButterflyGlobals.TTC)
        if simbase.blinkTrolley:
            taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        
        '''destinationZone = ToontownGlobals.ToontownCentral
        extDoor0 = DistributedDoorAI.DistributedDoorAI(self.air, destinationZone, DoorTypes.EXT_STANDARD, doorIndex = 2, lockValue = 0, swing = 3)
        extDoorList = [extDoor0]
        
        intDoor0 = DistributedDoorAI.DistributedDoorAI(self.air, destinationZone, DoorTypes.INT_STANDARD, doorIndex = 2, lockValue = 0, swing = 3)
        intDoor0.setOtherDoor(extDoor0)
        intDoor0.zoneId = ToontownGlobals.ToonHall
        for extDoor in extDoorList:
            extDoor.setOtherDoor(intDoor0)
            extDoor.zoneId = ToontownGlobals.ToontownCentral
            extDoor.generateWithRequired(ToontownGlobals.ToontownCentral)
            extDoor.sendUpdate('setDoorIndex', [
                extDoor.getDoorIndex()])
            self.addDistObj(extDoor)
        
        intDoor0.generateWithRequired(ToontownGlobals.ToonHall)
        intDoor0.sendUpdate('setDoorIndex', [
            intDoor0.getDoorIndex()])
        self.addDistObj(intDoor0)'''
        
        messenger.send('TTHoodSpawned', [
            self])

    
    def shutdown(self):
        HoodDataAI.HoodDataAI.shutdown(self)
        messenger.send('TTHoodDestroyed', [
            self])

    
    def _deleteTrolley(self, task):
        self.trolley.requestDelete()
        taskMgr.doMethodLater(0.5, self._createTrolley, 'createTrolley')
        return Task.done

    
    def _createTrolley(self, task):
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.trolley = trolley
        taskMgr.doMethodLater(0.5, self._deleteTrolley, 'deleteTrolley')
        return Task.done


