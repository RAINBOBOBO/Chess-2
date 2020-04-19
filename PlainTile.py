
class PlainTile():
	def __init__(self, x, y, piece = None):
		self.x = x
		self.y = y

		if piece == None:
			self.piece = None
		else:
			self.piece = piece
