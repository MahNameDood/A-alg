from node import Node
import math

def surrounding(s, grid, walls, open_grids, closed_grids, end):
	selected = s.pos
	neighbors = []
	if selected[0] > 0:

		p = (selected[0]-1, selected[1])
		if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
			neighbors.append(p)

		if selected[1] > 0:

			p = (selected[0]-1, selected[1]-1)
			if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
				neighbors.append(p)

		if selected[1] < len(grid)-1:

			p = (selected[0]-1, selected[1]+1)
			if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
				neighbors.append(p)

			

	if selected[0] < len(grid[0]):

		p = (selected[0]+1, selected[1])
		if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
			neighbors.append(p)

		if selected[1] > 0:

			p = (selected[0]+1, selected[1]-1)
			if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
				neighbors.append(p)

		if selected[1] < len(grid)-1:

			p = (selected[0]+1, selected[1]+1)
			if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
				neighbors.append(p)

	if selected[1] < len(grid)-1:
		p = (selected[0], selected[1]+1)
		if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
			neighbors.append(p)

	if selected[1] > 0:
		p = (selected[0], selected[1]-1)
		if walls.count(p) == 0 and open_grids.count(p) == 0 and closed_grids.count(p) == 0:
			neighbors.append(p)


	new_neighbors = []
	for n in neighbors:
		new_neighbors.append(Node(n, int(round(math.sqrt((n[0]-selected[0])**2+(n[1]-selected[1])**2), 1)*10), (abs(n[0] - end[0])+abs(n[1] - end[1]))*10, s))

	return new_neighbors


def get_node_pos(nodes):
	pos = []
	for node in nodes:
		pos.append(node.pos)
	return pos


def solve(grid, beginning_pos, end_pos, walls):
	beginning_node = Node(beginning_pos, 0, 0, 0)

	open_nodes = surrounding(beginning_node, grid, walls, [], [], end_pos)
	open_grids = get_node_pos(open_nodes)

	closed_grids = [beginning_pos]
	closed_nodes = [beginning_node]

	selected = beginning_pos
	print(open_grids)

	solved = True
	#while not solved:
		#pass

	return open_grids, open_nodes


