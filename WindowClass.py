# Create a Cell class that stores information about single cell: its coordinates and state( 1-alive, 0-dead)
# Create a Window class that creates nested lists of cells. Window class functions:
# create_cells() <- init func
# change_state() <- changes state of single cell


class Cell:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return "({}, {}), {}".format(self.x, self.y, self.state)

    def get_neighbours(self, window_object):
        x = self.x
        y = self.y
        side = window_object.side
        neighbours = []
        x_list = [x - side, x - side, x - side, x, x, x + side, x + side, x + side]
        y_list = [y - side, y, y + side, y - side, y + side, y - side, y, y + side]

        for m, n in zip(x_list, y_list):
            if window_object.width > m >= 0 and window_object.height > n >= 0:
                row = int(n / side)
                column = int(m / side)
                neighbour = window_object.window[row][column]
                neighbours.append(neighbour)

        return neighbours

    def change_state(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1


class Window(Cell):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.side = 10
        self.window = self.create_cells()

    def create_cells(self):
        array = []
        for y in range(0, self.height, self.side):
            row = []
            for x in range(0, self.width, self.side):
                cell = Cell(x, y)
                row.append(cell)
            array.append(row)
        return array

    def count_alive_neighbours(self, cell):
        alive = 0
        for neighbour in cell.neighbours:
            if self.window[int(neighbour[1]/10)][int(neighbour[0]/10)].state == 1:
                alive += 1
        return alive









