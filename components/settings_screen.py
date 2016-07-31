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


class SettingsScreen(Sidebar):
    def __init__(self):
        super(SettingsScreen, self).__init__()

        self.init_buttons()

    def init_buttons(self):
        self.btn_back = Button(
            'settings_screen',
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Back', color=COLOR_WHITE),
            on_left_click=self.load_prev)

        self.btn_reg = Button(
            'settings_screen',
            (self.max_witdh, 50),
            bg=(80, 80, 80),
            fg=(50, 50, 50),
            text=Text('Register', color=COLOR_WHITE),
            on_left_click=self.load_reg_form)

    def load_prev(self):
        self.hide()
        self.btn_back.on_left_click = None

    def load_reg_form(self):
        self.hide()
        ACTIVE.append('reg_form')

    def render(self):
        super(SettingsScreen, self).render()
        if self.btn_back.on_left_click is None:
            self.btn_back.on_left_click = self.load_prev
        self.btn_back.render((SCREEN_SIZE.W - self.width, 0))
        self.btn_reg.render((SCREEN_SIZE.W - self.width, 50))
