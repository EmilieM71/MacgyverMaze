class Position:

    def __init__(self, x, y):
        """Class representing a position in a two-dimensional maze

        Args:
            x (Integer): abscissa in mathematics, corresponds to the
            horizontal coordinate that is used to define a point.

            y (Integer): ordinate in mathematics, corresponds to the
            vertical coordinate that is used to define a point.

            The origin of the coordinate system is at the top and left of the maze.
            x increases when moving to the right and y increases when you move down.

            """

        self.x, self.y = x, y

    # method modifying the displayed object when it is called
    # ex :
    # display without using the method :
    # <gamemaze.models.position.Position object at 0x0F281570>
    # display without using the method : (0, 0)
    def __repr__(self):
        """When we enter our object in the interpreter the method
        modifies the display of the object when it is called"""
        return "({}, {})".format(self.x, self.y)


