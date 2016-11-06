# File: t (Python 2.4)

from panda3d.core import *
from direct.task import Task
from toontown.hood import ZoneUtil

class ToontownAccess:
    
    def __init__(self):
        self.startupModules = []

    def getModuleList(self):
        return self.startupModules

    
    def initModuleInfo(self):
        self.startupModules = self.getModuleList()
        taskMgr.doMethodLater(300, self.checkModuleInfo, 'moduleListTask')

    
    def delete(self):
        taskMgr.remove('moduleListTask')
        del self.startupModules

    
    def checkModuleInfo(self, task):
        currentModuleList = self.getModuleList()
        newModules = []
        for module in currentModuleList:
            if module not in self.startupModules:
                self.startupModules.insert(0, module)
                newModules.insert(0, module)
                continue
        
        self.sendUpdate('setModuleInfo', [
            newModules])

        return task.again

    
    def getModuleList(self):
        string = ('')
        for module in self.startupModules:
            string += str(module)

        moduleString = string
        moduleList = []
        if moduleString:
            moduleList = moduleString.split(',')
        
        return moduleList

    
    def sendUpdate(self, fieldName, args = [], sendToId = None):
        if base.cr and hasattr(base, 'localAvatar'):
            if not sendToId:
                pass
            dg = base.localAvatar.dclass.clientFormatUpdate(fieldName, base.localAvatar.doId, args)
            base.cr.send(dg)
        

    
    def canAccess(self, zoneId = None):
        if base.cr.isPaid():
            return True
        
        allowed = False
        allowedZones = [
            ToontownGlobals.ToontownCentral,
            ToontownGlobals.MyEstate,
            ToontownGlobals.GoofySpeedway,
            ToontownGlobals.Tutorial]
        specialZones = [
            ToontownGlobals.SellbotLobby]
        if hasattr(base.cr, 'newsManager') and base.cr.newsManager:
            holidayIds = base.cr.newsManager.getHolidayIdList()
            if ToontownGlobals.SELLBOT_NERF_HOLIDAY in holidayIds:
                specialZones.append(ToontownGlobals.SellbotHQ)
            
        
        place = base.cr.playGame.getPlace()
        if zoneId:
            myHoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        else:
            myHoodId = ZoneUtil.getCanonicalHoodId(place.zoneId)
        if hasattr(place, 'id'):
            myHoodId = place.id
        
        if myHoodId in allowedZones:
            allowed = True
        elif zoneId and zoneId in specialZones:
            allowed = True
        
        return allowed

