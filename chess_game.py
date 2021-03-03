'''
the main game
'''

import pygame
import os
import time
from client import Network
import pickle

pygame.font.init()

board = pygame.transform.scale(pygame.image.load(os.path.join("img3", "board.png")), (750, 750))
chessbg = pygame.image.load(os.path.join("img3", "chessbg.png"))
rect = (113, 113, 525, 525)

turn = "w"


def menuScreen(win, name):
    global bo, chessbg
    run = True
    offline = False

    while run:
        win.blit(chessbg, (0, 0))
        smallFont = pygame.font.SysFont("comicsans", 50)

        if offline:
            pass