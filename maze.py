import random


class Cell:

    def __init__(self, row, column):

        self.row = row
        self.column = column

        self.links = {}
        self.neighbors = {'north': None, 'south': None, 'east': None, 'west': None}

    def get_neighbors(self):
        return self.neighbors

    def set_neighbors(self, key, value=None):
        self.neighbors[key] = value

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            cell.unlink(self, False)

    def get_links(self):
        return tuple(self.links.keys())

    def is_linked(self, cell):
        return self.links.get(cell, False)

    def __repr__(self):
        return "Cell(%r,%r)" % (self.row, self.column)

    def __str__(self):
        return "Cell row %s column %s" % (self.row, self.column)


class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = []

        self.rowcount = -1
        self.cellcount = -1

        self.__prepare_grid()
        self.__configure_cells()

    def __prepare_grid(self):
        for i in range(self.rows):
            self.grid.append([Cell(i, j) for j in range(self.columns)])

    def __configure_cells(self):
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.grid[i][j]

                cell.set_neighbors('north', value=self[cell.row-1, cell.column])
                cell.set_neighbors('south', value=self[cell.row+1, cell.column])
                cell.set_neighbors('west', value=self[cell.row, cell.column-1])
                cell.set_neighbors('east', value=self[cell.row, cell.column+1])

    def __getitem__(self, key):
        if type(key)==int:
            if 0 <= key < self.rows and 0 <= key < self.columns:
                return self.grid[key]
        else:
            if 0 <= key[0] < self.rows and 0 <= key[1] < self.columns:
                return self.grid[key[0]][key[1]]

    def random_cell(self):
        return self[random.randrange(0, self.rows), random.randrange(0, self.columns)]

    def __len__(self):
        return self.rows*self.columns

    def each_row(self):
        while self.rowcount < self.rows-1:
            self.rowcount += 1
            yield self.grid[self.rowcount]

    def reload_rows(self):
        self.rowcount = -1

    def each_cell(self):
        while self.cellcount < len(self)-1:
            self.cellcount +=1
            yield self.grid[self.cellcount//self.rows][self.cellcount % self.columns]

    def reload_cells(self):
        self.cellcount = -1

    def __repr__(self):
        return "Grid (%r,%r)" % (self.rows, self.columns)

    def __str__(self):
        return "Grid row %s column %s" % (self.rows, self.columns)

if __name__ == '__main__':
    pass