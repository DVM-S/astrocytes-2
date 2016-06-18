from utils import COLOR_GREEN, FONT_ROBOTO, IMAGE_MENU, EVENT_STREAM
import pygame

from button import Button
from text import Text

pygame.init()


def load_game_1():
    print 'GAME 1 LOADED'


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.transform.scale(IMAGE_MENU, self.screen.get_size())

        self.init_buttons()

    def init_buttons(self):
        (width, height) = self.screen.get_size()

        self.game_1 = Button(
            self.screen, (
                (345 / 1024.0) * width,
                (94 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 1', FONT_ROBOTO),
            on_left_click=load_game_1
        )

        self.game_2 = Button(
            self.screen, (
                (345 / 1024.0) * width,
                (257 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 2', FONT_ROBOTO)
        )

        self.game_3 = Button(
            self.screen, (
                (345 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 3', FONT_ROBOTO)
        )

        self.game_4 = Button(
            self.screen, (
                (184 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=IMAGE_MENU,
            text=Text('Game 4', FONT_ROBOTO)
        )

        self.game_5 = Button(
            self.screen, (
                (22 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 5', FONT_ROBOTO)
        )

    def render(self):
        self.screen.blit(self.background, (0, 0))

        self.game_1.render(self.screen)
        self.game_2.render(self.screen)
        self.game_3.render(self.screen)
        self.game_4.render(self.screen)
        self.game_5.render(self.screen)

        pygame.display.update()
