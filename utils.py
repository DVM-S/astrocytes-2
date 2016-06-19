from rx.subjects import Subject
import ctypes
import numpy as np
import pygame

from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime


pygame.init()


# GLOBAL CONSTANTS
KINECT = PyKinectRuntime.PyKinectRuntime(
    PyKinectV2.FrameSourceTypes_Body |
    PyKinectV2.FrameSourceTypes_Color |
    PyKinectV2.FrameSourceTypes_BodyIndex)

EVENT_STREAM = Subject()
KINECT_EVENT_STREAM = Subject()
SCREEN_SIZE = (512, 384)
SCREEN = pygame.display.set_mode(
    SCREEN_SIZE, pygame.DOUBLEBUF |
    pygame.HWSURFACE)
PLAYER_SIZE = (
    KINECT.body_index_frame_desc.Width,
    KINECT.body_index_frame_desc.Height)
PLAYER = pygame.Surface(PLAYER_SIZE, 0, 32).convert_alpha()

NEW_BODY_FRAME_EVENT = 1 + pygame.USEREVENT
NEW_BODY_INDEX_FRAME_EVENT = 2 + pygame.USEREVENT


# GLOBAL VARIABLES
ACTIVE = {'CURR': 'menu', 'PREV': None}


# COLORS
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)


# FONTS
FONT_ROBOTO = pygame.font.Font('fonts/roboto/Roboto-Regular.ttf', 20)


# HELPER FUNCTIONS
def POST_EVENT(event_type, **event_data):
    e = pygame.event.Event(event_type, event_data)
    EVENT_STREAM.on_next(e)


def POST_NEW_BODY_FRAME_EVENT(**event_data):
    e = pygame.event.Event(NEW_BODY_FRAME_EVENT, event_data)
    KINECT_EVENT_STREAM.on_next(e)


def POST_NEW_BODY_INDEX_FRAME_EVENT(**event_data):
    e = pygame.event.Event(NEW_BODY_INDEX_FRAME_EVENT, event_data)
    KINECT_EVENT_STREAM.on_next(e)


def render_player(frame):
    hide = (frame == 255)
    show = (frame != 255)

    frame[hide] = 0
    frame[show] = 255

    frame = np.array((frame, frame, frame, frame))
    (r, g, b, a) = frame
    r[r == 255] = 100

    frame = np.ravel(frame.T)
    PLAYER.lock()
    address = KINECT.surface_as_array(PLAYER.get_buffer())
    ctypes.memmove(address, frame.ctypes.data, frame.size)
    del address
    PLAYER.unlock()
