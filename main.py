from gamelogic import Columns
from settings import Settings
import pygame
import time

settings = Settings()

def run_game():
	'''driver for the game'''
	pygame.init()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption('Columns 2')
	gl = Columns(settings,screen)
	return gl.runGame()

h_s = 0

print("\nWelcome to my game Columns 2!\nThis is a custom remake of the classic video game \
Columns created by Jay Geertsen in 1989\nIf you enjoy this game, feel free to check \
out my other projects @ github.com/tommyli3318\n")

print("For each of the following prompts, type in your response and hit the ENTER key:\
\nType 'quit' anytime to exit\n")

while True:
	diff_i = input("\n\nChoose a difficulty (e[asy],n[ormal],h[ard],i[nsane]): ")
	while not diff_i in ('e','easy','n','normal','h','hard','i','insane','quit'):
		diff_i = input("Invalid input, please enter 'e','n','h',or 'i ('quit' to exit)': ")

	if diff_i == 'quit':
		print("Thanks for playing!")
		time.sleep(1)
		break
	elif diff_i in ('e','easy'):
		settings.ic = 3
	elif diff_i in ('n','normal'):
		settings.ic = 4
	elif diff_i in ('h','hard'):
		settings.ic = 5
	else:
		settings.ic = 7

	new_score = run_game()
	# keep track of high score
	if new_score > h_s:
		h_s = new_score
	settings.timer = 500

	print(f"Your current highest score: {h_s}\n")
	p_a = input("Play again? (y/n): ")
	while p_a not in ('y','n'):
		p_a = input("Invalid input, please enter 'y' or 'n': ")
	if p_a == 'n':
		print("Thanks for playing!")
		time.sleep(1)
		break