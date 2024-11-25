from pieces.piece import Piece
from straightmove import StraightMove
from constants import Color, Move


class Rook(Piece, StraightMove):
    def __init__(self, row, col, color):
        self.hasMoved = False
        super().__init__("R", row, col, color)

    def check_move(self, board, row, col, lastMove):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None and pieceAtDestination.color != self.color:
            if self.straight_clear_path(board, row, col):
                self.hasMoved = True
                return Move.CAPTURE

        if pieceAtDestination == None:
            if self.straight_clear_path(board, row, col):
                self.hasMoved = True
                return Move.REGULAR

        return Move.INVALID
