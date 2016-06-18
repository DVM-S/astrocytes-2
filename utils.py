import pygame
from rx.subjects import Subject

pygame.init()


# EVENT STREAM
EVENT_STREAM = Subject()


# COLORS
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)


# FONTS
FONT_ROBOTO = pygame.font.Font('fonts/roboto/Roboto-Regular.ttf', 20)


# IMAGES
IMAGE_MENU = pygame.image.load('menu.png')
