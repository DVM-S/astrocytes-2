from utils import (  # COLORS & FONTS
    COLOR_RED,
    COLOR_YELLOW,
    FONT_DROID)
from utils import (  # KINECT
    KINECT,
    EVENT_STREAM,
    KINECT_FRAME_SIZE,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT)
from utils import (  # PYGAME
    CORRECT_ANSWER,
    INCORRECT_ANSWER,
    SCREEN,
    SCREEN_SIZE,
    Size)


from pykinect2 import PyKinectV2
import pygame
import random

from components.text import Text


class Game_4:
    def __init__(self):
        self.punch_frame = 0
        self.punch = None
        self.punch_frame_length = 4

        self.bg = pygame.image.load('game_4/game_4.png')
        self.q_tab = pygame.image.load('game_4/Q-tab.png')

        self.croc_left = pygame.image.load('game_4/croc-left.png')
        self.croc_left_big = pygame.image.load('game_4/croc-left-big.png')
        self.croc_right = pygame.image.load('game_4/croc-right.png')
        self.croc_right_big = pygame.image.load('game_4/croc-right-big.png')

        self.player_left = pygame.image.load('game_4/player-left.png')
        self.player_left_big = pygame.image.load('game_4/player-left-big.png')
        self.player_right = pygame.image.load('game_4/player-right.png')
        self.player_right_big = pygame.image.load('game_4/player-right-big.png')

        EVENT_STREAM.subscribe(self.event_handler)
        # self.tab = pygame.image.load('tab.png')

    def event_handler(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.punch = 'player_left'
            if e.key == pygame.K_RIGHT:
                self.punch = 'player_right'

        if e.type == NEW_BODY_FRAME_EVENT:
            self.body_frame = e.body_frame
        elif e.type == NEW_BODY_INDEX_FRAME_EVENT:
            self.body_index_frame = e.body_index_frame

    def croc_punch_left(self):
        pass

    def crock_punch_right(self):
        pass

    def player_punch_left(self):
        pass

    def player_punch_right(self):
        pass

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, (SCREEN_SIZE.W, SCREEN_SIZE.H)), (0, 0))
        # SCREEN.blit(self.croc_left, (330, 275))
        # SCREEN.blit(self.croc_right, (530, 275))

        # SCREEN.blit(self.croc_left_big, (330, 200))
        # SCREEN.blit(self.croc_right_big, (430, 200))

        # SCREEN.blit(self.player_left, (0, 400))
        # SCREEN.blit(self.player_right, (800, 310))

        # SCREEN.blit(self.player_left_big, (130, 190))
        # SCREEN.blit(self.player_right_big, (430, 190))

        if not self.punch == 'croc_left':
            SCREEN.blit(self.croc_left, (330, 275))

        if not self.punch == 'croc_right':
            SCREEN.blit(self.croc_right, (530, 275))

        if not self.punch == 'player_left':
            SCREEN.blit(self.player_left, (0, 400))

        if not self.punch == 'player_right':
            SCREEN.blit(self.player_right, (800, 310))

        if self.punch == 'croc_left':
            SCREEN.blit(self.croc_left_big, (330, 200))
            self.punch_frame += 1
            if self.punch_frame == self.punch_frame_length:
                self.punch_frame = 0
                self.punch = None

        if self.punch == 'croc_right':
            SCREEN.blit(self.croc_right_big, (430, 190))
            self.punch_frame += 1
            if self.punch_frame == self.punch_frame_length:
                self.punch_frame = 0
                self.punch = None

        if self.punch == 'player_left':
            SCREEN.blit(self.player_left_big, (130, 190))
            self.punch_frame += 1
            if self.punch_frame == self.punch_frame_length:
                self.punch_frame = 0
                self.punch = None

        if self.punch == 'player_right':
            SCREEN.blit(self.player_right_big, (430, 190))
            self.punch_frame += 1
            if self.punch_frame == self.punch_frame_length:
                self.punch_frame = 0
                self.punch = None

        SCREEN.blit(self.q_tab, (0, 601))

        pygame.display.update()
