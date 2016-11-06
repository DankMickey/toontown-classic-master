from otp.ai.MagicWordManagerAI import MagicWordManagerAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.coghq import CogDisguiseGlobals
from toontown.quest import Quests

class ToontownMagicWordManagerAI(MagicWordManagerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownMagicWordManagerAI')

    def __init__(self, air):
        MagicWordManagerAI.__init__(self, air)
        self.air = air

    def generate(self):
        MagicWordManagerAI.generate(self)

    def announceGenerate(self):
        MagicWordManagerAI.announceGenerate(self)

    def d_setAvatarRich(self, avId, zoneId):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setMoney(av.getMaxMoney())
        
    def d_setToonMax(self, avId, zoneId):
        if avId not in self.air.doId2do:
            return
        
        av = self.air.doId2do[avId]
            
        emotes = list(av.getEmoteAccess())
        for emoteId in OTPLocalizer.EmoteFuncDict.values():
           if emoteId >= len(emotes):
              continue
           if emoteId in (17, 18, 19):
              continue
           emotes[emoteId] = 1
        av.b_setEmoteAccess(emotes)
        
        av.b_setCogParts(
            [
              CogDisguiseGlobals.PartsPerSuitBitmasks[0],
              CogDisguiseGlobals.PartsPerSuitBitmasks[1],
              CogDisguiseGlobals.PartsPerSuitBitmasks[2],
              CogDisguiseGlobals.PartsPerSuitBitmasks[3]
            ]
        )
        
        av.b_setCogLevels([49] * 4)
        av.b_setCogTypes([7, 7, 7, 7])

        hoods = list(ToontownGlobals.HoodsForTeleportAll)
        av.b_setHoodsVisited(hoods)
        av.b_setTeleportAccess(hoods)  

        av.b_setMoney(av.getMaxMoney())
        av.b_setBankMoney(10000)
        
        av.b_setQuestCarryLimit(4)
        
        av.b_setQuests([])
        av.b_setRewardHistory(Quests.ELDER_TIER, [])
        
        if simbase.wantPets:
            av.b_setPetTrickPhrases(range(7))
        
        av.b_setMaxHp(ToontownGlobals.MaxHpLimit)
        av.toonUp(av.getMaxHp() - av.hp)

    def d_setMaxBankMoney(self, avId, zoneId):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setBankMoney(av.getMaxBankMoney())
        
    def d_setTeleportAcess(self, avId, zoneId):
        if avId not in self.air.doId2do:
            return
        
        av = self.air.doId2do[avId]    
        av.b_setTeleportAccess([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000])
        av.b_setHoodsVisited([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000])
        av.b_setZonesVisited([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000])

    def d_setAvatarToonUp(self, avId, zoneId):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setHp(av.getMaxHp())
        
    def d_setCogIndex(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return
            
        if not -1 <= num <= 3:
            return 

        av = self.air.doId2do[avId]
        av.b_setCogIndex(num)
        
    def d_setPinkSlips(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setPinkSlips(num)

    def d_setNewSummons(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return

        (suitIndex, type) = num.split(' ')
        av = self.air.doId2do[avId]
        av.b_setCogSummonsEarned(suitIndex)
        av.addCogSummonsEarned(suitIndex, type)
        
    def d_restockUnites(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        num = min(num, 32767)
        av.restockAllResistanceMessages(num)
        
    def d_setName(self, avId, zoneId, string):
        if avId not in self.air.doId2do:
            return
            
        (firstPart, secondPart, thirdPart, fourthPart) = string.split(' ')
        av = self.air.doId2do[avId]
        name = firstPart + secondPart + thirdPart + fourthPart
        av.b_setName(name)

    def d_setTickets(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setTickets(num)
 
    def d_startHoliday(self, holidayId):
        #Theres probably a better way going about this, 
        #But this will do for now.
        self.air.newsManager.d_startHoliday(holidayId)
        
    def d_endHoliday(self, holidayId):
        #Theres probably a better way going about this, 
        #But this will do for now.
        self.air.newsManager.d_endHoliday(holidayId)
     
    def d_sendSystemMessage(self, message, style):
        #This one may not work completely do to MW permanter splitting issues.
        self.air.newsManager.d_sendSystemMessage(message, style)

    def d_setCogPageFull(self, avId, zoneId, num):
        if avId not in self.air.doId2do:
            return

        av = self.air.doId2do[avId]
        av.b_setCogStatus([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        av.b_setCogCount([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    def setMagicWord(self, magicWord, avId, zoneId):
        avId = self.air.getAvatarIdFromSender()
        actualMagicWord = magicWord[1:]

        if actualMagicWord == 'rich':
            self.d_setMaxBankMoney(avId, zoneId)
        elif actualMagicWord == 'maxBankMoney':
            self.d_setAvatarRich(avId, zoneId)
        elif actualMagicWord == 'maxToon':
            self.d_setToonMax(avId, zoneId)
        elif actualMagicWord == 'toonUp':
            self.d_setAvatarToonUp(avId, zoneId)
        elif actualMagicWord == 'enableTpAll':
            self.d_setTeleportAcess(avId, zoneId)
        elif actualMagicWord == 'startHoliday':
            self.d_startHoliday(holidayId=actualMagicWord[len('startHoliday') + 1:])
        elif actualMagicWord == 'endHoliday':
            self.d_endHoliday(holidayId=actualMagicWord[len('endHoliday') + 1:])
        elif actualMagicWord == 'smsg':      
            pass #In till i can split correctly, This will be passed.
        elif actualMagicWord == 'cogIndex':
            self.d_setCogIndex(avId, zoneId, num=actualMagicWord[len('cogIndex') + 1:])
        elif actualMagicWord == 'unites':
            self.d_restockUnites(avId, zoneId, num=actualMagicWord[len('unites') + 1:])
        elif actualMagicWord == 'name':
            self.d_setName(avId, zoneId, string=actualMagicWord[len('name') + 1:])
        elif actualMagicWord == 'pinkSlips':
            self.d_setPinkSlips(avId, zoneId, num=actualMagicWord[len('pinkSlips') + 1:])
        elif actualMagicWord == 'tickets':
            self.d_setTickets(avId, zoneId, num=actualMagicWord[len('tickets') + 1:])
        elif actualMagicWord == 'newSummons':
            self.d_setNewSummons(avId, zoneId, num=actualMagicWord[len('newSummons') + 1:])
        elif actualMagicWord == 'cogPageFull':
            self.d_setCogPageFull(avId, zoneId, num=actualMagicWord[len('newSummons') + 1:])
        else:
            return

        MagicWordManagerAI.setMagicWord(self, magicWord, avId, zoneId)

    def disable(self):
        MagicWordManagerAI.disable(self)

    def delete(self):
        MagicWordManagerAI.delete(self)
