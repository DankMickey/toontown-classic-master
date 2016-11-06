from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from time import gmtime, strftime
import base64, os, json
from direct.distributed.MsgTypes import *

class AccountUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountUD')

    # Client agent states:
    ANONYMOUS = 1
    ESTABLISHED = 2

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.accountStore = 'account-store.json'
        self.accountStoreDefault = {
            'Accounts': {
            }
        }

        self.playToken2sender = { }

        # Look in the astron configuration.
        self.databaseId = 4003

    def generate(self):
        DistributedObjectGlobalUD.generate(self)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

    def requestLogin(self, playToken):
        if len(playToken) == 0:
            return None

        self.checkForAccount(base64.b64decode(playToken), self.air.getMsgSender())

    def checkForAccount(self, playToken, sender):
        if not os.path.exists(self.accountStore):
            self.createAccountStoreFile()

        self.playToken2sender[playToken] = sender
        (ret, doId) = self.checkStoreForDoId(playToken)

        if ret == 'success':
            self.updateStoredAccount(playToken, doId)
        else:
            self.createNewAccount(playToken)

    def checkStoreForDoId(self, playToken):
        with open(self.accountStore, 'rb') as accStore:
            accounts = json.loads(accStore.read())
            accStore.close()

        if playToken in accounts['Accounts']:
            return ('success', accounts['Accounts'][playToken])

        return ('failure', 0)

    def createAccountStoreFile(self):
        with open(self.accountStore, 'w+') as accStore:
            accStore.write(json.dumps(self.accountStoreDefault))
            accStore.close()

    def createNewAccount(self, playToken):
        fields = {
            'ACCOUNT_AV_SET': [],
            'pirateAvatars': [], # Uh, do we need this?
            'HOUSE_ID_SET': [],
            'ESTATE_ID': 0,
            'ACCOUNT_AV_SET_DEL': [],
            'CREATED': str(strftime("%Y-%m-%d %H:%M:%S", gmtime())),
            'LAST_LOGIN': str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        }

        self.air.dbInterface.createObject(databaseId=self.databaseId,
                                        dclass=self.air.dclassesByName.get('AccountUD'),
                                        fields=fields,
                                        callback=self._createdNewAccount,
                                        extraArg=playToken)

    def _createdNewAccount(self, doId, playToken):
        with open(self.accountStore, 'rb') as accStore:
            accounts = json.loads(accStore.read())
            accStore.close()

        accounts['Accounts'][playToken] = doId

        with open(self.accountStore, 'r+') as accStore:
            accStore.write(json.dumps(accounts))
            accStore.close()

        self._activateSender(playToken, doId)

    def updateStoredAccount(self, playToken, doId):
        self.air.dbInterface.queryObject(databaseId=self.databaseId,
                                        doId=doId,
                                        callback=self._updateStoredAccount,
                                        dclass=self.air.dclassesByName.get('AccountUD'),
                                        extraArg=playToken)

    def _updateStoredAccount(self, dclass, fields, playToken):
        with open(self.accountStore, 'rb') as accStore:
            accounts = json.loads(accStore.read())
            accStore.close()

        doId = accounts['Accounts'][playToken]
        self.air.dbInterface.updateObject(self.databaseId,
                            doId,
                            self.air.dclassesByName.get('AccountUD'),
                            {'LAST_LOGIN': str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))})

        self._activateSender(playToken, doId)

    def _activateSender(self, playToken, doId):
        target = self.playToken2sender[playToken]

        datagram = PyDatagram()
        datagram.addServerHeader(target, self.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addUint64(doId)
        self.air.send(datagram)

        datagram = PyDatagram()
        datagram.addServerHeader(target, self.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addUint64(doId)
        self.air.send(datagram)

        datagram = PyDatagram()
        datagram.addServerHeader(target, self.air.ourChannel, CLIENTAGENT_SET_STATE)
        datagram.addUint16(self.ESTABLISHED)
        self.air.send(datagram)

        self.sendUpdateToChannel(target, 'loginComplete', [])


    def disable(self):
        DistributedObjectGlobalUD.disable(self)

    def delete(self):
        DistributedObjectGlobalUD.delete(self)
