from panda3d.core import NodePath
import math, random

class CMover:

    def __init__(self, objNodePath, fwdSpeed, rotSpeed):
        self.objNodePath = objNodePath
        self.fwdSpeed = fwdSpeed
        self.rotSpeed = rotSpeed
        self.cImpluses = [ ]
        self.currDt = None

    def integrate(self):
		pass

    def getNodePath(self):
        return self.objNodePath
       
    def setFwdSpeed(self, fwdSpeed):
        self.fwdSpeed = fwdSpeed
    
    def getFwdSpeed(self):
		return self.fwdSpeed

    def setRotSpeed(self, rotSpeed):
        self.rotSpeed = rotSpeed
       
    def getRotSpeed(self):
		return self.rotSpeed
	
    def addRotShove(self, rotVel):
		pass # This is suppose to calculate the value from "rotVel" and set the pets rotation acordingly.
	
    def addShove(self, vel):
		pass # This is suppose to calculate the value from "vel" and set the pets position acordingly.
    
    def processCImpulses(self, dt):
		if dt in self.cImpluses:
			self.cImpluses.remove(dt)
		
		self.cImpluses.append(dt)
		self.currDt = dt
	
    def getDt(self):
		if self.currDt not in self.cImpluses:
			return None
		
		return self.currDt

