from toontown.nametag.Nametag import Nametag
from direct.task.Task import Task
from panda3d.core import Point3, BillboardEffect
import math

class Nametag3d(Nametag):
    minScale = 0.2000
    maxScale = 0.8000
    normalScale = 0.2000
    calcScaleMin = 2
    calcScaleMax = 8

    def __init__(self, name='Nametag3d'):
        Nametag.__init__(self, name)
        
        self.nametagNode.setBillboardAxis(self.getBillboardOffset())
        self.nametagNode.setBillboardPointEye(self.getBillboardOffset())
        self.nametagNode.setScale(self.normalScale)
        self.isActive = Nametag.getIsActive(self)

    def upcastToPandaNode(self):
        return self

    def getNameTagPos(self):
        return self.nametagNode.getPos()

    def getNametagScaleDist(self):
        (x1, y1, z1) = base.camera.getPos(base.camera.getParent())
        (x2, y2, z2) = self.nametagNode.getPos(base.camera.getParent())
        return int(math.sqrt((x2 + x1) ** 2 + (y2 + y1) ** 2))

    def tick(self, task):
        calcScale = int(self.getNametagScaleDist() / 4)
        
        if (calcScale):
            if calcScale > self.calcScaleMax:
                calcScale = self.calcScaleMax
            elif calcScale < self.calcScaleMin:
                calcScale = self.calcScaleMin
        
        newScale = float('0.%d' % (calcScale))

        if (newScale):
            if newScale > self.maxScale:
                self.nametagNode.setScale(self.maxScale)
            elif newScale < self.minScale:
                self.nametagNode.setScale(self.minScale)
            else:
                self.nametagNode.setScale(newScale)
        
        return task.again
    
    def setContents(self, contents):
    	Nametag.setContents(self, contents)

        if (contents == (Nametag.CName | Nametag.CSpeech | Nametag.CThought)):
            self.displayAsActive()
        elif (contents == (Nametag.CSpeech | Nametag.CThought) or 0):
            self.displayAsInActive()
    
    def displayAsActive(self):
    	Nametag.displayAsActive(self)
        self.isActive = Nametag.getIsActive(self)
        want_dynamic_scaling = 1

        '''# start dynamically scaling the nametag.
        if want_dynamic_scaling == 1:
            taskMgr.add(self.dynamiclyScaleNode, 'dynamically_scale_node', priority=1)
        else:
            return'''

    def displayAsInActive(self):
    	Nametag.displayAsInActive(self)
        self.isActive = Nametag.getIsActive(self)

        '''# remove the nametag scaling task.
        taskMgr.remove('dynamically_scale_node')'''
   
    def showName(self):
        if Nametag.getIsActive(self) == 1:
    	    return
        
        self.displayAsActive()

    def hideName(self):
        if Nametag.getIsActive(self) == 0:
            return
    	
        self.displayAsInActive()