class Settings():
	"""settings for the game"""
	def __init__(self):
		self.screen_width = 300
		self.screen_height = 600
		self.width = 50
		self.height = 50
		self.bgColor = (0,0,0)
		self.timer = 500
		self.blocksize = 50
		self.ic = 4
		self.gm = 1

		#makes a list of 10 different colors
		gray = (128,128,128)
		white = (224,224,224)
		red = (255,102,102)
		orange = (255,178,102)
		yellow = (255,255,102)
		green = (178,255,102)
		blue = (102,178,255)
		purple = (178,102,255)
		pink = 	(255,204,255)
		lightBlue = (204,255,255)
		self.colors = [gray,white,red,orange,yellow,green,blue,purple,pink,lightBlue]

if __name__ == '__main__':
	print("Please launch the game by running main.py")

	