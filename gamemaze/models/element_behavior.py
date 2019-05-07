from enum import Enum


class ElementBehavior(Enum):
    """Enumerating behaviors for an item when the hero
    tries to move over it"""
    block = 1  # block the hero: prevents movement
    pick_up = 2  # allows the hero to pick up the object
    # on its position
    start = 3  # set the starting position of the hero
    end = 4  # set the end of the game
