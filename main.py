from gamelogic import Columns
from settings import Settings
import pygame

def run_game():
	'''driver for the game'''
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption('Columns 2')
	gl = Columns(settings,screen)
	gl.runGame()


#while True:
	#input("")
run_game()

#asdjasopdjwaoijd