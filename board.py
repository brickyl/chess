class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.mapping = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
        self.mapping = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
        self.pieces = []
        self.inactivePieces = []

    def printBoard(self):
        print()
        for i in range(len(self.board)):
            line = str(8-i) + "  "
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                if piece == None:
                    line += "x"
                    line += " "
                else:
                    line += piece.toString()
                    line += " "
            print(line)
        print()
        print("   a b c d e f g h")
        print()

    def givePieceAtLocation(self, row, col):
        

b = Board()
b.printBoard()