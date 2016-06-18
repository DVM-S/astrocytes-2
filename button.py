from utils import FONT_ROBOTO, IMAGE_MENU
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

        self.render(screen)

    def click(self, pos, btn):
        if (
            (self.x < pos[0] and pos[0] < self.x + self.w) and
            (self.y < pos[1] and pos[1] < self.y + self.h)
        ):
            if btn[0] == 1:
                self.left_click_callback()

            elif btn[1] == 1:
                self.middle_click_callback()

            elif btn[2] == 1:
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

        mouse_pos = pygame.mouse.get_pos()
        mouse_btn = pygame.mouse.get_pressed()
        self.click(mouse_pos, mouse_btn)
