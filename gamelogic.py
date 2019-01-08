import pygame, random

class Columns():
	'''
	game logic for the video game Columns
	'''
	#make a grid board, 12 by 6 (50 by 50)
	#creating fallers 
	#moving and rotating them
	#and having them freeze

	def __init__(self, settings, screen):
		'''assigns instance variables for the class'''
		self.run = True
		self.settings = settings
		self.screen = screen
		self.timer = 500
		#important info for blocks: x pos, y pos, color
		self.blocks = []
		#creates the first faller
		self.createFaller()
		#adds USEREVENT for making the faller drop every second
		self.dropTime = pygame.USEREVENT + 1
		#TESTING
		pygame.time.set_timer(self.dropTime, self.timer)
		#makes a dictionary of "roofs" that will keep track of when a faller should freeze
		#keys should match x values, possible x values: 0, 50, 100, 150, 200, 250
		#values are the y values ("roofs") of each x value
		self.bottom = self.settings.screen_height - 50
		self.roof = {"0": self.bottom, "50": self.bottom, "100": self.bottom, "150": self.bottom, "200": self.bottom, "250": self.bottom}
		self.score = 0

	def rungame(self):
		'''main loop of the game'''
		while self.run:
			#gameloop goes here
			self.checkEvent()
			self.updateScreen()
			self.checkGameOver()
		
	def checkLeft(self) -> bool:
		'''checks if the faller can move to the left by comparing its Y value and value of the roof to the left'''
		#self.faller[2][1] is the x value of the bottommost block of the faller
		#self.faller[2][2] is the y value of the bottommost block of the faller
		return(self.roof[str(self.faller[2][1]-50)] >= self.faller[2][2])

	def checkRight(self) -> bool:
		'''checks if the faller can move to the right by comparing its Y value and value of the roof to the right'''
		#self.faller[2][1] is the x value of the bottommost block of the faller
		#self.faller[2][2] is the y value of the bottommost block of the faller
		return(self.roof[str(self.faller[2][1]+50)] >= self.faller[2][2])

	def checkFreeze(self):
		'''determines if current faller should freeze'''
		#it should freeze if y value of bottom block matches the respective "roof"
		#looks up in the roof dictionary with the x value to find the y "roof" value
		if self.faller[2][2] >= self.roof[str(self.faller[2][1])]:
			#update dictionary, freeze current faller, create new faller 
			self.roof[str(self.faller[2][1])] -= 150
			self.blocks += self.faller
			#creates new faller
			self.createFaller()

	def checkEvent(self):
		'''checks all events of the game'''
		#short circuits so self.checkLeft() and self.checkRight() don't run into out of bound errors
		for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
					# quit if the q key or exit button is pressed
					self.run = False
				elif event.type == self.dropTime:
					#this ordering makes fallers freeze at the next "tick" of time after they have landed
					#drop the faller every second
					self.checkFreeze()
					self.dropFaller()
					self.checkMatching()
					self.dropBlocks()
				elif event.type == pygame.KEYDOWN:
					#moves the faller to the left, checks conditions to see if it is allowed to move left
					if event.key == pygame.K_LEFT and self.faller[0][1] > 0 and self.checkLeft():
						for block in self.faller:
							#block[1] is the x value
							block[1] -= 50
					#moves the faller to the right, checks conditions to see if it is allowed to move right
					elif event.key == pygame.K_RIGHT and self.faller[0][1] < self.settings.screen_width - self.settings.width and self.checkRight():
						for block in self.faller:
							#faller[1] is the x value
							block[1] += 50
					#rotates faller
					elif event.key == pygame.K_SPACE:
						self.rotateFaller()

	def createFaller(self):
		'''creates a faller, stores color, x, and y in a 2D list. Two blocks, but never all three, can be the same color.'''
		#grabs two unique numbers from 0 to 9, puts them into a list
		#TESTING
		#index = random.sample(range(0, 9), 2)
		index = random.sample(range(0, 4), 2)
		#this implementation ensures that the faller will not have 3 blocks of the same color
		color1 = self.settings.colors[index[0]]
		color2 = self.settings.colors[index[1]]
		#TESTING
		color3 = random.choice(self.settings.colors[0:4])
		#randomizes the x position where the faller appears
		x1 = random.choice([0,50,100,150,200,250])
		x2 = x1
		x3 = x1
		#makes the fallers appear with only bottom block visible
		y1 = -150
		y2 = -100
		y3 = -50
		#creates a new faller
		self.faller = [[color1,x1,y1],[color2,x2,y2],[color3,x3,y3]]

	def rotateFaller(self):
		'''rotates the faller when spacebar is pressed'''
		#rotates the faller, bottom block becomes top and the rest move down
		#self.faller = [[color1,x1,y1],[color2,x2,y2],[color3,x3,y3]]
		#color is self.faller[x][0] where x can be 0,1, or 2
		temp = self.faller[2][0]
		self.faller[2][0] = self.faller[1][0]
		self.faller[1][0] = self.faller[0][0]
		self.faller[0][0] = temp

	def dropFaller(self):
		'''drops the faller down one block'''
		#makes each block fall down
		for block in self.faller:
			#block[2] is the y of each block
			block[2] += 50

	def updateScreen(self):
		'''updates the screen'''
		self.screen.fill(self.settings.bgColor)
		#draw (window,color, (x,y, width, height))
		#draws frozen blocks
		if len(self.blocks) > 0:
			for bl in self.blocks:
				pygame.draw.rect(self.screen, bl[0], (bl[1], bl[2], self.settings.width, self.settings.height))
		#draws blocks in the faller
		for block in self.faller:
			pygame.draw.rect(self.screen, block[0], (block[1], block[2], self.settings.width, self.settings.height))
		pygame.display.flip()
		pygame.display.update()

	def checkMatching(self):
		'''checks for matching color blocks (3 in a row vertically, horizontally, or diagonally), and removes them'''
		# should check self.blocks, remove blocks, drop blocks, update roofs
		# idea: make a removeList and remove everything at the end
		if len(self.blocks) >= 3:
			removeList = []
			for bl in self.blocks:
				#check for vertical matching
				if [bl[0], bl[1], bl[2]+50] in self.blocks and [bl[0], bl[1], bl[2]+100] in self.blocks:
					#add the blocks to removeList
					removeList.append([bl[0], bl[1], bl[2]])
					removeList.append([bl[0], bl[1], bl[2]+50])
					removeList.append([bl[0], bl[1], bl[2]+100])

				#checks for horizontal matching
				if [bl[0], bl[1]+50, bl[2]] in self.blocks and [bl[0], bl[1]+100, bl[2]] in self.blocks:
					#add the blocks to removeList
					removeList.append([bl[0], bl[1], bl[2]])
					removeList.append([bl[0], bl[1]+50, bl[2]])
					removeList.append([bl[0], bl[1]+100, bl[2]])

				#check for diagonal matching
				if [bl[0], bl[1]+50, bl[2]+50] in self.blocks and [bl[0], bl[1]+100, bl[2]+100] in self.blocks:
					removeList.append([bl[0], bl[1], bl[2]])
					removeList.append([bl[0], bl[1]+50, bl[2]+50])
					removeList.append([bl[0], bl[1]+100, bl[2]+100])
				if [bl[0], bl[1]+50, bl[2]-50] in self.blocks and [bl[0], bl[1]+100, bl[2]-100] in self.blocks:
					removeList.append([bl[0], bl[1], bl[2]])
					removeList.append([bl[0], bl[1]+50, bl[2]-50])
					removeList.append([bl[0], bl[1]+100, bl[2]-100])

			#if there's something to remove
			if len(removeList) > 0:
				# takes out duplicates from removeList to create uniqueRemoveList
				uniqueRemoveList = []
				for bl in removeList:
					if bl not in uniqueRemoveList:
						uniqueRemoveList.append(bl)
				# updates score accordingly, player gains more points for removing more blocks at once
				score_multiplier = len(uniqueRemoveList) - 2
				if score_multiplier > 0:
					self.score += 10 * score_multiplier
					print('Match! +' + str(10 * score_multiplier), ' Your Score: ' + str(self.score))
				# removes the blocks and update roof dictionary
				for block in uniqueRemoveList:
					self.roof[str(block[1])] += 50
					self.blocks.remove(block)
					#increases the drop speed
					if self.timer > 100:
						self.timer = int(self.timer*.99) + 1
						pygame.time.set_timer(self.dropTime, self.timer)

	def dropBlocks(self):
		'''drops blocks after blocks are matched and removed'''
		#grab the tallest block of each column, compare against roof, use that difference to update self.blocks
		for x in range(0,251,50):
			#makes a list of a single column of blocks
			column = []
			for bl in self.blocks:
				if bl[1] == x:
					column.append(bl)

			#makes a list of the y values for each block in column
			yList = []
			for blo in column:
				# check for continuous y's, if +100 or +200 exists but not +50, need to drop blocks
				yList.append(blo[2])
				yList.sort()
				#yList is a sorted list of y values for a column
			
			y = -1
			if len(yList)>0:
				if yList[-1] != 550:
					#there is empty space on the bottom row
					y = yList[-1]
				else:
					for i in range(1, len(yList)):
						if yList[i] - yList[i-1] != 50:
							#there is empty space
							y = yList[i-1] 
							break
				#y == -1 means no empty space
				if y == -1:
					continue
				ydiff = y - yList[0]
				#y is the topmost value of the empty space
				#ydiff is the value between y and the topmost block

				#drops blocks
				for yinc in range(0,ydiff+1, 50):
					for block in self.blocks:
						if block[1] == x and block[2] == y-yinc:
							block[2] += 50
							break

	def checkGameOver(self):
		'''exits the game if one column fills up'''
		min_value = min(self.roof.values()) + 50
		if min_value <= 0:
			self.run = False
			print("Game Over! Your final score: " + str(self.score))