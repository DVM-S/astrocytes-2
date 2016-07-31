from utils import (  # COLORS & FONTS
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
    CORRECT_ANSWER,
    INCORRECT_ANSWER,
    render_player,
    SCREEN,
    SCREEN_SIZE,
    Size)


from pykinect2 import PyKinectV2
import csv
import pygame
import random

from components.text import Text


class Game_4:
    def __init__(self):
        self.punch_frame_length = 4
        self.player_size = Size(
            int(KINECT_FRAME_SIZE.W / 1.5),
            int(KINECT_FRAME_SIZE.H / 1.5))

        self.level = 1
        self.health = 100.0
        self.triggered_once_this_turn = False
        self.should_load_next_question = True
        self.player_reset = True
        self.question = True
        self.punch_frame = 0
        self.punch = None

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

        self.health_red = pygame.image.load('game_4/health-red.png')
        self.health_green = pygame.image.load('game_4/health-green.png')

        self.body_frame = None
        self.body_index_frame = None

        self.new_questions = []
        self.right_questions = []
        self.wrong_questions = []

        with open('game_4/questions.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                question = {
                    'text': row[0],
                    'option1': row[1],
                    'option2': row[2],
                }
                if row[3] == 'A':
                    question['answer'] = 1
                elif row[3] == 'B':
                    question['answer'] = 2
                self.new_questions.append(question)

        # self.tab = pygame.image.load('tab.png')
        KINECT_EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if e.type == NEW_BODY_FRAME_EVENT:
            self.body_frame = e.body_frame
        elif e.type == NEW_BODY_INDEX_FRAME_EVENT:
            self.body_index_frame = e.body_index_frame

    # def croc_punch_left(self):
    #     pass

    # def crock_punch_right(self):
    #     pass

    # def player_punch_left(self):
    #     pass

    # def player_punch_right(self):
    #     pass

    def load_next_question(self):
        q_idx = random.randint(0, len(self.new_questions) - 1)
        self.question = self.new_questions.pop(q_idx)
        print self.question
        self.should_load_next_question = False
        self.player_reset = False
        self.triggered_once_this_turn = False

    def render(self):
        if self.should_load_next_question:
            if self.player_reset:
                self.load_next_question()

        SCREEN.blit(pygame.transform.scale(self.bg, (SCREEN_SIZE.W, SCREEN_SIZE.H)), (0, 0))
        # SCREEN.blit(self.croc_left, (330, 275))
        # SCREEN.blit(self.croc_right, (530, 275))

        # SCREEN.blit(self.player_left, (0, 400))
        # SCREEN.blit(self.player_right, (800, 310))

        # SCREEN.blit(self.croc_left_big, (330, 200))
        # SCREEN.blit(self.croc_right_big, (430, 200))

        # SCREEN.blit(self.player_left_big, (130, 190))
        # SCREEN.blit(self.player_right_big, (430, 190))
        health_rect = self.health_red.get_rect()
        health_rect.midtop = (SCREEN_SIZE.W / 2, 20)
        SCREEN.blit(self.health_red, health_rect)
        SCREEN.blit(
            self.health_green,
            health_rect,
            (0, 0, (self.health / 100.0) * health_rect.width, health_rect.height))

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
            SCREEN.blit(self.croc_right_big, (430, 200))
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

        n = 30

        question_text = self.question['text']
        question_text = [question_text[i:i+n] for i in range(0, len(question_text), n)]
        for (i, line) in enumerate(question_text):
            line = Text(line, FONT_DROID, 30, (15, 244, 198))
            line_rect = line.get_rect()
            line_rect.center = (SCREEN_SIZE.W / 2, SCREEN_SIZE.H - 140 + (0.5 + i) * line_rect.height)
            line.render(line_rect)

        option1 = Text(self.question['option1'], FONT_DROID, 40, (1, 22, 39))
        option2 = Text(self.question['option2'], FONT_DROID, 40, (1, 22, 39))

        if self.body_frame is not None:
            render_player(
                self.body_index_frame,
                self.player_size,
                'bottom center')

            for body in self.body_frame.bodies:
                if not body.is_tracked:
                    continue
                joints = body.joints

                hand_left = joints[PyKinectV2.JointType_HandLeft].Position.z
                hand_right = joints[PyKinectV2.JointType_HandRight].Position.z

                spine_mid = joints[PyKinectV2.JointType_SpineMid].Position.z

                player_choice = 0
                if spine_mid - hand_left > 0.5:
                    player_choice = 1
                if spine_mid - hand_right > 0.5:
                    player_choice = 2

                if player_choice == self.question['answer']:
                    if self.question['answer'] == 1:
                        self.punch = 'player_left'
                    elif self.question['answer'] == 2:
                        self.punch = 'player_right'

                    if not self.triggered_once_this_turn:
                        self.triggered_once_this_turn = True
                        CORRECT_ANSWER.play()
                        self.right_questions.append(self.question)
                        self.health += 10
                        if self.health > 100:
                            self.health = 100
                        self.should_load_next_question = True

                elif not player_choice == 0:
                    if self.question['answer'] == 1:
                        self.punch = 'croc_right'
                    elif self.question['answer'] == 2:
                        self.punch = 'croc_left'

                    if not self.triggered_once_this_turn:
                        self.triggered_once_this_turn = True
                        INCORRECT_ANSWER.play()
                        self.wrong_questions.append(self.question)
                        self.health -= 10
                        self.should_load_next_question = True
                else:
                    if self.should_load_next_question:
                        self.player_reset = True

        pygame.display.update()
