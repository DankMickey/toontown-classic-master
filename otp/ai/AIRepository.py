import os, string, threading
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from direct.distributed.AstronInternalRepository import AstronInternalRepository
from toontown.distributed.ToontownDistrictAI import ToontownDistrictAI
from toontown.distributed.ToontownDistrictStatsAI import ToontownDistrictStatsAI
from toontown.hood.TTHoodDataAI import TTHoodDataAI
from toontown.hood.DDHoodDataAI import DDHoodDataAI
from toontown.hood.BRHoodDataAI import BRHoodDataAI
from toontown.hood.MMHoodDataAI import MMHoodDataAI
from toontown.hood.DGHoodDataAI import DGHoodDataAI
from toontown.hood.OZHoodDataAI import OZHoodDataAI
from toontown.hood.GZHoodDataAI import GZHoodDataAI
from toontown.hood.GSHoodDataAI import GSHoodDataAI
from toontown.hood.DLHoodDataAI import DLHoodDataAI
from toontown.hood.CSHoodDataAI import CSHoodDataAI
from toontown.hood.BossbotHQDataAI import BossbotHQDataAI
from toontown.hood.CashbotHQDataAI import CashbotHQDataAI
from toontown.hood.LawbotHQDataAI import LawbotHQDataAI
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from otp.distributed import OtpDoGlobals
from toontown.ai.TrophyManagerAI import TrophyManagerAI
from toontown.dnaparser import DNAParser
from toontown.dnaparser.DNAParser import *
from direct.distributed.MsgTypes import *
from toontown.ai.HolidayManagerAI import HolidayManagerAI
from otp.ai.AIZoneData import AIZoneDataStore
from toontown.ai.WelcomeValleyManagerAI import WelcomeValleyManagerAI
from toontown.ai.NewsManagerAI import NewsManagerAI
from otp.ai.TimeManagerAI import TimeManagerAI
from toontown.ai.ToontownMagicWordManagerAI import ToontownMagicWordManagerAI
from toontown.safezone.SafeZoneManagerAI import SafeZoneManagerAI
from toontown.estate.EstateManagerAI import EstateManagerAI
from toontown.pets.PetManagerAI import PetManagerAI
from toontown.tutorial.TutorialManagerAI import TutorialManagerAI
from toontown.toon import NPCToons
from toontown.ai.QuestManagerAI import QuestManagerAI
from toontown.coghq.FactoryManagerAI import FactoryManagerAI
from toontown.coghq.MintManagerAI import MintManagerAI
from toontown.coghq.LawOfficeManagerAI import LawOfficeManagerAI
from toontown.suit.SuitInvasionManagerAI import SuitInvasionManagerAI
from toontown.coghq.CountryClubManagerAI import CountryClubManagerAI
from toontown.racing.DistributedRacePadAI import DistributedRacePadAI
from toontown.fishing.FishManagerAI import FishManagerAI
from toontown.uberdog.DistributedPartyManagerAI import DistributedPartyManagerAI
from toontown.parties.PartyManagerAI import PartyManagerAI

class AIRepository(AstronInternalRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('AIRepository')
    GameGlobalsId = OtpDoGlobals.OTP_DO_ID_TOONTOWN

    def __init__(self, baseChannel, serverId, districtName, dcFileNames, dcSuffix='AI'):
        AstronInternalRepository.__init__(self, baseChannel=baseChannel, serverId=serverId, dcFileNames=dcFileNames, dcSuffix=dcSuffix)
        self.districtName = districtName
        self.zoneTable = { }
        self.dnaDataMap = { }
        self.dnaStoreMap = { }
        self.buildingManagers = { }
        self.suitPlanners = { }
        self.hoodsStarted = [ ]
        self.fishingPonds = { }
        self.viewingPads = { }
        self.fishingSpots = { }
        self.wantCogdominiums = config.GetBool('want-cog-dominiums', True)
        self.wantTrackClsends = config.GetBool('want-track-clsends', False)
        self.doLiveUpdates = config.GetBool('want-do-live-updates', False)
        self.useAllMinigames = config.GetBool('use-all-minigames', True)
        self.wantAprilFools = config.GetBool('want-april-fools', True) # Disable this on release.
        self.zoneDataStore = AIZoneDataStore()
        self.zoneAllocator = UniqueIdAllocator(ToontownGlobals.DynamicZonesBegin, ToontownGlobals.DynamicZonesEnd)
        self.valleyZoneAllocator = UniqueIdAllocator(ToontownGlobals.WelcomeValleyBegin, ToontownGlobals.WelcomeValleyEnd)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender() >> 32) & 0xFFFFFFFF

    def handleConnected(self):
        AstronInternalRepository.handleConnected(self)
        self.createShardObject()

    def createShardObject(self):
        self.acceptOnce('districtGenerated', self.handleDistrictGenerated)
        
        self.districtId = self.allocateChannel()
        self.district = ToontownDistrictAI(self, name=self.districtName)
        self.district.generateWithRequiredAndId(doId=self.districtId,
    											parentId=self.GameGlobalsId,
    											zoneId=OtpDoGlobals.OTP_ZONE_ID_DISTRICTS)

        dg = PyDatagram()
        dg.addServerHeader(simbase.air.districtId, simbase.air.ourChannel, STATESERVER_OBJECT_SET_AI)
        dg.addChannel(simbase.air.ourChannel)
        simbase.air.send(dg)

    def handleDistrictGenerated(self, doId, name):
    	self.notify.info('ToontownDistrictAI generated with doId: %d and name: %s' % (doId, name))
        # create npc details in zones.
        if config.GetBool('want-npcs', True):
            NPCToons.generateZone2NpcDict()

        self.createGlobals()
        self.createHoodData()
    	
    	self.district.b_setAvailable(1)

    def createGlobals(self):
        self.districtStats = ToontownDistrictStatsAI(self, districtId=self.districtId)
        self.districtStats.generateWithRequiredAndId(doId=self.allocateChannel(),
                                                    parentId=self.GameGlobalsId,
                                                    zoneId=OtpDoGlobals.OTP_ZONE_ID_DISTRICTS_STATS)

        self.trophyMgr = TrophyManagerAI(self)

        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.holidayManager = HolidayManagerAI(self)
        self.holidayManager.start()

        self.welcomeValleyManager = WelcomeValleyManagerAI(self)
        self.welcomeValleyManager.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.magicWordMgr = ToontownMagicWordManagerAI(self)
        self.magicWordMgr.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.safeZoneMgr = SafeZoneManagerAI(self)
        self.safeZoneMgr.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.estateMgr = EstateManagerAI(self)
        self.estateMgr.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.petMgr = PetManagerAI(self)
        
        self.tutorialMgr = TutorialManagerAI(self)
        self.tutorialMgr.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.questManager = QuestManagerAI(self)

        self.factoryMgr = FactoryManagerAI(self)
        
        self.mintMgr = MintManagerAI(self)
        
        self.officeMgr = LawOfficeManagerAI(self)

        self.suitInvasionManager = SuitInvasionManagerAI(self)

        self.countryClubMgr = CountryClubManagerAI(self)
        
        self.fishingManager = FishManagerAI(self)

        self.partyManager = DistributedPartyManagerAI(self)
        self.partyManager.generateWithRequired(OtpDoGlobals.OTP_ZONE_ID_MANAGEMENT)

        self.partyCreationMgr = PartyManagerAI(self)

    def storeDNAMapHood(self, zoneId, dnaFileName):
        AIRepository.loadDNAFileAI(self.dnaStoreMap[zoneId], dnaFileName)

    def createGolfCartBlocks(self, zoneId, index):
        self.dnaDataMap[zoneId].add(DNANode('viewing_pad_%d' % (index)))

        # TODO: Starting blocks:
        self.dnaDataMap[zoneId].add(DNANode('starting_block_%d' % (1)))
        # ----------------------

        self.viewingPads['pads'][zoneId]['viewing_pad_%d' % (index)] = DistributedRacePadAI(self, zoneId)
        self.viewingPads['pads'][zoneId]['viewing_pad_%d' % (index)].generateWithRequired(zoneId)
    
    def createFishingSpotBlocks(self, zoneId, index):
        if ZoneUtil.isCogHQZone(zoneId):
            return
        if zoneId == ToontownGlobals.OutdoorZone:
            return
        if zoneId == ToontownGlobals.GoofySpeedway:
            return
        self.dnaDataMap[zoneId] = DNAData('fishing_spot_%d' % (index))
        self.dnaDataMap[zoneId].add(DNANode('fishing_spot_%d' % (index)))
        self.fishingManager.createSpotsInZone(zoneId, self.dnaDataMap[zoneId])
        
        

    def storeDNAData(self, zoneId):
        if zoneId == ToontownGlobals.OutdoorZone:
            self.dnaDataMap[zoneId] = DNAData('picnic_table_%d' % (1))
            self.dnaDataMap[zoneId].add(DNANode('picnic_table_%d' % (2)))
        elif zoneId == ToontownGlobals.GolfZone:
            self.dnaDataMap[zoneId] = DNAData('viewing_pad_%d' % (1))

            self.viewingPads['pads'] = { }
            self.viewingPads['pads'][zoneId] = { }
            self.viewingPads['pads'][zoneId]['viewing_pad_%d' % (1)] = DistributedRacePadAI(self, zoneId)
            self.viewingPads['pads'][zoneId]['viewing_pad_%d' % (1)].generateWithRequired(zoneId)
            
            for x in range(1, 2):
                self.createGolfCartBlocks(zoneId, x)


    def storeHoodData(self, zoneId, hoodObj):
        self.zoneTable[zoneId] = [[zoneId, hoodObj, 1, 1]]
        self.dnaStoreMap[zoneId] = DNAStorage()

        if zoneId in ToontownGlobals.HoodHierarchy:
            ext = ''
            if zoneId == ToontownGlobals.DonaldsDock:
                ext = 'phase_6/dna/donalds_dock_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_6/dna/donalds_dock_sz.dna')
            elif zoneId == ToontownGlobals.ToontownCentral:
                ext = 'phase_5/dna/toontown_central_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_4/dna/toontown_central_sz.dna')
            elif zoneId == ToontownGlobals.TheBrrrgh:
                ext = 'phase_8/dna/the_burrrgh_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_8/dna/the_burrrgh_sz.dna')
            elif zoneId == ToontownGlobals.MinniesMelodyland:
                ext = 'phase_6/dna/minnies_melody_land_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_6/dna/minnies_melody_land_sz.dna')
            elif zoneId == ToontownGlobals.DaisyGardens:
                ext = 'phase_8/dna/daisys_garden_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_8/dna/daisys_garden_sz.dna')
            elif zoneId == ToontownGlobals.DonaldsDreamland:
                ext = 'phase_8/dna/donalds_dreamland_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_8/dna/donalds_dreamland_sz.dna')
            elif zoneId == ToontownGlobals.GoofySpeedway:
                ext = 'phase_6/dna/goofy_speedway_sz.dna'
            elif zoneId == ToontownGlobals.OutdoorZone:
                ext = 'phase_6/dna/outdoor_zone_sz.dna'
            elif zoneId == ToontownGlobals.SellbotHQ:
                ext = 'phase_9/dna/cog_hq_sellbot_%d.dna'
                self.storeDNAMapHood(zoneId, 'phase_9/dna/cog_hq_sellbot_sz.dna')
            elif zoneId == ToontownGlobals.CashbotHQ:
                ext = 'phase_10/dna/cog_hq_cashbot_sz.dna'
            elif zoneId == ToontownGlobals.LawbotHQ:
                ext = 'phase_11/dna/cog_hq_lawbot_sz.dna'
            else:
                self.notify.warning('Could not load DNA for hood: %d' % zoneId)
                # This hood's dna could not have been loaded but its still a hood
                # so we must call startup for it.
                self.startupHoodData(zoneId, hoodObj)
                return
            
            streets = ToontownGlobals.HoodHierarchy[zoneId]
            for zone in streets:
                try:
                    AIRepository.loadDNAFileAI(self.dnaStoreMap[zoneId], ext % zone)
                except:
                    try:
                        AIRepository.loadDNAFileAI(self.dnaStoreMap[zoneId], ext)
                    except:
                        self.notify.warning('Could not find zone: %d to generate!' % zoneId)
        
        self.storeDNAData(zoneId)
        self.fishingManager.createPondInZone(zoneId)
        self.createFishingSpotBlocks(zoneId, 4)
        self.partyCreationMgr.createPartyGateInZone(zoneId)
        self.startupHoodData(zoneId, hoodObj)

    def startupHoodData(self, zoneId, hoodObj):
        if zoneId not in self.hoodsStarted:
            if zoneId in ToontownGlobals.hoodNameMap:
                self.notify.info('Staring up hood: %s with zoneId: %d' % (ToontownGlobals.hoodNameMap[zoneId][2], zoneId))

            hoodObj.startup()
            # Append the hood zone to the started list after its done generating all its
            # objects.
            self.hoodsStarted.append(zoneId)

    def createHoodData(self):
        self.storeHoodData(zoneId=ToontownGlobals.DonaldsDock, hoodObj=DDHoodDataAI(self, zoneId=ToontownGlobals.DonaldsDock))
        self.storeHoodData(zoneId=ToontownGlobals.ToontownCentral, hoodObj=TTHoodDataAI(self, zoneId=ToontownGlobals.ToontownCentral))
        self.storeHoodData(zoneId=ToontownGlobals.TheBrrrgh, hoodObj=BRHoodDataAI(self, zoneId=ToontownGlobals.TheBrrrgh))
        self.storeHoodData(zoneId=ToontownGlobals.MinniesMelodyland, hoodObj=MMHoodDataAI(self, zoneId=ToontownGlobals.MinniesMelodyland))
        self.storeHoodData(zoneId=ToontownGlobals.DaisyGardens, hoodObj=DGHoodDataAI(self, zoneId=ToontownGlobals.DaisyGardens))
        self.storeHoodData(zoneId=ToontownGlobals.OutdoorZone, hoodObj=OZHoodDataAI(self, zoneId=ToontownGlobals.OutdoorZone))
        self.storeHoodData(zoneId=ToontownGlobals.GolfZone, hoodObj=GZHoodDataAI(self, zoneId=ToontownGlobals.GolfZone))
        self.storeHoodData(zoneId=ToontownGlobals.GoofySpeedway, hoodObj=GSHoodDataAI(self, zoneId=ToontownGlobals.GoofySpeedway))
        self.storeHoodData(zoneId=ToontownGlobals.DonaldsDreamland, hoodObj=DLHoodDataAI(self, zoneId=ToontownGlobals.DonaldsDreamland))
        self.storeHoodData(zoneId=ToontownGlobals.SellbotHQ, hoodObj=CSHoodDataAI(self, zoneId=ToontownGlobals.SellbotHQ))
        self.storeHoodData(zoneId=ToontownGlobals.CashbotHQ, hoodObj=CashbotHQDataAI(self, zoneId=ToontownGlobals.CashbotHQ))
        self.storeHoodData(zoneId=ToontownGlobals.LawbotHQ, hoodObj=LawbotHQDataAI(self, zoneId=ToontownGlobals.LawbotHQ))
        self.storeHoodData(zoneId=ToontownGlobals.BossbotHQ, hoodObj=BossbotHQDataAI(self, zoneId=ToontownGlobals.BossbotHQ))

    @staticmethod
    def loadDNAFileAI(dnaStore, dnaFileName):
        DNAParser.loadDNAFileAI(dnaStore, dnaFileName)

    @staticmethod
    def lookupDNAFileName(dnaFileName):
        for _ in range(3, 13):
            if os.path.exists('resources/phase_%d/dna/%s' % (_, dnaFileName)):
                return 'phase_%d/dna/%s' % (_, dnaFileName)

    def lostConnection(self):
        AstronInternalRepository.lostConnection(self)
        self.holidayManager.stop()

        for zoneId in self.buildingManagers:
            self.buildingManagers[zoneId].cleanup()
            del self.buildingManagers[zoneId]
        
        for zoneId in self.zoneTable:
            if zoneId in self.hoodsStarted:
                self.zoneTable[zoneId][0][1].shutdown()
                self.hoodsStarted.remove(zoneId)
                del self.zoneTable[zoneId]
        
        self.fishingManager.cleanup()

    def allocateZone(self, isValley=False):
        if isValley:
            return self.valleyZoneAllocator.allocate()

        return self.zoneAllocator.allocate()

    def deallocateZone(self, zoneId, isValley=False):
        if isValley:
            self.valleyZoneAllocator.free(zoneId)
            return

        self.zoneAllocator.free(zoneId)

    def getTrackClsends(self):
        return self.wantTrackClsends

    def incrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() + 1)

    def decrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() - 1)

    def sendQueryToonMaxHp(self, doId, checkResult):
        pass

    def sendSetZone(self, do, zoneId):
        self.sendSetLocation(do, do.parentId, zoneId)

    def _isValidPlayerLocation(self, parentId, zoneId):
        if not parentId:
            return False

        if zoneId > ToontownGlobals.DynamicZonesEnd:
            return False
        
        if zoneId == 0:
            return False

        return True

    def getZoneDataStore(self):
        return self.zoneDataStore

    def getAvatarExitEvent(self, doId):
        if doId not in self.doId2do:
            return None

        return 'delete-%d' % doId

    def findFishingPonds(self, dnaData, zoneId, area):
        if dnaData in self.dnaDataMap:
            fishingPond = self.fishingPonds[zoneId]
            if fishingPond.getArea() == area:
                return fishingPond

    def findFishingSpots(self, dnaData, zoneId):   
            fishingSpotGroups = []
            fishingSpots = []
            for x in range(dnaData.getNumChildren()):
                dnaGroup = dnaData.at(x)
                fishingSpotId = dnaGroup.getName().split('_')[2]
                fishingSpotGroups.append(dnaGroup)
                try:
                    fishingSpots.append(self.fishingSpots['spots'][zoneId][dnaGroup.getName()])
                except:
                    pass
                
                return (fishingSpots, fishingSpotGroups)


    def findRacingPads(self, dnaData, zoneId, area, type = '', overrideDNAZone = False):
        viewPadGroups = []
        viewPads = []

        if overrideDNAZone:
            for x in range(dnaData.getNumChildren()):
                dnaGroup = dnaData.at(x)
                viewPadId = dnaGroup.getName().split('_')[2]
                viewPadGroups.append(dnaGroup)
                try:
                    viewPads.append(self.viewingPads['pads'][zoneId][dnaGroup.getName()])
                except:
                    pass

        return (viewPads, viewPadGroups)

    def findStartingBlocks(self, dnaGroup, distRacePad, zoneId=0):
        startingBlocks = []
        if zoneId:
            dnaData = self.dnaDataMap[zoneId]
            for x in range(dnaData.getNumChildren()):
                actualDnaGroup = dnaData.at(x)
                viewPadId = actualDnaGroup.getName().split('_')[2]
                startingBlocks = self.zoneTable[zoneId][0][1].findStartingBlocks(actualDnaGroup, distRacePad)

        return startingBlocks





