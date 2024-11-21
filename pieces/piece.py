from abc import ABCMeta, abstractmethod
from constants import Color, Move


class Piece(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, row, col, color):
        # self.color = None
        self.row = row  # ranks
        self.col = col  # files
        self.name = name
        self.color = color
        # self.abbreviation = None
        # self.startPosition = None

    @abstractmethod
    def check_move(self, board, row, col, lastMove):
        # returns enum that represents move status
        # returns Move.INVALID if unsuccessful
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    def move(self, board, row, col, lastMove):
        status = self.check_move(board, row, col, lastMove)

        if status == Move.REGULAR or status == Move.CAPTURE:
            board.setPieceAtLocation(self.row, self.col, None)
            self.row = row
            self.col = col
            board.setPieceAtLocation(row, col, self)

        else:
            raise Exception("Invalid move.")

    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return self.name.lower()
