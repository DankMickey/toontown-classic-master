from toontown.nametag.Nametag2d import Nametag2d

class NametagFloat2d(Nametag2d):

    def __init__(self):
        Nametag2d.__init__(self, 'NametagFloat2d')

    def upcastToPandaNode(self):
        Nametag2d.upcastToPandaNode(self)