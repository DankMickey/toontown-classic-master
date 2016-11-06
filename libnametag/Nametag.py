from panda3d.core import *
from NametagUtil import *
from direct.task.Task import Task
from toontown.nametag import NametagGlobals

class Nametag(PandaNode):
    CSpeech = CSpeech
    CThought = CThought
    CName = CName

    def __init__(self, name):
        PandaNode.__init__(self, name)
        self.avatar = None
        self.font = None
        self.colorCode = 0
        self.name = ''
        self.contents = 0
        self.isActive = 0
        self.textNode = None
        self.text = None
        self.chatWordWrap = 10.0
        self.billboardOffset = 2
        self.nameFg = VBase4(0.3, 0.3, 0.7, 1)
        self.nameBg = VBase4(1, 1, 1, 1)
        self.nametagIcon = NodePath('nametagIcon')
        self.nametagNode = NodePath.anyPath(self).attachNewNode('nametag')

    def displayAsActive(self):
        if (not self.font) or (self.isActive):
            return

        # Lets clear the nametagNode, to prevent any issues.
        if (not self.nametagNode.isEmpty()):
            self.nametagNode.node().removeAllChildren()

        textNode = self.nametagNode.attachNewNode(TextNode('nameText'), 1)
        self.textNode = textNode
        self.text = self.textNode.node()
        self.text.setFont(self.font)
        self.text.setTextColor(self.nameFg)
        self.text.setAlign(TextNode.ACenter)
        self.text.setWordwrap(self.getChatWordwrap())
        self.text.setText(self.sortNameCharacters(self.getName()))
        textNode.setScale(0.90)

        nametagModel = NametagGlobals.nametagCardModel
        if not nametagModel:
            card = loader.loadModel('phase_3/models/props/panel')
            nametagModel = card
            nametagCardDimensions = VBase4(-0.5, 0.5, -0.5, 0.5)
        
        nametagCard = nametagModel.copyTo(self.nametagNode, 0)
        nametagCard.setColor(VBase4(1, 1, 1, 1))
        nametagCard.setTransparency(TransparencyAttrib.MAlpha)
        self.sidePadding = 0.23
        self.topPadding = 0.13
        nametagCard.setScale(textNode, (textNode.node().getLeft() - textNode.node().getRight() - 0.15), 
            1, (textNode.node().getTop() + self.topPadding - textNode.node().getBottom()))
        nametagCard.setTwoSided(1, 0)
        nametagCard.setColorScale(VBase4(0.8, 0.8, 0.8, 0.5))

        # Adjust the card acording to the nametag text node.
        nametagCard.setPos(textNode.getBounds().getCenter())
        nametagCard.setScissor(textNode.node().getLeft(), textNode.node().getRight(), 
            textNode.node().getBottom(), textNode.node().getTop())

        # Move text infront of nametag.
        textNode.setY(nametagCard.getY() - 0.03)
        textNode.setAttrib(DepthWriteAttrib.make(0))
        
        #Add in our tick task.
        self.tickTaskName = str(self.getUniqueName()) + '-tick'
        self.tickTask = taskMgr.add(self.tick, self.tickTaskName, priority=1)

    def displayAsInActive(self):
        if self.isActive:
            if not self.nametagNode.isEmpty():
                #If the tick task still exists; Remove it.
                if self.tickTask is not None:
                    taskMgr.remove(self.tickTask)
                    self.tickTask = None
                
                self.nametagNode.node().removeAllChildren()
                

            self.setIsActive(0)

    def sortNameCharacters(self, name):
        nameParts = list(name.split(' '))
        if len(nameParts) == 1:
            namePart = nameParts[0]
            return ('%s' % (namePart))
        elif len(nameParts) == 2:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            return ('%s %s' % (namePart, namePart_0))
        elif len(nameParts) == 3:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            namePart_1 = nameParts[2]
            return ('%s %s\n%s' % (namePart, namePart_0, namePart_1))
        elif len(nameParts) == 4:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            namePart_1 = nameParts[2]
            namePart_2 = nameParts[3]
            return ('%s %s\n%s %s' % (namePart, namePart_0, namePart_1, namePart_2))
        elif len(nameParts) == 5:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            namePart_1 = nameParts[2]
            namePart_2 = nameParts[3]
            namePart_3 = nameParts[4]
            namePart_4 = namePart[5]
            return ('%s %s\n%s %s\n%s' % (namePart, namePart_0, namePart_1, namePart_2, namePart_3, namePart_4))
        elif len(nameParts) == 6:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            namePart_1 = nameParts[2]
            namePart_2 = nameParts[3]
            namePart_3 = nameParts[4]
            namePart_4 = namePart[5]
            namePart_5 = nameParts[6]
            return ('%s %s\n%s %s\n%s %s' % (namePart, namePart_0, namePart_1, namePart_2, namePart_3, namePart_4, namePart_5))
        elif len(nameParts) == 7:
            namePart = nameParts[0]
            namePart_0 = nameParts[1]
            namePart_1 = nameParts[2]
            namePart_2 = nameParts[3]
            namePart_3 = nameParts[4]
            namePart_4 = namePart[5]
            namePart_5 = nameParts[6]
            namePart_6 = nameParts[7]
            return ('%s %s\n%s %s\n%s %s\n%s' % (namePart, namePart_0, namePart_1, namePart_2, namePart_3, namePart_4, namePart_5, namePart_6))

    def upcastToClickablePopup(self):
        pass

    def downcastToNametag2d(self):
        pass

    def setIsActive(self, isActive):
        self.isActive = isActive
        self.update()

    def getIsActive(self):
        return self.isActive

    def setChatWordwrap(self, chatWordWrap):
        self.chatWordWrap = chatWordWrap
        self.update()

    def getChatWordwrap(self):
        return self.chatWordWrap

    def setAvatar(self, avatar):
        self.avatar = avatar
        self.update()

    def getAvatar(self):
        return self.avatar

    def clearAvatar(self):
        self.avatar = None

    def setFont(self, font):
        self.font = font
        self.update()

    def getFont(self):
        return self.font

    def setColorCode(self, colorCode):
        self.colorCode = colorCode
        self.update()

    def getColorCode(self):
    	return self.colorCode      
        
    def setWordwrap(self, wrap):
        self.nametagWordWrap = wrap
        self.update()
        
    def setNameWordWrap(self, wordWrap):
        self.setWordwrap(wordWrap)
      
    def setName(self, name):
        self.name = name
        self.update()

    def getName(self):
        return self.name

    def getNametagIcon(self):
        return self.nametagIcon

    def setContents(self, contents):
        self.contents = contents
        self.update()

    def setBillboardOffset(self, billboardOffset):
        self.billboardOffset = billboardOffset
        self.update()
        
    def setTextColor(self, color):
        if not self.text:
            return
        
        if __debug__:
            print("%s: Setting Nametag Color to %s" % (self.getUniqueName(), str(color)))
        self.text.setTextColor(color)

    def getBillboardOffset(self):
        return self.billboardOffset
        
    def getUniqueName(self):
        return 'Nametag-' + str(id(self))
        
    #Temporary till we get ClickablePopups working.  
    def getClickState(self): 
        return 0
        
    def update(self):
        if not self.avatar:
            self.hideName()
        elif not self.font:
            self.hideName()     
        elif self.name and not self.isActive:
            self.showName()
        else:
            pass #Have nothing else to fill this spot.
            
    def tick(self, task):
        return Task.done  
            
    def showName(self):
        pass
      
    def hideName(self):
        pass