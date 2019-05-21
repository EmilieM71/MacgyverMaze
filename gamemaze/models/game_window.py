import pygame


class GameWindow:

    def __init__(self, height, width, icon_image, title):
        """Create a window with title and icon."""
        self.Height = height
        self.Width = width
        self.IconImage = icon_image
        self.Title = title
        self.surface = None

    def new_window(self):
        """Create a window with title and icon."""

        # Creating the Window
        self.surface = pygame.display.set_mode((self.Width, self.Height))

        # Window title
        pygame.display.set_caption(self.Title)

        # Window icon
        pygame.display.set_icon(pygame.image.load(self.IconImage))

    def new_rect(self, x, y, width, height, color):

        # to change the background color : it's necessary to create a rectangle
        # with a parameter : the color, the coordinates of the point at the top
        # left relative to the surface of the window (x=0, y=0), the width and
        # height of that rectangle (size 300, 200)
        pygame.draw.rect(self.surface, color, (x, y, width, height))
