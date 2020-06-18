import pygame


class Button:
    def __init__(self, x, y, color, width, height, text= ''):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            screen.blit(text, (self.x+10, self.y+10))