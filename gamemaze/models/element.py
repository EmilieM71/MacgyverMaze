class Element:

    def __init__(self, name, image, position, behavior):
        """class that characterizes the elements of the labyrinth by their names,
        images, positions and behaviors.

        Args:
            name (String): is the name of the element
            image [GameImage]
            position [Position]
            behavior [element_behavior]

        """
        self.Name = name
        self.Image = image
        self.Position = position
        self.Behavior = behavior

    # method modifying the displayed object when it is called
    # ex :
    # display without using the method :
    # <gamemaze.models.element.Element object at 0x0F8655B0>
    # display without using the method :
    # (start, <Surface(30x30x24 SW)>, (0, 0), ElementBehavior.start)
    def __repr__(self):
        """When we enter our object in the interpreter the method
        modifies the display of the object when it is called"""
        return "({}, {}, {}, {})".format(self.Name, self.Image, self.Position, self.Behavior)


def main():
    pass


if __name__ == "__main__":
    main()
