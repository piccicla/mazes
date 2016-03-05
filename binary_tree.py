import random

class Binary_tree:

    def __init__(self, grid):
        grid.reload_cells()
        for cell in grid.each_cell():
            neighbors = []
            n = cell.get_neighbors()
            if n['north']:
                neighbors.append(n['north'])
            if n['east']:
                neighbors.append(n['east'])
            if neighbors:
                cell.link(random.choice(neighbors))