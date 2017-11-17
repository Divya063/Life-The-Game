#life_main.py
import random
import time
import os
import life_events

class Player:
	#Class to make player objects
	def __init__(self, gender):
		self.gender = gender
		self.age = 0
		
	def getName(self):
		"""Give the player a name from their gender"""
		
		if self.gender == 'M':
			try:
				with open('life_data/life_husbandNames.txt','r') as file:
					lit = []
					for lines in file:
						lit.append(lines.strip('\n'))
						
					self.name = random.choice(lit)
					
			except FileNotFoundError:
				print('from func "getName" error FileNotFoundError')
				time.sleep(2)
				quit()
		
		elif self.gender == 'F':
			try:
				with open('life_data/life_wifeNames.txt') as file:
					lit = []
					for lines in file:
						lit.append(lines.strip('\n'))
						
					self.name = random.choice(lit)
					
			except FileNotFoundError:
				print('from func "getName" error FileNotFoundError')
				time.sleep(2)
				quit()
					
	def getPartner(self):
		"""Give the player their partners name"""
	
		if self.gender == 'M':
			try:
				with open('life_data/life_wifeNames.txt', 'r') as file:
					lit = []
					for lines in file:
						lit.append(lines.strip('\n'))
						
					self.partner = random.choice(lit)
					
			except FileNotFoundError:
				print('from func "getPartner" error FileNotFoundError')
				time.sleep(2)
				quit()
				
		elif self.gender == 'F':
			try:
				with open('life_data/life_husbandNames.txt','r') as file:
					lit = []
					for lines in file:
						lit.append(lines.strip('\n'))
						
				self.partner = random.choice(lit)
			
			except FileNotFoundError:
				print('from func "getPartner" error FileNotFoundError')
				time.sleep(2)
				quit()
				
	def getDeathAge(self):
		"""Calculate when the player will die, from the age of 80 to 110"""
		
		lit = list(range(80, 110))
		self.deathAge = random.choice(lit)
		
	def getJobName(self):
		"""Gives the player the name of their company that they will work at"""
	
		try:
			with open('life_data/life_conames.txt','r') as file:
				list = []
				for lines in file:
					list.append(lines.strip('\n'))
					
				self.jobName = random.choice(list)
				
		except FileNotFoundError:
			print('from func "getJobName" error FileNotFoundError')
			time.sleep(2)
			quit()
			
	def luckyOrNot(self):
		"""Chooses if the player is going to be lucky or not."""
		lit = ['lucky','unlucky']
		self.luck = random.choice(lit)
			
	def birthday(self):
		"""Ages the player"""
		self.age += 1
		print('You are now {} years old.'.format(self.name))
			
	def init(self):
		"""Initializes the player"""
		Player.getName(self)
		Player.getPartner(self)
		Player.getDeathAge(self)
		Player.getJobName(self)
		
	def checkIfDead(self):
		lit = list(range(0, 101))
		lit.append('die')
		if self.age == self.deathAge: endGame('age')
		
		elif random.choice(lit) == 'die': endGame('random')
	
		else: pass
		
	def printInfo(self):
		print('Info:\n')
		print('Name:',self.name)
		print('Age:',self.age)
		print('Gender:',self.gender)
		input('Press enter to continue')
		
class Graphics:
	#Class to call the differnt menus
	def bigMenu():
		with open('life_graphics/life_menu.txt','r') as file:
			menu = file.read()
			return menu

	def smallMenu():
		with open('life_graphics/life_port_menu.txt','r') as file:
			menu = file.read()
			return menu
			
def endGame(type):
	#Causes the end of the game
	if type == 'age':
		print('Your age has come. You have died of old age.')
		time.sleep(2)
		menu()
		
	elif type == 'random':
		print('You have died of a random unknown cause')
		time.sleep(2)
		menu()
		
	else:
		print('from func "endGame" custom error "Unknown arg"')
		time.sleep(2)
		quit()
	
def makeCharater():
	#Create a player object
	global player
	lit = ['M','F']
	sum = random.choice(lit)
	player = Player(sum)
	player.init()
	menu()
	
def menu():
	#Prints menu.
	while True:
		os.system('cls')
		print(Graphics.bigMenu())
		ask = input('Life/Command>').lower()
		
		if ask == 's':
			print('Starting...')
			time.sleep(1)
			gameLoop()
			
		elif ask == 'i':
			player.printInfo()
			
		elif ask == 'g':
			print('Re-generating...')
			time.sleep(1)
			makeCharater()
			
		else:
			print("Sorry, I didn't understand that!")
			time.sleep(2)
			continue
			
def gameLoop():
	#Starts gameloop
	while True:
		os.system('cls')
		player.checkIfDead()
		ask = input(Graphics.smallMenu())
	
	
makeCharater()#Starts game