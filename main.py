from utils import (
    ACTIVE,
    EVENT_STREAM,
    KINECT,
    POST_NEW_BODY_FRAME_EVENT,
    POST_NEW_BODY_INDEX_FRAME_EVENT,
    SCREEN,
    SCREEN_SIZE)

import pygame

from game_1 import Game_1
from game_2 import Game_2
from menu import Menu


class Astrocytes:
    def __init__(self):
        pygame.display.set_caption('Astrocytes')
        self.background = pygame.Surface(SCREEN_SIZE)

        self.menu = Menu()
        self.game_1 = Game_1()
        self.game_2 = Game_2()

        EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        self.check_exit(e)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for e in pygame.event.get():
                EVENT_STREAM.on_next(e)

            if ACTIVE['CURR'] == 'menu':
                self.menu.render()

            elif ACTIVE['CURR'] == 'game_1':
                if KINECT.has_new_body_frame():
                    POST_NEW_BODY_FRAME_EVENT(
                        body_frame=KINECT.get_last_body_frame())

                if KINECT.has_new_body_index_frame():
                    POST_NEW_BODY_INDEX_FRAME_EVENT(
                        body_index_frame=KINECT.get_last_body_index_frame())

                self.game_1.render()

            elif ACTIVE['CURR'] == 'game_2':
                if KINECT.has_new_body_frame():
                    POST_NEW_BODY_FRAME_EVENT(
                        body_frame=KINECT.get_last_body_frame())

                if KINECT.has_new_body_index_frame():
                    POST_NEW_BODY_INDEX_FRAME_EVENT(
                        body_index_frame=KINECT.get_last_body_index_frame())

                self.game_2.render()

            pygame.display.update()

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
    game = Astrocytes()
    game.run()
