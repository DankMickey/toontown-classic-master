from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
from direct.directnotify import DirectNotifyGlobal

from toontown.toonbase import ToontownGlobals
from toontown.suit import SuitDNA

import random, time

class DistributedSuitInvasionManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuitInvasionManagerAI')
    minDuration = config.GetInt('invasion-min-duration', 7 * 60) # 7 mins
    maxDuration = config.GetInt('invasion-min-duration', 25 * 60) # 25 mins
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        
        self.skel = False
        self.curInvading = None
        
        self.startTime = 0
        self.startTimeTS = 0
        self.duration = 0
        self.numCogs = 0
        
        self.otherInvasions = {}
        self.invasionInterval = config.GetInt('invasion-interval', 30 * 60) # 30 minutes
        self.invasionChance = config.GetFloat('invasion-chance', .35) # 35% of chance
        self.invasionChanceSkel = config.GetFloat('invasion-chance-skel', self.invasionChance) # Chance of getting skels
        
    def __checkInvasion(self, task=None):
        if self.hasInvading():
            if task:
                return task.again
          
        self.notify.debug('Checking if we should start an invasion...')
        if random.random() < self.invasionChance:
            self.notify.debug('Time to have a random invasion!')
            skel = False
            if random.random() < self.invasionChanceSkel:
                if random.random() < self.invasionChanceSkel:
                    self.notify.debug('Doing skels this random invasion')
                    skel = True
                    
            if not skel:
                pool = SuitDNA.suitHeadTypes[:]
                for iv in self.otherInvasions.values():
                    if iv in pool:
                        self.notify.debug('%s already invading another shard' % iv)
                        pool.remove(iv)
                    
                if not pool:
                    pool = SuitDNA.suitHeadTypes[:]
                    
                suitName = random.choice(pool)
                
            else:
                suitName = None
                
            self.startInvasion(suitName=suitName, skel=skel)
            
        else:
            self.notify.debug('Not now, maybe later...')
            
        if task:
            return task.again
        
    def __handleInvasionEvent(self, data):
        self.otherInvasions[self.air.getMsgSender()] = data['suitName']
        
    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        
        self.accept('invasionEvent', self.__handleInvasionEvent)
        taskMgr.doMethodLater(self.invasionInterval, self.__checkInvasion, self.taskName('invasion-interval'))
        
        if not self.air.wantMegaInvasions:
            return
        
        def testInvasion(holidayId, suitIndex):
            if self.air.holidayManager.isHolidayRunning(holidayId):
                suitName = SuitDNA.suitHeadTypes[suitIndex]
                self.notify.info('Starting mega invasion of %s' % suitName)
                self.startInvasion(suitName, skel=self.air.holidayManager.isHolidayRunning(ToontownGlobals.SKELECOG_INVASION), mega=True)
                return 1
            
        if testInvasion(ToontownGlobals.MR_HOLLYWOOD_INVASION, 31):
            return

        if testInvasion(ToontownGlobals.YES_MAN_INVASION, 2):
            return
        
        if testInvasion(ToontownGlobals.TIGHTWAD_INVASION, 18):
            return

        if testInvasion(ToontownGlobals.TELEMARKETER_INVASION, 25):
            return

        if testInvasion(ToontownGlobals.HEADHUNTER_INVASION, 5):
            return

        if testInvasion(ToontownGlobals.SPINDOCTOR_INVASION, 13):
            return

        if testInvasion(ToontownGlobals.MONEYBAGS_INVASION, 21):
            return

        if testInvasion(ToontownGlobals.TWOFACES_INVASION, 29):
            return

        if testInvasion(ToontownGlobals.MINGLER_INVASION, 30):
            return

        if testInvasion(ToontownGlobals.LOANSHARK_INVASION, 22):
            return

        if testInvasion(ToontownGlobals.CORPORATE_RAIDER_INVASION, 6):
            return

        if testInvasion(ToontownGlobals.ROBBER_BARON_INVASION, 23):
            return

        if testInvasion(ToontownGlobals.LEGAL_EAGLE_INVASION, 14):
            return
        
        if testInvasion(ToontownGlobals.BIG_WIG_INVASION, 15):
            return
        
        if testInvasion(ToontownGlobals.BIG_CHEESE_INVASION, 7):
            return
        
        if testInvasion(ToontownGlobals.DOWN_SIZER_INVASION, 4):
            return
        
        if testInvasion(ToontownGlobals.MOVER_AND_SHAKER_INVASION, 28):
            return
        
        if testInvasion(ToontownGlobals.DOUBLETALKER_INVASION, 10):
            return
        
        if testInvasion(ToontownGlobals.PENNY_PINCHER_INVASION, 17):
            return
        
        if testInvasion(ToontownGlobals.NAME_DROPPER_INVASION, 26):
            return
        
        if testInvasion(ToontownGlobals.AMBULANCE_CHASER_INVASION, 11):
            return
        
        if testInvasion(ToontownGlobals.MICROMANAGER_INVASION, 3):
            return
        
        if testInvasion(ToontownGlobals.NUMBER_CRUNCHER_INVASION, 20):
            return
            
        if testInvasion(ToontownGlobals.BLOODSUCKER_INVASION, 9):
            return
            
        # No mega invasion scheduled, attempt a simple invasion
        self.__checkInvasion()
        
    def getCurrentInvasion(self):
        name = self.curInvading or ''
        return (name, self.skel, False, self.startTime, self.duration)
        
    def getInvadingCog(self):
        if self.hasInvading():
            self.numCogs += 1
            self.broadcastInvasionEvent()
        return (self.curInvading, self.skel)
        
    def hasInvading(self):
        return self.skel or (self.curInvading != None)
        
    def startInvasion(self, suitName=None, skel=False, mega=False):
        self.withdrawAllCogs()
        
        skel = bool(skel)
        mega = bool(mega)
        
        self.skel = skel
        self.curInvading = suitName if suitName != '' else None
        self.numCogs = 0
        
        self.startTime = globalClockDelta.localToNetworkTime(globalClock.getRealTime(), bits = 32)
        self.startTimeTS = int(time.time())
        
        if not mega:
            self.duration = int(random.random() * (self.maxDuration - self.minDuration) + self.minDuration) # 5 - 15 mins
            taskMgr.doMethodLater(self.duration, self.__stop, self.taskName('end-invasion'))
            
        else:
            self.duration = 1
        
        self.sendUpdate('startInvasion', [suitName or '', skel, 0, self.startTime, self.duration])
        self.sendUpdate('setCurrentInvasion', self.getCurrentInvasion())
        
        self.notify.debug('Invasion started: %s (%s); duration = %s secs' % (suitName, skel, self.duration))
        messenger.send('startInvasion')
        self.broadcastInvasionEvent()
        
    def __stop(self, task=None):
        self.withdrawAllCogs()
        
        self.skel = False
        self.curInvading = None
        self.startTime = self.startTimeTS = self.duration = self.numCogs = 0
        
        self.sendUpdate('invasionOver', [])
        self.sendUpdate('setCurrentInvasion', self.getCurrentInvasion())
        
        messenger.send('endInvasion')
        self.broadcastInvasionEvent()
        
        if task:
            self.notify.debug('Invasion is over')
            return task.done
            
    def withdrawAllCogs(self):
        for planner in self.air.suitPlanners.values():
            planner.flySuits()
            
    def abort(self):
        self.notify.info('Invasion aborted')
        taskMgr.remove(self.taskName('end-invasion'))
        self.__stop(None)
        
    def isMega(self):
        return self.hasInvading() and self.duration == 1
        
    def broadcastInvasionEvent(self):
        data = {'duration': self.duration, 'startTime': self.startTimeTS,
                'suitName': self.curInvading or '', 'skel': self.skel,
                'numCogs': self.numCogs}
        self.air.sendNetEvent('invasionEvent', [data])
            
from otp.ai.MagicWordGlobal import *
@magicWord(chains=[CHAIN_ADM], types=[int])
def invasion(index = -1):
    av = spellbook.getInvoker()
    dsi = av.air.suitInvasionManager
    
    if not -1 <= index <= 31:
        return 'Invalid value! Must be between -1 (stop inv) and 31!'
        
    if index == -1:
        if not dsi.hasInvading():
            return 'No invasion in progress!'
            
        elif dsi.isMega():
            return 'Current invasion is mega. Use ~megainv controls!'
            
        else:
            dsi.abort()
    
    else:
        if dsi.hasInvading():
            return 'An invasion is already progress! Use ~invasion -1 to stop it!'
            
        else:
            dsi.startInvasion(SuitDNA.suitHeadTypes[index])

@magicWord(chains=[CHAIN_ADM])
def invasionext():
    dsi = simbase.air.suitInvasionManager
        
    if dsi.hasInvading():
        return 'An invasion is already progress! Use ~invasion -1 to stop it!'
            
    dsi.startInvasion(suitName = None, skel = True)
   
@magicWord(chains=[CHAIN_HEAD], types=[int])   
def megainv(index = -1):
    av = spellbook.getInvoker()
    dsi = av.air.suitInvasionManager
    
    if not -1 <= index <= 31:
        return 'Invalid value! Must be between -1 (stop inv) and 31!'
        
    if index == -1:
        if not dsi.isMega():
            return 'Cannot stop current invasion (if any): not mega! Use ~invasion controls!'
            
        dsi.abort()
        
    else:
        if dsi.hasInvading():
            return 'An invasion is already progress! Use ~invasion -1 to stop it!'
            
        dsi.startInvasion(SuitDNA.suitHeadTypes[index], mega=True)
        return 'Successfully started mega invasion!'
        