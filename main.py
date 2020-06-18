import sys
import pygame
from WindowClass import Window
from interface import Button


pygame.init()
pygame.display.set_caption("Game of life")
clock = pygame.time.Clock()
WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
lightgrey = (64, 64, 64)


def draw_board(window_object):
    game_window = window_object.window
    side = window_object.side
    rows = len(game_window)
    columns = len(game_window[0])
    x = 0
    y = 0
    for row in range(rows):
        for column in range(columns):
            cell = game_window[row][column]
            if cell.state == 1:
                pygame.draw.rect(screen, white, [x, y, side, side], 0)
            elif cell.state == 0:
                pygame.draw.rect(screen, white, [x, y, side, side], 1)
            x += side
        y += side
        x = 0


def fill_board():
    mousex, mousey = pygame.mouse.get_pos()
    for row in window.window:
        for cell in row:
            if cell.x + 10 > mousex > cell.x and cell.y + 10 > mousey > cell.y:
                cell.change_state()


def count_alive_neighbours(neighbours):
    alive = 0
    for neighbour in neighbours:
        if neighbour.state == 1:
            alive += 1
    return alive


def update(window):
    new_window = Window(500, 500)

    for row, new_row in zip(window.window, new_window.window):
        for cell, new_cell in zip(row, new_row):
            neighbours = cell.get_neighbours(window)
            alive = count_alive_neighbours(neighbours)
            if cell.state == 0 and alive == 3:
                new_cell.state = 1
            elif cell.state ==1 and alive in [2,3]:
                new_cell.state = 1
            elif cell.state ==1:
                new_cell.state = 0
    return new_window


generation = 1
window = Window(500, 500)
button = Button(520, 50, lightgrey, 150, 40, 'Generation: ')

draw = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and draw:
            fill_board()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            draw = False

    screen.fill(grey)
    draw_board(window)
    button.draw(screen)
    pygame.display.update()
    if not draw:
        window = update(window)
        generation += 1
        clock.tick(0.5)

pygame.quit()
sys.exit()
