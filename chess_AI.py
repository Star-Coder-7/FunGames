import random

pieceScore = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "P": 1}
CHECKMATE = 1000
STALEMATE = 0


def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) - 1)]


def findBestMove():
    pass


'''
Score the board based on material
'''


def scoreMaterial(board):
    pass
