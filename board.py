from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.knight import Knight
from constants import Color, Move
from utils.move_logging import reverse_move


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.white = []
        self.black = []
        # self.white_king = King(0, 3, Color.WHITE, self)
        # self.black_king = King(7, 3, Color.BLACK, self)

        # # Pawns
        # for i in range(8):
        #     for j in range(8):
        #         if i == 1:
        #             Pawn(i, j, Color.WHITE, self)

        #         if i == 6:
        #             Pawn(i, j, Color.BLACK, self)

        # Queens
        Queen(0, 4, Color.WHITE, self)
        Queen(7, 4, Color.BLACK, self)

        # # Rooks
        # Rook(0, 0, Color.WHITE, self)
        # Rook(0, 7, Color.WHITE, self)
        # Rook(7, 0, Color.BLACK, self)
        # Rook(7, 7, Color.BLACK, self)

        # # Bishops
        # Bishop(0, 2, Color.WHITE, self)
        # Bishop(0, 5, Color.WHITE, self)
        # Bishop(7, 2, Color.BLACK, self)
        # Bishop(7, 5, Color.BLACK, self)

        # # Knights
        # Knight(0, 1, Color.WHITE, self)
        # Knight(0, 6, Color.WHITE, self)
        # Knight(7, 1, Color.BLACK, self)
        # Knight(7, 6, Color.BLACK, self)

    def printBoard(self):
        # debugging mode: the rows are 0-indexed right now
        print()
        print("[chess] --- Board ---")
        for i in range(len(self.board)):
            line = "    " + str(i + 1) + "  "
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
        print("       h g f e d c b a")
        print()

    def getPieceAtLocation(self, row, col):
        piece = self.board[row][col]
        return piece

    def setPieceAtLocation(self, row, col, piece):
        self.board[row][col] = piece

    def checkDetect(self):
        # instead of checking every single piece, maybe check the row, column, and diagonals
        # that the king is on, plus knights of the opposite color. only check until you run
        # into a piece (only knight can jump).
        for piece in self.black:
            if (
                piece.check_move(self, self.white_king.row, self.white_king.col, None)
                != Move.INVALID
            ):
                return Color.WHITE

        for piece in self.white:
            if (
                piece.check_move(self, self.black_king.row, self.black_king.col, None)
                != Move.INVALID
            ):
                return Color.BLACK

        return None

    def pieceRemoval(self, piece):
        # function to remove a piece from a board using row and col
        self.setPieceAtLocation(piece.row, piece.col, None)
        if piece.color == Color.WHITE:
            self.white.remove(piece)
        else:
            self.black.remove(piece)

    def pieceRestore(self, piece):
        if piece in self.white or piece in self.black:
            raise Exception("Tried to restore active piece.")

        self.setPieceAtLocation(piece.row, piece.col, piece)
        if piece.color == Color.WHITE:
            self.white.append(piece)
        else:
            self.black.append(piece)

    def transport(self, piece, newRow, newCol):
        self.setPieceAtLocation(piece.row, piece.col, None)
        self.setPieceAtLocation(newRow, newCol, piece)
        piece.row = newRow
        piece.col = newCol

    def countMoves(self, moves, forCheckmate=False):
        # returns the number of moves that are valid given a certain board and moves (necessary for calculating en passant)
        success = 0

        # write the brute force version first, then update the move checking process to be more efficient

        for piece in self.black:
            if isinstance(piece, King):
                movesToTry = [
                    (1, 1),
                    (1, 0),
                    (1, -1),
                    (0, 1),
                    (0, -1),
                    (-1, 1),
                    (-1, 0),
                    (-1, -1),
                ]
                for tup in movesToTry:
                    a, b = tup
                    try:
                        if piece.move(self, piece.row + a, piece.col + b, moves) == True:
                            success += 1
                            if forCheckmate:
                                return True
                            reverse_move(self, moves)
                    except IndexError:
                        pass

            if isinstance(piece, Pawn):
                movesToTry = [1, 0, -1]
                for move in movesToTry:
                    try:
                        newRow = piece.row + piece.color.value
                        newCol = piece.col + move
                        if piece.move(self, newRow, newCol, moves) == True:
                            success += 1
                            print(piece.row, piece.col, newRow, newCol)
                            if forCheckmate:
                                return True
                            reverse_move(self, moves)

                    except IndexError:
                        pass

                try:
                    newRow = piece.row + piece.color.value * 2
                    if piece.move(self, newRow, piece.col, moves) == True:
                        success += 1
                        print(piece.row, piece.col, newRow, piece.col)

                        if forCheckmate:
                            return True
                        reverse_move(self, moves)
                except IndexError:
                    pass

            if isinstance(piece, Queen):
                pass

            if isinstance(piece, Bishop):
                pass

            if isinstance(piece, Knight):
                pass

            if isinstance(piece, Rook):
                pass

        for piece in self.white:
            pass

        if success == 0 and forCheckmate:
            return False

        return success

    def detectCheckmate(self):
        # uses a snippet of count_moves() code to see if there are more than 0 valid moves
        pass

    # COUNT VALID MOVES FUNCTION
    # CHECKMATE DETECTION FUNCTION

    # checkmate detection(?)
    # checkmate is when no matter what move you make, your king will get gobbled up nom nom
    # checkmate also occurs when you cannot make any valid moves while being in check <-- stop counting as soon as there's 1 valid move
    # stalemate occurs when you cannot make any valid moves while NOT in check <-- stop counting as soon as there's 1 valid move
    # can count number of moves SMARTLY for each piece
