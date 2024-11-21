class DiagonalMove:
    def diag_clear_path(self, board, row, col):
        dirRow = 0
        dirCol = 0
        if row > self.row:
            dirRow = 1
        if row < self.row:
            dirRow = -1
        if col > self.col:
            dirCol = 1
        if col < self.col:
            dirCol = -1
        if dirRow == 0 or dirCol == 0:
            return False

        iterRow = self.row + dirRow
        iterCol = self.col + dirCol
        while iterRow >= 0 and iterRow < 8 and iterCol >= 0 and iterCol < 8:
            if iterRow == row and iterCol == col:
                return True
            if board.getPieceAtLocation(iterRow, iterCol) != None:
                return False
            iterRow += dirRow
            iterCol += dirCol
        return False
