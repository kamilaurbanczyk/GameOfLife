import sys
import pygame
from WindowClass import Window
from tests import fill_board


pygame.init()
pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)


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


def count_alive_neighbours(neighbours):
    alive = 0
    for neighbour in neighbours:
        if neighbour.state == 1:
            alive += 1
    return alive

def update(window):
    for row in window.window:
        for cell in row:
            neighbours = cell.get_neighbours(window.window)
            alive = count_alive_neighbours(neighbours)
            if cell.state == 0 and alive == 3:
                cell.state = 1
            elif cell.state ==1 and alive in [2,3]:
                pass
            elif cell.state ==1:
                cell.state = 0


window = Window(WIDTH, HEIGHT)
fill_board(window)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    draw_board(window.window)
    pygame.display.update()
    update(window)
    clock.tick(0.5)

pygame.quit()
sys.exit()
