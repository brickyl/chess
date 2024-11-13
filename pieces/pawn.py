from pieces.piece import Piece
from constants import Color, Move


class Pawn(Piece):
    def __init__(self, row, col, color):
        self.enpassant = False
        super().__init__("P", row, col, color)

    def check_move(self, board, row, col):
        pieceAtDestination = board.getPieceAtLocation(row, col)
        if pieceAtDestination != None: # CAPTURE case
            if pieceAtDestination.color == self.color:
                return Move.INVALID
            else: 
                # checking if the pawn row is +1 and also checking if the column is +/-1
                if row-self.row == self.color.value * 1 and abs(col - self.col) == 1:
                    return Move.CAPTURE
        else:
            # checking if the pawn row is +1 and the column is the same
            if abs(row - self.row) == self.color.value * 1 and col == self.col:
                return Move.REGULAR
            else:
                return Move.INVALID

    def move(self, board, row, col):
        if self.check_move(board, row, col) != Move.INVALID:
            board.setPieceAtLocation(self.row, self.col, None)
            self.row = row
            self.col = col
            board.setPieceAtLocation(row, col, self)
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