from random import randint
from gamemaze.models.element import Element
from gamemaze.models.element_behavior import ElementBehavior
from gamemaze.models.game_image import GameImage
from gamemaze.constants import (WALL_CHAR, START_CHAR, END_CHAR, KEEPER_IMAGE,
                                SIZE_SPRITE, FLOOR_TILES, STRUCTURE_WALL,
                                NEEDLE_IMAGE, TUBE_IMAGE, ETHER_IMAGE)


class Maze:

    def __init__(self, file_path):
        """class that characterizes the elements of the labyrinth by their names,
                images, positions and behaviors.

                Args:
                    :param file_path (String): path of the file that contains the
                    structure of the level

                    :param list[Element] : list of elements that characterizes the maze

                    :param (int) : width corresponding to the number of characters in the
                    first line of the file determined by the load_from_file method

                    :param(int) : height corresponding to the number of rows in the file
                    determined by the load_from_file method

                """
        self.FilePath = file_path
        self.Elements = []
        self.Height = 0
        self.Width = 0

    def load_from_file(self):
        start = GameImage(FLOOR_TILES, 160, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        end = GameImage(FLOOR_TILES, 220, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        wall = GameImage(STRUCTURE_WALL, 40, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
        keeper = GameImage(KEEPER_IMAGE, 0, 0, 32, 36, SIZE_SPRITE, SIZE_SPRITE)
        needle = GameImage(NEEDLE_IMAGE, 0, 0, 545, 720, SIZE_SPRITE, SIZE_SPRITE)
        tube = GameImage(TUBE_IMAGE, 0, 0, 259, 194, SIZE_SPRITE, SIZE_SPRITE)
        ether = GameImage(ETHER_IMAGE, 0, 0, 225, 225, SIZE_SPRITE, SIZE_SPRITE)
        with open(self.FilePath, 'r') as file:
            for y, line in enumerate(file):
                self.Height += 1
                for x, c in enumerate(line):
                    if y == 1:
                        self.Width += 1
                    if c == START_CHAR:
                        self.Elements.append(
                            Element('start', start.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(3)))
                    elif c == END_CHAR:
                        self.Elements.append(
                            Element('end', end.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(4)))
                        self.Elements.append(
                            Element('keeper', keeper.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(1)))
                    elif c == WALL_CHAR:
                        self.Elements.append(
                            Element('wall', wall.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(1)))

        inventory = 0
        while inventory < 4:
            x = randint(0, self.Width)
            y = randint(0, self.Height)
            for element in self.Elements:
                if x * SIZE_SPRITE != element.X and y * SIZE_SPRITE != element.Y:
                    inventory += 1
                    if inventory == 1:
                        self.Elements.append(
                            Element('needle', needle.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(2)))
                    elif inventory == 2:
                        self.Elements.append(
                            Element('tube', tube.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(2)))
                    elif inventory == 3:
                        self.Elements.append(
                            Element('ether', ether.surface,
                                    x * SIZE_SPRITE, y * SIZE_SPRITE,
                                    ElementBehavior(2)))
        print(self.Elements)

    def display(self, window_name):
        """Function that allows to display the labyrinth """
        for element in self.Elements:
            window_name.blit(element.Image, (element.X, element.Y))


def main():
    pass


if __name__ == "__main__":
    main()
