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


def redrawGameWindow(win, bo, p1, p2, color, ready):
    win.blit(board, (0, 0))
    bo.draw(win, color)

    formatTime1 = str(int(p1 // 60)) + ":" + str(int(p1 % 60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))

    if int(p1 % 60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2%60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]

    font = pygame.font.SysFont('comicsans', 30)

    try:
        txt = font.render(bo.p1Name + "Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render(bo.p2Name + "Time: " + str(formatTime1), 1, (255,255,255))
    except Exception as e:
        print(e)

    win.blit(txt, (520, 10))
    win.blit(txt2, (520, 700))

    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (10, 20))

    if color == 's':
        txt3 = font.render("SPECTATOR MODE", 1, (255, 0, 0))
        win.blit(txt3, (width / 2 - txt3.get_width() / 2, 10))

    if not ready:
        show = "Waiting for Player"
        if color == 's':
            pass