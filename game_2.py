from utils import (  # COLORS & FONTS
    COLOR_BLUE,
    COLOR_GREEN,
    COLOR_RED,
    COLOR_YELLOW,
    FONT_DROID)
from utils import (  # KINECT
    KINECT,
    KINECT_EVENT_STREAM,
    KINECT_FRAME_SIZE,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT)
from utils import (  # PYGAME
    PLAYER,
    render_player,
    RIGHT_ANSWER,
    SCREEN,
    WRONG_ANSWER,
    SCREEN_SIZE)

from pykinect2 import PyKinectV2
import pygame
import random

from text import Text

INCR = 20
(W_c, H_c) = FONT_DROID.size(' ')


class Game_2:
    def __init__(self):
        self.bg = pygame.image.load('game_1.jpg')
        self.probability_of_good_char = 0.3  # Probability of next character being good
        self.margin_row = 20

        self.chars_on_screen = []
        self.good_chars_on_screen_count = 0
        self.frame = 0

        (W_s, H_s) = SCREEN_SIZE
        self.target_size = 20
        self.player_size = (W_s / 2, H_s / 2)

        self.body_frame = None
        self.body_index_frame = None

        KINECT_EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if e.type == NEW_BODY_FRAME_EVENT:
            self.body_frame = e.body_frame
        elif e.type == NEW_BODY_INDEX_FRAME_EVENT:
            self.body_index_frame = e.body_index_frame

    def check_collisions(self):
        for body in self.body_frame.bodies:
            if not body.is_tracked:
                continue
            joints = body.joints
            jointPoints = KINECT.body_joints_to_depth_space(joints)

            hand_left = jointPoints[PyKinectV2.JointType_HandLeft]
            hand_right = jointPoints[PyKinectV2.JointType_HandRight]

            (W_p, H_p) = self.player_size
            (W_kf, H_kf) = KINECT_FRAME_SIZE
            (W_s, H_s) = SCREEN_SIZE

            target_left = pygame.draw.circle(
                SCREEN,
                COLOR_BLUE,
                (
                    int(hand_left.x * W_p / W_kf + (W_s - W_p) / 2),
                    int(hand_left.y * H_p / H_kf + H_s - H_p)
                ), self.target_size)
            target_right = pygame.draw.circle(
                SCREEN,
                COLOR_BLUE,
                (
                    int(hand_right.x * W_p / W_kf + (W_s - W_p) / 2),
                    int(hand_right.y * H_p / H_kf + H_s - H_p)
                ), self.target_size)

            for char in self.chars_on_screen:
                if char.collide(target_left) or char.collide(target_right):
                    if char.is_good:
                        RIGHT_ANSWER.play()
                    else:
                        WRONG_ANSWER.play()

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, SCREEN_SIZE), (0, 0))

        bad_chars = list('BCDFGHJKLMNPQRSTVWXYZ')
        good_chars = list('AEIOU')
        next_char_at = (self.margin_row + H_c) / INCR

        self.frame += 1
        if self.frame % next_char_at == 0:
            if random.random() <= self.probability_of_good_char:
                char = Char(random.choice(good_chars), is_good=True)
            else:
                char = Char(random.choice(bad_chars), is_good=False)
            self.chars_on_screen.append(char)

        if self.body_index_frame is not None:
            for char in self.chars_on_screen:
                char.render()

            self.check_collisions()
            render_player(self.body_index_frame)
            (W_s, H_s) = SCREEN_SIZE
            (W_p, H_p) = self.player_size
            SCREEN.blit(
                pygame.transform.scale(PLAYER, self.player_size),
                ((W_s - W_p) / 2, H_s - H_p))

            self.chars_on_screen = [char for char in self.chars_on_screen if char.fresh]

        pygame.display.update()


class Char:
    def __init__(self, char, is_good):
        self.fresh = True
        self.is_good = is_good
        if self.is_good:
            self.text = Text(char, FONT_DROID, COLOR_GREEN)
        else:
            self.text = Text(char, FONT_DROID, COLOR_RED)

        (W_s, H_s) = SCREEN_SIZE
        margin_edge = W_s / 4
        self.rect = self.text.text_surface.get_rect()
        self.rect.x = random.randint(margin_edge, SCREEN_SIZE[0] - W_c - margin_edge)
        self.rect.y = -H_c

    def collide(self, rect):
        did_collide = self.rect.colliderect(rect)
        if did_collide:
            self.fresh = False
        return did_collide

    def move(self):
        self.rect.y += INCR
        (W_s, H_s) = SCREEN_SIZE
        if self.rect.y >= H_s:
            self.fresh = False

    def render(self):
        self.move()
        self.text.render(SCREEN, self.rect)
