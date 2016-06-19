import pygame
from rx.subjects import Subject

pygame.init()


# GLOBAL STATE VARIABLES
EVENT_STREAM = Subject()
SCREEN_SIZE = (512, 384)
SCREEN = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE)
ACTIVE = {'CURR': 'menu', 'PREV': None}


# GLOBAL CONSTANTS
KINECT_BODY_FRAMES = 'KINECT_BODY_FRAMES'


# COLORS
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)


# FONTS
FONT_ROBOTO = pygame.font.Font('fonts/roboto/Roboto-Regular.ttf', 20)
