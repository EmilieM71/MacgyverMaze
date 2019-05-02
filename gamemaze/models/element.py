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
        self.image = image
        self.position = position
        self.behavior = behavior


def main():
    from gamemaze.constants import (STRUCTURE_WALL, NEEDLE_IMAGE, TUBE_IMAGE,
                                    ETHER_IMAGE, SIZE_SPRITE)
    from gamemaze.models.game_image import GameImage
    from gamemaze.models.element_behavior import ElementBehavior

    # Load, crop and resizing image from class GameImage
    wall = GameImage(STRUCTURE_WALL, 40, 20, 20, 20, SIZE_SPRITE, SIZE_SPRITE)
    needle = GameImage(NEEDLE_IMAGE, 0, 0, 545, 720, SIZE_SPRITE, SIZE_SPRITE)
    tube = GameImage(TUBE_IMAGE, 0, 0, 259, 194, SIZE_SPRITE, SIZE_SPRITE)
    ether = GameImage(ETHER_IMAGE, 0, 0, 225, 225, SIZE_SPRITE, SIZE_SPRITE)

    block = ElementBehavior(1)
    pick_up = ElementBehavior(2)

    # Create element
    walls = Element('wall', wall, (0, 30), block)
    needle = Element('needle', needle, (30, 0), pick_up)
    tube = Element('tube', tube, (30, 30), pick_up)
    ether = Element('ether', ether, (60, 60), pick_up)


if __name__ == "__main__":
    main()
