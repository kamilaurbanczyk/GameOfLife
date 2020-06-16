import sys
import pygame
from WindowClass import Window
from tests import test


pygame.init()
pygame.display.set_caption("Game of life")
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (64, 64, 64)


def draw_board(window):
    x = 0
    y = 0
    a = 10
    for i in range(80):
        for j in range(80):
            cell = window[j][i]
            if cell.state == 1:
                pygame.draw.rect(screen, white, [x, y, a, a], 0)
            elif cell.state == 0:
                pygame.draw.rect(screen, white, [x, y, a, a], 1)
            x += a
        y += a
        x = 0

# TO DELETE FUNCTION
def print_my_array(array):
    for row in array:
        for cell in row:
            print(cell)


window = Window(WIDTH, HEIGHT)

test(window)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    draw_board(window.window)
    pygame.display.update()


pygame.quit()
sys.exit()
