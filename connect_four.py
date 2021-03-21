import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

ROW_COUNT = 6
COL_COUNT = 7


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
        for r in range(ROW_COUNT-3):
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
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                board[r - 3][c + 3] == piece:
                return True


def drawBoard(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQ_SIZE, r * SQ_SIZE + SQ_SIZE, SQ_SIZE, SQ_SIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQ_SIZE + SQ_SIZE / 2),
                                               int(r * SQ_SIZE + SQ_SIZE + SQ_SIZE / 2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQ_SIZE + SQ_SIZE / 2), height -
                                                 int(r * SQ_SIZE + SQ_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQ_SIZE + SQ_SIZE / 2), height -
                                                    int(r * SQ_SIZE + SQ_SIZE / 2)), RADIUS)
    pygame.display.update()


board = createBoard()
printBoard(board)
gameOver = False
turn = 0

pygame.init()

SQ_SIZE = 100

width = COL_COUNT * SQ_SIZE
height = (ROW_COUNT + 1) * SQ_SIZE

size = (width, height)

RADIUS = int(SQ_SIZE / 2 - 5)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Connect 4')
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)


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
            if turn == 0:
                pygame.draw.circle(screen, RED, (posX, int(SQ_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posX, int(SQ_SIZE / 2)), RADIUS)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQ_SIZE))
            # print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posX = event.pos[0]
                col = int(math.floor(posX / SQ_SIZE))

                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 1)

                    if winningMove(board, 1):
                        label = myfont.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        gameOver = True

            # Ask for Player 2 Input
            else:
                posX = event.pos[0]
                col = int(math.floor(posX / SQ_SIZE))

                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 2)

                    if winningMove(board, 2):
                        label = myfont.render("Player 2 wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        gameOver = True

            printBoard(board)
            drawBoard(board)

            turn += 1
            turn %= 2

            if gameOver:
                pygame.time.wait(3000)
