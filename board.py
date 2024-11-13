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

                if i == 6:
                    pawn = Pawn(i, j, Color.BLACK)
                    self.board[i][j] = pawn

        # self.pieces = []
        # self.inactivePieces = []

    def printBoard(self):
    # debugging mode: the rows are 0-indexed right now
        print()
        for i in range(len(self.board)):
            line = str(i) + "  "
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
        print("   h g f e d c b a")
        print()

    def getPieceAtLocation(self, row, col):
        piece = self.board[row][col]
        return piece
    
    def setPieceAtLocation(self, row, col, piece):
        self.board[row][col] = piece


b = Board()
b.printBoard()
