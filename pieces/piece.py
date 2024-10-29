from abc import ABCMeta, abstractmethod

class Piece(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, row, col):
        # self.color = None
        self.inactive = False # includes captured pieces or promoted pawns
        self.row = row # ranks
        self.col = col # files
        self.name = name
        # self.abbreviation = None
        # self.startPosition = None
        
    @abstractmethod
    def move(self, row, col):
        # returns "move_no_capture" if success, returns "move_with_capture" 
        # throws an exception if unsuccessful 
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    @abstractmethod
    def capture(self, piece):
        pass

    def __str__(self):
        return self.name


