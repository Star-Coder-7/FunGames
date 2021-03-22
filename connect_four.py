import numpy as np
import random
import pygame
import sys
import math

pygame.init()

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
SQ_SIZE = 100
RADIUS = int(SQ_SIZE / 2 - 5)

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WIN_LENGTH = 4

width = COL_COUNT * SQ_SIZE
height = (ROW_COUNT + 1) * SQ_SIZE
size = (width, height)


def createBoard():
    board = np.zeros((ROW_COUNT, COL_COUNT))
    return board


def dropPiece(board, row, col, piece):
    board[row][col] = piece


def isValidLocation(board, col):
    return board[ROW_COUNT - 1][col] == 0


def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def printBoard(board):
    print(np.flip(board, 0))


def winningMove(board, piece):
    # Check horizontal locations for win
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and \
                board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and \
                board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                board[r - 3][c + 3] == piece:
                return True


def evaluateWindow(window, piece):
    score = 0
    oppPiece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        oppPiece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(oppPiece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def scorePosition(board, piece):
    score = 0

    # Score center column
    centerArray = [int(i) for i in list(board[:, COL_COUNT // 2])]
    centerCount = centerArray.count(piece)
    score += centerCount * 3

    # Score Horizontal
    for r in range(ROW_COUNT):
        rowArray = [int(i) for i in list(board[r, :])]
        for c in range(COL_COUNT - 3):
            window = rowArray[c:c + WIN_LENGTH]
            score += evaluateWindow(window, piece)

    # Score Vertical
    for c in range(COL_COUNT):
        colArray = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT-3):
            window = colArray[r:r + WIN_LENGTH]
            score += evaluateWindow(window, piece)

    # Score positive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT - 3):
            window = [board[r + i][c + i] for i in range(WIN_LENGTH)]
            score += evaluateWindow(window, piece)

    for r in range(ROW_COUNT-3):
        for c in range(COL_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(WIN_LENGTH)]
            score += evaluateWindow(window, piece)

    return score


def isTerminalNode(board):
    return winningMove(board, PLAYER_PIECE) or winningMove(board, AI_PIECE) or len(getValidLocations(board)) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    validLocations = getValidLocations(board)
    isTerminal = isTerminalNode(board)
    if depth == 0 or isTerminal:
        if isTerminal:
            if winningMove(board, AI_PIECE):
                return None, 100000000000000
            elif winningMove(board, PLAYER_PIECE):
                return None, -10000000000000
            else:  # Game is over, no more valid moves
                return None, 0
        else:  # Depth is zero
            return None, scorePosition(board, AI_PIECE)

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = getNextOpenRow(board, col)
            bCopy = board.copy()
            dropPiece(bCopy, row, col, AI_PIECE)
            newScore = minimax(bCopy, depth-1, alpha, beta, False)[1]
            if newScore > value:
                value = newScore
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(validLocations)
        for col in validLocations:
            row = getNextOpenRow(board, col)
            bCopy = board.copy()
            dropPiece(bCopy, row, col, PLAYER_PIECE)
            newScore = minimax(bCopy, depth-1, alpha, beta, True)[1]
            if newScore < value:
                value = newScore
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def getValidLocations(board):
    validLocations = []
    for col in range(COL_COUNT):
        if isValidLocation(board, col):
            validLocations.append(col)
    return validLocations


def pickBestMove(board, piece):

    validLocations = getValidLocations(board)
    bestScore = -10000
    bestCol = random.choice(validLocations)
    for col in validLocations:
        row = getNextOpenRow(board, col)
        tempBoard = board.copy()
        dropPiece(tempBoard, row, col, piece)
        score = scorePosition(tempBoard, piece)
        if score > bestScore:
            bestScore = score
            bestCol = col

    return bestCol


def drawBoard(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQ_SIZE, r * SQ_SIZE + SQ_SIZE, SQ_SIZE, SQ_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQ_SIZE + SQ_SIZE / 2),
                                               int(r * SQ_SIZE + SQ_SIZE + SQ_SIZE / 2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(c * SQ_SIZE + SQ_SIZE / 2), height -
                                                 int(r * SQ_SIZE + SQ_SIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (int(c * SQ_SIZE + SQ_SIZE / 2), height -
                                                    int(r * SQ_SIZE + SQ_SIZE / 2)), RADIUS)

    pygame.display.update()


screen = pygame.display.set_mode(size)
board = createBoard()
printBoard(board)
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)
turn = random.randint(PLAYER, AI)
gameOver = False

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_SPACE:
                sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQ_SIZE))
            posX = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (posX, int(SQ_SIZE / 2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQ_SIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == PLAYER:
                posX = event.pos[0]
                col = int(math.floor(posX / SQ_SIZE))

                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, PLAYER_PIECE)

                    if winningMove(board, PLAYER_PIECE):
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        gameOver = True

                    turn += 1
                    turn %= 2

                    printBoard(board)
                    drawBoard(board)


    # Ask for Player 2 Input
    if turn == AI and not gameOver:
        # col = random.randint(0, COL_COUNT - 1)
        # col = pickBestMove(board, AI_PIECE)
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

        if isValidLocation(board, col):
            # pygame.time.wait(500)
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, AI_PIECE)

            if winningMove(board, AI_PIECE):
                label = myfont.render("Player 2 wins!", 1, YELLOW)
                screen.blit(label, (40, 10))
                gameOver = True

            printBoard(board)
            drawBoard(board)

            turn += 1
            turn %= 2

    if gameOver:
        pygame.time.wait(5000)

pygame.quit()