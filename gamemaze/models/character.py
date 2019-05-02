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
    import pygame
    from gamemaze.constants import COTE_WINDOW, IMAGE_ICON, TITLE_WINDOW, HERO_SOURCE, KEEPER_IMAGE, SIZE_SPRITE
    from gamemaze.models.game_image import GameImage

    pygame.init()
    # 1- Creating the Window
    window = pygame.display.set_mode((COTE_WINDOW, COTE_WINDOW))
    # 2- Window icon
    icon = pygame.image.load(IMAGE_ICON)
    pygame.display.set_icon(icon)
    # 3- Window title
    pygame.display.set_caption(TITLE_WINDOW)

    # Load, crop and resizing image from class GameImage
    hero = GameImage(HERO_SOURCE, 0, 0, 32, 32, SIZE_SPRITE, SIZE_SPRITE)
    keeper = GameImage(KEEPER_IMAGE, 0, 0, 32, 36, SIZE_SPRITE, SIZE_SPRITE)

    # Create character
    mg = Character('MacGyver', hero)
    mg.display(window)
    the_keeper = Character('keeper', keeper)
    the_keeper.display(window)


if __name__ == "__main__":
    main()
