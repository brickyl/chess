from board import Board
from pieces.pawn import Pawn
from utils.notation import decodeChessNotation, encodeRowColNotation
from constants import Move, Color


class Chess:
    def __init__(self):
        self.turn = 0
        self.board = Board()
        self.gameOver = False

    def gameRun(self):
        while not self.gameOver:
            # while (not self.gameOver()):
            print("Give me a move!")
            move = input()
            if len(move) != 5:
                raise Exception("Formatted move incorrectly.")
            startPos = move[0:2] # 'b3'
            endPos = move[-2:] # 'b4'
            startRowCol = decodeChessNotation(startPos) # (3, 1)
            endRowCol = decodeChessNotation(endPos) # (4, 1)

            # Now figure out what to do with endPos
            piece = self.board.getPieceAtLocation(*startRowCol)
            move_status = None
            if piece != None:
                move_status = piece.move(self.board, *endRowCol)
            else:
                raise Exception("No starting piece found.")
            
            print(self.board)
        

            # now figure out if the new destination is a location that the piece can get to
            # if so, classify the type of move, and any resulting actions
            # piece.tryMove(pieceAtDestination.row, pieceAtDestination.col) --> returns success or fail, and type of move
            

            self.gameOver = True

        self.board.printBoard()


if __name__ == "__main__":
    c = Chess()
    c.gameRun()
