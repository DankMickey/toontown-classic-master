from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from toontown.chat.TTWhiteList import TTWhiteList

class ChatAgentUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("ChatAgentUD")

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
        self.whiteList = TTWhiteList()

    def chatMessage(self, message):
        sender = self.air.getAvatarIdFromSender()
        if sender == 0 or not sender:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(), 'Account sent chat without an avatar', message)
            return

        cleanMessage = message

        self.air.writeServerEvent('chat-said', sender, message, cleanMessage)

        DistributedAvatar = self.air.dclassesByName['DistributedAvatarUD']
        dg = DistributedAvatar.aiFormatUpdate('setTalk', sender, sender, self.air.ourChannel, [0, 0, '', cleanMessage, modifications, 0])
        self.air.send(dg)