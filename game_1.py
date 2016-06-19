from utils import EVENT_STREAM, KINECT, NEW_BODY_FRAME_EVENT, SCREEN, SCREEN_SIZE, draw_player
from math import atan2, degrees, pi
from pykinect2 import PyKinectV2
import pygame

pygame.init()

GAME_1_BG = pygame.image.load('game_1.jpg')


class Game_1:
    def __init__(self):
        self._bodies = None

        self.bg = GAME_1_BG

        EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        pass

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, SCREEN_SIZE), (0, 0))

        pygame.display.update()
