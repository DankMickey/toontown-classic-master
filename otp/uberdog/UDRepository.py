from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.distributed.AstronInternalRepository import AstronInternalRepository
from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed import OtpDoGlobals

class UDRepository(AstronInternalRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('UDRepository')
    GameGlobalsId = OtpDoGlobals.OTP_DO_ID_TOONTOWN
    dbId = 4003

    def __init__(self, baseChannel, serverId, dcFileNames, dcSuffix='UD'):
        AstronInternalRepository.__init__(self, baseChannel=baseChannel, serverId=serverId, dcFileNames=dcFileNames, dcSuffix=dcSuffix)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender() >> 32) & 0xFFFFFFFF

    def handleConnected(self):
        AstronInternalRepository.handleConnected(self)
        self.createRootObject()

    def createRootObject(self):
        self.directory = DistributedDirectoryAI(self)
        self.directory.generateWithRequiredAndId(doId=self.getGameDoId(), 
                                                parentId=0, 
                                                zoneId=0)
        self.createGlobals()

    def createGlobals(self):
        self.csm = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CLIENT_SERVICES_MANAGER, 'ClientServicesManager')
        self.centralLogger = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CENTRAL_LOGGER, 'CentralLogger')
        self.deliveryManager = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_TOONTOWN_DELIVERY_MANAGER, 'DistributedDeliveryManager')
        self.chatAgent = self.generateGlobalObject(OtpDoGlobals.OTP_DO_ID_CHAT_MANAGER, 'ChatAgent')

    def lostConnection(self):
        AstronInternalRepository.lostConnection(self)
