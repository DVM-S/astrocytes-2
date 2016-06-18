import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('menu.png')

    def render(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()
