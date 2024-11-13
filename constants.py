from enum import Enum

class Color(Enum):
    BLACK = -1
    WHITE = 1

class Move(Enum):
    REGULAR = 1
    CAPTURE = 2
    IRREGULAR = 3
    INVALID = 4

mapping = {"h": 0, "g": 1, "f": 2, "e": 3, "d": 4, "c": 5, "b": 6, "a": 7} # orientation: black side top
