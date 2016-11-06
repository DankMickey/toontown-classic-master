from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import random

COLORS = (Vec4(0.917, 0.164, 0.164, 1),
 Vec4(0.152, 0.75, 0.258, 1),
 Vec4(0.598, 0.402, 0.875, 1),
 Vec4(0.133, 0.59, 0.977, 1),
 Vec4(0.895, 0.348, 0.602, 1),
 Vec4(0.977, 0.816, 0.133, 1),
 Vec4(0.463, 0.79, 0.977, 1))

class ToontownLoadingScreen():
    __module__ = __name__

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.head = None
        screen = loader.loadModel('phase_3/models/gui/progress-background')
        self.gui = screen.find('**/gui')
        self.bg = screen.find('**/background')
        
        self.tip = DirectLabel(guiId='ToontownLoadingScreenTip', parent = self.gui, relief = None,
                                 text='', text_scale = TTLocalizer.TLStip, textMayChange = 1, pos=(-1, 0, -0.93),
                                 text_fg = (1, 1, 1, 1), text_wordwrap = 35, text_align = TextNode.ALeft,
                                 text_shadow = (0, 0, 0, 1))
                                 
        self.title = DirectLabel(guiId = 'ToontownLoadingScreenTitle', parent = self.gui, relief = None,
                                 pos = (0, 0, -0.77), text = '', textMayChange = 1, text_scale = 0.08,
                                 text_fg = (0, 0, 0.5, 1), text_align = TextNode.ACenter,
                                 text_font = ToontownGlobals.getSignFont())
                                 
        self.name = DirectLabel(guiId = 'ToontownLoadingScreenName', parent = self.gui, relief = None,
                                 pos = (0, 0, -0.63), text = '', textMayChange = 1, text_scale = 0.13,
                                 text_fg = (0, 0, 0.5, 1), text_align = TextNode.ACenter,
                                 text_font = ToontownGlobals.getSignFont())
                                 
        self.presenting = DirectLabel(guiId = 'ToontownLoadingScreenPresent', parent = self.gui, relief = None,
                                 pos = (0, 0, 0.77), text = '', textMayChange = 1, text_scale = 0.13,
                                 text_fg = (0, 0, 0.5, 1), text_align = TextNode.ACenter,
                                 text_font = ToontownGlobals.getSignFont())
                                 
        self.waitBar = DirectWaitBar(guiId = 'ToontownLoadingScreenWaitBar', parent = self.gui,
                                     frameSize = (-1.06, 1.06, -0.03, 0.03), pos = (0, 0, -0.85),
                                     text = '')

    def destroy(self):
        self.tip.destroy()
        self.title.destroy()
        self.name.destroy()
        self.presenting.destroy()
        self.waitBar.destroy()
        self.gui.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory):
        self.waitBar['range'] = range
        self.title['text'] = label
        self.tip['text'] = self.getTip(tipCategory)
        self.__count = 0
        self.__expectedCount = range
        if gui:
            if hasattr(base, 'localAvatar'):
                self.name['text'] = base.localAvatar.name
                self.presenting['text'] = TTLocalizer.Presenting
                for av in base.cr.avList:
                    if av.id == int(base.localAvatar.doId):
                        from toontown.toon import ToonHead          
                        self.bg.setColor(COLORS[av.position])
                        self.name['text_fg'] = COLORS[av.position]
                        self.presenting['text_fg'] = COLORS[av.position]
                        self.title['text_fg'] = COLORS[av.position] - 0.2
                        self.head = ToonHead.ToonHead()
                        self.head.setupHead(base.localAvatarStyle, forGui=1)
                        self.head.wrtReparentTo(render2dp)
                        self.head.setPos(0, 0, -0.2)
                        self.head.fitAndCenterHead(1, forGui=1)
                        self.head.setDepthOffset(2)
                        self.head.setBin('unsorted', 0, 1)
                        self.head.startBlink()
            else:
                self.name['text'] = ''
                self.presenting['text'] = ''
                self.bg.setColor(COLORS[6])
                self.title['text_fg'] = COLORS[6] - 0.2
                
            self.bg.reparentTo(render2dp, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
        else:
            self.waitBar.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.title.reparentTo(aspect2dp, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.name.reparentTo(self.gui)
        self.presenting.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.bg.reparentTo(hidden)
        if self.head:
            self.head.delete()
            self.head = None 
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)