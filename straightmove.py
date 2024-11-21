class StraightMove:
    def straight_clear_path(self, board, row, col):
        sameRow = False
        sameCol = False
        if self.row == row: sameRow = True
        if self.col == col: sameCol = True

        if sameRow: 
            # traverse the row
            if col > self.col:
                # to the right
                for i in range(self.col+1, col):
                    if board.getPieceAtLocation(self.row, i) != None:
                        return False
                return True

            elif col < self.col:
                # to the left
                for i in range(self.col-1, col, -1):
                    if board.getPieceAtLocation(self.row, i) != None:
                        return False
                return True

        elif sameCol:
            if row > self.row:
                # go down
                for i in range(self.row+1, row):
                    if board.getPieceAtLocation(i, self.col) != None:
                        return False
                return True
            
            elif row < self.row:
                for i in range(self.row-1, row, -1):
                    if board.getPieceAtLocation(i, self.col) != None:
                        return False
                return True
        else:
            return False

