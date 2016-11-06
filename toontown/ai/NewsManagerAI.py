from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals

class NewsManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('NewsManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.weeklyCalenderHolidays = []
        self.yearlyCalenderHolidays = []
        self.oncelyCalenderHolidays = []
        self.relativelyCalenderHolidays = []
        self.multipleCalenderHolidays = []

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def d_setHolidayIdList(self, holidayList):
        self.sendUpdate('setHolidayIdList', [
            holidayList])

    def d_setPopulation(self, population):
        self.sendUpdate('setPopulation', [
            population])
            
    def d_sendSystemMessage(self, message, style):
        self.sendUpdate('sendSystemMessage', [
            message, style])
            
    def d_startHoliday(self, holidayId):
        self.sendUpdate('startHoliday', [
            holidayId])
        self.d_holidayNotify()
            
    def d_holidayNotify(self):
        self.sendUpdate('holidayNotify', [])
            
    def d_endHoliday(self, holidayId):
        self.sendUpdate('endHoliday', [
            holidayId])
            
    def d_setInvasionStatus(self, todo1, todo2, todo3, todo4):
        pass #In till cogs are fixed. This should pass.

    def getWeeklyCalendarHolidays(self):
        return self.weeklyCalenderHolidays

    def getYearlyCalendarHolidays(self):
        return self.yearlyCalenderHolidays

    def getOncelyCalendarHolidays(self):
        return self.oncelyCalenderHolidays

    def getRelativelyCalendarHolidays(self):
        return self.relativelyCalenderHolidays

    def getMultipleStartHolidays(self):
        return self.multipleCalenderHolidays

    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)
