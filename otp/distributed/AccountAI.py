from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class AccountAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
