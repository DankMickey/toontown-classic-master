import __builtin__
import sys
import os
import time
import types

class Main:

    def __init__(self):
        self.userData = 'userdata/'
        self.resourcesDir = 'resources/'
        self.logsDir = self.userData + 'logs/'
        self.logPrefix = 'toontownclassic-'
        self.isPandaWindowOpen = False

    def setup(self):
        self.prepareDirs()
        self.createNewLog()
        self.evaluateArguments()

    def setRegistry(self, type, value):
        # TODO!
        pass

    def getGame2Done(self):
        return True

    def isDummy(self):
        return True

    def setPandaErrorCode(self, errorCode):
        # TODO:
        pass

    def setPandaWindowOpen(self):
        if not self.isPandaWindowOpen:
            self.isPandaWindowOpen = True

    def getAccountServer(self):
        return ('')

    def getDeployment(self):
        return ('ToontownClassic-US')

    def getBlue(self):
        return ('')

    def getGameServer(self):
        if self.gameServer:
		    return self.gameServer
            
    def getInjectorRequest(self):
        if self.injectorWant:
            return self.injectorWant

    def getPlayToken(self):
        if self.playToken:
            return self.playToken
            
    def getUsername(self):
        if self.username:
            return self.username
    
    def getDISLToken(self):
        return ('')

    def getNeedPwForSecretKey(self):
        return False

    def setDisconnectDetailsNormal(self):
        pass

    def setIsNotNewInstallation(self):
        pass

    def setDisconnectDetails(self, index, message):
        pass

    def getPhaseComplete(self, phase):
        return True

    def isTestServer(self):
        return False

    def createNewLog(self):
        ltime = 1 and time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                                   ltime[3], ltime[4], ltime[5])

        logfile = self.logsDir + 'ToontownClassic-' + logSuffix + '.log'

        class LogAndOutput:
            def __init__(self, orig, log):
                self.orig = orig
                self.log = log

            def write(self, str):
                self.log.write(str)
                self.log.flush()
                self.orig.write(str)
                self.orig.flush()

            def flush(self):
                self.log.flush()
                self.orig.flush()

        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.__stdout__, log)
        logErr = LogAndOutput(sys.__stderr__, log)
        sys.stdout = logOut
        sys.stderr = logErr

    def prepareDirs(self):
        if not os.path.exists(self.userData):
            os.makedirs(self.userData)
            os.makedirs(self.logsDir)

        if not os.path.exists(self.resourcesDir):
            os.makedirs(self.resourcesDir)

    def evaluateArguments(self):
        playToken = os.environ.get('TOONTOWN_LOGIN_PLAYTOKEN')
        gameServer = os.environ.get('GAME_SERVER')
        wantDevInjector = os.environ.get('WANT_DEV_INJECTOR')
        if playToken != None:
            if len(playToken) == 0:
                sys.exit()
                return

        if gameServer != None:
            if len(gameServer) == 0:
                sys.exit()
                return

        if wantDevInjector:
            wantDevInjector = wantDevInjector
        else:
            wantDevInjector = False
		
        # TODO: implement a hash key from the launcher which it will generate one time, every time.
        # Looks like everything is ok, launch the game.
        self.startGame(playToken, gameServer, wantDevInjector)

    def startGame(self, playToken, gameServer, wantDevInjector):
        self.playToken = playToken
        self.gameServer = gameServer
        self.injectorWant = wantDevInjector
        self.username = self.playToken
        from toontown.toonbase import ToontownStart
        ToontownStart = ToontownStart
        
        return

__builtin__.launcher = Main()
launcher.setup()