from Form import Form, FormText, Input, FormButton

from utils import (  # COLORS & FONTS
    ACTIVE,
    COLOR_BLUE,
    COLOR_GREEN,
    COLOR_RED,
    COLOR_YELLOW,
    COLOR_WHITE,
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


class LoginForm:
    def __init__(self):
        # Create form
        self.f = Form(False)

        # Add objects
        self.f.add_object('text', FormText('REGISTRATION', label_style=['bold']))
        self.f.add_object('first_name', Input('First Name'))
        self.f.add_object('last_name', Input('Last Name'))

        self.f.add_object('username', Input('Username'))

        self.f.add_object('submit', FormButton('Submit', self.submit, ()))
        self.f.add_object('reset', FormButton('Reset', self.f.clear, ()))

        EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if ACTIVE[-1] == 'login_form':
            if e.type == pygame.KEYDOWN:
                self.f.update(SCREEN, e)

    def submit(self):
        form_result = self.f.submit()
        print form_result
        ACTIVE.pop()

    def render(self):
        print 123
        self.f.render(SCREEN)

        pygame.display.update()
