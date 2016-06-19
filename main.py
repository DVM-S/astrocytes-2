from utils import ACTIVE, EVENT_STREAM, SCREEN, SCREEN_SIZE
import pygame

from menu import Menu
from game_1 import Game_1


class Astrocytes:
    def __init__(self):
        self.background = pygame.Surface(SCREEN_SIZE)

        self.menu = Menu()
        self.game_1 = Game_1()

        EVENT_STREAM.subscribe(self.event_handler)
        pygame.display.set_caption('Astrocytes')

    def event_handler(self, e):
        self.check_exit(e)

    def run(self):
        while True:
            EVENT_STREAM.on_next(pygame.event.wait())
            if ACTIVE['CURR'] == 'menu':
                self.menu.render()
            elif ACTIVE['CURR'] == 'game_1':
                self.game_1.render()

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
