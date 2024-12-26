from utils.notation import decodeChessNotation
from constants import INPUT_STATUS


def parse_input(move):
    # CREATE AN ENUM FOR RETURN OUTPUT

    if move.lower() == "quit":
        return INPUT_STATUS.QUIT
    elif move.lower() == "undo":
        # reverse_move()
        return INPUT_STATUS.UNDO

    try: 
        startPos = move[0:2]  # 'b3'
        reformattedStartRow = int(startPos[1]) - 1
        endPos = move[-2:]  # 'b4'
        reformattedEndRow = int(endPos[1]) - 1

        startPos = startPos[0] + (str(reformattedStartRow))
        endPos = endPos[0] + (str(reformattedEndRow))
        
        startRowCol = decodeChessNotation(startPos)  # (3, 1)
        endRowCol = decodeChessNotation(endPos)  # (4, 1)
        return (startRowCol, endRowCol)
    except:
        return INPUT_STATUS.FORMAT_INCORRECT
