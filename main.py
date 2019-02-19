from gamelogic import Columns
from settings import Settings
import pygame

print("\nWelcome to my game Columns 2!\nThis is a custom remake of the classic video game \
Columns created by Jay Geertsen in 1989\nIf you enjoy this game, feel free to check \
out my other projects @ github.com/tommyli3318\n")


settings = Settings()
pygame.init()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Columns 2')
pygame.font.init()


def text_to_screen(text, screen, pos, color=(0,0,0), f=40):
	font = pygame.font.SysFont("Impact",f)
	text_obj = font.render(text, True, color)
	d = text_obj.get_rect()
	#center text
	pos = (settings.screen_width/2.4+(pos[0]-d.width)/2, pos[1])
	screen.blit(text_obj, pos)

def button(text, x,y, width, height, i_c, a_c):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + width > cur[0] > x and y + height > cur[1] > y:
		pygame.draw.rect(screen, a_c, (x,y,width,height))
		if click[0] == 1:
			return text
	else:
		pygame.draw.rect(screen, i_c, (x,y,width,height))
	text_to_screen(text, screen, (x,y))


def menu():
	'''menu for the game'''
	while True:
		screen.fill(settings.bgColor)
		# display menus
		text_to_screen("Columns 2", screen, (settings.screen_width/6, settings.screen_height/20), (255,255,255), 50)
		text_to_screen(f"Your last score: {new_score}",screen,(settings.screen_width/6,110),(255,255,255),20)
		text_to_screen(f"Your highest score: {high_score}",screen,(settings.screen_width/6,150),(255,255,255),20)

		if button("Easy", settings.screen_width/6,settings.screen_height/3,200,50, (50,190,120), (128,255,152)) != None:
			return "e"
		elif button("Normal", settings.screen_width/6,settings.screen_height/3+100,200,50, (100,120,255), (180,180,255)) != None:
			return "n"
		elif button("Hard", settings.screen_width/6,settings.screen_height/3+200,200,50, (190,190,0), (255,255,0)) != None:
			return "h"
		elif button("Insane", settings.screen_width/6,settings.screen_height/3+300,200,50, (150,45,45), (255,45,45)) != None:
			return "i"
		pygame.display.flip()
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()


def run_game():
	'''driver for the game'''
	diff = menu()
	if diff == 'e':
		settings.ic = 3
		settings.gm = 0.25
	elif diff == 'n':
		settings.ic = 4
		settings.gm = 1
	elif diff == 'h':
		settings.ic = 5
		settings.gm = 1.5
	else:
		settings.ic = 7
		settings.gm = 4

	gl = Columns(settings,screen)
	return gl.runGame()

new_score = 0.0
high_score = 0.0

while True:
	# write to a file to keep track of all time high score
	try:
		with open("high_score.txt",'r') as log:
			high_score = float(log.read())
	except:
		with open("high_score.txt",'w') as log:
			log.write('0.0')

	try:
		# game loop, exit on exception
		new_score = run_game()
		if new_score > high_score:
			with open("high_score.txt",'w') as log:
				log.write(str(new_score))
		settings.timer = 500
	except:
		print("Thanks for playing Columns 2!")
		break
