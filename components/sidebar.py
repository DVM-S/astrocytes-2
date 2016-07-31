from utils import (
    ACTIVE,
    SCREEN,
    SCREEN_SIZE)

import pygame

from components.button import Button
from components.text import Text


class Sidebar(object):
    def __init__(self):
        self.hidden = True
        self.width = 0
        self.max_witdh = 200

    def hide(self):
        self.width = 0
        self.hidden = True
        ACTIVE.pop()

    def render(self):
        if self.hidden:
            tint = pygame.Surface(
                (SCREEN_SIZE.W, SCREEN_SIZE.H),
                pygame.SRCALPHA)
            tint.fill((0, 0, 0, 150))
            SCREEN.blit(tint, (0, 0))
            self.hidden = False

        if self.width < self.max_witdh:
            self.width += 50

        SCREEN.fill(
            (100, 100, 100),
            (SCREEN_SIZE.W - self.width, 0, self.width, SCREEN_SIZE.H))
