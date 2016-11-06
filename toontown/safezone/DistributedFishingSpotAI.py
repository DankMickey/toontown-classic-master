from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.fishing import FishGlobals

class DistributedFishingSpotAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpotAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.pondDoId = 0
        self.posHpr = None
        self.pond = None
        self.x = 0
        self.y = 0
        self.z = 0
        self.h = 0
        self.p = 0
        self.r = 0
        #self.doId = self.getDoId()
        
        self.spotOccupied = False
        self.spotOccupier = 0

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        
    def setPondDoId(self, pondId):
    	self.pondDoId = pondId
            
    def d_setPondDoId(self, pondId):
        self.sendUpdate('setPondDoId', [pondId])
        
    def b_setPondDoId(self, pondId):
        self.setPondDoId(pondId)
        self.d_setPondDoId(pondId)
        
    def getPondDoId(self):
    	return self.pondDoId
        
    def getArea(self):
        self.pond = self.air.doId2do[self.pondDoId]
        return self.pond.getArea()
    
    def setPosHpr(self, x, y, z, h, p, r):
        self.x = x
        self.y = y
        self.z = z
        self.h = h
        self.p = p
        self.r = r
    	self.posHpr = [x, y, z, h, p, r]
        
    def d_setPosHpr(self, x, y, z, h, p, r):
        if __debug__:
            print(':FishManagerAI: Setting xyz to %x, %x, %x for spot!' % (x, y, z,))
        self.sendUpdate('setPosHpr', [x, y, z, h, p, r])
        
    def b_setPosHpr(self, x, y, z, h, p, r):
        if x <= 0 and y <= 0 and z <= 0:
            x = -120
            y = -120
            z = -120
        self.d_setPosHpr(x, y, z, h, p, r)
        self.setPosHpr(x, y, z, h, p, r)
    
    def getPosHpr(self):
    	return [self.x, self.y, self.z, self.h, self.p, self.r]
    
    def _checkSender(self):
    	avatarId = self.air.getAvatarIdFromSender()
    	
    	if avatarId not in self.air.doId2do.keys():
    		return None
    	
    	return avatarId
    
    def requestEnter(self):
    	avatarId = self._checkSender()
    	if not avatarId:
    		return
    	
    	if not self.spotOccupied:
            self.b_setOccupied(avatarId, True)
            self.d_setMovie(FishGlobals.EnterMovie, 0, 0, 0, 0, 0, 0)
    	else:
    		self.rejectEnter(avatarId)
    
    def rejectEnter(self, avatarId):
    	self.sendUpdateToAvatarId(avatarId, 'rejectEnter', [
    		])
    
    def requestExit(self):
    	avatarId = self._checkSender()
    	if not avatarId:
    		return
    	
    	if self.spotOccupied:
            self.b_setOccupied(0, False)
            self.d_setMovie(FishGlobals.ExitMovie, 0, 0, 0, 0, 0, 0)
    
    def setOccupied(self, avatarId, isOccupied):
    	self.spotOccupied = isOccupied
    	self.spotOccupier = avatarId
        
    def d_setMovie(self, mode, code, genus, species, weight, p, h):
        self.sendUpdate('setMovie', [mode, code, genus, species, weight, p, h])
    
    def d_setOccupied(self, avatarId):
    	self.sendUpdate('setOccupied', [
    		avatarId])
    
    def b_setOccupied(self, avatarId, isOccupied):
    	self.setOccupied(avatarId, isOccupied)
    	self.d_setOccupied(avatarId)

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
