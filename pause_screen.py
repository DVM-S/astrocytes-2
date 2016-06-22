from utils import (
    ACTIVE,
    COLOR_BLACK,
    COLOR_WHITE,
    FONT_ROBOTO,
    SCREEN,
    SCREEN_SIZE)

import pygame

from button import Button
from text import Text


def load_menu():
    ACTIVE.append('menu')


def load_prev():
    ACTIVE.pop()


def quit():
    pass


class PauseScreen:
    def __init__(self):
        self.hidden = True
        self.width = 0
        self.max_witdh = 200

        self.init_buttons()

    def init_buttons(self):
        self.btn_back = Button(
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Back', FONT_ROBOTO, COLOR_WHITE),
            on_left_click=load_prev)

        self.btn_menu = Button(
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Main Menu', FONT_ROBOTO, COLOR_WHITE),
            on_left_click=load_menu)

        self.btn_quit = Button(
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Quit', FONT_ROBOTO, COLOR_WHITE),
            on_left_click=quit)

    def hide(self):
        self.width = 0
        self.hidden = True

    def render(self):
        if self.hidden:
            tint = pygame.Surface(
                (SCREEN_SIZE.W, SCREEN_SIZE.H),
                pygame.SRCALPHA)
            tint.fill((0, 0, 0, 150))
            SCREEN.blit(tint, (0, 0))
            self.hidden = False

        SCREEN.fill(
            (100, 100, 100),
            (SCREEN_SIZE.W - self.width, 0, self.width, SCREEN_SIZE.H))

        self.btn_back.render((SCREEN_SIZE.W - self.width, 0))
        self.btn_menu.render((SCREEN_SIZE.W - self.width, 50))
        self.btn_quit.render((SCREEN_SIZE.W - self.width, 100))

        if self.width < self.max_witdh:
            self.width += 50