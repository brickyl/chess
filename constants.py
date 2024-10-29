from enum import Enum

class Color(Enum):
    BLACK = 1
    WHITE = 2

class Move(Enum):
    REGULAR = 1
    CAPTURE = 2
    IRREGULAR = 3
    INVALID = 4

mapping = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
