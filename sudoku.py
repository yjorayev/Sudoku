class State:
	def __init__(self):
		self.board = []
		for i in range(9):
			row = []
			for j in range(9):
				row.append(0)
			self.board.append(row)

	def printState(self):
		for i in range(9):
			for j in range(9):
				print(self.board[i][j], end = " | ")
			print()
		print("End\n")


	def setValue(self, rowIndex, colIndex, value):
		if(rowIndex not in range(9) or colIndex not in range(9) or value not in range(10)):
			raise Exception("cause of the problem")("Cannot perform the requested operation. Row and Column indeces must be in range 0-9, value must be in range 1-9.")
		self.board[rowIndex][colIndex]=value

	def isValid(self, rowIndex, colIndex):
		for i in range(9):
			if(i != colIndex):
				if(self.board[rowIndex][i] == self.board[rowIndex][colIndex]):
					return False

		for i in range(9):
			if(i != rowIndex):
				if(self.board[i][colIndex] == self.board[rowIndex][colIndex]):
					return False

		if(rowIndex in range(3)):
			rowRange = 0
		elif(rowIndex in range(3, 6)):
			rowRange = 3
		elif(rowIndex in range(6, 9)):
			rowRange = 6

		if(colIndex in range(3)):
			colRange = 0
		elif(colIndex in range(3, 6)):
			colRange = 3
		elif(colIndex in range(6, 9)):
			colRange = 6


		for i in range(rowRange, rowRange+3):
			for j in range(colRange, colRange+3):
				if(i != rowIndex and j!= colIndex):
					if(self.board[i][j] == self.board[rowIndex][colIndex]):
						return False
		return True

	def nextEmptyCell(self):
		for i in range(9):
			for j in range(9):
				if(self.board[i][j]==0):
					position = {"row": i, "col": j}
					return position

		return None

	def getDomain(self, rowIndex, colIndex):
		domain = []
		for i in range(1, 10):
			domain.append(i)

		for i in range(9):
			if(self.board[rowIndex][i] in domain):
				domain.remove(self.board[rowIndex][i])
			if(self.board[i][colIndex] in domain):
				domain.remove(self.board[i][colIndex])

		if(rowIndex in range(3)):
			rowRange = 0
		elif(rowIndex in range(3, 6)):
			rowRange = 3
		elif(rowIndex in range(6, 9)):
			rowRange = 6

		if(colIndex in range(3)):
			colRange = 0
		elif(colIndex in range(3, 6)):
			colRange = 3
		elif(colIndex in range(6, 9)):
			colRange = 6

		for i in range(rowRange, rowRange+3):
			for j in range(colRange, colRange+3):
				if(self.board[i][j] in domain):
					domain.remove(self.board[i][j])

		return domain

def solveSudoku(state):
	next = state.nextEmptyCell()
	if(next == None):
		return state
	rowIndex = next['row']
	colIndex = next['col']
	domain = state.getDomain(rowIndex, colIndex)
	for each in domain:
		state.setValue(rowIndex, colIndex, each)
		#state.printState()
		if(state.isValid(rowIndex, colIndex)):
			if(solveSudoku(state)):
				return state
	state.setValue(rowIndex, colIndex, 0)
	return False	


game = State()
game.setValue(0, 0, 4)
game.setValue(0, 1, 3)
game.setValue(0, 4, 6)
game.setValue(0, 5, 9)
game.setValue(0, 6, 7)
game.setValue(0, 7, 8)

game.setValue(1, 0, 6)
game.setValue(1, 2, 2)
game.setValue(1, 3, 5)
game.setValue(1, 5, 1)
game.setValue(1, 6, 4)
game.setValue(1, 7, 9)


game.setValue(2, 1, 9)
game.setValue(2, 2, 7)
game.setValue(2, 3, 8)
game.setValue(2, 5, 4)
game.setValue(2, 7, 6)
game.setValue(2, 8, 2)

game.setValue(3, 1, 2)
game.setValue(3, 2, 6)
game.setValue(3, 4, 9)
game.setValue(3, 5, 5)
game.setValue(3, 7, 4)
game.setValue(3, 8, 7)

game.setValue(4, 0, 3)
game.setValue(4, 1, 7)
game.setValue(4, 3, 6)
game.setValue(4, 5, 2)
game.setValue(4, 6, 9)
game.setValue(4, 7, 1)

game.setValue(5, 0, 9)
game.setValue(5, 2, 1)
game.setValue(5, 3, 7)
game.setValue(5, 4, 4)
game.setValue(5, 7, 2)
game.setValue(5, 8, 8)

game.setValue(6, 1, 1)
game.setValue(6, 2, 9)
game.setValue(6, 3, 3)
game.setValue(6, 4, 2)
game.setValue(6, 6, 8)
game.setValue(6, 8, 4)

game.setValue(7, 0, 2)
game.setValue(7, 2, 8)
game.setValue(7, 4, 5)
game.setValue(7, 5, 7)
game.setValue(7, 7, 3)
game.setValue(7, 8, 6)

game.setValue(8, 0, 7)
game.setValue(8, 1, 6)
game.setValue(8, 3, 4)
game.setValue(8, 4, 1)
game.setValue(8, 6, 2)
game.setValue(8, 8, 9)

print("Initial state")
game.printState()
solution = solveSudoku(game)
if(solution == False):
	print("Cannot be solved")
else:
	print("Solution state")
	solution.printState()