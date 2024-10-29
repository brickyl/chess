from enum import Enum

# class syntax
class Move(Enum):
    REGULAR = 1
    CAPTURE = 2
    IRREGULAR = 3
    INVALID = 4