###
import maze
from binary_tree import Binary_tree

print('##################################')
print('testing Cell class')
#define 3 cells, link them, set/get neighbours
c1 = maze.Cell(4, 4)
c2 = maze.Cell(4, 5)
c3 = maze.Cell(1, 5)
print(c1)
print(c2)
c1.link(c2, False)
c1.link(c3)
print(c1.get_links(), c2.get_links())
print(c1.is_linked(c2))
print(c2.is_linked(c1))
print(c1.is_linked(c3))
print(c3.is_linked(c1))
print(c1.get_neighbors())
c1.set_neighbors('north', c3)
print(c1.get_neighbors())



print('##################################')
print('testing Grid class')
g=maze.Grid(4,4)
print(len(g))
print(g[2, 2])
print(g[0, 4])
print(g[4, 0])
print(g[4, 4])
c1 = g.random_cell()
c2 = g.random_cell()
print(c1)
print(c1.get_neighbors())
print(c2)
print(c2.get_neighbors())
c3 = g[0, 3]
print('get a cell:', c3)
print(c3.get_neighbors())
r0 = g[0]
print('get a row:', r0)
print('row iteration')
for row in g.each_row():
    print(row)
print('cell iteration')
for cell in g.each_cell():
    print(cell)
print('row iteration after reloading')
g.reload_rows()
for row in g.each_row():
    print(row)
print('cell iteration after reloading')
g.reload_cells()
for cell in g.each_cell():
    print(cell)
print('row iteration backward')
for row in g.each_row(forward=False):
    print(row)
print('cell iteration backward')
for cell in g.each_cell(forward=False):
    print(cell)

print('##################################')
print('testing Binary tree')

g=maze.Grid(10,10)
Binary_tree(g)
print(g)


