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
    pass