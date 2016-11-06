import math, time, random
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from toontown.toonbase import ToontownGlobals
from direct.task.Task import Task

class DistributedRealTime(DistributedObject.DistributedObject):
    notify = directNotify.newCategory('DistributedRealTime')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.dayTrack = None
        self.sunTrack = None
        self.sunMoonNode = None
        self.zoneId = 0
        self.load()

    def disable(self):
        self.notify.debug('disable')
        self.__stopBirds()
        self.__stopCrickets()
        DistributedObject.DistributedObject.disable(self)
        self.ignore('enterFlowerSellBox')

    def delete(self):
        self.notify.debug('delete')
        self.unload()
        DistributedObject.DistributedObject.delete(self)

    def load(self):
        self.birdSound = base.cr.playGame.hood.loader.birdSound
        self.cricketSound = base.cr.playGame.hood.loader.cricketSound
        self.sun = loader.loadModel('phase_4/models/props/sun.bam')
        self.moon = loader.loadModel('phase_5.5/models/props/moon.bam')
        self.sunMoonNode = base.cr.playGame.hood.loader.geom.attachNewNode('sunMoon')
        self.sunMoonNode.setPosHpr(0, 0, 0, 0, 0, 0)
        if self.sun:
            self.sun.reparentTo(self.sunMoonNode)
            self.sun.setY(270)
            self.sun.setScale(2)
            self.sun.setBillboardPointEye()
        if self.moon:
            self.moon.reparentTo(self.sunMoonNode)
            self.moon.setY(-270)
            self.moon.setScale(15)
            self.moon.setBillboardPointEye()
        self.sunMoonNode.setP(30)
        if 'toontown.hood.BRHood.BRHood' or 'toontown.hood.DDHood.DDHood' in str(base.cr.playGame.hood)[1:]:
            self.sunMoonNode.hide()

    def unload(self):
        self.ignoreAll()
        self.__killDaytimeTask()
        self.__stopBirds()
        self.__stopCrickets()
        if self.dayTrack:
            self.dayTrack.pause()
            self.dayTrack = None
        self.__killSunTask()
        if self.sunTrack:
            self.sunTrack.pause()
            self.sunTrack = None
        if self.sunMoonNode:
            self.sunMoonNode.removeNode()
            del self.sunMoonNode
            self.sunMoonNode = None
        return

    def setDawnTime(self, ts):
        self.notify.debug('setDawnTime')
        self.dawnTime = ts
        self.sendUpdate('requestServerTime', [])

    def requestServerTime(self):
        pass

    def setServerTime(self, ts):
        self.notify.debug('setServerTime')
        self.serverTime = ts
        self.clientTime = time.time() % ToontownGlobals.DAY_NIGHT_PERIOD
        self.deltaTime = self.clientTime - self.serverTime
        if base.dayNightEnabled:
            self.__initDaytimeTask()
            self.__initSunTask()

    def getDeltaTime(self):
        curTime = time.time() % ToontownGlobals.DAY_NIGHT_PERIOD
        dawnTime = self.dawnTime
        dT = (curTime - dawnTime - self.deltaTime) % ToontownGlobals.DAY_NIGHT_PERIOD
        self.notify.debug(
            'getDeltaTime = %s. curTime=%s. dawnTime=%s. serverTime=%s.  deltaTime=%s'
            % (dT, curTime, dawnTime, self.serverTime, self.deltaTime))
        return dT

    def __initDaytimeTask(self):
        self.__killDaytimeTask()
        task = Task(self.__dayTimeTask)
        dT = self.getDeltaTime()
        task.ts = dT
        taskMgr.add(task, self.taskName('daytime'))

    def __killDaytimeTask(self):
        taskMgr.remove(self.taskName('daytime'))

    def __dayTimeTask(self, task):
        taskName = self.taskName('daytime')
        track = Sequence(Parallel(
                             LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, ToontownGlobals.HALF_DAY_PERIOD, Vec4(1, 0.6, 0.6, 1)),
                             LerpColorScaleInterval(base.cr.playGame.hood.sky, ToontownGlobals.HALF_DAY_PERIOD, Vec4(1, 0.8, 0.8, 1))),
                         Parallel(
                             LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, ToontownGlobals.HALF_NIGHT_PERIOD, Vec4(0.2, 0.2, 0.5, 1)),
                             LerpColorScaleInterval(base.cr.playGame.hood.sky, ToontownGlobals.HALF_NIGHT_PERIOD, Vec4(0.2, 0.2, 0.4, 1))),
                         Parallel(
                             LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, ToontownGlobals.HALF_NIGHT_PERIOD, Vec4(0.6, 0.6, 0.8, 1)),
                             LerpColorScaleInterval(base.cr.playGame.hood.sky, ToontownGlobals.HALF_NIGHT_PERIOD, Vec4(0.5, 0.5, 0.6, 1))),
                         Parallel(
                             LerpColorScaleInterval(base.cr.playGame.hood.loader.geom, ToontownGlobals.HALF_DAY_PERIOD, Vec4(1, 1, 1, 1)),
                             LerpColorScaleInterval(base.cr.playGame.hood.sky, ToontownGlobals.HALF_DAY_PERIOD, Vec4(1, 1, 1, 1))),
                         Func(base.cr.playGame.hood.loader.geom.clearColorScale),
                         Func(base.cr.playGame.hood.sky.clearColorScale))
        if self.dayTrack:
            self.dayTrack.finish()
        self.dayTrack = track
        ts = 0
        if hasattr(task, 'ts'):
            ts = task.ts
        self.dayTrack.start(ts)
        taskMgr.doMethodLater(ToontownGlobals.DAY_NIGHT_PERIOD - ts, self.__dayTimeTask, self.taskName('daytime'))
        return Task.done

    def __initSunTask(self):
        self.__killSunTask()
        task = Task(self.__sunTask)
        dT = self.getDeltaTime()
        task.ts = dT
        taskMgr.add(task, self.taskName('sunTask'))

    def __killSunTask(self):
        taskMgr.remove(self.taskName('sunTask'))

    def __sunTask(self, task):
        sunMoonNode = self.sunMoonNode
        sun = self.sun
        h = 30
        halfPeriod = ToontownGlobals.DAY_NIGHT_PERIOD / 2.0
        track = Sequence(Parallel(
                             LerpHprInterval(sunMoonNode, ToontownGlobals.HALF_DAY_PERIOD, Vec3(0, 0, 0)),
                             LerpColorScaleInterval(sun, ToontownGlobals.HALF_DAY_PERIOD, Vec4(1, 1, 0.5, 1))),
                         Func(sun.clearColorScale),
                         Func(self.__stopBirds),
                         LerpHprInterval(sunMoonNode, 0.2, Vec3(0, -h - 3, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, -h + 2, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, -h - 1.5, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, -h, 0)),
                         Func(self.notify.debug, 'night'),
                         Wait(ToontownGlobals.HALF_NIGHT_PERIOD - 0.5),
                         LerpHprInterval(sunMoonNode, ToontownGlobals.HALF_NIGHT_PERIOD, Vec3(0, 0, 0)),
                         Func(self.__startBirds),
                         LerpHprInterval(sunMoonNode, 0.2, Vec3(0, h + 3, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, h - 2, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, h + 1.5, 0)),
                         LerpHprInterval(sunMoonNode, 0.1, Vec3(0, h, 0)),
                         Func(self.notify.debug, 'day'),
                         Func(sunMoonNode.setHpr, 0, h, 0),
                         Wait(ToontownGlobals.HALF_DAY_PERIOD - 0.5))
        if self.sunTrack:
            self.sunTrack.finish()
        self.sunTrack = track
        ts = 0
        if hasattr(task, 'ts'):
            ts = task.ts
            if self.birdSound and self.cricketSound:
                if ts > ToontownGlobals.HALF_DAY_PERIOD and ts < ToontownGlobals.DAY_NIGHT_PERIOD - ToontownGlobals.HALF_DAY_PERIOD:
                    self.__stopBirds()
                    self.__startCrickets()
                else:
                    self.__stopCrickets()
                    self.__startBirds()
        self.sunTrack.start(ts)
        taskMgr.doMethodLater(ToontownGlobals.DAY_NIGHT_PERIOD - ts, self.__sunTask, self.taskName('sunTask'))
        return Task.done

    def __stopBirds(self):
        taskMgr.remove('estate-birds')

    def __startBirds(self):
        self.__stopBirds()
        taskMgr.doMethodLater(1, self.__birds, 'estate-birds')

    def __birds(self, task):
        if self.birdSound:
            base.playSfx(random.choice(base.cr.playGame.hood.loader.birdSound))
        t = random.random() * 20.0 + 1
        taskMgr.doMethodLater(t, self.__birds, 'estate-birds')
        return Task.done

    def __stopCrickets(self):
        taskMgr.remove('estate-crickets')

    def __startCrickets(self):
        self.__stopCrickets()
        taskMgr.doMethodLater(1, self.__crickets, 'estate-crickets')

    def __crickets(self, task):
        sfx = base.cr.playGame.hood.loader.cricketSound
        if self.cricketSound:
            track = Sequence(Func(base.playSfx, random.choice(sfx)), Wait(1))
            track.start()
        t = random.random() * 20.0 + 1
        taskMgr.doMethodLater(t, self.__crickets, 'estate-crickets')
        return Task.done