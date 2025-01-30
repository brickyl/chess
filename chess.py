from board import Board

# from utils.notation import decodeChessNotation, encodeRowColNotation
from utils.parsemove import parse_input
from utils.move_logging import reverse_move

from constants import Color, INPUT_STATUS


class Chess:
    def __init__(self):
        self.turn = 0
        self.board = Board()
        self.gameOver = False
        self.moves = []
        print(
            """[chess] Welcome to Chess! Enter moves by starting square to destination square by column and row (ie. b2 b3). Have fun!
[chess] White pieces are represented by uppercase characters, while black pieces are lowercase.
[chess] You can exit the program by entering 'quit'. You may undo a move by entering 'undo'."""
        )

    def gameRun(self):
        while not self.gameOver:
            self.board.printBoard()
            player = self.curr_player()
            print(
                "[chess] Give me a move, player '",
                str(player.name).lower(),
                "'!",
                sep="",
            )
            total_moves = self.board.countMoves(self.moves, player)
            print("[chess] Total available moves: " + str(total_moves))

            move = input()
            parsedInput = parse_input(move)
            if parsedInput == INPUT_STATUS.FORMAT_INCORRECT:
                print("[chess] Incorrectly formatted move. Try again.")
                continue
            elif parsedInput == INPUT_STATUS.QUIT:
                print("[chess] Game exited.")
                return
            elif parsedInput == INPUT_STATUS.UNDO:
                reverse_result = reverse_move(self.board, self.moves)
                if reverse_result == False:
                    print("[chess] No moves to undo.")
                else:
                    print("[chess] Undo successful.")
                continue
            else:
                startRowCol, endRowCol = parsedInput

            piece = self.board.getPieceAtLocation(*startRowCol)
            if piece == None:
                print("[chess] No starting piece found. Try again.")
                continue
            elif piece.color != player:
                print("[chess] Not your piece. Try again.")
                continue

            move_success = piece.move(self.board, *endRowCol, self.moves)
            if move_success == False:
                print("[chess] Illegal move made. Try again.")
                continue

        print("[chess] ------ Game over! ------")
        self.board.printBoard()

    def curr_player(self):
        # calculates who the current player should be based on the self.moves list
        if len(self.moves) % 2 == 0:
            return Color.WHITE
        else:
            return Color.BLACK
        # if len(self.moves) == 0:
        # return Color.WHITE
        # if self.moves[-1][0].color == Color.WHITE:
        #     return Color.BLACK:
        # else:
        #     return Color.WHITE


if __name__ == "__main__":
    c = Chess()
    c.gameRun()
