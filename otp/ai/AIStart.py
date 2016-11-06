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
    name = 'toontown'

__builtin__.game = Game()
__builtin__.simbase = AIBase()

from toontown.dnaparser.DNAParser import DNAData
__builtin__.DNAData = DNAData

from otp.ai.AIRepository import AIRepository
simbase.air = AIRepository(baseChannel=400100000, serverId=10000, 
                        districtName='Nutty Summit', # TODO
                        dcFileNames=dcFileNames)

simbase.air.notify.setInfo(True)
simbase.air.notify.setDebug(False)
simbase.air.notify.setWarning(False)

try:
    simbase.air.connect(host='127.0.0.1', port=7198)
except:
    raise Exception('Failed to connect to the gameserver!')

simbase.run()