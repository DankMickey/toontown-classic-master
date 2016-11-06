# File: t (Python 2.4)

from pandac.PandaModules import *
import SafeZoneLoader
import TTPlayground
import random
from toontown.launcher import DownloadForceAcknowledge

class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.mid'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.mid'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.dna'

    
    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        library = self.geom.find('**/*toon_landmark_TT_library_DNARoot')
        libraryDoor = library.find('**/door_double_round_ur')
        '''libraryShadow = library.find('**/*Shadow2')
        for child in library.getChildren():
            print child
        libraryShadow.setPos(0, 8, 0)
        #libraryDoor.setEffect(DecalEffect.make())
        libraryDoor.setPos(0, -0.0032, 0)'''
        '''hqTT = self.geom.find('**/*toon_landmark_hqTT_DNARoot')
        hqTTHoleRight1 = hqTT.find('**/*doorFrameHoleRight_0')
        hqTTHoleLeft1 = hqTT.find('**/*doorFrameHoleLeft_0')
        hqTTHoleRight2 = hqTT.find('**/*doorFrameHoleRight_1')
        hqTTHoleLeft2 = hqTT.find('**/*doorFrameHoleLeft_1')
        hqTTHoleLeft1.setPos(0, -0.5, 0)
        hqTTHoleLeft2.setPos(0, 0.5, 0)
        hqTTHoleRight1.setPos(0, -0.5, 0)
        hqTTHoleRight2.setPos(0, 0.5, 0)'''
        libraryShadow = library.find('**/square_drop_shadow')
        #libraryShadow.setBin('fixed', 14)
        #libraryShadow.setPos(0, 0, 0)
        self.birdSound = map(base.loadSfx, [
            'phase_4/audio/sfx/SZ_TC_bird1.mp3',
            'phase_4/audio/sfx/SZ_TC_bird2.mp3',
            'phase_4/audio/sfx/SZ_TC_bird3.mp3'])

    
    def unload(self):
        del self.birdSound
        SafeZoneLoader.SafeZoneLoader.unload(self)

    
    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    
    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)


