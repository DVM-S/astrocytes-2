from utils import FONT_ROBOTO, IMAGE_MENU, EVENT_STREAM
import pygame

from text import Text

pygame.init()


class Button:
    def __init__(self, screen, (x, y, w, h), bg, fg=None, text=None,
                 on_left_click=None, on_middle_click=None, on_right_click=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.bg = bg
        self.fg = fg
        self.text = text

        self.left_click_callback = on_left_click
        self.middle_click_callback = on_middle_click
        self.right_click_callback = on_right_click

        EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(e)

    def on_click(self, e):
        if (
            (self.x < e.pos[0] and e.pos[0] < self.x + self.w) and
            (self.y < e.pos[1] and e.pos[1] < self.y + self.h)
        ):
            if e.button == 1:
                if self.left_click_callback:
                    self.left_click_callback()

            elif e.button == 2:
                if self.middle_click_callback:
                    self.middle_click_callback()

            elif e.button == 3:
                if self.right_click_callback:
                    self.right_click_callback()

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
