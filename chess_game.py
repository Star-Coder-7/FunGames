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
            off = smallFont.render("Server Offline, Try Again Later...", 1, (255, 0, 0))
            win.blit(off, (width / 2 - off.get_width() / 2, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                offline = False
                try:
                    bo = connect()
                    run = False
                    main()
                    break
                except:
                    print("Server Offline")
                    offline = True


def redrawGameWindow(win, bo, p1, p2, color, ready)):
    pass