import pygame
from gamemaze.constants import (CASE_SIZE, GRAY, WHITE, SYRINGE_IMAGE,
                                BLOOD_STAIN, MACGYVER_SOURCE, RED, GREEN)
from gamemaze.models.element_behavior import ElementBehavior
from gamemaze.models.game_image import GameImage


class Hero:
    """ class to create the hero of the game, characterized by a name, an
    image, and a starting position."""

    def __init__(self, name, image, maze, window):
        """
        Args:
            name (String): is the name of the character

            image [GameImage] : load, crop, resize an image and then
            transform it into a usable surface with PyGame

            maze [GameMaze]

            window [GameWindow]

        The origin of the coordinate system is at the top and left of the maze.
        x increases when moving to the right and y when you move down.

        """
        self.Name = name
        self.Image = image

        self.Maze = maze
        self.Window = window

        # position of the element whose name is start
        start_element = [element for element in self.Maze.Elements
                         if element.Name == 'start'][0]
        self.X = start_element.X
        self.Y = start_element.Y

        # Object pick_up
        self.Needle = False
        self.Tube = False
        self.Ether = False

    def display(self):
        """method for displaying the elements that form the maze"""
        self.Window.surface.blit(self.Image, (
            self.X * CASE_SIZE, self.Y * CASE_SIZE))

    def move(self, direction):
        """Method to move the hero"""
        # Save actual position
        new_x = self.X
        new_y = self.Y

        # Move to the right
        if direction == 'right':
            new_x += 1
        # Move to the left
        elif direction == 'left':
            new_x -= 1
        # Move to the down
        elif direction == 'down':
            new_y += 1
        # Move to the up
        elif direction == 'up':
            new_y -= 1

        # test if new position is out of maze
        if (new_x < 0 or new_x > self.Maze.Width - 1) \
                or (new_y < 0 or new_y > self.Maze.Height - 1):
            return

        # Search if the new position is the same as an element of the maze
        current_element = [el for el in self.Maze.Elements
                           if new_x == el.X and new_y == el.Y]
        if current_element \
                and current_element[0].Behavior == ElementBehavior.block:
            return

        else:
            if current_element \
                    and current_element[0].Behavior == ElementBehavior.end:
                self.end_game()

            else:
                if current_element \
                        and current_element[0].Behavior == \
                        ElementBehavior.pick_up:
                    self.pick_up(current_element[0])

                self.X = new_x
                self.Y = new_y
                self.display()

    def pick_up(self, element_to_pick_up):
        """Method for picking up objects when the hero is in the same position
        as the object :
        - Deletes the image of the object
        - Displays the image of the object picked up to the right of the game
        - Decreases the inventory of objects to recover from 1
        - Display the image of a syringe when the 3 objects are picked up
        """

        if element_to_pick_up.Name == 'needle':
            self.Needle = True
        elif element_to_pick_up.Name == 'tube':
            self.Tube = True
        else:
            self.Ether = True

        syringe = GameImage(SYRINGE_IMAGE, 0, 0, 90, 90, CASE_SIZE, CASE_SIZE)
        list_for_display = [[3, 60], [2, 90], [1, 120]]
        display_pos = [el[1] for el in list_for_display
                       if self.Maze.Inventory == el[0]][0]

        # display the image in the banner
        self.Window.surface.blit(element_to_pick_up.Image, (460, display_pos))
        # delete image in maze
        self.Maze.Elements.remove(element_to_pick_up)
        # increment the object counter by 1
        self.Maze.Inventory -= 1

        if self.Maze.Inventory == 0:
            text_syringe = pygame.font.Font(None, 20)
            text_s = text_syringe.render("Vous avez une seringue ! ", True,
                                         WHITE, GRAY)
            self.Window.surface.blit(text_s, (460, 160))
            self.Window.surface.blit(syringe.surface, (460, 200))

    def end_game(self):
        """ Method that determines the end of the game when the hero is in the
        same position as the goalkeeper. Check if the hero at all objects"""

        keeper_element = [el for el in self.Maze.Elements
                          if el.Name == 'keeper'][0]

        if self.Maze.Inventory == 0:
            MacGyver = GameImage(MACGYVER_SOURCE, 0, 0, 32, 32, 30, 30)
            self.Image = MacGyver.surface
            # Display text "you win"
            text_end_win = pygame.font.Font(None, 40)
            text_win = text_end_win.render("GAGNER", True, GREEN, GRAY)
            self.Window.surface.blit(text_win, (455, 250))
            # delete keeper image in maze
            self.Maze.Elements.remove(keeper_element)
            self.Y += 1
            self.display()

        else:
            blood = GameImage(BLOOD_STAIN, 224, 0, 32, 32, 30, 30)
            self.Image = blood.surface
            text_end_lose = pygame.font.Font(None, 40)
            text_lose = text_end_lose.render("PERDU", True, RED, GRAY)
            self.Window.surface.blit(text_lose, (455, 250))
            list_object = [[self.Needle, "l'aiguille"],
                           [self.Tube, "le tube"],
                           [self.Ether, "l'ether"]]
            missing_object = []
            for item in list_object:
                if not item[0]:
                    missing_object.append(item[1])

            if len(missing_object) > 1:
                missing_object = " ,".join(missing_object)
            else:
                missing_object = str(missing_object[0])
            text_missing_object = pygame.font.Font(None, 20)
            text_object = text_missing_object.render(
                "Object manquant : ", True, WHITE, GRAY)
            self.Window.surface.blit(text_object, (455, 280))
            text_missing_name_object = pygame.font.Font(None, 20)
            text_name_object = text_missing_name_object.render(
                missing_object, True, WHITE, GRAY)
            self.Window.surface.blit(text_name_object, (455, 310))

        # Display text for propose a new game
        text_new_game = pygame.font.Font(None, 20)
        text_for_new_game = text_new_game.render(
            "Appuie sur ENTER pour rejouer", True, WHITE, GRAY)
        self.Window.surface.blit(text_for_new_game, (455, 350))

