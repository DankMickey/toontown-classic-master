import json
import os

class ToontownSettings:

    def __init__(self):
        self.userData = 'userdata/'
        self.settings = self.userData + 'properties.json'

        # Render engine library names
        self.GL = 'pandagl'
        self.DX7 = 'pandadx7' # Unknown?
        self.DX8 = 'pandadx8'
        self.DX9 = 'pandadx9'

    def readSettings(self):
        if not os.path.exists(self.settings):
            self.writeSettings()

        with open(self.settings, 'rb') as properties:
            jdata = json.loads(properties.read())
            self.setWindowedMode(jdata['setWindowedMode'])
            self.setMusic(jdata['setMusic'])
            self.setSfx(jdata['setSfx'])
            self.setToonChatSounds(jdata['setToonChatSounds'])
            self.setMusicVolume(jdata['setMusicVolume'])
            self.setSfxVolume(jdata['setSfxVolume'])
            self.setResolution(jdata['setResolution'])
            properties.close()

        return

    def writeSettings(self):
        fields = {
            'setWindowedMode': True, \
            'setMusic': True, \
            'setSfx': True, \
            'setToonChatSounds': True, \
            'setMusicVolume': 0.1, \
            'setSfxVolume': 0.7, \
            'setResolution': 1 \
        }

        with open(self.settings, 'w+') as properties:
            properties.write(json.dumps(fields, properties, indent=4))
            properties.close()

        return

    def setWindowedMode(self, wantWindowedMode):
        self.wantWindowedMode = wantWindowedMode

    def getWindowedMode(self):
        return self.wantWindowedMode

    def setMusic(self, wantMusic):
        self.wantMusic = wantMusic

    def getMusic(self):
        return self.wantMusic

    def setSfx(self, wantSfx):
        self.wantSfx = wantSfx

    def getSfx(self):
        return self.wantSfx

    def setToonChatSounds(self, wantToonChatSounds):
        self.wantToonChatSounds = wantToonChatSounds

    def getToonChatSounds(self):
        return self.wantToonChatSounds

    def setMusicVolume(self, musicVolume):
        self.musicVolume = musicVolume

    def getMusicVolume(self):
        return self.musicVolume

    def setSfxVolume(self, sfxVolume):
        self.sfxVolume = sfxVolume

    def getSfxVolume(self):
        return self.sfxVolume

    def setResolution(self, resolution):
        self.resolution = resolution

    def getResolution(self):
        return self.resolution

    def getEmbeddedMode(self):
        return False

    def doSavedSettingsExist(self):
        if os.path.exists(self.settings):
            return True

        return False

    def getAcceptingNewFriends(self):
        return True # TODO: add to config!

    def getAcceptingNonFriendWhispers(self):
        return True # TODO: add to config!