from toontown.racing.DistributedKartPadAI import DistributedKartPadAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM
from direct.distributed.ClockDelta import *

class DistributedRacePadAI(DistributedKartPadAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedRacePadAI')

    def __init__(self, air, area):
        DistributedKartPadAI.__init__(self, air, area)
        FSM.__init__(self, 'DistributedRacePadAI')
        self.waitingCountdown = False
        self.state = ['', self.getTimestamp()]
        self.slots = [
            0, 
            0, 
            0, 
            0]
        self.trackInfo = [
            0, 
            0]

    def generate(self):
        DistributedKartPadAI.generate(self)

    def announceGenerate(self):
        DistributedKartPadAI.announceGenerate(self)
        self.enterOff()

    def getTimestamp(self):
        return globalClockDelta.getRealNetworkTime(bits=32)

    def enterOff(self):
        self.d_setState('WaitEmpty', self.getTimestamp())

    def enterWaitEmpty(self):
        pass

    def enterWaitCountdown(self):
        pass

    def enterWaitBoarding(self):
        pass

    def enterAllAboard(self):
        pass

    def setState(self, state, timestamp):
        self.request(state)

    def d_setState(self, state, timestamp):
        self.sendUpdate('setState', [
            state,
            timestamp])

    def b_setState(self, state, timestamp):
        self.setState(state, timestamp)
        self.d_setState(state, timestamp)
    
    def getState(self):
        return self.state

    def getTrackInfo(self):
        return self.trackInfo

    def disable(self):
        DistributedKartPadAI.disable(self)

    def delete(self):
        DistributedKartPadAI.delete(self)
