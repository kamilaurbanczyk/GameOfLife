# Create a class that stores information about single cell: its coordinates and state( 1-alive, 0-dead)


class Cell:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return "({}, {}), {}".format(self.x, self.y, self.state)


def create_array(width, height):
    array = []
    for y in range(0, height, 10):
        row = []
        for x in range(0, width, 10):
            cell = Cell(x, y)
            row.append(cell)
        array.append(row)
    return array



