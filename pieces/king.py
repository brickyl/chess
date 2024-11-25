from pieces.piece import Piece
from pieces.rook import Rook
from straightmove import StraightMove
from constants import Color, Move


class King(Piece, StraightMove):
    def __init__(self, row, col, color):
        self.hasMoved = False
        super().__init__("K", row, col, color)

    def check_move(self, board, row, col, lastMove):
        if abs(self.row - row) <= 1 and abs(self.col - col) <= 1:
            pieceAtDest = board.getPieceAtLocation(row, col)
            if pieceAtDest != None and pieceAtDest.color != self.color:
                self.hasMoved = True
                return Move.CAPTURE
            elif pieceAtDest == None:
                self.hasMoved = True
                return Move.REGULAR

        # castling
        elif self.hasMoved == False and self.row == row:
            potentialRookKingside = board.getPieceAtLocation(row, 0)
            potentialRookQueenside = board.getPieceAtLocation(row, 7)
            if (
                col == 1
                and self.straight_clear_path(board, row, 0)
                and type(potentialRookKingside) == Rook
                and potentialRookKingside.hasMoved == False
            ):
                potentialRookKingside.hasMoved = True
                self.hasMoved = True
                return Move.KINGSIDE_CASTLE
            elif (
                col == 5
                and self.straight_clear_path(board, row, 7)
                and type(potentialRookQueenside) == Rook
                and potentialRookQueenside.hasMoved == False
            ):
                potentialRookQueenside.hasMoved = True
                self.hasMoved = True
                return Move.QUEENSIDE_CASTLE

        return Move.INVALID

    def move(self, board, row, col, lastMove):
        status = self.check_move(board, row, col, lastMove)
        if status != Move.QUEENSIDE_CASTLE and status != Move.KINGSIDE_CASTLE:
            super().move(board, row, col, lastMove)
        else:
            if status == Move.KINGSIDE_CASTLE:
                hRook = board.getPieceAtLocation(row, 0)
                board.setPieceAtLocation(row, hRook.col, None)
                hRook.col = col + 1
                board.setPieceAtLocation(row, hRook.col, hRook)
            else:
                aRook = board.getPieceAtLocation(row, 7)
                board.setPieceAtLocation(row, aRook.col, None)
                aRook.col = col - 1
                board.setPieceAtLocation(row, aRook.col, aRook)
            board.setPieceAtLocation(self.row, self.col, None)
            self.row = row
            self.col = col
            board.setPieceAtLocation(self.row, self.col, self)
