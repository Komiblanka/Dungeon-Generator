from random import randint

class Dungeon:
	Size = ""
	Number_of_Themes = 0 
	Builder = ""


	def __init__(self):
		self.GenerateSize()
		self.GenerateNumberOfThemes()
		self.GenerateBuilder()

	def GenerateSize(self):
		Table = ["Small", "Medium", "Large", "Huge"]
		self.Size = CheckTable(Table) 
	
	def GenerateNumberOfThemes(self):
		DungeonSize = self.Size

		if DungeonSize == "Small":
			self.Number_of_Themes = randint(1, 4)
		elif DungeonSize == "Medium":
			self.Number_of_Themes = randint(1, 6)
		elif DungeonSize == "Large":
			self.Number_of_Themes = randint(1, 6) + 1
		elif DungeonSize == "Huge":
			self.Number_of_Themes = randint(1, 6) + 2
		else:
			self.Number_of_Themes = 0
	
	def GenerateBuilder(self):
		Table = ["aliens/precursors", 
			"demigod/demon"
			"natural (caves, etc.)", 
			"natural (caves, etc.)", 
			"religious order/cult", 
			"Humanoid (p49)", 
			"Humanoid (p49)", 
			"dwarves/gnomes", 
			"dwarves/gnomes", 
			"elves", 
			"wizard/madman", 
			"monarch/warlord"]
		
		self.Builder= CheckTable(Table) 


	def printDungeon(self):
		print "Size: " + self.Size
		print "Number of themes: " + str(self.Number_of_Themes)
		print "Builder: " + self.Builder

def CheckTable(Table):
	return Table[randint(0, len(Table) - 1)]


	
MyDungeon = Dungeon()

MyDungeon.printDungeon()
