# File: t (Python 2.4)

import ActiveCell
from direct.directnotify import DirectNotifyGlobal

class DirectionalCell(ActiveCell.ActiveCell):
    notify = DirectNotifyGlobal.directNotify.newCategory('DirectionalCell')
    
    def __init__(self, cr):
        ActiveCell.ActiveCell.__init__(self, cr)


