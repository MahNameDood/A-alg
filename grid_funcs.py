import pygame, numpy as np, random
from color_props import colors

def create(w,h):
	grid = []
	for y in range(h):
		grid.append([])
		for x in range(w):
			grid[y].append('empty')

	return np.array(grid)

def render(win, size, grid, beginning_pos, end_pos, walls):
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			rect = pygame.Rect((x*size, y*size), (size, size))
			col = colors['empty']

			if (x,y) == beginning_pos:
				col = colors['start']
			elif (x,y) == end_pos:
				col = colors['end']
			elif walls.count((x,y))>0:
				col = colors['unwalkable']

			pygame.draw.rect(win, col, rect)


