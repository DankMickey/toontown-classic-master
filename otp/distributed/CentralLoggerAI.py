from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class CentralLoggerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CentralLoggerAI')

    def sendMessage(self, todo0, todo1, todo2, todo3):
        pass