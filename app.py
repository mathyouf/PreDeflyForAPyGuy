import os, pygame, math, random
from pygame.locals import *
from settings import Settings
from game import Game

def main():

	game = Game()
	game.loop()
	game.quit()

if __name__ == '__main__':
	main()