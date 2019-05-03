class Character:
    def __init__(self, name, image, position):
        """class to create the characters of the game,
        characterized by a name, an image, and a starting position.
        With a method that displays them.

        Args:
            name (String): is the name of the character
            image [GameImage]
            position [Position]

        """
        self.Name = name
        self.Image = image
        self.Position = position

    def display(self, window_name):
        window_name.blit(self.Image, self.Position)


def main():
    pass


if __name__ == "__main__":
    main()
