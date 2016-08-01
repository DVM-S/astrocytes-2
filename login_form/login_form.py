from Form import Form, FormText, Input, FormButton

from utils import EVENT_STREAM, SCREEN, ACTIVE, STORE

from api import get_api_key

import pygame
import pygame.gfxdraw
import random
import math

from components.text import Text


def rad(deg):
    return deg / 180.0 * math.pi


class LoginForm:
    def __init__(self):
        # Create form
        self.f = Form(False)

        # Add objects
        self.f.add_object('text', FormText('REGISTRATION', label_style=['bold']))
        self.f.add_object('username', Input('Username'))
        self.f.add_object('password', Input('Password'))

        self.f.add_object('submit', FormButton('Submit', self.submit, ()))
        self.f.add_object('reset', FormButton('Reset', self.f.clear, ()))

        EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if ACTIVE[-1] == 'login_form':
            if e.type == pygame.KEYDOWN:
                self.f.update(SCREEN, e)

    def submit(self):
        form_result = self.f.submit()

        api_key = get_api_key(form_result['username'], form_result['password'])
        print api_key
        STORE['username'] = form_result['username']
        STORE['api_key'] = api_key
        ACTIVE.pop()

    def render(self):
        self.f.render(SCREEN)

        pygame.display.update()
