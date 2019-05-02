import pygame
from gamemaze.constants import (HERO_SOURCE, SIZE_SPRITE)


class GameImage:

    def __init__(self, file_path, x, y, w, h, width, height):

        # Load image
        self.file_path = file_path

        # crop images
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # Resizing image
        self.width = width
        self.height = height

    def load_image(self):
        pygame.transform.scale(
            (pygame.image.load(self.file_path)).subsurface(
                self.x, self.y, self.w, self.h), (self.width, self.height))


def main():
    hero = GameImage(HERO_SOURCE, 0, 0, 32, 32, SIZE_SPRITE, SIZE_SPRITE)
    hero.load_image()


if __name__ == "__main__":
    main()
