from otp.distributed.DistributedDistrictAI import DistributedDistrictAI
from direct.directnotify import DirectNotifyGlobal

class ToontownDistrictAI(DistributedDistrictAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownDistrictAI')

    def __init__(self, air, name='Not Given'):
        DistributedDistrictAI.__init__(self, air, name)

    def generate(self):
        DistributedDistrictAI.generate(self)

    def announceGenerate(self):
        DistributedDistrictAI.announceGenerate(self)

    def getAllowAHNNLog(self):
        return False

    def disable(self):
        DistributedDistrictAI.disable(self)

    def delete(self):
        DistributedDistrictAI.delete(self)
