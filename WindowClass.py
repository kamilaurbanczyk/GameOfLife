# Create a Cell class that stores information about single cell: its coordinates and state( 1-alive, 0-dead)
# Create a Window class that creates nested lists of cells. Window class functions:
# create_cells() <- init func
# change_state() <- changes state of cell
#


class Cell:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return "({}, {}), {}".format(self.x, self.y, self.state)


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = self.create_cells()

    def create_cells(self):
        array = []
        for y in range(0, self.height, 10):
            row = []
            for x in range(0, self.width, 10):
                cell = Cell(x, y)
                row.append(cell)
            array.append(row)
        return array

    def change_state(self, x, y, new_state):
        self.window[x][y].state = new_state




