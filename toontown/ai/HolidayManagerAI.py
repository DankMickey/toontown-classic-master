from toontown.ai.HolidayBaseAI import HolidayBaseAI
from toontown.toonbase import ToontownGlobals

decorationHolidays = [
    ToontownGlobals.WINTER_DECORATIONS,
    ToontownGlobals.WACKY_WINTER_DECORATIONS,
    ToontownGlobals.HALLOWEEN_PROPS,
    ToontownGlobals.SPOOKY_PROPS,
    ToontownGlobals.HALLOWEEN_COSTUMES,
    ToontownGlobals.SPOOKY_COSTUMES,
    ToontownGlobals.CRASHED_LEADERBOARD]
promotionalSpeedChatHolidays = [
    ToontownGlobals.ELECTION_PROMOTION]

class HolidayManagerAI(HolidayBaseAI):

    def __init__(self, air):
        HolidayBaseAI.__init__(self, air, holidayId=0)
        self.currentHolidays = [ ]

    def start(self):
        self.currentHolidays.append(ToontownGlobals.HALLOWEEN)

        if len(self.currentHolidays) > 0:
            self.setHolidayIdList(self.currentHolidays)

        self.setPopulation(self.air.districtStats.getAvatarCount())

    def setHolidayIdList(self, holidayList):
        self.air.newsManager.d_setHolidayIdList(holidayList)

    def setPopulation(self, population):
        self.air.newsManager.d_setPopulation(population)

    def stop(self):
        for holidayId in self.currentHolidays:
            self.currentHolidays.remove(holidayId)
            
    def isMoreXpHolidayRunning(self):
        if ToontownGlobals.MORE_XP_HOLIDAY in self.currentHolidays:
            self.xpMultiplier = 2
            return True
        return False
       
    def getXpMultiplier(self):
        return self.xpMultiplier