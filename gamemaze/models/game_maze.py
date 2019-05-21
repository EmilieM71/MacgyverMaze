from random import randint
from gamemaze.models.element import Element
from gamemaze.models.element_behavior import ElementBehavior
from gamemaze.models.game_image import GameImage
from gamemaze.constants import (WALL_CHAR, START_CHAR, END_CHAR, KEEPER_IMAGE,
                                SIZE_SPRITE, FLOOR_TILES, STRUCTURE_WALL,
                                NEEDLE_IMAGE, TUBE_IMAGE, ETHER_IMAGE)


class GameMaze:

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
        self.Inventory = 0

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
                        if c != '\n':
                            self.Width += 1
                    if c == START_CHAR:
                        self.Elements.append(
                            Element('start', start.surface,
                                    x, y,
                                    ElementBehavior(3)))
                    elif c == END_CHAR:
                        self.Elements.append(
                            Element('end', end.surface,
                                    x, y,
                                    ElementBehavior(4)))
                        self.Elements.append(
                            Element('keeper', keeper.surface,
                                    x, y,
                                    ElementBehavior(1)))
                    elif c == WALL_CHAR:
                        self.Elements.append(
                            Element('wall', wall.surface,
                                    x, y,
                                    ElementBehavior(1)))
        # print(self.Elements)
        item = 0
        while self.Inventory < 3:
            list_object = [['needle', needle.surface],
                           ['tube', tube.surface],
                           ['ether', ether.surface]]
            x = randint(0, self.Width - 1)
            y = randint(0, self.Height - 1)

            el = [element for element in self.Elements if element.X == x and element.Y == y]
            if not el:
                self.Elements.append(
                    Element(list_object[item][0], list_object[item][1],
                            x, y, ElementBehavior(2)))
                item += 1
                self.Inventory += 1

    def display(self, window_name):
        """Function that allows to display the labyrinth """
        for element in self.Elements:
            window_name.blit(element.Image, (element.X*SIZE_SPRITE, element.Y*SIZE_SPRITE))


def main():
    pass


if __name__ == "__main__":
    main()
