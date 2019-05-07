class Hero:

    def __init__(self, name, image, x, y):
        """class to create the characters of the game,
        characterized by a name, an image, and a starting position.
        With a method that displays them.

        Args:
            name (String): is the name of the character

            image [GameImage] : load, crop, resize an image and then
            transform it into a usable surface with PyGame

            x (integer) : abscissa in mathematics, corresponds to the
            horizontal coordinate that is used to define a point.

            y (integer): ordinate in mathematics, corresponds to the
            vertical coordinate that is used to define a point.

        The origin of the coordinate system is at the top and left of the maze.
        x increases when moving to the right and y increases when you move down.

        """
        self.Name = name
        self.Image = image
        self.X = x
        self.Y = y

    def display(self, window_name):
        """method for displaying the elements that form the maze"""
        window_name.blit(self.Image, (self.X, self.Y))

    def move(self):
        pass

    def pick_up(self):
        pass
