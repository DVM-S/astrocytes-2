from utils import (
    ACTIVE,
    COLOR_GREEN,
    SCREEN,
    SCREEN_SIZE)

import pygame
import webbrowser

from components.button import Button
from components.text import Text


def load_game(idx):
    ACTIVE.append('game_%d' % (idx))


def load_profile_page():
    ACTIVE.append('profile_page')


def load_settings_screen():
    ACTIVE.append('settings_screen')


def open_webpage():
    webbrowser.open('http://astrocytes.azurewebsites.net/')


class Menu:
    def __init__(self):
        self.bg = pygame.transform.scale(
            pygame.image.load('menu/menu.png'),
            (SCREEN_SIZE.W, SCREEN_SIZE.H))

        self.init_buttons()

    def init_buttons(self):
        self.logo_btn = Button(
            'menu',
            (30, 30),
            bg=pygame.image.load('menu/logo.png'),
            on_left_click=open_webpage)

        self.game_btn = Button('menu', (
                (305 / 1024.0) * SCREEN_SIZE.W,
                (305 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g.png'),
            fg=pygame.image.load('menu/gf.png'),
            on_left_click=lambda: load_game(2)
        )

        self.btn_1 = Button('menu', (
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g1.png'),
            fg=pygame.image.load('menu/g1f.png')
        )

        self.btn_2 = Button('menu', (
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g4.png'),
            fg=pygame.image.load('menu/g4f.png'),
            on_left_click=lambda: load_game(4)
        )

        self.btn_3 = Button('menu', (
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g3.png'),
            fg=pygame.image.load('menu/g3f.png'),
            on_left_click=load_profile_page
        )

        self.btn_4 = Button('menu', (
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g2.png'),
            fg=pygame.image.load('menu/g2f.png'),
            on_left_click=lambda: load_game(1)
        )

        self.btn_5 = Button('menu', (
                (143 / 1024.0) * SCREEN_SIZE.W,
                (143 / 768.0) * SCREEN_SIZE.H),
            bg=pygame.image.load('menu/g5.png'),
            fg=pygame.image.load('menu/g5f.png'),
        )

        self.hamburger = Button('menu', (
                51 * SCREEN_SIZE.W / 1024,
                31 * SCREEN_SIZE.H / 768),
            bg=pygame.image.load('menu/hamburger.png'),
            on_left_click=load_settings_screen
        )

    def render(self):
        SCREEN.blit(self.bg, (0, 0))

        self.logo_btn.render((
            ((12) / 1024.0) * SCREEN_SIZE.W,
            ((8) / 768.0) * SCREEN_SIZE.H))
        self.game_btn.render((
            ((22 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((94 + 60) / 768.0) * SCREEN_SIZE.H))
        self.btn_1.render((
            ((345 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((94 + 60) / 768.0) * SCREEN_SIZE.H))
        self.btn_2.render((
            ((345 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((257 + 60) / 768.0) * SCREEN_SIZE.H))
        self.btn_3.render((
            ((345 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((420 + 60) / 768.0) * SCREEN_SIZE.H))
        self.btn_4.render((
            ((184 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((420 + 60) / 768.0) * SCREEN_SIZE.H))
        self.btn_5.render((
            ((22 + 10) / 1024.0) * SCREEN_SIZE.W,
            ((420 + 60) / 768.0) * SCREEN_SIZE.H))
        self.hamburger.render((
            ((944) / 1024.0) * SCREEN_SIZE.W,
            ((21) / 768.0) * SCREEN_SIZE.H))
