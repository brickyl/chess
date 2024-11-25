from enum import Enum


class Color(Enum):
    BLACK = -1
    WHITE = 1


class Move(Enum):
    REGULAR = 1
    CAPTURE = 2
    INVALID = 3
    PAWN_PROMOTE = 4
    PAWN_ENPASSANT = 5
    KINGSIDE_CASTLE = 6
    QUEENSIDE_CASTLE = 7


mapping = {
    "h": 0,
    "g": 1,
    "f": 2,
    "e": 3,
    "d": 4,
    "c": 5,
    "b": 6,
    "a": 7,
}  # orientation: black side top
