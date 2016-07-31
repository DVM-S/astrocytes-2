from utils import (
    ACTIVE,
    COLOR_BLACK,
    COLOR_WHITE,
    FONT_ROBOTO,
    SCREEN,
    SCREEN_SIZE)

import pygame

from components.button import Button
from components.text import Text
from components.sidebar import Sidebar


class PauseScreen(Sidebar):
    def __init__(self):
        super(PauseScreen, self).__init__()

        self.init_buttons()

    def init_buttons(self):
        self.btn_back = Button(
            'pause_screen',
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Back', color=COLOR_WHITE),
            on_left_click=self.load_prev)

        self.btn_menu = Button(
            'pause_screen',
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Main Menu', color=COLOR_WHITE),
            on_left_click=self.load_menu)

        self.btn_quit = Button(
            'pause_screen',
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Quit', color=COLOR_WHITE),
            on_left_click=self.quit_game)

    def load_menu(self):
        self.hide()
        ACTIVE.append('menu')

    def load_prev(self):
        self.hide()

    def quit_game(self):
        pygame.quit()
        quit()

    def render(self):
        super(PauseScreen, self).render()
        self.btn_back.render((SCREEN_SIZE.W - self.width, 0))
        self.btn_menu.render((SCREEN_SIZE.W - self.width, 50))
        self.btn_quit.render((SCREEN_SIZE.W - self.width, 100))
