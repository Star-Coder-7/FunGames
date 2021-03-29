import pygame
from constants import BLACK, RED, BLUE, ROWS, COLS, GREEN, SQ_SIZE
from pieces import Pieces


class Board:

    def __init__(self):
        self.board = []
        self.blueLeft = self.greenLeft = 12
        self.blueKings = self.greenKings = 0
        self.createBoard()

    def drawSquares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def evaluate(self):
        return self.greenLeft - self.blueLeft + (self.greenKings * 0.5 - self.blueKings * 0.5)

    def getAllPieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.makeKing()
            if piece.color == GREEN:
                self.greenKings += 1
            else:
                self.blueKings += 1

    def getPiece(self, row, col):
        return self.board[row][col]

    def createBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Pieces(row, col, GREEN))
                    elif row > 4:
                        self.board[row].append(Pieces(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.drawSquares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLUE:
                    self.blueLeft -= 1
                else:
                    self.greenLeft -= 1

    def winner(self):
        if self.blueLeft <= 0:
            return GREEN
        elif self.greenLeft <= 0:
            return BLUE

        return None

    def getValidMoves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == BLUE or piece.king:
            moves.update(self._traverseLeft(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverseRight(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == GREEN or piece.king:
            moves.update(self._traverseLeft(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverseRight(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverseLeft(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverseLeft(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverseRight(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _traverseRight(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.update(self._traverseLeft(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverseRight(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves