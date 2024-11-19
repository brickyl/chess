from utils.notation import decodeChessNotation


def parse_move(move):
    if len(move) != 5:
        raise Exception("Formatted move incorrectly.")
    startPos = move[0:2]  # 'b3'
    reformattedStartRow = int(startPos[1]) - 1
    endPos = move[-2:]  # 'b4'
    reformattedEndRow = int(endPos[1]) - 1
    startPos = startPos[0] + (str(reformattedStartRow))
    endPos = endPos[0] + (str(reformattedEndRow))
    startRowCol = decodeChessNotation(startPos)  # (3, 1)
    endRowCol = decodeChessNotation(endPos)  # (4, 1)
    return (startRowCol, endRowCol)
