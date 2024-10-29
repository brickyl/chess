from pieces.pawn import Pawn
from constants import Color, Move


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if i == 1:
                    pawn = Pawn(i, j, Color.WHITE)
                    self.board[i][j] = pawn

        self.pieces = []
        self.inactivePieces = []

    def printBoard(self):
        print()
        for i in range(len(self.board)):
            line = str(8 - i) + "  "
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                if piece == None:
                    line += "x"
                    line += " "
                else:
                    line += str(piece)
                    line += " "
            print(line)
        print()
        print("   a b c d e f g h")
        print()

    def getPieceAtLocation(self, row, col):
        piece = self.board[row][col]
        if piece != None:
            return str(self.board[row][col])
        return "x"


b = Board()
b.printBoard()
