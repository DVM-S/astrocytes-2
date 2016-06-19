from utils import EVENT_STREAM, SCREEN
import pygame

from menu import Menu


class Astrocytes:
    def __init__(self):
        size = (width, height) = (512, 384)
        self.background = pygame.Surface(SCREEN.get_size())

        self.render = 'menu'
        self.menu = Menu()

        EVENT_STREAM.subscribe(self.event_handler)
        pygame.display.set_caption('Astrocytes')

    def event_handler(self, e):
        self.check_exit(e)

    def run(self):
        while True:
            EVENT_STREAM.on_next(pygame.event.wait())

            if self.render == 'menu':
                self.menu.render()

    def check_exit(self, e):
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif (e.type == pygame.KEYDOWN):
            if e.key == pygame.K_F4:
                if bool(e.mod & pygame.KMOD_ALT):
                    pygame.quit()
                    quit()


if __name__ == '__main__':
    pygame.init()

    game = Astrocytes()
    game.run()
