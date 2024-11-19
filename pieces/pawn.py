from pieces.piece import Piece
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from constants import Color, Move


class Pawn(Piece):
    def __init__(self, row, col, color):
        self.enpassant = False
        super().__init__("P", row, col, color)

    def check_move(self, board, row, col):

        pieceAtDestination = board.getPieceAtLocation(row, col)
        if pieceAtDestination != None:
            if pieceAtDestination.color != self.color:
                # checking if the pawn row is +1 and also checking if the column is +/-1
                if row - self.row == self.color.value and abs(col - self.col) == 1:
                    if self.color == Color.WHITE and row == 7 or self.color == Color.BLACK and row == 0:
                        return Move.PAWN_PROMOTE
                    return Move.CAPTURE
        else:
            # checking if the pawn row is +1 and the column is the same
            if row - self.row == self.color.value and col == self.col:
                if self.color == Color.WHITE and row == 7 or self.color == Color.BLACK and row == 0:
                    return Move.PAWN_PROMOTE
                return Move.REGULAR
            elif row - self.row == self.color.value * 2 and col == self.col:
                if self.color == Color.WHITE and self.row == 1:
                    print("W", str(self.row))
                    return Move.REGULAR
                if self.color == Color.BLACK and self.row == 6:
                    print("B", str(self.row))
                    return Move.REGULAR
        return Move.INVALID

    def move(self, board, row, col):
        status = self.check_move(board, row, col)
        if status == Move.REGULAR or status == Move.CAPTURE:
            board.setPieceAtLocation(self.row, self.col, None)
            self.row = row
            self.col = col
            board.setPieceAtLocation(row, col, self)
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
            board.setPieceAtLocation(row, col, newPiece)
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

    # Returns True if the move did not result in a promotion, False if the move results in a promotion
    # if self.row != 1:
    #         self.row -= 1
    #         return True
    # else:
    #     return self.promote()

    def capture(self, row, col):
        pass

    def promote(self):
        self.inactive = True
        return False
