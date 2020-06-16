# Create a Cell class that stores information about single cell: its coordinates and state( 1-alive, 0-dead)
# Create a Window class that creates nested lists of cells. Window class functions:
# create_cells() <- init func
# change_state() <- changes state of cell


class Cell:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return "({}, {}), {}".format(self.x, self.y, self.state)

    def get_neighbours(self, array, a=10):
        x = self.x
        y = self.y
        neigbours = []
        x_list = [x-a, x-a, x-a, x, x, x+a, x+a, x+a]
        y_list = [y-a, y, y+a, y-a, y+a, y-a, y, y+a]

        # for m, n in zip(x_list, y_list):
        #     if 800 >= m >= 0 and 800 >= n >= 0:
        #         neigbours_coordinates.append((m, n))
        # return neigbours_coordinates
        for m, n in zip(x_list, y_list):
            if 800 > m >= 0 and 800 > n >= 0:
                row = int(n/a)
                column = int(m/a)
                neighbour = array[row][column]
                neigbours.append(neighbour)

        return neigbours


class Window(Cell):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.a = 10
        self.window = self.create_cells()

    def create_cells(self):
        array = []
        for y in range(0, self.height, self.a):
            row = []
            for x in range(0, self.width, self.a):
                cell = Cell(x, y)
                row.append(cell)
            array.append(row)
        return array

    def change_state(self, column, row, new_state):
        self.window[row][column].state = new_state

    def count_alive_neighbours(self, cell):
        alive = 0
        for neighbour in cell.neighbours:
            if self.window[int(neighbour[1]/10)][int(neighbour[0]/10)].state == 1:
                alive += 1
        return alive

    def choose_action(self, cell, alive_neigbours):
        if alive_neigbours == 2:
            pass








