from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals

class ChatAgent(DistributedObjectGlobal):
    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def delete(self):
        self.ignoreAll()
        self.cr.chatManager = None
        DistributedObjectGlobal.delete(self)

    def sendChatMessage(self, message):
        self.sendUpdate('chatMessage', [message])