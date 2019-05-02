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
        self.X = x
        self.Y = y
