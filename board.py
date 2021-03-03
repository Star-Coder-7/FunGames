from piece import Bishop
from piece import King
from piece import Rook
from piece import Pawn
from piece import Queen
from piece import Knight
import time
import pygame


class Board:
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ready = False
        self.last = None
        self.copy = True
        self.board = [[0 for x in range(8)] for _ in range(rows)]

        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[1][0] = Pawn(1, 0, "b")
        self.board[1][1] = Pawn(1, 1, "b")
        self.board[1][2] = Pawn(1, 2, "b")
        self.board[1][3] = Pawn(1, 3, "b")
        self.board[1][4] = Pawn(1, 4, "b")
        self.board[1][5] = Pawn(1, 5, "b")
        self.board[1][6] = Pawn(1, 6, "b")
        self.board[1][7] = Pawn(1, 7, "b")

        self.board[6][0] = Pawn(6, 0, "w")
        self.board[6][1] = Pawn(6, 1, "w")
        self.board[6][2] = Pawn(6, 2, "w")
        self.board[6][3] = Pawn(6, 3, "w")
        self.board[6][4] = Pawn(6, 4, "w")
        self.board[6][5] = Pawn(6, 5, "w")
        self.board[6][6] = Pawn(6, 6, "w")
        self.board[6][7] = Pawn(6, 7, "w")

        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Queen(7, 3, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")

        self.p1Name = input("What is player 1's name? Please enter it here (1-10 characters): ")
        self.p2Name = input("What is player 2's name? Please enter it here (1-10 characters): ")

        if 1 <= len(self.p1Name) <= 10 and 1 <= len(self.p2Name) <= 10:
            pass
        else:
            print("Sorry, the name's must be from 1-10 characters.")
            self.p1Name = input("What is player 1's name? Please enter it here: ")
            self.p2Name = input("What is player 2's name? Please enter it here: ")

        self.turn = "w"

        self.time1 = 900
        self.time2 = 900

        self.storedTime1 = 0
        self.storedTime2 = 0

        self.winner = None
        self.startTime = time.time()

    def updateMoves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].updateValidMoves(self.board)

    def draw(self, win, color):
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (4 - x) + round(self.startX + (x * self.rect[2] / 8))
            yy = 3 + round(self.startY + (y * self.rect[3] / 8))
            pygame.draw.circle(win, (0, 0, 255), (xx + 32, yy + 30), 34, 4)
            xx1 = (4 - x) + round(self.startX + (x1 * self.rect[2] / 8))
            yy1 = 3+ round(self.startY + (y1 * self.rect[3] / 8))
            pygame.draw.circle(win, (0, 0, 255), (xx1 + 32, yy1 + 30), 34, 4)

        s = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win, color)
                    if self.board[i][j].isSelected:
                        s = (i, j)

    def getDangerMoves(self, color):
        dangerMoves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for move in self.board[i][j].moveList:
                            dangerMoves.append(move)

    def isChecked(self, color):
        self.updateMoves()
        dangerMoves = self.getDangerMoves(color)
        kingPos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        kingPos = (j, i)

    def select(self, col, row, color):
        pass