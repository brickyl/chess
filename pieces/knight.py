from pieces.piece import Piece
from constants import Color, Move


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__("N", row, col, color)

    def check_move(self, board, row, col, lastMove):
        return Move.INVALID

    def move(self, board, row, col, lastMove):
        raise Exception("Invalid move.") 