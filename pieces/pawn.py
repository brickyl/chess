from pieces.piece import Piece
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from constants import Color, Move


class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__("P", row, col, color)

    def check_move(self, board, row, col, lastMove):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None:
            if pieceAtDestination.color != self.color:
                # checking for capture
                if row - self.row == self.color.value and abs(col - self.col) == 1:
                    if (
                        self.color == Color.WHITE
                        and row == 7
                        or self.color == Color.BLACK
                        and row == 0
                    ):
                        return Move.PAWN_PROMOTE
                    return Move.CAPTURE
                
        else:
            # checking regular moves
            if row - self.row == self.color.value and col == self.col:
                if (
                    self.color == Color.WHITE
                    and row == 7
                    or self.color == Color.BLACK
                    and row == 0
                ):
                    return Move.PAWN_PROMOTE
                return Move.REGULAR
            
            elif row - self.row == self.color.value * 2 and col == self.col:
                if (
                    self.color == Color.WHITE
                    and self.row == 1
                    or self.color == Color.BLACK
                    and self.row == 6
                ):
                    return Move.REGULAR
                
            # checking capture-en passant
            elif row - self.row == self.color.value and abs(col - self.col) == 1:
                (
                    lastMovePiece,
                    lastMoveStartRow,
                    lastMoveStartCol,
                    lastMoveDestRow,
                    lastMoveDestCol,
                ) = lastMove
                if (
                    type(lastMovePiece) == Pawn
                    and lastMoveDestRow - lastMoveStartRow
                    == 2 * lastMovePiece.color.value
                    and lastMoveStartCol == lastMoveDestCol
                    and lastMoveStartCol == col
                ):
                    return Move.PAWN_ENPASSANT
                
        return Move.INVALID

    def move(self, board, row, col, lastMove):
        status = self.check_move(board, row, col, lastMove)

        if status == Move.REGULAR or status == Move.CAPTURE:
            super().move(board, row, col, lastMove)

        elif status == Move.PAWN_PROMOTE:
            promotionMsg = "What would you like to promote your pawn into? The options are: Q, N, B, R."
            print(promotionMsg)
            promoPiece = input().upper()
            newPiece = None

            if promoPiece == "Q":
                newPiece = Queen(row, col, self.color)
            elif promoPiece == "N":
                newPiece = Knight(row, col, self.color)
            elif promoPiece == "B":
                newPiece = Bishop(row, col, self.color)
            elif promoPiece == "R":
                newPiece = Rook(row, col, self.color)
            if newPiece == None:
                raise Exception("Invalid promotion.")

            board.setPieceAtLocation(self.row, self.col, None)
            potential_captured = board.getPieceAtLocation(row, col)
            if potential_captured != None:
                if potential_captured.color == Color.BLACK:
                    board.black.remove(potential_captured)
                else:
                    board.white.remove(potential_captured)
            board.setPieceAtLocation(row, col, newPiece)

        elif status == Move.PAWN_ENPASSANT:
            board.setPieceAtLocation(self.row, self.col, None)
            captured = board.getPieceAtLocation(row - self.color.value, col)
            if captured.color == Color.BLACK:
                board.black.remove(captured)
            else:
                board.white.remove(captured)
            self.row = row
            self.col = col
            board.setPieceAtLocation(row, col, self)
            board.setPieceAtLocation(row - self.color.value, col, None)

        else:
            raise Exception("Invalid move.")

        # check if there's a piece there
        # [CAPTURE]
        # if so, what color is it?
        # if enemy piece, check if capture is possible
        # capture is possible if
        # the piece can capture that way
        # there are no other pieces in between (unless knight)
        # check is not revealed
        # en passant is unique
        # if friendly piece, can't move. return false
        # [MOVE]
        # if not, check if move is possible
        # move is possible if
        # piece can get there on a blank board
        # there are no other pieces in between (unless knight)
        # check is not revealed