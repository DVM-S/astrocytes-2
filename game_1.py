from utils import (
    draw_player,
    KINECT,
    KINECT_EVENT_STREAM,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT,
    SCREEN,
    SCREEN_SIZE)

from math import atan2, degrees, pi
from pykinect2 import PyKinectV2
import pygame

pygame.init()

GAME_1_BG = pygame.image.load('game_1.jpg')


class Game_1:
    def __init__(self):
        self.bg = GAME_1_BG
        self.body_frame = None
        self.body_index_frame = None

        KINECT_EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if e.type == NEW_BODY_FRAME_EVENT:
            self.body_frame = e.body_frame
        elif e.type == NEW_BODY_INDEX_FRAME_EVENT:
            self.body_index_frame = e.body_index_frame

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, SCREEN_SIZE), (0, 0))

        if self.body_index_frame is not None:
            draw_player(
                self.body_index_frame,
                pygame.Surface(
                    (
                        KINECT.body_index_frame_desc.Width,
                        KINECT.body_index_frame_desc.Height),
                    0, 32).convert_alpha())

        pygame.display.update()
