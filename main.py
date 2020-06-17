import sys
import pygame
from WindowClass import Window
from tests import fill_board

pygame.init()
pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()
WIDTH = 700
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)


def draw_board(window_object):
    game_window = window_object.window
    side = window_object.side
    rows = len(game_window)
    columns = len(game_window[0])
    x = 0
    y = 0
    for column in range(columns):
        for row in range(rows):
            cell = game_window[row][column]
            if cell.state == 1:
                pygame.draw.rect(screen, white, [x, y, side, side], 0)
            elif cell.state == 0:
                pygame.draw.rect(screen, white, [x, y, side, side], 1)
            x += side
        y += side
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
            neighbours = cell.get_neighbours(window)
            alive = count_alive_neighbours(neighbours)
            if cell.state == 0 and alive == 3:
                cell.state = 1
            elif cell.state ==1 and alive in [2,3]:
                pass
            elif cell.state ==1:
                cell.state = 0


window = Window(500, 500)
fill_board(window)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    draw_board(window)
    pygame.display.update()
    update(window)
    clock.tick(0.5)

pygame.quit()
sys.exit()
