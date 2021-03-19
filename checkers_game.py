import pygame
from constants import BLUE, PURPLE, PINK, SQ_SIZE
from board import Board


class Game:

    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.drawValidMoves(self.validMoves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.validMoves = {}

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.getPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.board.getValidMoves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.validMoves:
            self.board.move(self.selected, row, col)
            skipped = self.validMoves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.changeTurn()
        else:
            return False

        return True

    def drawValidMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, PINK, (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2), 15)

    def changeTurn(self):
        self.validMoves = {}
        if self.turn == BLUE:
            self.turn = PURPLE
        else:
            self.turn = BLUE
