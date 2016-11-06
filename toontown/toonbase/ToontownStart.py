# File: t (Python 2.4)

import __builtin__
from pandac.PandaModules import *

from panda3d.core import loadPrcFileData
loadPrcFileData("", "interpolate-frames 1")

try:
    loadPrcFile('config/Config.prc')
except:
    raise Exception('ToontownStart: Could not load Config.prc variable file!')

class game:
    name = 'toontown'
    process = 'client'
    
if __debug__:
   __injector__ = launcher.getInjectorRequest()
   if __injector__ == '1' or __injector__ == 'True':
        from direct.stdpy import threading, thread
        import sys

        def __inject_wx(_):
            code = textbox.GetValue()
            exec (code, globals())

        def openInjector_wx():
            import wx
            
            app = wx.App(redirect = False)
                
            frame = wx.Frame(None, title = "In-Game Management Tool", size=(640, 400), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
            panel = wx.Panel(frame)
            button = wx.Button(parent = panel, id = -1, label = "Alter", size = (50, 20), pos = (295, 0))
            global textbox
            textbox = wx.TextCtrl(parent = panel, id = -1, pos = (20, 22), size = (600, 340), style = wx.TE_MULTILINE)
            frame.Bind(wx.EVT_BUTTON, __inject_wx, button)

            frame.Show()
            app.SetTopWindow(frame)
            
            textbox.AppendText("")
            
            threading.Thread(target = app.MainLoop).start()
            

        openInjector_wx()

__builtin__.game = game()
import time
import os
import sys
import random
import __builtin__

try:
    pass
except:
    from toontown.launcher.ToontownDummyLauncher import ToontownDummyLauncher
    launcher = ToontownDummyLauncher()
    __builtin__.launcher = launcher

launcher.setRegistry('EXIT_PAGE', 'normal')
pollingDelay = 0.5
print 'ToontownStart: Polling for game2 to finish...'
while not launcher.getGame2Done():
    time.sleep(pollingDelay)
print 'ToontownStart: Game2 is finished.'
print 'ToontownStart: Starting the game.'
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
print 'ToontownStart: setting default font'
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
import ToonBase
ToonBase.ToonBase()
if base.win == None:
    print 'Unable to open window; aborting.'
    sys.exit()

launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').setBin('fixed', 20)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
if base.musicManagerIsValid:
    music = base.musicManager.getSound('phase_3/audio/bgm/tt_theme.mid')
    if music:
        music.setLoop(1)
        music.setVolume(0.90000000000000002)
        music.play()
    
    print 'ToontownStart: Loading default gui sounds'
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.mp3'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.mp3'))
else:
    music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
print 'ToontownStart: serverVersion: ', serverVersion
version = OnscreenText(serverVersion, pos = (-1.3, -0.97499999999999998), scale = 0.059999999999999998, fg = Vec4(0, 0, 1, 0.59999999999999998), align = TextNode.ALeft)
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE)
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
base.startShow(cr, launcher.getGameServer())
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
__builtin__.loader = base.loader
try:
    base.run()
except SystemExit:
    raise 
except:
    from direct.showbase import PythonUtil
    print PythonUtil.describeException()
    raise