
class Board():
	def __init__(self, width = None, height = None, board = None):
		if width == None:
			self.width = 8
		else:
			self.width = width

		if height == None:
			self.height = 8
		else:
			self.height = height

		if board == None:
			self.board = []
		else:
			self.board = board
