import pygame

black = (0, 0, 0)
white = (255, 255, 255)
lightgrey = (128, 128, 128)
grey = (64, 64, 64)
orange = (255, 165, 0)


class Button:
    def __init__(self, x, y, width, height, onclick=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick = onclick

    def draw(self, screen, text):
        if self.onclick:
            pygame.draw.rect(screen, grey, (self.x, self.y, self.width, self.height), 1)
            pygame.draw.rect(screen, orange, (self.x - 1, self.y - 1, self.width - 1, self.height - 1), 0)
        else:
            pygame.draw.rect(screen, white, (self.x - 1, self.y - 1, self.width + 1, self.height + 1), 1)
            pygame.draw.rect(screen, grey, (self.x, self.y, self.width - 1, self.height - 1), 0)

        if text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(text, 1, (255, 255, 255))
            screen.blit(text, (self.x + 10, self.y + 10))
