import os
import keyboard
from settings import Settings
from processGameState import gameState


class Game():
    def __init__(self):
        pass

    def loop(self):
        try:
            gameState().takeScreenShot()
        except KeyboardInterrupt:
            pass
                
    def quit(self):
        pass
