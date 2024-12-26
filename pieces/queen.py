from pieces.piece import Piece
from diagonalmove import DiagonalMove
from straightmove import StraightMove
from constants import Color, Move


class Queen(Piece, DiagonalMove, StraightMove):
    def __init__(self, row, col, color, board):
        super().__init__("Q", row, col, color, board)

    def check_move(self, board, row, col, _):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None and pieceAtDestination.color != self.color:
            if self.diag_clear_path(board, row, col) or self.straight_clear_path(board, row, col):
                return Move.CAPTURE
        
        if pieceAtDestination == None: 
            if self.diag_clear_path(board, row, col) or self.straight_clear_path(board, row, col):
                return Move.REGULAR
            
        return Move.INVALID


