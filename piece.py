import pygame
import os

bBishop = pygame.image.load(os.path.join("img3", "black_bishop.png"))
bKing = pygame.image.load(os.path.join("img3", "black_king.png"))
bKnight = pygame.image.load(os.path.join("img3", "black_knight.png"))
bPawn = pygame.image.load(os.path.join("img3", "black_pawn.png"))
bQueen = pygame.image.load(os.path.join("img3", "black_queen.png"))
bRook = pygame.image.load(os.path.join("img3", "black_rook.png"))

wBishop = pygame.image.load(os.path.join("img3", "white_rook.png"))
wKing = pygame.image.load(os.path.join("img3", "white_rook.png"))
wKnight = pygame.image.load(os.path.join("img3", "white_rook.png"))
wPawn = pygame.image.load(os.path.join("img3", "white_rook.png"))
wQueen = pygame.image.load(os.path.join("img3", "white_rook.png"))
wRook = pygame.image.load(os.path.join("img3", "white_rook.png"))

b = [bBishop, bKing, bKnight, bPawn, bQueen, bRook]
w = [wBishop, wKing, wKnight, wPawn, wQueen, wRook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))


class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.moveList = []
        self.king = False
        self.pawn = False

    def isSelected(self):
        return self.selected

    def updateValidMoves(self, board):
        self.moveList = self.validMoves(board)

    def draw(self, win, color):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        x = (4 - self.col) + round(self.startX + (self.col * self.rect[2] / 8))
        y = 3 + round(self.startY + (self.row * self.rect[3] / 8))

        if self.selected and self.color == color:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 62, 62), 4)

        win.blit(drawThis, (x, y))

        '''if self.selected and self.color == color:  # Remove false to draw dots
           moves = self.move_list
           for move in moves:
               x = 33 + round(self.startX + (move[0] * self.rect[2] / 8))
               y = 33 + round(self.startY + (move[1] * self.rect[3] / 8))
               pygame.draw.circle(win, (255, 0, 0), (x, y), 10)'''

    def changePos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return str(self.col) + " " + str(self.row)


class Bishop(Piece):
    pass