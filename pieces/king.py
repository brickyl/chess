from pieces.piece import Piece
from pieces.rook import Rook
from straightmove import StraightMove
from constants import Color, Move


class King(Piece, StraightMove):
    def __init__(self, row, col, color, board):
        self.hasMoved = False
        super().__init__("K", row, col, color, board)

    def check_move(self, board, row, col, moves):
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

    def move(self, board, row, col, moves):
        status = self.check_move(board, row, col, moves)
        if status == Move.REGULAR or status == Move.CAPTURE:
            return super().move(board, row, col, moves) 
        else:
            oldRow, oldCol = self.row, self.col

            if status == Move.KINGSIDE_CASTLE:
                rook = board.getPieceAtLocation(row, 0)
                oldRookRow, oldRookCol = rook.row, rook.col
                board.transport(rook, row, rook.col + 2)

            else:
                rook = board.getPieceAtLocation(row, 7)
                oldRookRow, oldRookCol = rook.row, rook.col # what if rook is None?
                board.transport(rook, row, rook.col - 3)
            
            board.transport(self, row, col)
            return (self, oldRow, oldCol, status, (rook, oldRookRow, oldRookCol))
