import sys
import pygame

pygame.init()
pygame.display.set_caption("Game of life")
SIZE = (1000, 800)
screen = pygame.display.set_mode(SIZE)

black = (0, 0, 0)
white = (255, 255, 255)
grey = (64, 64, 64)


def draw_board():
    x = 0
    y = 0
    a = 10
    for i in range(100):
        for j in range(100):
            pygame.draw.rect(screen, white, [x, y, a, a], 1)
            x += a
        y += a
        x = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    draw_board()
    pygame.display.update()


pygame.quit()
sys.exit()
