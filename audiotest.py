from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from panda3d.core import loadPrcFileData

try:
    loadPrcFile('config/Config.prc')
except:
    print('AudioTest: Could not load Config.prc variable file!')

base = ShowBase()
mySound = base.loader.loadMusic("phase_3/audio/bgm/tt_theme.mid")
mySound.play()

base.run()