# File: t (Python 2.4)

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
import MintInterior
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import CashbotHQExterior
import CashbotHQBossBattle
from pandac.PandaModules import DecalEffect

class CashbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotCogHQLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('mintInterior', self.enterMintInterior, self.exitMintInterior, [
            'quietZone',
            'cogHQExterior']))
        for stateName in [
            'start',
            'cogHQExterior',
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('mintInterior')
        
        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.mid'
        self.cogHQExteriorModelPath = 'phase_10/models/cogHQ/CashBotShippingStation'
        self.cogHQLobbyModelPath = 'phase_10/models/cogHQ/VaultLobby'
        self.geom = None

    
    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadCashbotHQAnims()

    
    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)

    
    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.CashbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ddLinkTunnel = self.geom.find('**/LinkTunnel1')
            ddLinkTunnel.setName('linktunnel_dl_9252_DNARoot')
            locator = self.geom.find('**/sign_origin')
            backgroundGeom = self.geom.find('**/EntranceFrameFront')
            backgroundGeom.node().setEffect(DecalEffect.make())
            signText = DirectGui.OnscreenText(text = TTLocalizer.DonaldsDreamland[-1], font = ToontownGlobals.getSuitFont(), scale = 3, fg = (0.87, 0.87, 0.87, 1), mayChange = False, parent = backgroundGeom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)
            #Doors
            doors = self.geom.find('**/CFODoor1:CFODoor')
            door0 = doors.find('**/leftDoor/+GeomNode')
            door1 = doors.find('**/rightDoor/+GeomNode')
            door0.node().setEffect(DecalEffect.make())
            door1.node().setEffect(DecalEffect.make())
            doorFrame = doors.find('**/doorFrame')
            doorFrameHoleLeftGeom = doors.find('**/doorFrameHoleLeft/+GeomNode')
            doorFrameHoleRightGeom = doors.find('**/doorFrameHoleRight/+GeomNode')
            doorFrameHoleLeft = doors.find('**/doorFrameHoleLeft')
            doorFrameHoleRight = doors.find('**/doorFrameHoleRight')
            for doorHoleGeom in [doorFrameHoleLeftGeom, doorFrameHoleRightGeom]:
                doorHoleGeom.node().setEffect(DecalEffect.make())
            for doorHole in [doorFrameHoleLeft, doorFrameHoleRight]:
                doorHole.setPos(0, -0.0083, 0)
                #doorHole.hide()
            '''blackDoor = self.geom.find('**/blackDoor/+GeomNode')
            blackDoor.node().setEffect(DecalEffect.make())
            blackDoor.hide()'''
            doorFrame.node().setEffect(DecalEffect.make())
            #Logos
            logos1 = self.geom
            #TODO: Add all the logos so none will flicker on Intel
            CBLogoBB1 = logos1.find('**/CBLogoBB1')
            CBLogoBB2 = logos1.find('**/CBLogoBB2')
            CBLogoBB3 = logos1.find('**/CBLogoBB3')
            CBLogoBB25 = logos1.find('**/CBLogoBB25')
            CBLogoBB26 = logos1.find('**/CBLogoBB26')
            CBLogoBB27 = logos1.find('**/CBLogoBB27')
            CBLogoBB28 = logos1.find('**/CBLogoBB28')
            CBLogoBB29 = logos1.find('**/CBLogoBB29')
            CBLogoBB30 = logos1.find('**/CBLogoBB30')
            CBLogoBB31 = logos1.find('**/CBLogoBB31')
            for logo in [CBLogoBB1, CBLogoBB2, CBLogoBB3, CBLogoBB25, CBLogoBB26, CBLogoBB27, 
                         CBLogoBB28, CBLogoBB29, CBLogoBB30, CBLogoBB31]:
                logo.node().setEffect(DecalEffect.make())
        elif zoneId == ToontownGlobals.CashbotLobby:
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit CashbotLobby')
            
            '''door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)'''
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    
    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadCashbotHQAnims()

    
    def enterMintInterior(self, requestStatus):
        self.placeClass = MintInterior.MintInterior
        self.mintId = requestStatus['mintId']
        self.enterPlace(requestStatus)

    
    def exitMintInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.mintId

    
    def getExteriorPlaceClass(self):
        return CashbotHQExterior.CashbotHQExterior

    
    def getBossPlaceClass(self):
        return CashbotHQBossBattle.CashbotHQBossBattle


