from enum import Enum


class ElementBehavior(Enum):
    """Enumerating behaviors for an item when the hero
    tries to move over it
    :arg
        :param block (int): prevents the movement of the hero

        :param pick_up (int): allows the hero to be able to pick up an object
        when he moves on it

        :param start (int): set the starting position of the hero

        :param end (int): set the end of the game
        """

    block = 1
    pick_up = 2
    start = 3
    end = 4
