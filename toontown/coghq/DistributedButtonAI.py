# File: D (Python 2.4)

from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
import DistributedSwitchBase
import DistributedSwitchAI

class DistributedButtonAI(DistributedSwitchAI.DistributedSwitchAI):
    setColor = DistributedSwitchBase.stubFunction
    setModel = DistributedSwitchBase.stubFunction

