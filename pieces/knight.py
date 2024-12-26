from pieces.piece import Piece
from constants import Color, Move


class Knight(Piece):
    def __init__(self, row, col, color, board):
        super().__init__("N", row, col, color, board)

    def check_move(self, board, row, col, _):
        pieceAtDest = board.getPieceAtLocation(row, col)
        if pieceAtDest != None and pieceAtDest.color != self.color:
            if abs(self.col - col) == 2 and abs(self.row - row) == 1:
                return Move.CAPTURE
            if abs(self.row - row) == 2 and abs(self.col - col) == 1:
                return Move.CAPTURE
        elif pieceAtDest == None:
            if abs(self.col - col) == 2 and abs(self.row - row) == 1:
                return Move.REGULAR
            if abs(self.row - row) == 2 and abs(self.col - col) == 1:
                return Move.REGULAR
        return Move.INVALID
