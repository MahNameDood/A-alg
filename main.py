import pygame, sys, random
import grid_funcs as gf
from color_props import colors_list
from algorithm import solve

pygame.init()
pygame.font.init()

verdana = pygame.font.SysFont('verdana', 20)

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
opened = []
opened_nodes = []
closed = []

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
	keys = pygame.key.get_pressed()



	if mode == 'editing':
		if pygame.mouse.get_pressed()[0]:
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

		if keys[pygame.K_RETURN] and beginning_pos != 'none' and end_pos != 'none':
			mode = 'simulating'

	elif mode == 'simulating':
		opened, opened_nodes = solve(grid, beginning_pos, end_pos, walls)
		mode = 'none'




	gf.render(win, size, grid, beginning_pos, end_pos, walls, opened, closed)

	if mode == 'editing':
		text_surf = verdana.render(f'selected: {colors_list[editing_selected_idx]}', True, (0,0,0))
		win.blit(text_surf, (10,10))

	if mode == 'simulating' or mode == 'none':
		for node in opened_nodes:
			if (round((pygame.mouse.get_pos()[0]-size/2)/size), round((pygame.mouse.get_pos()[1]-size/2)/size)) == node.pos:
				text_surf = verdana.render(f'POS: {node.pos}', True, (0,0,0))
				win.blit(text_surf, (10,10))
				text_surf = verdana.render(f'F: {node.f}', True, (0,0,0))
				win.blit(text_surf, (10,30))
				text_surf = verdana.render(f'G: {node.g}', True, (0,0,0))
				win.blit(text_surf, (10,50))
				text_surf = verdana.render(f'H: {node.h}', True, (0,0,0))
				win.blit(text_surf, (10,70))


	pygame.display.update()
	clock.tick(60)