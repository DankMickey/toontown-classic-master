# File: t (Python 2.4)

from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior
import FactoryInterior
import SellbotHQExterior
import SellbotHQBossBattle
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
aspectSF = 0.72270000000000001

class SellbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotCogHQLoader')
    
    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, [
            'quietZone',
            'factoryInterior',
            'cogHQExterior']))
        for stateName in [
            'start',
            'cogHQExterior',
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')
        
        self.fsm.addState(State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, [
            'quietZone',
            'factoryExterior']))
        for stateName in [
            'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryInterior')
        
        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.mid'
        self.cogHQExteriorModelPath = 'phase_9/models/cogHQ/SellbotHQExterior'
        self.cogHQLobbyModelPath = 'phase_9/models/cogHQ/SellbotHQLobby'
        self.factoryExteriorModelPath = 'phase_9/models/cogHQ/SellbotFactoryExterior'
        self.geom = None

    
    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    
    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)

    
    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            dgLinkTunnel = self.geom.find('**/Tunnel1')
            dgLinkTunnel.setName('linktunnel_dg_5316_DNARoot')
            factoryLinkTunnel = self.geom.find('**/Tunnel2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11200_DNARoot')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            dgSign = cogSign.copyTo(dgLinkTunnel)
            dgSign.setPosHprScale(0.0, -291.5, 29, 180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            dgSign.node().setEffect(DecalEffect.make())
            dgText = DirectGui.OnscreenText(text = TTLocalizer.DaisyGardens[-1], font = ToontownGlobals.getSuitFont(), pos = (0, -0.29999999999999999), scale = TTLocalizer.SCHQLdgText, mayChange = False, parent = dgSign)
            dgText.setDepthWrite(0)
            factorySign = cogSign.copyTo(factoryLinkTunnel)
            factorySign.setPosHprScale(148.625, -155, 27, -90.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            factorySign.node().setEffect(DecalEffect.make())
            factoryTypeText = DirectGui.OnscreenText(text = TTLocalizer.Sellbot, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, mayChange = False, parent = factorySign)
            factoryTypeText.setDepthWrite(0)
            factoryText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.12, mayChange = False, parent = factorySign)
            factoryText.setDepthWrite(0)
            #Lights
            lights = self.geom.find('**/SpotLights')
            light1 = lights.find('**/Spot1')
            light2 = lights.find('**/Spot2')
            light3 = lights.find('**/Spot3')
            light4 = lights.find('**/Spot4')
            light5 = lights.find('**/Spot5')
            light6 = lights.find('**/Spot6')
            #First Set
            LightInterval1 = light1.hprInterval(4.0, Vec3(0, 0, 5))
            LightInterval2 = light1.hprInterval(4.0, Vec3(0, 0, -5))
            LightInterval3 = light1.hprInterval(4.0, Vec3(0, 0, 0))
            LightSequence = Sequence(LightInterval1, LightInterval2, LightInterval3)
            LightSequence.loop()
            #Second Set
            LightInterval4 = light2.hprInterval(4.0, Vec3(0, 0, -3))
            LightInterval5 = light2.hprInterval(4.0, Vec3(0, 0, 3))
            LightInterval6 = light2.hprInterval(4.0, Vec3(0, 0, 0))
            LightSequence1 = Sequence(LightInterval4, LightInterval5, LightInterval6)
            LightSequence1.loop()
            #Third Set
            LightInterval7 = light3.hprInterval(4.0, Vec3(0, 0, 3))
            LightInterval8 = light3.hprInterval(4.0, Vec3(0, 0, -3))
            LightInterval9 = light3.hprInterval(4.0, Vec3(0, 0, 0))
            LightSequence2 = Sequence(LightInterval7, LightInterval8, LightInterval9)
            LightSequence2.loop()
            #Fourth Set
            LightInterval10 = light4.hprInterval(4.0, Vec3(0, 0, -5))
            LightInterval11 = light4.hprInterval(4.0, Vec3(0, 0, 3))
            LightInterval12 = light4.hprInterval(4.0, Vec3(0, 0, 0))
            LightSequence3 = Sequence(LightInterval10, LightInterval11, LightInterval12)
            LightSequence3.loop()
            #Final Set
            LightInterval13 = light5.hprInterval(4.0, Vec3(0, 0, 3))
            LightInterval14 = light5.hprInterval(4.0, Vec3(0, 0, -3))
            LightInterval15 = light5.hprInterval(4.0, Vec3(0, 0, 0))
            LightSequence4 = Sequence(LightInterval13, LightInterval14, LightInterval15)
            LightSequence4.loop()
            #Doors
            doors = self.geom.find('**/doors')
            door0 = doors.find('**/door_0')
            door1 = doors.find('**/door_1')
            door2 = doors.find('**/door_2')
            door3 = doors.find('**/door_3')
            index = 0
            for door in [
                door0,
                door1,
                door2,
                door3]:
                doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
                door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
                door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
                doorFrame.node().setEffect(DecalEffect.make())
                index += 1
            
        elif zoneId == ToontownGlobals.SellbotFactoryExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            factoryLinkTunnel = self.geom.find('**/tunnel_group2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11000_DNARoot')
            factoryLinkTunnel.find('**/tunnel_sphere').setName('tunnel_trigger')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            elevatorSignSF = 15
            hqSign = cogSign.copyTo(factoryLinkTunnel)
            hqSign.setPosHprScale(0.0, -353, 27.5, -180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            hqSign.node().setEffect(DecalEffect.make())
            hqTypeText = DirectGui.OnscreenText(text = TTLocalizer.Sellbot, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, mayChange = False, parent = hqSign)
            hqTypeText.setDepthWrite(0)
            hqText = DirectGui.OnscreenText(text = TTLocalizer.Headquarters, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.10000000000000001, mayChange = False, parent = hqSign)
            hqText.setDepthWrite(0)
            frontDoor = self.geom.find('**/doorway1')
            fdSign = cogSign.copyTo(frontDoor)
            fdSign.setPosHprScale(62.740000000000002, -87.989999999999995, 17.260000000000002, 2.7200000000000002, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            fdSign.node().setEffect(DecalEffect.make())
            fdTypeText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = TTLocalizer.SCHQLfdTypeText, mayChange = False, parent = fdSign)
            fdTypeText.setDepthWrite(0)
            fdText = DirectGui.OnscreenText(text = TTLocalizer.SellbotFrontEntrance, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = TTLocalizer.SCHQLdgText, mayChange = False, parent = fdSign)
            fdText.setDepthWrite(0)
            sideDoor = self.geom.find('**/doorway2')
            sdSign = cogSign.copyTo(sideDoor)
            sdSign.setPosHprScale(-164.78, 26.280000000000001, 17.25, -89.890000000000001, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            sdSign.node().setEffect(DecalEffect.make())
            sdTypeText = DirectGui.OnscreenText(text = TTLocalizer.Factory, font = ToontownGlobals.getSuitFont(), pos = (0, -0.25), scale = 0.074999999999999997, mayChange = False, parent = sdSign)
            sdTypeText.setDepthWrite(0)
            sdText = DirectGui.OnscreenText(text = TTLocalizer.SellbotSideEntrance, font = ToontownGlobals.getSuitFont(), pos = (0, -0.34000000000000002), scale = 0.10000000000000001, mayChange = False, parent = sdSign)
            sdText.setDepthWrite(0)
        elif zoneId == ToontownGlobals.SellbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit SellbotLobby')
            
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            front = self.geom.find('**/frontWall')
            front.node().setEffect(DecalEffect.make())
            door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    
    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()

    
    def enterFactoryExterior(self, requestStatus):
        self.placeClass = FactoryExterior.FactoryExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    
    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None

    
    def enterFactoryInterior(self, requestStatus):
        self.placeClass = FactoryInterior.FactoryInterior
        self.enterPlace(requestStatus)

    
    def exitFactoryInterior(self):
        self.exitPlace()
        self.placeClass = None

    
    def getExteriorPlaceClass(self):
        return SellbotHQExterior.SellbotHQExterior

    
    def getBossPlaceClass(self):
        return SellbotHQBossBattle.SellbotHQBossBattle


