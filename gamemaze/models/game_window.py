import pygame
import os
from gamemaze.constants import BLACK, WHITE, GRAY


class GameWindow:
    """class use to create a new window, with title, icon, background"""

    def __init__(self, name, height, width, icon_image, title, bg_color):
        """Create a window with title and icon."""
        self.Name = name
        self.Height = height
        self.Width = width
        self.IconImage = icon_image
        self.Title = title
        self.BgColor = bg_color
        self.surface = None

    def new_window(self):
        """Create a window with title and icon."""
        pygame.init()  # launch of PyGame

        # Position the window on the screen at (400,600).
        os.environ['SDL_VIDEO_WINDOW_POS'] = "700,150"
        # Create window
        self.surface = pygame.display.set_mode((self.Width, self.Height))
        # Fill the window with a background color
        self.surface.fill(BLACK)
        # Put a title to the window
        pygame.display.set_caption(self.Title)
        # Add window icon
        pygame.display.set_icon(pygame.image.load(self.IconImage))
        # Refresh the screen
        pygame.display.flip()

    def new_rect(self, x, y, width, height, color):
        """
        To change the background color on a part of the window, it's necessary
        to create a rectangle with a parameter : the color, the coordinates of
        the point at the top left relative to the surface of the window
        (x=0, y=0), the width and height of that rectangle (size 300, 200)
        """
        pygame.draw.rect(self.surface, color, (x, y, width, height))

    def display_text(self, text, font_size, font_color, background_color,
                     position_x, position_y):
        """Method for displaying text"""
        texts = pygame.font.Font(None, font_size)
        text_home = texts.render(text, True, font_color, background_color)
        self.surface.blit(text_home, (position_x, position_y))

    def display_inventory(self, hero):
        """Method for displaying hero inventory"""
        nb_object_to_find = pygame.font.Font(None, 15)
        text_object = nb_object_to_find.render("Nombre d'objets à trouver : ",
                                               True, WHITE, GRAY)
        self.surface.blit(text_object, (455, 10))
        inventory = pygame.font.Font(None, 20)
        text_inventory = inventory.render(str(hero.Maze.Inventory), True,
                                          WHITE, GRAY)
        self.surface.blit(text_inventory, (600, 10))
