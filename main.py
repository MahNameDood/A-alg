import pygame, sys, random
import grid_funcs as gf
from color_props import colors_list

pygame.init()
pygame.font.init()

verdana = pygame.font.SysFont('verdana', 10)

WIDTH = 1800
HEIGHT = 1000
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

size = 50
grid = gf.create(round(WIDTH/size), round(HEIGHT/size))

mode = 'editing'
editing_selected_idx = 0

beginning_pos = 'none'
end_pos = 'none'
walls = []

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEWHEEL:
			if editing_selected_idx < len(colors_list)-1 and event.y > 0:
				editing_selected_idx += 1
			elif editing_selected_idx > 0 and event.y < 0:
				editing_selected_idx -= 1

	win.fill((0,0,0))

	if mode == 'editing' and pygame.mouse.get_pressed()[0]:
		hovered = (round((pygame.mouse.get_pos()[0]-size/2)/size), round((pygame.mouse.get_pos()[1]-size/2)/size))
		if colors_list[editing_selected_idx] == 'start':
			beginning_pos = hovered
		elif colors_list[editing_selected_idx] == 'end':
			end_pos = hovered
		elif colors_list[editing_selected_idx] == 'unwalkable':
			walls.append(hovered)
		else:
			if hovered == beginning_pos:
				beginning_pos = 'none'
			elif hovered == end_pos:
				end_pos = 'none'
			elif walls.count(hovered) > 0:
				walls.remove(hovered)

	gf.render(win, size, grid, beginning_pos, end_pos, walls)

	if mode == 'editing':
		text_surf = verdana.render(f'selected: {colors_list[editing_selected_idx]}', True, (0,0,0))
		win.blit(text_surf, (10,10))

	pygame.display.update()
	clock.tick(60)