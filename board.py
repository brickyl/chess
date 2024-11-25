from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.knight import Knight
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
        # self.board[6][4] = Queen(6, 4, Color.WHITE)
        self.board[0][3] = King(0, 3, Color.WHITE)
        self.board[7][3] = King(7, 3, Color.BLACK)
        self.board[0][0] = Rook(0, 0, Color.WHITE)
        self.board[0][7] = Rook(0, 7, Color.WHITE)
        self.board[7][0] = Rook(7, 0, Color.BLACK)
        self.board[7][7] = Rook(7, 7, Color.BLACK)
        # self.board[2][4] = Queen(2, 4, Color.BLACK)
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
