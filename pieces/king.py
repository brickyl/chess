from pieces.piece import Piece
from pieces.rook import Rook
from straightmove import StraightMove
from constants import Color, Move
from utils import handle_piece


class King(Piece, StraightMove):
    def __init__(self, row, col, color, board):
        self.hasMoved = False
        super().__init__("K", row, col, color, board)

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
        if status == Move.REGULAR or status == Move.CAPTURE:
            super().move(board, row, col, lastMove)
        else:
            if status == Move.KINGSIDE_CASTLE:
                hRook = board.getPieceAtLocation(row, 0)
                handle_piece.transport(board, hRook, row, hRook.col + 1)

            else:
                aRook = board.getPieceAtLocation(row, 7)
                handle_piece.transport(board, aRook, row, aRook.col + 1)
            handle_piece.transport(board, self, row, col)
