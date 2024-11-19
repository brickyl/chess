from pieces.piece import Piece
from constants import Color, Move


class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__("R", row, col, color)

    def check_move(self, board, row, col):
        return Move.INVALID

    def move(self, board, row, col):
        raise Exception("Invalid move.")