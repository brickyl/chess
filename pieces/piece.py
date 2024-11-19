from abc import ABCMeta, abstractmethod
from constants import Color


class Piece(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, row, col, color):
        # self.color = None
        self.inactive = False  # includes captured pieces or promoted pawns
        self.row = row  # ranks
        self.col = col  # files
        self.name = name
        self.color = color
        # self.abbreviation = None
        # self.startPosition = None

    @abstractmethod
    def check_move(self, board, row, col):
        # returns enum that represents move status
        # returns Move.INVALID if unsuccessful
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    @abstractmethod
    def move(self, board, row, col):
        # conducts the move
        # this might be the same function for all piece classes. if so, then just declare this function here.
        # it might not be the same function if I use this function
        # to make changes to other pieces during interactive moves (captures + special moves)
        pass

    # @abstractmethod
    # def capture(self, piece):
    #     pass

    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return self.name.lower()
