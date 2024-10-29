from board import Board
from pieces.pawn import Pawn
from utils.notation import decodeChessNotation, encodeRowColNotation

class Chess:
    def __init__(self):
        self.turn = 0
        self.board = Board()
        self.gameOver = False

    def gameRun(self):
        while (not self.gameOver):
        # while (not self.gameOver()):
            print("Give me a move!")
            move = input()
            if len(move) != 5:
                raise Exception("Formatted move incorrectly.")
            startPos = move[0:2]
            endPos = move[-2:]
            piece = self.board.getPieceAtLocation((decodeChessNotation(startPos)))
            # Now figure out what to do with endPos

            self.gameOver = True
            
        self.board.printBoard()
    
if __name__ == "__main__":
    c = Chess()
    c.gameRun()
