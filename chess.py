from board import Board
from pieces.pawn import Pawn
from utils.notation import decodeChessNotation, encodeRowColNotation
from utils.parsemove import parse_move
from constants import Move, Color


# doesn't handle invalid moves by letting you try again yet
class Chess:
    def __init__(self):
        self.turn = 0
        self.board = Board()
        self.gameOver = False
        self.player = Color.WHITE
        self.lastMove = None
        startMessage = "Welcome to Chess! Enter moves by starting square to destination square by column and row (ie. b2 b3). Have fun!"
        pieceRepMessage = "Note: White pieces are represented by uppercase characters, while black pieces are lowercase."
        print(startMessage)
        print(pieceRepMessage)

    def gameRun(self):
        while not self.gameOver:
            self.board.printBoard()
            print(
                "Give me a move, player '", str(self.player.name).lower(), "'!", sep=""
            )
            move = input()
            parsedMove = parse_move(move)
            startRowCol, endRowCol = parsedMove
            # endRowCol = parsedMove[1]

            # Now figure out what to do with endPos
            piece = self.board.getPieceAtLocation(*startRowCol)
            if piece == None:
                print("No starting piece found.")
                return
            elif piece.color != self.player:
                print("Not your piece.")
                return
            piece.move(self.board, *endRowCol, self.lastMove)
            self.lastMove = (piece, *startRowCol, *endRowCol)

            # now figure out if the new destination is a location that the piece can get to
            # if so, classify the type of move, and any resulting actions
            # piece.tryMove(pieceAtDestination.row, pieceAtDestination.col) --> returns success or fail, and type of move

            if self.player == Color.BLACK:
                self.player = Color.WHITE
            else:
                self.player = Color.BLACK

        print("------ Game over! ------")
        self.board.printBoard()


if __name__ == "__main__":
    c = Chess()
    c.gameRun()
