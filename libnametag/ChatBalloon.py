from panda3d.core import *

class ChatBalloon(NodePath):
    TEXT_SHIFT = (0.1, -0.05, 1.1)
    TEXT_SHIFT_REVERSED = -0.05
    TEXT_SHIFT_PROP = 0.08
    NATIVE_WIDTH = 10.0
    MIN_WIDTH = 2.5
    MIN_HEIGHT = 1
    BUBBLE_PADDING = 0.3
    BUBBLE_PADDING_PROP = 0.05
    BUTTON_SCALE = 6
    BUTTON_SHIFT = (-0.2, 0, 0.6)
    FRAME_SHIFT = (0.2, 1.4)

    def __init__(self, modelNode):
        self.modelNode = modelNode