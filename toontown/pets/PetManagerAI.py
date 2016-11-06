from toontown.toonbase import ToontownGlobals

class PetManagerAI:

    def __init__(self, air):
        self.air = air

    def getAvailablePets(self, minNum, maxNum):
        return [minNum, maxNum]