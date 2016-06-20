from utils import (
    KINECT_EVENT_STREAM,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT,
    SCREEN,
    SCREEN_SIZE)

import pygame


class Game_3:
    def __init__(self):
        self.bg = pygame.image.load('game_3.jpg')

        (W_s, H_s) = SCREEN_SIZE
        self.player_size = (W_s / 3, H_s / 3)
        KINECT_EVENT_STREAM.subscribe(self.event_handler)

    def event_handler(self, e):
        if e.type == NEW_BODY_FRAME_EVENT:
            self.body_frame = e.body_frame
        elif e.type == NEW_BODY_INDEX_FRAME_EVENT:
            self.body_index_frame = e.body_index_frame

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, SCREEN_SIZE), (0, 0))
        pygame.display.update()
