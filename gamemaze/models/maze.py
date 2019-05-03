from random import sample
from gamemaze.models.position import Position
from gamemaze.models.element import Element
from gamemaze.models.element_behavior import ElementBehavior
from gamemaze.models.game_image import GameImage
from gamemaze.constants import (WALL_CHAR, START_CHAR, END_CHAR, PATH_CHAR,
                                SIZE_SPRITE, FLOOR_TILES, STRUCTURE_WALL,
                                NEEDLE_IMAGE, TUBE_IMAGE, ETHER_IMAGE)


class Maze:

    def __init__(self, file_path):
        self.FilePath = file_path
        self.Elements = []
        self.PositionPath = []
        self.Objects = []
        self.Height = self.height()
        self.Width = self.width()

    def height(self):
        """Calculate the number of rows in a file: corresponds to the height"""
        with open(self.FilePath, 'r') as file:
            nb_line = 0
            for _ in file:
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
        start = GameImage(FLOOR_TILES, 160, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        end = GameImage(FLOOR_TILES, 220, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        wall = GameImage(STRUCTURE_WALL, 40, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        needle = GameImage(NEEDLE_IMAGE, 0, 0, 545, 720, SIZE_SPRITE, SIZE_SPRITE)
        tube = GameImage(TUBE_IMAGE, 0, 0, 259, 194, SIZE_SPRITE, SIZE_SPRITE)
        ether = GameImage(ETHER_IMAGE, 0, 0, 225, 225, SIZE_SPRITE, SIZE_SPRITE)
        with open(self.FilePath, 'r') as file:
            for y, line in enumerate(file):
                for x, c in enumerate(line):
                    if c == START_CHAR:
                        self.Elements.append(
                            Element('start', start.surface,
                                    Position(x * SIZE_SPRITE, y * SIZE_SPRITE),
                                    ElementBehavior(3)))
                    elif c == END_CHAR:
                        self.Elements.append(
                            Element('end', end.surface,
                                    Position(x * SIZE_SPRITE, y * SIZE_SPRITE),
                                    ElementBehavior(4)))
                    elif c == WALL_CHAR:
                        self.Elements.append(
                            Element('wall', wall.surface,
                                    Position(x * SIZE_SPRITE, y * SIZE_SPRITE),
                                    ElementBehavior(1)))
                    elif c == PATH_CHAR:
                        self.PositionPath.append(Position(x * SIZE_SPRITE, y * SIZE_SPRITE))

        self.Objects = sample(self.PositionPath, 3)
        self.Elements.append(
            Element('needle', needle.surface, self.Objects[0],
                    ElementBehavior(2)))
        self.Elements.append(
            Element('tube', tube.surface, self.Objects[1],
                    ElementBehavior(2)))
        self.Elements.append(
            Element('ether', ether.surface, self.Objects[2],
                    ElementBehavior(2)))

    def display(self, window_name):
        """Function that allows to display the labyrinth """
        for element in self.Elements:
            if element.Name == 'start':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))
            elif element.Name == 'end':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))
            elif element.Name == 'wall':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))
            elif element.Name == 'needle':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))
            elif element.Name == 'tube':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))
            elif element.Name == 'ether':
                window_name.blit(element.Image, (element.Position.x, element.Position.y))


def main():
    pass


if __name__ == "__main__":
    main()
