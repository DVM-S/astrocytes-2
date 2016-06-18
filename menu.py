import pygame
from text import Text

pygame.init()

ROBOTO = pygame.font.Font('fonts/roboto/Roboto-Regular.ttf', 20)


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.transform.scale(
            pygame.image.load('menu.png'),
            self.screen.get_size())

    def render(self):
        self.screen.blit(self.background, (0, 0))

        (width, height) = self.screen.get_size()

        text = Text('Game 1', ROBOTO)
        btn = pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                (345 / 1024.0) * width,
                (94 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height
            )
        )
        text.render(self.screen, btn)

        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                (345 / 1024.0) * width,
                (257 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height
            )
        )

        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                (345 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height
            )
        )

        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                (184 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height
            )
        )

        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            (
                (22 / 1024.0) * width,
                (420 / 768.0) * height,
                (143 / 1024.0) * width,
                (143 / 768.0) * height
            )
        )

        pygame.display.update()
