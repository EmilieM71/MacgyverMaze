from enum import Enum


class ElementBehavior(Enum):
    block = 1  # prevents the passage of the character (hero)
    pick_up = 2
    start = 3
    end = 4
