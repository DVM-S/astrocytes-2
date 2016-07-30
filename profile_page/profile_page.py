from utils import (  # COLORS & FONTS
    COLOR_BLUE,
    COLOR_GREEN,
    COLOR_RED,
    COLOR_YELLOW,
    COLOR_WHITE,
    FONT_DROID)
from utils import (  # KINECT
    KINECT,
    KINECT_EVENT_STREAM,
    KINECT_FRAME_SIZE,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT)
from utils import (  # PYGAME
    CORRECT_ANSWER,
    INCORRECT_ANSWER,
    render_player,
    SCREEN,
    SCREEN_SIZE,
    Size)

from pykinect2 import PyKinectV2
import pygame
import pygame.gfxdraw
import random
import math

from components.text import Text

# CHAR_SIZE = Size(FONT_DROID.size(' '))
CHAR_SIZE = Size((28, 54))
LAST_X = 0


def rad(deg):
    return deg / 180.0 * math.pi


class ProfilePage:
    def __init__(self):
        self.bg = pygame.image.load('profile_page/profile_page.png')
        self.origin = (722 / 1024.0 * SCREEN_SIZE.W, 389 / 768.0 * SCREEN_SIZE.H)
        self.step_size = 26.0 / 1024 * SCREEN_SIZE.W
        self.step_count = 8

        self.domain_angles = {
            'arithmetic': -90.0,
            'consistency': -30.0,
            'linguistics': 30.0,
            'cooperation': 90.0,
            'mental_ability': 150.0,
            'general_knowledge': 210.0,
        }

        self.domain_scores = {
            'arithmetic': 10.0,
            'consistency': 20.0,
            'linguistics': 30.0,
            'cooperation': 40.0,
            'mental_ability': 50.0,
            'general_knowledge': 60.0,
        }

        self.domains = [
            'arithmetic',
            'consistency',
            'linguistics',
            'cooperation',
            'mental_ability',
            'general_knowledge',
        ]

        KINECT_EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        pass

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, (SCREEN_SIZE.W, SCREEN_SIZE.H)), (0, 0))

        points = []
        for domain in self.domains:
            score = math.log(self.domain_scores[domain]) / math.log(max(self.domain_scores.values()))
            radius = score * self.step_size * (self.step_count - 1)
            angle = rad(self.domain_angles[domain])
            point = (
                radius * math.cos(angle) + self.origin[0],
                radius * math.sin(angle) + self.origin[1])
            points.append(point)

        pygame.gfxdraw.filled_polygon(SCREEN, points, (38, 187, 249))
        pygame.gfxdraw.aapolygon(SCREEN, points, (38, 187, 249))

        pygame.display.update()
