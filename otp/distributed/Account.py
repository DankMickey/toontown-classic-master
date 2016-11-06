# File: o (Python 2.4)

from direct.distributed import DistributedObjectGlobal
import base64

class Account(DistributedObjectGlobal.DistributedObjectGlobal):
    
    def __init__(self, cr):
        DistributedObjectGlobal.DistributedObjectGlobal.__init__(self, cr)
        self.doneEvent = ''

    def setDoneEvent(self, doneEvent):
        self.doneEvent = doneEvent

    def requestLogin(self, playToken):
        if len(playToken) == 0:
            return None

        self.sendUpdate('requestLogin', [base64.b64encode(playToken)])

    def loginComplete(self):
        messenger.send(self.doneEvent, [{'mode': 'success'}])


