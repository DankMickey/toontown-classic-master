import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPLocalizer
from direct.interval.IntervalGlobal import *
from otp.otpbase import OTPLocalizer
from toontown.estate import GardenGlobals

class CatalogGardenItem(CatalogItem.CatalogItem):
    sequenceNumber = 0

    def makeNewItem(self, itemIndex = 0, count = 3, tagCode = 1):
        self.gardenIndex = itemIndex
        self.numItems = count
        self.giftCode = tagCode
        CatalogItem.CatalogItem.makeNewItem(self)

    def getPurchaseLimit(self):
        if self.gardenIndex == GardenGlobals.GardenAcceleratorSpecial:
            return 1
        else:
            return 100

    def reachedPurchaseLimit(self, avatar):
        if self in avatar.onOrder and self in avatar.mailboxContents or self in avatar.onGiftOrder:
            return 1
        else:
            return 0

    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.CatalogAcceptGarden

        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    def saveHistory(self):
        return 1

    def getTypeName(self):
        return TTLocalizer.GardenTypeName

    def getName(self):
        return GardenGlobals.Specials[self.gardenIndex]['photoName']