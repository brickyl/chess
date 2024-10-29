from piece import Piece
class Pawn(Piece):
    def __init__(self, row, col, color):
        self.color = color
        self.enpassant = False
        super.__init__(row, col)

    def isValidMove(self):
        # check if there is a piece there
        pass
    
    def move(self, row, col):
    # Returns True if the move did not result in a promotion, False if the move results in a promotion
        if self.row != 1:
                self.row -= 1
                return True
        else:
            return self.promote() 

    def capture(self, row, col):
        pass

    def promote(self):
        self.inactive = True
        return False