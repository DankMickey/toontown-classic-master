from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal

class ObjectServerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectServerUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def generate(self):
        DistributedObjectGlobalUD.generate(self)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

    def disable(self):
        DistributedObjectGlobalUD.disable(self)

    def delete(self):
        DistributedObjectGlobalUD.delete(self)
