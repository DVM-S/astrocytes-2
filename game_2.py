from utils import (
    COLOR_BLUE,
    KINECT,
    KINECT_EVENT_STREAM,
    KINECT_FRAME_SIZE,
    NEW_BODY_FRAME_EVENT,
    NEW_BODY_INDEX_FRAME_EVENT,
    PLAYER,
    render_player,
    SCREEN,
    SCREEN_SIZE)

from pykinect2 import PyKinectV2
import pygame
import random


class Game_2:
    def __init__(self):
        self.all_particles = []
        self.bg = pygame.image.load('game_2.jpg')
        self.body_frame = None
        self.body_index_frame = None
        self.totalOrange = 0

        (W_s, H_s) = SCREEN_SIZE
        self.target_size = 20
        self.player_size = (W_s / 2, H_s / 2)

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

            # for particle in self.all_particles:
            #     if particle.hidden:
            #         continue

            #     (width, height) = SCREEN_SIZE
            #     if particle.rect.y >= height:
            #         particle.hidden = True
            #         if particle.good:
            #             self.totalOrange -= 1

            #     if (
            #         particle.rect.colliderect(target_left) or
            #         particle.rect.colliderect(target_right)
            #     ):
            #         if particle.good:
            #             self.totalOrange -= 1

            #         particle.hidden = True

    def generate_particles(self, number):
        if pygame.time.get_ticks() % 10 != 0:
            return

        chars = list('abcdefghijklmnopqrstuvwxyz')
        vowels = list('aeiou')
        charactersNormal = [x for x in chars]
        charactersGood = charactersNormal + (1 * vowels)
        charactersBad = list(set(charactersNormal) - set(vowels))

        for x in xrange(number):
            if self.totalOrange == 0:
                randomCharacter = random.sample(vowels, 1)[0]
            elif self.totalOrange <= 10:
                randomCharacter = random.sample(charactersGood, 1)[0]
            else:
                randomCharacter = random.sample(charactersBad, 1)[0]
            good = False
            if randomCharacter in vowels:
                good = True
                self.totalOrange += 1
            particle = Particle(randomCharacter, good)
            self.all_particles.append(particle)

    def render(self):
        SCREEN.blit(pygame.transform.scale(self.bg, SCREEN_SIZE), (0, 0))

        if self.body_index_frame is not None:
            self.generate_particles(2)
            for particle in self.all_particles:
                if not particle.hidden:
                    particle.rect.y += 1
                    SCREEN.blit(particle.textSurface, particle.rect)

            render_player(self.body_index_frame)
            self.check_collisions()
            (W_s, H_s) = SCREEN_SIZE
            (W_p, H_p) = self.player_size
            SCREEN.blit(
                pygame.transform.scale(PLAYER, self.player_size),
                ((W_s - W_p) / 2, H_s - H_p))


class Particle:
    def __init__(self, character, good):
        self.character = character
        self.font = pygame.font.Font(None, 32)
        self.good = good
        self.hidden = False
        self.textSurface = self.font.render('%s' % (character), 1, (0, 0, 0))
        self.rect = self.textSurface.get_rect()
        self.rect.x = random.randint(20, 1000)
        self.rect.y = -20
