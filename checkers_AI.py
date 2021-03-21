from copy import deepcopy
import pygame

BLUE = (0, 0, 255)
PURPLE = (101, 18, 224)


def minimax(pos, depth, maxPLayer, game):
    if depth == 0 or pos.winner() is not None:
        return pos.evaluate(), pos

    if maxPLayer:
        maxEval = float('-inf')
        bestMove = None
        for move in getAllMoves(pos, PURPLE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                bestMove = move

        return maxEval, bestMove
    else:
        minEval = float('inf')
        bestMove = None
        for move in getAllMoves(pos, BLUE, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                bestMove = move

        return minEval, bestMove


def simulateMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def getAllMoves(board, color, game):
    moves = []

    for piece in board.getAllPieces(color):
        validMoves = board.getValidMoves(piece)
        for move, skip in validMoves.items():
            # drawMoves(game, board, piece)
            tempBoard = deepcopy(board)
            tempPiece = tempBoard.getPiece(piece.row, piece.col)
            newBord = simulateMove(tempPiece, move, tempBoard, game, skip)
            moves.append(newBord)

    return moves


def drawMoves(game, board, piece):
    validMoves = board.getValidMoves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.drawValidMoves(validMoves.keys())

    pygame.display.update()
    # pygame.time.delay(100)
