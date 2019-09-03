import os
import keyboard
from settings import Settings
from processGameState import gameState


class Game():
    def __init__(self):
        pass

    def loop(self):
        x = 1
        try:
            while True:
                gameState().takeScreenShot()
        except KeyboardInterrupt:
            pass
                
    def quit(self):
        pass
