import pygame
from gamemaze.constants import (HERO_SOURCE, SIZE_SPRITE)


class GameImage:

    def __init__(self, file_path, x, y, w, h, width, height):

        # For load image
        self.file_path = file_path

        # Parameter for crop images
        self.x, self.y, self.w, self.h = x, y, w, h

        # Parameter for resizing image
        self.width, self.height = width, height

        # Surface use for PyGame
        self.surface = pygame.transform.scale(
            (pygame.image.load(self.file_path)).subsurface(
                self.x, self.y, self.w, self.h), (self.width, self.height))


def main():
    pass


if __name__ == "__main__":
    main()
