from pieces.piece import Piece
from diagonalmove import DiagonalMove
from constants import Color, Move


class Bishop(Piece, DiagonalMove):
    def __init__(self, row, col, color, board):
        super().__init__("B", row, col, color, board)

    def check_move(self, board, row, col, lastMove):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None and pieceAtDestination.color != self.color:
            if self.diag_clear_path(board, row, col):
                return Move.CAPTURE
        
        if pieceAtDestination == None: 
            if self.diag_clear_path(board, row, col):
                return Move.REGULAR
            
        return Move.INVALID
