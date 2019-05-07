class Element:

    def __init__(self, name, image, x, y, behavior):
        """class that characterizes the elements of the labyrinth by their names,
        images, positions and behaviors.

        Args:
            name (String): is the name of the element

            image [GameImage] : load, crop, resize an image and then
            transform it into a usable surface with PyGame

            x (integer) : abscissa in mathematics, corresponds to the
            horizontal coordinate that is used to define a point.

            y (integer): ordinate in mathematics, corresponds to the
            vertical coordinate that is used to define a point.

            behavior [element_behavior] : behavior of an element when
            the hero tries to move on it

        The origin of the coordinate system is at the top and left of the maze.
        x increases when moving to the right and y increases when you move down.

        """
        self.Name = name
        self.Image = image
        self.X = x
        self.Y = y
        self.Behavior = behavior

    # method modifying the displayed object when it is called
    # ex : display without using the method :
    # <gamemaze.models.element.Element object at 0x0F8655B0>
    # display without using the method :
    # (start, <Surface(30x30x24 SW)>, (0, 0), ElementBehavior.start)
    def __repr__(self):
        """When we enter our object in the interpreter the method
        modifies the display of the object when it is called"""
        return "({}, {}, ({}, {}), {})".format(self.Name, self.Image, self.X, self.Y, self.Behavior)


def main():
    pass


if __name__ == "__main__":
    main()
