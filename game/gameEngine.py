class gameEngine:
	maxPlayers = 2
	numPlayers = 0
	playerNames = []
	maxTurns = 10
	
	def addPlayer(self,pname):
		self.numPlayers += 1
		self.playerNames.append(pname)
		
	def getPlayerName(self,index):
		if index < self.numPlayers:
			return self.playerNames[index]
		else:
			return []
	
	def canAdd(self):
		return self.numPlayers < self.maxPlayers