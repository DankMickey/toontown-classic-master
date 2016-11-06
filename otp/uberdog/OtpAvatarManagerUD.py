from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
from toontown.toon.ToonDNA import ToonDNA
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from cPickle import loads, dumps

class OtpAvatarManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('OtpAvatarManagerUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.databaseId = 4003
        self.pendingNames = { }

    def generate(self):
        DistributedObjectGlobalUD.generate(self)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
    
    def requestAvatarList(self, value):
        sender = self.air.getAccountIdFromChannel()

        self.air.dbInterface.queryObject(databaseId=self.databaseId,
                                        doId=sender,
                                        callback=self._gotAccountFields,
                                        extraArg=sender)

    def _gotAccountFields(self, dclass, fields, sender):
        avatarList = fields['ACCOUNT_AV_SET']

        if len(avatarList) > 0:
            for avatarId in avatarList:
				if avatarId != 0:
					self.getAvatarFields(avatarList, avatarId, sender)

        self.sendUpdateToChannel(sender, 'avatarListResponse', [dumps(avatarList)])

    def getAvatarFields(self, avatarList, avatarId, ownerId):
        pass

    def sendCheckNameTyped(self, avId, nameSet):
        sender = self.air.getAccountIdFromChannel()
        # TODO: Check name to make sure its approiate!

        if int(avId) == 0:
            pass # TODO

        pendingname = ''
        approvedname = '' + nameSet
        rejectedname = ''

        self.pendingNames[sender] = approvedname

        self.sendUpdateToChannel(sender, 'sendCheckNameTypedResp', [
            str(avId), 
            pendingname, 
            approvedname, 
            rejectedname])

    def sendRequestCreateAvatar(self, avDNA, avName, avPosition):
        sender = self.air.getAccountIdFromChannel()

        toonDNA = ToonDNA()
        toonDNA.makeFromNetString(avDNA)

        if self.pendingNames[sender]:
            avName = self.pendingNames[sender]
            del self.pendingNames[sender]

        fields = {
            'setName': (avName,),
            'setDNAString': (avDNA,),
            'setPositionIndex': (str(avPosition),),
            'setDISLid': (sender,)
        }

        self.air.dbInterface.createObject(databaseId=self.databaseId,
                                        dclass=self.air.dclassesByName.get('DistributedToonUD'),
                                        fields=fields,
                                        callback=self._createdAvatar,
                                        extraArg=sender)

    def _createdAvatar(self, doId, sender):
        self.air.dbInterface.queryObject(databaseId=self.databaseId,
                                        doId=sender,
                                        callback=self._updateAccountFields,
                                        extraArg=[doId, sender])

    def _updateAccountFields(self, dclass, fields, args):
        (doId, sender) = args

        newFields = fields['ACCOUNT_AV_SET']
        newFields.append(doId)

        self.air.dbInterface.updateObject(self.databaseId,
                                        sender,
                                        self.air.dclassesByName.get('AccountUD'),
                                        {'ACCOUNT_AV_SET': newFields})

        self.sendUpdateToChannel(sender, 'sendRequestCreateAvatarResp', [doId])

    def requestChooseAvatar(self, avId):
        avatarIdFromChannel = self.air.getAvatarIdFromChannelCode()
        sender = self.air.getAccountIdFromChannel()

        print avId

        self.air.sendActivate(avId, 0, 0, self.air.dclassesByName.get('DistributedToonUD'))
        
        datagram = PyDatagram()
        datagram.addServerHeader(avId, self.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addUint64(sender)
        self.air.send(datagram)

        datagram = PyDatagram()
        datagram.addServerHeader(sender, self.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addUint64(sender)
        self.air.send(datagram)

        dg = PyDatagram()
        dg.addServerHeader(avId, self.air.ourChannel, STATESERVER_OBJECT_SET_OWNER)
        dg.addChannel(sender)
        self.air.send(dg)

    def disable(self):
        DistributedObjectGlobalUD.disable(self)

    def delete(self):
        DistributedObjectGlobalUD.delete(self)
