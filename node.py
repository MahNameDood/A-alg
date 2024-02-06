class Node:
	def __init__(self, pos, G, H, parent):
		self.pos = pos
		self.g = G
		self.h = H
		self.f = G + H
		self.parent = parent