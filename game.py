import os, pygame
import keyboard
from settings import Settings

class Game():
    def __init__(self):
        pass

    def loop(self):
        x = 1
        try:
            while True:
                x = x+1
                print(x)
        except KeyboardInterrupt:
            pass
                
    def quit(self):
        pass
