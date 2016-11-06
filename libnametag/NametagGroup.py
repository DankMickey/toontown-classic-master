from NametagUtil import *
from toontown.nametag.Nametag3d import Nametag3d
from toontown.nametag.Nametag2d import Nametag2d
from toontown.nametag import NametagGlobals

class NametagGroup:
    CCNormal = CCNormal
    CCNonPlayer = CCNonPlayer
    CCFreeChat = CCFreeChat
    CCSpeedChat = CCSpeedChat
    CCSuit = CCSuit
    CCNoChat = CCNoChat
    CCToonBuilding = CCToonBuilding  

    def __init__(self):
        self.avatar = None
        self.font = None
        self.uniqueId = ''
        self.displayName = ''
        self.numChatPages = 0
        self.chatString = ''
        self.colorCode = 0
        self.name = ''
        self.uniqueId = ''
        self.displayName = ''
        self.numChatPages = 0
        self.isActive = 0
        self.pageNumber = 0
        self.numNametags = 0
        self.stompChatText = ''
        self.visible3d = True
        self.nameFg = VBase4(0.3, 0.3, 0.7, 1)
        self.nameBg = VBase4(1, 1, 1, 1)
        self.tickTask = taskMgr.add(self.tick, 'nametag', sort=45)
        self.nametag3d = Nametag3d()
        self.nametag2d = Nametag2d()
        self.nametags = [ ]
     
    def manage(self, manager):
        if self.nametag3d:
            self.addNametag(self.nametag3d)
 
        if self.nametag2d:
            self.addNametag(self.nametag2d)
 
    def unmanage(self, manager):
        if self.nametag3d:
            self.removeNametag(self.nametag3d)
 
        if self.nametag2d:
            self.removeNametag(self.nametag2d)
 
    def addNametag(self, nameNode):
        if nameNode not in self.nametags:
            self.nametags.append(nameNode)
 
    def removeNametag(self, nameNode):
        if nameNode in self.nametags:
            self.nametags.remove(nameNode)
     
    def getNametag3d(self):
        return self.nametag3d
     
    def getNametag2d(self):
        return self.nametag2d
     
    def getNumChatPages(self):
        return self.numChatPages
     
    def setChat(self, chatString, flags):
        self.chatString = chatString
        self.updateTags()
     
    def getChat(self):
        return self.chatString
 
    def setQtColor(self, color):
        self.color = color
     
    def clearChat(self):
        if len(self.chatString) > 0:
            self.chatString[len(self.chatString):]
     
    def setActive(self, isActive):
        self.isActive = isActive
        self.getNametag3d().setIsActive(isActive)
        self.updateTags()
     
    def hasButton(self):
        pass # TODO!
 
    def clearShadow(self):
        pass # TODO!
     
    def isActive(self):
        return self.isActive
 
    def updatePageNumbers(self):
        self.numChatPages += 1
     
    def getNameIcon(self):
        return self.getNametag3d().getNametagIcon()
     
    def getUniqueId(self):
        return self.uniqueId
 
    def setObjectCode(self, code):
        self.uniqueId = ('nametag-%d' % (code))
         
    def getStompText(self):
        pass
      
    def getStompDelay(self):
        pass
      
    def setNameWordwrap(self, wordWrap, nametag):
        if nametag in self.nametags:
            nametag.setChatWordwrap(wordWrap)
            
    def getChatStomp(self):
        return len(self.chatString)
        
    def getNameTagPos(self):
        self.nametag3d.getNameTagPos()
    
    def manage(self, manager):
        if self.nametag3d:
            self.addNametag(self.nametag3d)

        if self.nametag2d:
            self.addNametag(self.nametag2d)

    def unmanage(self, manager):
        if self.nametag3d:
            self.removeNametag(self.nametag3d)

        if self.nametag2d:
            self.removeNametag(self.nametag2d)

    def addNametag(self, nameNode):
        if nameNode not in self.nametags:
            self.nametags.append(nameNode)

    def removeNametag(self, nameNode):
        if nameNode in self.nametags:
            self.nametags.remove(nameNode)
    
    def getNametag3d(self):
        return self.nametag3d
    
    def getNametag2d(self):
        return self.nametag2d
    
    def setAvatar(self, avatar):
        self.avatar = avatar
        self.getNametag3d().setAvatar(avatar)
        self.updateTags()
    
    def setFont(self, font):
        self.font = font
        self.getNametag3d().setFont(font)
        self.updateTags()
         
    
    def setColorCode(self, colorCode):
        self.colorCode = colorCode
        self.getNametag3d().setColorCode(colorCode)
        self.updateTags()
    
    def setName(self, name):
        self.name = name
        self.getNametag3d().setName(name)
        self.updateTags()
    
    def setDisplayName(self, name):
        self.name = name
        self.getNametag3d().setName(name)
        self.updateTags()
    
    def getNumChatPages(self):
        return self.numChatPages
    
    def setChat(self, chatString, flags):
        self.chatString = chatString
        self.updateTags()
    
    def getChat(self):
        return self.chatString

    def setQtColor(self, color):
        self.color = color
        self.updateTags()
    
    def clearChat(self):
        if len(self.chatString) > 0:
            self.chatString[len(self.chatString):]
    
    def setActive(self, isActive):
        self.isActive = isActive
        self.getNametag3d().setIsActive(isActive)
    
    def hasButton(self):
        pass # TODO!

    def clearShadow(self):
        pass # TODO!
    
    def isActive(self):
        return self.isActive

    def setContents(self, contents):
        self.getNametag3d().setContents(contents)
        
    def setNameWordWrap(self, wrap):
        self.getNametag3d().setNameWordWrap(wrap)
    
    def setPageNumber(self, pageNumber):
        self.pageNumber = pageNumber
        self.updatePageNumbers()
        self.updateTags()
    
    def updatePageNumbers(self):
        self.numChatPages += 1
    
    def getNameIcon(self):
        return self.getNametag3d().getNametagIcon()
        
    def setUniqueId(self, code):
        self.setObjectCode(code)
    
    def getUniqueId(self):
        return self.uniqueId

    def setObjectCode(self, code):
        self.uniqueId = ('nametag-%d' % (code))
        self.updateTags()
       
    def getObjectCode(self):
        return self.uniqueId
        
    def getStompText(self):
        pass
     
    def getStompDelay(self):
        pass

    def getChatStomp(self):
        return len(self.chatString)
        
    def displayAsActive(self):
        if self.isActive:
            return
            
        self.isActive = self.getNametag3d().isActive
        self.getNametag3d().displayAsActive()
        
    def displayAsInActive(self):
        if not self.isActive:
            return
        
        self.isActive = self.getNametag3d().isActive
        self.getNametag3d().displayAsInActive()
        
    def getClickState(self):
        return self.getNametag3d().getClickState()
        
    def updateTags(self):
        if self.colorCode == 0:
            self.colorCode = CCNormal
        elif self.colorCode == 1:
            self.colorCode = CCNoChat
        elif self.colorCode == 2:
            self.colorCode = CCNonPlayer
        elif self.colorCode == 3:
            self.colorCode = CCSuit
        elif self.colorCode == 4:
            self.colorCode = CCToonBuilding
        elif self.colorCode == 7:
            self.colorCode = CCSpeedChat
        elif self.colorCode == 8:
            self.colorCode = CCFreeChat
        else:
            self.colorCode = CCNormal
        if self.colorCode in NametagGlobals.NametagColors:
            self.nameFg = NametagGlobals.NametagColors[self.colorCode][self.getClickState()]
        for nametag in self.nametags:
            nametag.font = self.font
            nametag.name = self.name
            nametag.nameFg = self.nameFg
            nametag.nameBg = self.nameBg
            nametag.isActive = self.isActive
            nametag.displayName = self.displayName
            nametag.colorCode = self.colorCode
            nametag.avatar = self.avatar
            nametag.setTextColor(self.nameFg)
            nametag.update()
        
    def tick(self, task):
        if not self.nametag2d:
           return
        if not self.nametag3d:
           return
        
        return task.cont

