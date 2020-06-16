import sys
import pygame
from classes import Cell, create_array

pygame.init()
pygame.display.set_caption("Game of life")
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (64, 64, 64)


def draw_board():
    window = []
    x = 0
    y = 0
    a = 10
    for i in range(10):
        row= []
        for j in range(10):
            cell = Cell(x, y)
            row.append(cell)
            pygame.draw.rect(screen, white, [x, y, a, a], 1)
            x += a
        window.append(row)
        y += a
        x = 0
    return window


def draw_board2(window):
    x = 0
    y = 0
    a = 10
    for i in range(80):
        row= []
        for j in range(80):
            cell = window[j][i]
            if cell.state:
                pygame.draw.rect(screen, white, [x, y, a, a], 0)
            else:
                pygame.draw.rect(screen, white, [x, y, a, a], 1)
            x += a
        y += a
        x = 0


def print_my_array(array):
    for row in array:
        for cell in row:
            print(cell)


# my_array = [[Cell(1,1) for i in range(10)] for n in range(10)]
window = create_array(WIDTH, HEIGHT)
print_my_array(window)
window[2][2].state = 1
# print(window[2][2])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    draw_board2(window)
    pygame.display.update()


pygame.quit()
sys.exit()
