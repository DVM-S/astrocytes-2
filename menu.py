from utils import COLOR_GREEN, EVENT_STREAM, FONT_ROBOTO, SCREEN, SCREEN_SIZE
import pygame

from button import Button
from text import Text

pygame.init()

MENU_BG = pygame.image.load('menu.png')


def load_game_1():
    print 'GAME 1 LOADED'


class Menu:
    def __init__(self):
        self.background = pygame.transform.scale(MENU_BG, SCREEN_SIZE)

        self.init_buttons()

    def init_buttons(self):
        (width, height) = SCREEN_SIZE

        self.game_1 = Button(
            (
                (345 / 1024.0) * width,
                (94 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 1', FONT_ROBOTO),
            on_left_click=load_game_1
        )

        self.game_2 = Button(
            (
                (345 / 1024.0) * width,
                (257 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 2', FONT_ROBOTO)
        )

        self.game_3 = Button(
            (
                (345 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 3', FONT_ROBOTO)
        )

        self.game_4 = Button(
            (
                (184 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=MENU_BG,
            text=Text('Game 4', FONT_ROBOTO)
        )

        self.game_5 = Button(
            (
                (22 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height),
            bg=COLOR_GREEN,
            text=Text('Game 5', FONT_ROBOTO)
        )

    def render(self):
        SCREEN.blit(self.background, (0, 0))

        self.game_1.render()
        self.game_2.render()
        self.game_3.render()
        self.game_4.render()
        self.game_5.render()

        pygame.display.update()
