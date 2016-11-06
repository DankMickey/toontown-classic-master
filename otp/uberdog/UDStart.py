from pandac.PandaModules import *
import __builtin__

try:
    loadPrcFile('config/Config.prc')
except:
    raise Exception('Failed to load the Config.prc variable file!')

from direct.showbase.PythonUtil import *
from otp.ai.AIBase import AIBase

dcFileNames = ['resources/phase_3/etc/otp.dc', 'resources/phase_3/etc/toon.dc']
loadPrcFileData('', 'want-dev True')

class Game:
    name = 'uberDog'

__builtin__.game = Game()
__builtin__.simbase = AIBase()

from otp.uberdog.UDRepository import UDRepository
simbase.air = UDRepository(baseChannel=200100000, serverId=10000, 
                        dcFileNames=dcFileNames)

simbase.air.notify.setInfo(True)
simbase.air.notify.setDebug(True)
simbase.air.notify.setWarning(True)

try:
    simbase.air.connect(host='127.0.0.1', port=7198)
except:
    raise Exception('Failed to connect to the gameserver!')

simbase.run()