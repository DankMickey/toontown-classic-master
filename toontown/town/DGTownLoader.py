import TownLoader
import DGStreet
from toontown.suit import Suit
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *

class DGTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        if base.cr.newsManager:
            holidayIds = base.cr.newsManager.getDecorationHolidayId()
            if ToontownGlobals.HALLOWEEN_COSTUMES in holidayIds:
                self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_owl1.ogg', 'phase_4/audio/sfx/SZ_TC_owl2.ogg', 'phase_4/audio/sfx/SZ_TC_owl3.ogg'])
                self.cricketSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_owl1.ogg', 'phase_4/audio/sfx/SZ_TC_owl2.ogg', 'phase_4/audio/sfx/SZ_TC_owl3.ogg'])
            else:
                self.birdSound = map(base.loadSfx, ['phase_8/audio/sfx/SZ_DG_bird_01.ogg', 'phase_8/audio/sfx/SZ_DG_bird_02.ogg', 'phase_8/audio/sfx/SZ_DG_bird_03.ogg', 'phase_8/audio/sfx/SZ_DG_bird_04.ogg'])
                self.cricketSound = map(base.loadSfx, ['phase_4/audio/sfx/cricket_chirp.ogg'])
        self.streetClass = DGStreet.DGStreet
        self.musicFile = 'phase_8/audio/bgm/DG_SZ.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/DG_SZ.ogg'
        self.townStorageDNAFile = 'phase_8/dna/storage_DG_town.dna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_8/dna/daisys_garden_' + str(self.canonicalBranchZone) + '.dna'
        self.createHood(dnaFile)

    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)
