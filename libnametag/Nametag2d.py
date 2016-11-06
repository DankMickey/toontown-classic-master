from toontown.nametag.Nametag import Nametag

class Nametag2d(Nametag):

    def __init__(self, name='Nametag2d'):
        Nametag.__init__(self, name)

    def upcastToPandaNode(self):
        return self

	def setContents(self, contents):
		Nametag.setContents(self, contents)

        if contents == (0 & Nametag.CName | Nametag.CSpeech):
            self.displayAsActive()
        elif contents == (Nametag.CName | Nametag.CSpeech & Nametag.CName | Nametag.CSpeech):
            self.displayAsInActive()

    def displayAsActive(self):
        pass
    
    def displayAsInActive(self):
        pass