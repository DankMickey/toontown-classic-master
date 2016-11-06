from toontown.toonbase import ToontownGlobals
from toontown.dnaparser.DNAParser import DNASuitPoint
from toontown.suit.SuitLeg import SuitLeg
import math, random

class SuitLegList:

    def __init__(self, path, dnaStore, walkSpeed, fromSky, toSky, fromSuitBuilding, toSuitBuilding, toToonBuilding):
        self.path = path
        self.dnaStore = dnaStore
        self.walkSpeed = walkSpeed
        self.fromSky = fromSky
        self.toSky = toSky
        self.fromSuitBuilding = fromSuitBuilding
        self.toSuitBuilding = toSuitBuilding
        self.toToonBuilding = toToonBuilding

        self.suitLegs = { }
        self.suitLegsAtTime = { }
        self.nextSuitIndex = 0
    
    def getZoneId(self, legIndex):
        if legIndex in self.suitLegs:
            return self.suitLegs[legIndex].getZoneId()
        
        return 0
	
    def getType(self, legIndex):
        if legIndex in self.suitLegs:
            return self.suitLegs[legIndex].getType()
        
        return 0

    def getPointA(self):
        pass

    def getPointB(self):
        pass

    def getStartTime(self, legIndex):
        pass

    def getLegIndexAtTime(self, elapsed, legIndex):
        self.nextSuitIndex += 1

        # create a new suit leg
        suitLeg = SuitLeg(self.nextSuitIndex)

        if legIndex in self.suitLegs:
            suitLeg = self.suitLegs[legIndex]

            if suitLeg.getStartTime() == elapsed:
                return self.suitLegs[legIndex].getSuitLegIndex()

        suitLeg.setStartTime(elapsed)

        # store the new suitLeg by id.
        self.suitLegs[suitLeg.getSuitLegIndex()] = suitLeg

        # return the newly created suitLeg id.
        return suitLeg.getSuitLegIndex()

    def getLegTime(self):
        pass

    def getLeg(self, legIndex):
        if legIndex not in suitLegs:
            return None

        return self.suitLegs[legIndex]

    def getNumLegs(self):
        return len(self.suitLegs.keys())
    
    def isPointInRange(self, point, elapsed, pathCollBuffer):
        pass

    def getBlockNumber(self, legIndex):
        pass