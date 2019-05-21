import pygame
from gamemaze.constants import SIZE_SPRITE, GRAY, WHITE
from gamemaze.models.element_behavior import ElementBehavior


class Hero:

    def __init__(self, name, image, maze, window):
        """class to create the characters of the game,
        characterized by a name, an image, and a starting position.
        With a method that displays them.

        Args:
            name (String): is the name of the character

            image [GameImage] : load, crop, resize an image and then
            transform it into a usable surface with PyGame

            maze [GameMaze]

            window [GameWindow]

        The origin of the coordinate system is at the top and left of the maze.
        x increases when moving to the right and y increases when you move down.

        """
        self.Name = name
        self.Image = image

        self.Maze = maze
        self.Window = window

        # position of the element whose name is start
        self.X = [element.X for element in self.Maze.Elements if element.Name == 'start']
        self.Y = [element.Y for element in self.Maze.Elements if element.Name == 'start']

        # X and y coordinate used when moving the hero
        self.New_X = self.X[0]
        self.New_Y = self.Y[0]

    def display(self):
        """method for displaying the elements that form the maze"""
        self.Window.blit(self.Image, (self.New_X*SIZE_SPRITE, self.New_Y*SIZE_SPRITE))

    def move(self, direction):

        # Move to the right
        if direction == 'right':
            self.New_X += 1
        # Move to the left
        elif direction == 'left':
            self.New_X -= 1
        # Move to the down
        elif direction == 'down':
            self.New_Y += 1
        # Move to the up
        elif direction == 'up':
            self.New_Y -= 1
        # Search if the new position is the same as an element of the maze
        el_b = [el.Behavior for el in self.Maze.Elements if self.New_X == el.X and self.New_Y == el.Y]
        if not el_b:
            # we check that the new position is in the maze
            if 0 <= self.New_X <= self.Maze.Width-1 and 0 <= self.New_Y <= self.Maze.Height-1:
                # Move hero
                self.display()
            else:
                if direction == 'right':
                    self.New_X -= 1
                # Move to the left
                elif direction == 'left':
                    self.New_X += 1
                # Move to the down
                elif direction == 'down':
                    self.New_Y -= 1
                # Move to the up
                elif direction == 'up':
                    self.New_Y += 1
        elif el_b[0] == ElementBehavior(2):
            self.pick_up()
            self.display()
        elif el_b[0] == ElementBehavior(4):
            self.display()
            self.end_game()
        elif el_b[0] == ElementBehavior(3):
            self.display()
        elif el_b[0] == ElementBehavior(1):
            if direction == 'right':
                self.New_X -= 1
            # Move to the left
            elif direction == 'left':
                self.New_X += 1
            # Move to the down
            elif direction == 'down':
                self.New_Y -= 1
            # Move to the up
            elif direction == 'up':
                self.New_Y += 1

    def pick_up(self):
        name_object = [el.Name for el in self.Maze.Elements if self.New_X == el.X and self.New_Y == el.Y]  # ['needle']
        for ob in self.Maze.Elements:
            if ob.Name == name_object[0]:
                if self.Maze.Inventory == 3:
                    y = 60
                elif self.Maze.Inventory == 2:
                    y = 90
                elif self.Maze.Inventory == 1:
                    y = 120
                # display the image in the banner
                self.Window.blit(ob.Image, (460, y))

                # delete image in maze
                self.Maze.Elements.remove(ob)

                # increment the object counter by 1
                self.Maze.Inventory -= 1

    def end_game(self):
        if self.Maze.Inventory == 0:
            text_end_win = pygame.font.Font(None, 30)
            text_win = text_end_win.render("you win", True, WHITE, GRAY)
            self.Window.blit(text_win, (455, 160))
        else:
            text_end_lose = pygame.font.Font(None, 30)
            text_lose = text_end_lose.render("you lose", True, WHITE, GRAY)
            self.Window.blit(text_lose, (455, 160))
