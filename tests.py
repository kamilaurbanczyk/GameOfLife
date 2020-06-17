
def fill_board(window):
    for i in range(6, 12):
        window.change_state(i, i, 1)
        window.change_state(i, i+1, 1)
        window.change_state(i+2, i-3, 1)

    for i in range(35, 48):
        window.change_state(i, 16, 1)
        window.change_state(i, 15, 1)
        for j in range(34, 37):
            window.change_state(i-2, j, 1)
            window.change_state(i-1, j-4, 1)


def print_neighbours(array):
    for row in array:
        for cell in row:
            print(cell, cell.get_neighbours(array))
