from utils import (
    COLOR_BLACK,
    COLOR_WHITE,
    FONT_ROBOTO,
    SCREEN,
    SCREEN_SIZE)

import pygame

from button import Button
from text import Text


class PauseScreen:
    def __init__(self):
        self.hidden = True
        self.width = 0
        self.max_witdh = 200

        self.init_buttons()

    def init_buttons(self):
        self.btn_back = Button(
            (0, 0, 100, 100),
            bg=(0, 0, 0),
            fg=(100, 100, 100),
            text=Text('Back', FONT_ROBOTO, COLOR_WHITE))

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

        self.btn_back.render()
        SCREEN.fill(
            (100, 100, 100),
            (SCREEN_SIZE.W - self.width, 0, self.width, SCREEN_SIZE.H))

        if self.width < self.max_witdh:
            self.width += 50
