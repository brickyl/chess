from pieces.piece import Piece
from constants import Color, Move


class Pawn(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.enpassant = False
        super().__init__("P", row, col)


    def isValidMove(self):
        # check if there is a piece there
        pass

    def move(self, row, col, board):
        if self.row - row == 1 and self.col == col and board.getPieceAtLocation(row, col) == None:
            self.row = row
            self.col = col
            return True
        return False

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
