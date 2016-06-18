import pygame

from menu import Menu


class Astrocytes:
    def __init__(self):
        size = (width, height) = (512, 384)
        self.screen = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.background = pygame.Surface(self.screen.get_size())

        self.render = 'menu'
        self.menu = Menu(self.screen)

        pygame.display.set_caption('Astrocytes')

    def run(self):
        while True:
            event = pygame.event.wait()
            if self.render == 'menu':
                self.menu.render()

if __name__ == '__main__':
    pygame.init()

    game = Astrocytes()
    game.run()
