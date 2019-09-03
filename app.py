import os, math, random
from settings import Settings
from game import Game

def main():
    print('Starting Bot')
    game = Game()
    game.loop()
    game.quit()

if __name__ == '__main__':
	main()