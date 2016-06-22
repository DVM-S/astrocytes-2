from utils import (
    COLOR_RED,
    SCREEN,
    SCREEN_SIZE)

import pygame


class PauseScreen:
    def __init__(self):
        self.hidden = True
        self.width = 0
        self.max_witdh = 200

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

        if self.width < self.max_witdh:
            self.width += 50
