from utils import COLOR_BLACK
import pygame


class Text:
    def __init__(self, text, font, color=COLOR_BLACK, align='center center'):
        self.text_surface = font.render(text, True, color)
        self.align = align

    def render(self, screen, button_rect):
        (x, y) = (button_rect.x, button_rect.y)
        (w, h) = (button_rect.w, button_rect.h)
        text_rect = self.text_surface.get_rect()

        if self.align == 'top left':
            text_rect.topleft = (x, y)
        if self.align == 'top center':
            text_rect.midtop = (x + w / 2, y)
        if self.align == 'top right':
            text_rect.topright = (x + w, y)

        if self.align == 'center left':
            text_rect.midleft = (x, y + h / 2)
        if self.align == 'center center':
            text_rect.center = (x + w / 2, y + h / 2)
        if self.align == 'center right':
            text_rect.midleft = (x + w, y + h / 2)

        if self.align == 'bottom left':
            text_rect.bottomleft = (x, y + h)
        if self.align == 'bottom center':
            text_rect.midbottom = (x + w / 2, y + h)
        if self.align == 'bottom right':
            text_rect.bottomright = (x + w, y + h)

        screen.blit(self.text_surface, text_rect)
