from toontown.pets.PetChase import PetChase

class CPetChase(PetChase):

    def __init__(self, target, minDist, moveAngle):
        PetChase.__init__(self, target = target, minDist = minDist, moveAngle = moveAngle)

    def setMover(self, mover):
        PetChase._setMover(self, mover)

    def clearMover(self, mover):
        PetChase._clearMover(self, mover)

    def process(self, dt):
        PetChase._process(self, dt)