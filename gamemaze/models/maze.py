from random import sample
from gamemaze.models.position import Position
from gamemaze.constants import WALL_CHAR, START_CHAR, END_CHAR, PATH_CHAR, SIZE_SPRITE


class Maze:

    def __init__(self, file_path):
        self.FilePath = file_path
        self.Elements = [[], [], [], [], []]
        self.Height = self.height()
        self.Width = self.width()

    def height(self):
        """Calculate the number of rows in a file: corresponds to the height"""
        with open(self.FilePath, 'r') as file:
            nb_line = 0
            for line in file:
                nb_line += 1
        return nb_line

    def width(self):
        """Calculate the number of characters in a file: this corresponds to the width"""
        with open(self.FilePath, 'r') as file:
            line = file.readline()
            nb_c = 0
            for c in line:
                if c != '\n':
                    nb_c += 1
            return nb_c

    def load_from_file(self):
        with open(self.FilePath, 'r') as file:
            for y, line in enumerate(file):
                for x, c in enumerate(line):
                    if c == START_CHAR:
                        self.Elements[0] = (Position(x * SIZE_SPRITE, y * SIZE_SPRITE))
                    elif c == END_CHAR:
                        self.Elements[1] = (Position(x * SIZE_SPRITE, y * SIZE_SPRITE))
                    elif c == WALL_CHAR:
                        self.Elements[2].append(Position(x * SIZE_SPRITE, y * SIZE_SPRITE))
                    elif c == PATH_CHAR:
                        self.Elements[3].append(Position(x * SIZE_SPRITE, y * SIZE_SPRITE))

                self.Elements[4] = sample(self.Elements[3], 3)
                print(self.Elements)

    def display(self):
        pass


def main():

    # import pygame
    # from gamemaze.constants import COTE_WINDOW, IMAGE_ICON, TITLE_WINDOW, HERO_SOURCE, KEEPER_IMAGE, SIZE_SPRITE
    # from gamemaze.models.game_image import GameImage
    #
    # pygame.init()
    # # 1- Creating the Window
    # window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))
    # # 2- Window icon
    # # icon = pygame.image.load(IMAGE_ICON)
    # # pygame.display.set_icon(icon)
    # # 3- Window title
    # pygame.display.set_caption(TITLE_WINDOW)

    # Create maze
    level = Maze('level\level1')
    level.Height()
    level.Width
    level.load_from_file()


if __name__ == "__main__":
    main()
