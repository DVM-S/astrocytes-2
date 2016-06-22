from utils import (
    ACTIVE,
    COLOR_GREEN,
    FONT_ROBOTO,
    SCREEN,
    SCREEN_SIZE)

import pygame

from button import Button
from text import Text


def load_game(idx):
    ACTIVE.append('game_%d' % (idx))
    print 'GAME %d LOADED' % (idx)


class Menu:
    def __init__(self):
        self.bg = pygame.transform.scale(
            pygame.image.load('menu.png'),
            (SCREEN_SIZE.W, SCREEN_SIZE.H))

        self.init_buttons()

    def init_buttons(self):
        self.btn_1 = Button((
                (345 / 1024.0) * SCREEN_SIZE.W,
                (94 / 768.0) * SCREEN_SIZE.H,
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=COLOR_GREEN,
            text=Text('Game 1', FONT_ROBOTO),
            on_left_click=lambda: load_game(1)
        )

        self.btn_2 = Button((
                (345 / 1024.0) * SCREEN_SIZE.W,
                (257 / 768.0) * SCREEN_SIZE.H,
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=COLOR_GREEN,
            text=Text('Game 2', FONT_ROBOTO),
            on_left_click=lambda: load_game(2)
        )

        self.btn_3 = Button((
                (345 / 1024.0) * SCREEN_SIZE.W,
                (420 / 768.0) * SCREEN_SIZE.H,
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=COLOR_GREEN,
            text=Text('Game 3', FONT_ROBOTO),
            on_left_click=lambda: load_game(3)
        )

        self.btn_4 = Button((
                (184 / 1024.0) * SCREEN_SIZE.W,
                (420 / 768.0) * SCREEN_SIZE.H,
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=COLOR_GREEN,
            text=Text('Game 4', FONT_ROBOTO)
        )

        self.btn_5 = Button((
                (22 / 1024.0) * SCREEN_SIZE.W,
                (420 / 768.0) * SCREEN_SIZE.H,
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=COLOR_GREEN,
            text=Text('Game 5', FONT_ROBOTO)
        )

    def render(self):
        SCREEN.blit(self.bg, (0, 0))

        self.btn_1.render()
        self.btn_2.render()
        self.btn_3.render()
        self.btn_4.render()
        self.btn_5.render()
