from utils import FONT_ROBOTO, IMAGE_MENU
import pygame

from text import Text

pygame.init()


class Button:
    def __init__(self, screen, (x, y, w, h), bg, fg=None, text=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.bg = bg
        self.fg = fg

        self.text = text

        self.render(screen)

    def render(self, screen):
        if isinstance(self.bg, pygame.Surface):
            surface = pygame.transform.scale(IMAGE_MENU, (int(self.w), int(self.h)))
            surface_rect = surface.get_rect()
            surface_rect.topleft = (self.x, self.y)
            surface_rect.bottomright = (self.x + self.w, self.y + self.h)

            screen.blit(surface, surface_rect)

        elif isinstance(self.bg, tuple) and len(self.bg) == 3:
            surface_rect = pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w, self.h))

        if self.text:
            self.text.render(screen, surface_rect)
