from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from constants import Color, Move


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        # for i in range(8):
        #     for j in range(8):
        #         if i == 1:
        #             pawn = Pawn(i, j, Color.WHITE)
        #             self.board[i][j] = pawn

        #         if i == 6:
        #             pawn = Pawn(i, j, Color.BLACK)
        #             self.board[i][j] = pawn
        self.board[6][4] = Rook(6, 4, Color.WHITE)
        self.board[4][4] = Rook(4, 4, Color.WHITE)
        self.board[3][4] = Rook(3, 4, Color.BLACK)
        self.board[2][4] = Rook(2, 4, Color.BLACK)
        # self.pieces = []
        # self.inactivePieces = []

    def printBoard(self):
        # debugging mode: the rows are 0-indexed right now
        print()
        for i in range(len(self.board)):
            line = str(i + 1) + "  "
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
