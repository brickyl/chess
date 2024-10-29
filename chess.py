class Chess:
    def __init__(self):
        self.turn = NotImplemented
        self.board = NotImplemented

    def gameRun(self):
        while (not self.gameOver()):
            self.move()
        self.board.printBoard()

    def decodeChessNotation(self, notation):
        col = self.mapping[notation[0].lower()]
        row = int(notation[1])
        return str(8-row) + " " + str(col)

    def encodeRowColNotation(self, row, col):
        notation = list(self.mapping.keys())[list(self.mapping.values()).index(col)] # column
        notation += str(8-row) # row
        return notation