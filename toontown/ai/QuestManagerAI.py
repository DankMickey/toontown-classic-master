from toontown.toon.DistributedNPCSpecialQuestGiverAI import DistributedNPCSpecialQuestGiverAI
from toontown.building import FADoorCodes
from toontown.hood import ZoneUtil
from toontown.quest import Quests

QuestIdIndex = 0
QuestFromNpcIdIndex = 1
QuestToNpcIdIndex = 2
QuestRewardIdIndex = 3
QuestProgressIndex = 4


class QuestManagerAI:

    def __init__(self, air):
        self.air = air

    def toonPlayedMinigame(self, toon, toons):
        pass
        
    def requestInteract(self, toon, npc):
        pass
        
    def avatarQuestChoice(self, toon, npc):
        pass
        
    def avatarChoseQuest(self, todo1, todo2, todo3, todo4, todo5):
        pass
        
    def npcGiveTrackChoice(self, toon, tier):
        pass
        
    def avatarCancelled(self, npcId):
        npc = self.air.doId2do.get(npcId)
        if not npc:
            return
        taskMgr.remove(npc.uniqueName('clearMovie'))