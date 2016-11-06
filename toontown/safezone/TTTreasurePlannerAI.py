# File: T (Python 2.4)

from toontown.toonbase.ToontownGlobals import *
import RegenTreasurePlannerAI
import DistributedTTTreasureAI

class TTTreasurePlannerAI(RegenTreasurePlannerAI.RegenTreasurePlannerAI):
    
    def __init__(self, zoneId):
        self.healAmount = 3
        RegenTreasurePlannerAI.RegenTreasurePlannerAI.__init__(self, zoneId, DistributedTTTreasureAI.DistributedTTTreasureAI, 'TTTreasurePlanner', 20, 5)

    
    def initSpawnPoints(self):
        self.spawnPoints = [
            (-59.899999999999999, -6.9000000000000004, 1.2), #Gazebo Treasure
            (-90.599999999999994, -3.0, -0.75),
            (17.8089, -93.6201, 3.025),
            (94.200000000000003, 33.5, 4),
            (35.399999999999999, 43.100000000000001, 4),
            (67.099999999999994, 105.5, 2.5),
            (-99.150000000000006, -87.340699999999998, 0.52498999999999996),
            (1.6058600000000001, -119.492, 3.0249999999999999),
            (33.0573, -60.9531, 4.025),
            (129.137, -61.9039, 2.5249999999999999),
            (92.989999999999995, -159.399, 3.0249999999999999), #Party Hat Treasure
            (111.749, -8.5992700000000006, 4.5746599999999997),
            (41.999000000000002, -30.292300000000001, 4.0250000000000004),
            (31.064900000000002, -43.914900000000003, 4.0250000000000004),
            (10.015599999999999, 105.218, 2.5249999999999999),
            (66, 172.1, 3), #The Out Of Bounds One From TTO, Left out of bounds for classical feel. It got moved to out bounds in TTO when Goofy Speedway was added.
            (100.68000000000001, 93.989599999999996, 2.5249999999999999),
            (129.285, 58.610700000000001, 2.5249999999999999),
            (-28.627199999999998, 85.9833, 0.52500000000000002),
            (-114.613, 86.172700000000006, 0.52500000000000002),
            (-132.52799999999999, 31.254999999999999, 0.025000000000000001)]
        return self.spawnPoints

