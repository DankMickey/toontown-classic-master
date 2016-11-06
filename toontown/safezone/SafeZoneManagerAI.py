from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class SafeZoneManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SafeZoneManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.healFrequency = 30.0
        self.doId2do = { }

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def _getSenderDo(self):
        sender = self.air.getAvatarIdFromSender()
        if sender not in self.air.doId2do:
            return None

        return self.air.doId2do[sender]

    def enterSafeZone(self):
        do = self._getSenderDo()
        if not do:
            simbase.air.writeServerEvent('suspicious', self.air.getAvatarIdFromSender(), 'a non-existant toon requested enterSafeZone!')
            return

        maxHp = do.getMaxHp()
        if do.getHp() < maxHp:
            if do.getDoId() not in self.doId2do.keys():
                self.doId2do[do.getDoId()] = do
            
            do.startToonUp(self.healFrequency)

    def exitSafeZone(self):
        do = self._getSenderDo()
        if not do:
            simbase.air.writeServerEvent('suspicious', self.air.getAvatarIdFromSender(), 'a non-existant toon requested exitSafeZone!')
            return

        if do.getDoId() in self.doId2do.keys():
            toon = self.doId2do[do.getDoId()]
            if toon != None:
                toon.stopToonUp()
            
            del self.doId2do[do.getDoId()]

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)




