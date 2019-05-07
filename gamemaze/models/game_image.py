import pygame


class GameImage:

    def __init__(self, file_path, x, y, w, h, width, height):
        """
        Arg :
            for load image : pygame.image.load(file_path).convert_alpha()

            :param file_path (String): path of the file that contains the image


            for crop image : ImageLoad.subsurface(x, y, w, h)

            From the starting image that we want to crop, we define the
            coordinates of the upper left point of the surface that interests
            us (x, y), then we indicate the width and height (w, h) that we
            want to get, in pixel

            :param x (integer): abscissa in mathematics, corresponds to the
            horizontal coordinate that is used to define a point.
            :param y (integer): ordinate in mathematics, corresponds to the
            vertical coordinate that is used to define a point.
            :param w (integer): width
            :param h (integer): height


            for resizing image : pygame.transform.scale(image, (width, height))
            to resize the image we indicate the desired width and height in pixels
            :param width (integer): final width for display
            :param height (integer): final height for display


            the last parameter returns a surface usable by PyGame to display an image

        """

        # For load image
        self.file_path = file_path

        # Parameter for crop images
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # Parameter for resizing image
        self.width = width
        self.height = height

        # Parameter surface PyGame
        self.surface = pygame.transform.scale(
            (pygame.image.load(self.file_path)).subsurface(
                self.x, self.y, self.w, self.h), (self.width, self.height))


def main():
    pass


if __name__ == "__main__":
    main()
