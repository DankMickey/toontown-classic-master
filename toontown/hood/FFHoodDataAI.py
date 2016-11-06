from direct.directnotify import DirectNotifyGlobal
from toontown.safezone import FFTreasurePlannerAI
from toontown.toonbase import ToontownGlobals
import HoodDataAI

class FFHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('FFHoodDataAI')
    
    zoneId = ToontownGlobals.FunnyFarm
    treasurePlannerClass = FFTreasurePlannerAI.FFTreasurePlannerAI