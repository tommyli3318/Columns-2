from gamelogic import Columns
from settings import Settings
import pygame

def run_game():
	'''driver for the videogame Columns, closes the game if player loses'''
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption('Columns')
	gl = Columns(settings,screen)
	gl.rungame()

run_game()