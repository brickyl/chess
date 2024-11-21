from pieces.piece import Piece
from straightmove import StraightMove
from constants import Color, Move


class Rook(Piece, StraightMove):
    def __init__(self, row, col, color):
        super().__init__("R", row, col, color)

    def check_move(self, board, row, col, lastMove):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None and pieceAtDestination.color != self.color:
            if self.straight_clear_path(board, row, col):
                return Move.CAPTURE
        
        if pieceAtDestination == None: 
            if self.straight_clear_path(board, row, col):
                return Move.REGULAR
            
        return Move.INVALID


    def move(self, board, row, col, lastMove):
        status = self.check_move(board, row, col, lastMove)

        if status == Move.REGULAR or status == Move.CAPTURE:
            board.setPieceAtLocation(self.row, self.col, None)
            self.row = row
            self.col = col
            board.setPieceAtLocation(row, col, self)

        else:
            raise Exception("Invalid move.")