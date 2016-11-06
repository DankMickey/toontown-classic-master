from toontown.suit import SuitTimings 
from toontown.toonbase import ToontownGlobals

class SuitLeg:
    TOff = 0
    TWalk = 1
    TWalkFromStreet = 2
    TToSuitBuilding = 3
    TToCoghq = 4
    TFromCoghq = 5
    TToToonBuilding = 6

    def __init__(self, suitLegIndex):
        self.suitLegIndex = suitLegIndex
        self.startTime = 0

    def getSuitLegIndex(self):
        return self.suitLegIndex

    def getPointA(self):
        pass

    def getPointB(self):
        pass

    def getBlockNumber(self):
        pass

    def getZoneId(self):
        return 10000

    def getType(self):
        pass

    def getPosB(self):
        pass

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getStartTime(self):
        return self.startTime