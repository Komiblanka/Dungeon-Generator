from random import randint

class Area:
	Rarity = "Common"
	Discovery = "None"
	Danger = "None"
	Themed = "No"
	Type = []

	def __init__(self):
		self.AreaTypeContents()
		self.MainGenerator()

	def Print_Area(self):
		print "\nAREA:\n====="
		print "Themed: " + self.Themed
		print "Rarity: " + self.Rarity
		print "Discovery: \n\t" + self.Discovery
		print "Danger: \n\t" + self.Danger

	def AreaTypeContents(self):
		Table = [
			["Unthemed", "Common", "", ""], 
			["Unthemed", "Common", "", "Danger"], 
			["Unthemed", "Common", "Discovery", "Danger"], 
			["Unthemed", "Common", "Discovery", "Danger"], 
			["Unthemed", "Common", "Discovery", ""], 
			["Unthemed", "Common", "Discovery", ""], 
			["Themed", "Common", "", "Danger"], 
			["Themed", "Common", "Discovery", "Danger"], 
			["Themed", "Common", "Discovery", ""], 
			["Themed", "Unique", "", "Danger"], 
			["Themed", "Unique", "Discovery", "Danger"], 
			["Themed", "Unique", "Discovery", ""]]
		
		self.Type = CheckTable(Table) 
	
	def MainGenerator(self):
		self.Themed = self.Type[0]
		self.Rarity = self.Type[1]

		if self.Type[2] == "Discovery":
			self.GenerateDiscovery()
		
		if self.Type[3] == "Danger":
			self.GenerateDanger()

	def GenerateDiscovery(self):
		Table_Discovery_Type = [
					"Dressing", 
					"Dressing", 
					"Dressing", 
					"Feature", 
					"Feature", 
					"Feature", 
					"Feature", 
					"Feature", 
					"Feature", 
					"Find",
					"Find",
					"Find"]

		Table_Dressing = [
				"Dressing: Junk/debris", 
				"Dressing: Tracks/marks", 
				"Dressing: Signs of battle", 
				"Dressing: Writing/carving", 
				"Dressing: Warning", 
				"Dressing: Dead Creature (p49)", 
				"Dressing: Bones/remains", 
				"Dressing: Book/scroll/map", 
				"Dressing: Broken door/wall", 
				"Dressing: Breeze/wind/smell", 
				"Dressing: Lichen/moss/fungus", 
				"Dressing: Oddity (p50)"]

		Table_Feature = [
				"Feature: Cave-in/collapse", 
				"Feature: Pit/shaft/chasm", 
				"Feature: Pillars/columns", 
				"Feature: Locked door/gate", 
				"Feature: Alcoves/niches", 
				"Feature: Bridge/stairs/ramp", 
				"Feature: Fountain/well/pool", 
				"Feature: Puzzle", 
				"Feature: Altar/dais/platform", 
				"Feature: Statue/idol", 
				"Feature: Magic pool/statue/idol", 
				"Feature: Connection to another dungeon"]

		Table_Find = [
				"Find: Trinkets", 
			"Find: Tools", 
			"Find: Weapons/armor", 
			"Find: Supplies/trade goods", 
			"Find: Coins/gems/jewelry", 
			"Find: Poisons/potions", 
			"Find: Adventurer/captive", 
			"Find: Magic item", 
			"Find: Scroll/book", 
			"Find: Magic weapon/armor", 
			"Find: Artifact", 
			"Find: Roll twice"]

		Discovery = CheckTable(Table_Discovery_Type)

		if Discovery == "Dressing":
			self.Discovery = CheckTable(Table_Dressing)
		elif Discovery == "Feature":
			self.Discovery = CheckTable(Table_Feature)
		elif Discovery  == "Find":
			self.Discovery = CheckTable(Table_Find)
		else:
			self.Discovery = "None"

	def GenerateDanger(self):
		Table_Danger_Type = [
			"Trap", 
			"Trap", 
			"Trap", 
			"Trap", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Creature (pag 49)", 
			"Entity"]

		Table_Traps = [
				"Trap: Alarm", 
				"Trap: Ensnaring/paralyzing", 
				"Trap: Pit", 
				"Trap: Crushing", 
				"Trap: Piercing/puncturing", 
				"Trap: Chopping/slashing", 
				"Trap: Confusing (maze, etc.)", 
				"Trap: Gas (poison, etc.)", 
				"Trap: element (p50)", 
				"Trap: Ambush", 
				"Trap: Magical", 
				"Trap: Roll twice"]

		Table_Creatures = [
				"Creature: Waiting in ambush", 
				"Creature: Fighting/squabbling", 
				"Creature: Prowling/on patrol", 
				"Creature: Looking for food", 
				"Creature: Eating/resting", 
				"Creature: Guarding", 
				"Creature: On the move", 
				"Creature: Searching/scavenging", 
				"Creature: Returning to den", 
				"Creature: Making plans", 
				"Creature: Sleeping", 
				"Creature: Dying"]

		Table_Entity = [
				"Entity: Alien interloper", 
				"Entity: Vermin lord", 
				"Entity: Criminal mastermind", 
				"Entity: Warlord", 
				"Entity: High priest", 
				"Entity: Oracle", 
				"Entity: Wizard/witch/alchemist", 
				"Entity: Monster lord (p49)", 
				"Entity: Evil spirit/ghost", 
				"Entity: Undead lord (lich, etc.)", 
				"Entity: Demon", 
				"Entity: Dark god"]
	
		Danger = CheckTable(Table_Danger_Type)

		if Danger == "Trap":
			self.Danger = CheckTable(Table_Traps)
		elif Danger == "Creature (pag 49)":
			self.Danger = CheckTable(Table_Creatures)
		elif Danger  == "Entity":
			self.Danger = CheckTable(Table_Entity)
		else:
			self.Danger = "None"



class Dungeon:
	Size = ""
	Number_of_Themes = 0
	Number_of_Areas = 0
	Builder = ""
	Ruination = ""
	Themes = []
	Areas = []


	def __init__(self):
		self.GenerateSize()
		self.GenerateNumberOfThemesAndAreas()
		self.GenerateBuilder()
		self.GenerateThemes()
		self.GenerateAreas()
		self.GenerateRuination()

	def GenerateSize(self):
		Table = ["Small", "Medium", "Large", "Huge"]
		self.Size = CheckTable(Table) 
	
	def GenerateNumberOfThemesAndAreas(self):
		DungeonSize = self.Size

		if DungeonSize == "Small":
			self.Number_of_Themes = randint(1, 4)
			self.Number_of_Areas = randint(1, 6) + 2
		elif DungeonSize == "Medium":
			self.Number_of_Themes = randint(1, 6)
			self.Number_of_Areas = 2 * randint(1, 6) + 2
		elif DungeonSize == "Large":
			self.Number_of_Themes = randint(1, 6) + 1
			self.Number_of_Areas = 3 * randint(1, 6) + 6
		elif DungeonSize == "Huge":
			self.Number_of_Themes = randint(1, 6) + 2
			self.Number_of_Areas = 4 * randint(1, 6) + 10
		else:
			self.Number_of_Themes = 0
	
	def GenerateAreas(self):
		for i in range(0, self.Number_of_Areas):
			New_Area = Area()
			self.Areas.append(New_Area)
	
	def GenerateThemes(self):	
		Table_Rarity = ["Mundane", "Unusual", "Extraordinary"]
		
		Table_Mundane = [
				"Mundane:\t Rot/decay", 
				"Mundane:\t Torture/agony", 
				"Mundane:\t Madness", 
				"Mundane:\t All is lost", 
				"Mundane:\t Noble sacrifice", 
				"Mundane:\t Savage fury", 
				"Mundane:\t Survival", 
				"Mundane:\t Criminal activity", 
				"Mundane:\t Secrets/treachery", 
				"Mundane:\t Tricks and traps", 
				"Mundane:\t Invasion/infestation", 
				"Mundane:\t Factions at war" ]
		
		Table_Unusual = [
				"Unusual:\t Creation/invention", 
				"Unusual:\t Element (p50)", 
				"Unusual:\t Knowledge/learning", 
				"Unusual:\t Growth/expansion", 
				"Unusual:\t Deepening mystery", 
				"Unusual:\t Transformation/change", 
				"Unusual:\t Chaos and destruction", 
				"Unusual:\t Shadowy forces", 
				"Unusual:\t Forbidden knowledge", 
				"Unusual:\t Poison/disease", 
				"Unusual:\t Corruption/blight", 
				"Unusual:\t Impending disaster" ]

		Table_Extraotrinary = [
				"Extraordinary:\t Scheming evil", 
				"Extraordinary:\t Divination/scrying", 
				"Extraordinary:\t Blasphemy", 
				"Extraordinary:\t Arcane research", 
				"Extraordinary:\t Occult forces", 
				"Extraordinary:\t An ancient curse", 
				"Extraordinary:\t Mutation", 
				"Extraordinary:\t The unquiet dead", 
				"Extraordinary:\t Bottomless hunger", 
				"Extraordinary:\t Incredible power", 
				"Extraordinary:\t Unspeakable horrors", 
				"Extraordinary:\t Holy war" ]

		for themes in range(1, self.Number_of_Themes):
			Rarity = CheckTable(Table_Rarity)

			if Rarity == "Mundane":
				self.Themes.append(CheckTable(Table_Mundane))
			elif Rarity == "Unusual":
				self.Themes.append(CheckTable(Table_Unusual))
			elif Rarity == "Extraordinary":
				self.Themes.append(CheckTable(Table_Extraotrinary))
			else:
				self.Themes.append("Error")

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

	def GenerateRuination(self):
		Table = ["Arcane disaster", 
			"Damnation/curse", 
			"Earthquake/fire/flood", 
			"Plague/famine/drought", 
			"Overrun by monsters", 
			"War/invasion", 
			"Depleted resources", 
			"Better prospects elsewhere"]

		self.Ruination = CheckTable(Table) 

	def printDungeon(self):
		print "Size: " + self.Size
		print "Number of themes: " + str(self.Number_of_Themes)  
		print "Number of areas: " + str(self.Number_of_Areas)  
		print "Builder: " + self.Builder
		print "Ruination: " + self.Ruination
		print "Themes: "

		for Theme in self.Themes:
			print "\t" + Theme

		for Area in self.Areas:
			Area.Print_Area()

def CheckTable(Table):
	return Table[randint(0, len(Table) - 1)]


	
MyDungeon = Dungeon()

MyDungeon.printDungeon()

#MyArea = Area()
#MyArea.Print_Area()
