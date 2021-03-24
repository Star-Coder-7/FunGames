import casino
import pygame
import sys
import os
import math
import time
import tkinter as tk
from tkinter import messagebox

pygame.init()

cardBack = pygame.image.load(os.path.join('img5', 'cardBack.png'))
screen = pygame.display.set_mode((1300, 900))
pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('monospace', 70)
smallFont = pygame.font.SysFont('monospace', 30)
bg = pygame.image.load(os.path.join('img5', 'background.jpg'))
screen.fill((0,128,0))
clock = pygame.time.Clock()
deck = casino.Cards()
cardList = deck.getCards()
d = casino.Dealer(cardList)
p = casino.PLayer(cardList)

pygame.display.flip()

onTable = []
topCards = []
cardImg = [None]

# LOAD 52 IMAGES

aceClubs = pygame.image.load(os.path.join('img5', 'ace_of_clubs.png'))
aceSpades = pygame.image.load(os.path.join('img5', 'ace_of_spades.png'))
aceDiamonds = pygame.image.load(os.path.join('img5', 'ace_of_diamonds.png'))
aceHearts = pygame.image.load(os.path.join('img5', 'ace_of_hearts.png'))

twoClubs = pygame.image.load(os.path.join('img5', '2_of_clubs.png'))
twoDiamonds = pygame.image.load(os.path.join('img5', '2_of_diamonds.png'))
twoHearts = pygame.image.load(os.path.join('img5', '2_of_hearts.png'))
twoSpades = pygame.image.load(os.path.join('img5', '2_of_spades.png'))

threeClubs = pygame.image.load(os.path.join('img5', '3_of_clubs.png'))
threeSpades = pygame.image.load(os.path.join('img5', '3_of_spades.png'))
threeDiamonds = pygame.image.load(os.path.join('img5', '3_of_diamonds.png'))
threeHearts = pygame.image.load(os.path.join('img5', '3_of_hearts.png'))

fourClubs = pygame.image.load(os.path.join('img5', '4_of_clubs.png'))
fourSpades = pygame.image.load(os.path.join('img5', '4_of_spades.png'))
fourDiamonds = pygame.image.load(os.path.join('img5', '4_of_diamonds.png'))
fourHearts = pygame.image.load(os.path.join('img5', '4_of_hearts.png'))

fiveClubs = pygame.image.load(os.path.join('img5', '5_of_clubs.png'))
fiveSpades = pygame.image.load(os.path.join('img5', '5_of_spades.png'))
fiveDiamonds = pygame.image.load(os.path.join('img5', '5_of_diamonds.png'))
fiveHearts = pygame.image.load(os.path.join('img5', '5_of_hearts.png'))

sixClubs = pygame.image.load(os.path.join('img5', '6_of_clubs.png'))
sixSpades = pygame.image.load(os.path.join('img5', '6_of_spades.png'))
sixDiamonds = pygame.image.load(os.path.join('img5', '6_of_diamonds.png'))
sixHearts = pygame.image.load(os.path.join('img5', '6_of_hearts.png'))

sevenClubs = pygame.image.load(os.path.join('img5', '7_of_clubs.png'))
sevenSpades = pygame.image.load(os.path.join('img5', '7_of_spades.png'))
sevenDiamonds = pygame.image.load(os.path.join('img5', '7_of_diamonds.png'))
sevenHearts = pygame.image.load(os.path.join('img5', '7_of_hearts.png'))

eightClubs = pygame.image.load(os.path.join('img5', '8_of_clubs.png'))
eightSpades = pygame.image.load(os.path.join('img5', '8_of_spades.png'))
eightDiamonds = pygame.image.load(os.path.join('img5', '8_of_diamonds.png'))
eightHearts = pygame.image.load(os.path.join('img5', '8_of_hearts.png'))

nineClubs = pygame.image.load(os.path.join('img5', '9_of_clubs.png'))
nineSpades = pygame.image.load(os.path.join('img5', '9_of_spades.png'))
nineDiamonds = pygame.image.load(os.path.join('img5', '9_of_diamonds.png'))
nineHearts = pygame.image.load(os.path.join('img5', '9_of_hearts.png'))

tenClubs = pygame.image.load(os.path.join('img5', '10_of_clubs.png'))
tenSpades = pygame.image.load(os.path.join('img5', '10_of_diamonds.png'))
tenDiamonds = pygame.image.load(os.path.join('img5', '10_of_hearts.png'))
tenHearts = pygame.image.load(os.path.join('img5', '10_of_spades.png'))

jackClubs = pygame.image.load(os.path.join('img5', 'jack_of_clubs.png'))
jackSpades = pygame.image.load(os.path.join('img5', 'jack_of_spades.png'))
jackDiamonds = pygame.image.load(os.path.join('img5', 'jack_of_diamonds.png'))
jackHearts = pygame.image.load(os.path.join('img5', 'jack_of_hearts.png'))

queenClubs = pygame.image.load(os.path.join('img5', 'queen_of_clubs.png'))
queenSpades = pygame.image.load(os.path.join('img5', 'queen_of_spades.png'))
queenDiamonds = pygame.image.load(os.path.join('img5', 'queen_of_diamonds.png'))
queenHearts = pygame.image.load(os.path.join('img5', 'queen_of_hearts.png'))

kingClubs = pygame.image.load(os.path.join('img5', 'king_of_clubs.png'))
kingSpades = pygame.image.load(os.path.join('img5', 'king_of_spades.png'))
kingDiamonds = pygame.image.load(os.path.join('img5', 'king_of_diamonds.png'))
kingHearts = pygame.image.load(os.path.join('img5', 'king_of_hearts.png'))


cardImg.append([aceClubs, aceDiamonds, aceHearts, aceSpades])
cardImg.append([twoClubs, twoDiamonds, twoHearts, twoSpades])
cardImg.append([threeClubs, threeDiamonds, threeHearts, threeSpades])
cardImg.append([fourClubs, fourDiamonds, fourHearts, fourSpades])
cardImg.append([fiveClubs, fiveDiamonds, fiveHearts, fiveSpades])
cardImg.append([sixClubs, sixDiamonds, sixHearts, sixSpades])
cardImg.append([sevenClubs, sevenDiamonds, sevenHearts, sevenSpades])
cardImg.append([eightClubs, eightDiamonds, eightHearts, eightSpades])
cardImg.append([nineClubs, nineDiamonds, nineHearts, nineSpades])
cardImg.append([tenClubs, tenDiamonds, tenHearts, tenSpades])
cardImg.append([jackClubs, jackDiamonds, jackHearts, jackSpades])
cardImg.append([queenClubs, queenDiamonds, queenHearts, queenSpades])
cardImg.append([kingClubs, kingDiamonds, kingHearts, kingSpades])

one = pygame.image.load(os.path.join('img6', '1.png'))
two = pygame.image.load(os.path.join('img6', '2.png'))
five = pygame.image.load(os.path.join('img6', '5.png'))
ten = pygame.image.load(os.path.join('img6', '10.png'))
twenty = pygame.image.load(os.path.join('img6', '20.png'))

didBet = False
betChips = 0
chips = []
betArray = []
playerChips = []

chips.append([one, 20, 225, 1])
chips.append([two, 20, 300, 2])
chips.append([five, 20, 375, 5])
chips.append([ten, 20, 450, 10])
chips.append([twenty, 20, 525, 20])


def lost():
    screen.fill((0, 128, 0))
    label = myfont.render('Press any key to play again', 1, (255 , 255, 255))
    label2 = myfont.render('Out of chips...', 1, (255, 255, 255))
    screen.blit(label, (100, 450))
    screen.blit(label2, (350, 350))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            firstStart()

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def bet():
    global betChips
    global playerChips
    label = myfont.render('PLease place your bet', 1, (255, 255, 255))
    screen.blit(label, (230, 430))
    updateChips()
    pygame.display.update()

    while True:
        label = smallFont.render('Press space when finished', 1, (255, 255, 255))
        screen.blit(label, (430, 850))
        updateChips()
        pygame.display.update()
        ev = pygame.event.poll()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in range(len(chips)):
                if chips[i][1] < pos[0] < chips[i][1] + 50:
                    if chips[i][2] < pos[1] < chips[i][2] + 50:
                        if playerChips - chips[i][3] >= 0:
                            betChips += chips[i][3]
                            dealChips(chips[i][0], 525 + i * 50, 550, chips[i][1], chips[i][2])
                            playerChips -= chips[i][3]
                        else:
                            root = tk.Tk()
                            root.title('Warning Window')
                            messagebox.showinfo('Not enough chips!', ('You do not have enough \n chips to bet that '
                                                                      'amount, \n your current amount of chips is '
                                                                      + str(playerChips)))
                            try:
                                root.destroy()
                            except:
                                pass

        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if betChips >= 1:
                pygame.draw.rect(screen, (0, 128, 0), (429, 849, 600, 100))
                break


def drawChip(img, x, y):
    w = 50
    h = 50
    newIMG = pygame.transform.scale(img, (w, h))
    screen.blit(newIMG, (x, y))


def firstStart():
    global playerChips
    reset()
    playerChips = 50
    screen.fill((0, 128, 0))
    label = myfont.render('Welcome to Blackjack!', 1, (255, 255, 255))
    label2 = myfont.render('Press space to start', 1, (255, 255, 255))
    screen.blit(label2, (225, 550))
    screen.blit(label, (175, 400))
    pygame.display.update()

    while True:
        clock.tick(60)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            else:
                dealPlayer(675, 650)
                dealPlayer(500, 650)
                dealPlayer(675, 50)
                dealPlayer(500, 50)
                bet()
                main()


def restart():
    global playerChips
    screen.fill((0, 128, 0))
    pygame.display.update()

    if playerChips == 0:
        lost()

    while True:
        clock.tick(60)
        dealplayer(675, 650)
        dealplayer(500, 650)
        dealplayer(675, 50)
        dealplayer(500, 50)
        bet()
        main()


def reset():
    global onTable
    global cardImg
    global topCards
    global didBet
    global betChips
    global betArray
    betArray = []
    onTable = []
    topCards = []
    didBet = False
    betChips = 0
    time.sleep(1)


def dealChips(img, x, y, s, w):
    endx = x
    endy = y
    movex = s
    movey = w
    xDist = x - s
    yDist = y - w
    constantX = xDist / 50
    constantY = yDist / 50

    for i in range(100):
        if movey >= endy and movex >= endx:
            break
        else:
            screen.fill((0, 128, 0))
            drawChip(img, movex, movey)
            if movex <= endx:
                movex += constantX
            if movey <= endy:
                movey += constantY

        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for q in range(len(betArray)):
            drawChip(betArray[q][0], betArray[q][1], betArray[q][2])

        clock.tick(50)
        drawCard(cardBack, 15, 15)
        updateChips()
        pygame.display.update()

    betArray.append([img, movex, movey])


def dealPlayer(x, y):
    endx = x
    endy = y
    movex = 0
    movey = 0

    h = math.sqrt(endx ** 2 + endy ** 2)

    for i in range(round(h / 10)):
        screen.fill((0, 128, 0))
        movex += endx / (h / 10)
        movey += endy / (h / 10)
        drawCard(cardBack, movex, movey)

        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for w in range(len(betArray)):
            drawChip(betArray[w][0], betArray[w][1], betArray[w][2])

        clock.tick(50)
        drawCard(cardBack, 15, 15)
        updateChips()
        pygame.display.update()

    onTable.append([cardBack, x, y])


def dealPLayerHit(hit, x, y):
    endx = x
    endy = y
    movex = 0
    movey = 0

    h = math.sqrt(endx ** 2 + endy ** 2)

    for i in range(round(h / 10)):
        screen.fill((0, 128, 0))
        updateChips()
        movex += endx / (h/10)
        movey += endy / (h/10)
        drawCard(cardBack, movex, movey)

        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        for i in range(len(chips)):
            drawChip(chips[i][0], chips[i][1], chips[i][2])

        for w in range(len(betArray)):
            drawChip(betArray[w][0], betArray[w][1], betArray[w][2])

        drawCard(cardBack, 15, 15)
        clock.tick(50)
        pygame.display.update()

    onTable.append([hit, x, y])


def cardImage(n, suit):
    if suit == 'C':
        return cardImg[n][0]
    elif suit == 'D':
        return cardImg[n][1]
    elif suit == 'H':
        return cardImg[n][2]
    elif suit == 'S':
        return cardImg[n][3]


def updateChips():
    global playerChips
    pygame.draw.rect(screen, (0, 128, 0), (39, 585, 200, 40), 0)
    label = smallFont.render('Chips: ' + str(playerChips), 1, (255,255,255))
    screen.blit(label, (10, 585))


def updateScore(turn=False):
    dScore = d.getScore()
    pScore = p.getScore()
    score1 = smallFont.render(str(dScore), 1, (255,255,255))
    score2 = smallFont.render(str(pScore), 1, (255, 255, 255))
    screen.blit(score2, (1150, 700))
    if turn:
        screen.blit(score1, (1150, 50))


def drawCard(img, x, y):
    white = (255, 255, 255)
    w = 130
    h = 181
    pygame.draw.rect(screen, white, (x - 5, y - 4, w + 10, h + 8), 0)
    newIMG = pygame.transform.scale(img, (w, h))
    screen.blit(newIMG, (x, y))


def main():
    # DRAWING AND INIT
    # VARIABLES
    global d
    global p
    global playerChips
    deck = casino.Cards()
    cardList = deck.getCards()
    d = casino.Dealer(cardList)
    p = casino.PLayer(cardList)
    playerCards = p.deal()
    dealerCards = d.deal()
    allowHit = False
    playerReveal = False
    playerTurn = True
    playerStay = False
    onTable[2] = [cardImage(dealerCards[0][0], dealerCards[0][1]), 675, 50]
    onTable[3] = [cardBack, 500, 50]

    while True:
        pygame.display.update()
        clock.tick(60)
        # PLAYER DECISION
        if playerReveal is False:
            drawCard(cardBack, 675, 650)
            drawCard(cardBack, 500, 650)
            label = smallFont.render('Press space to reveal cards', 1, (255, 255, 255))
            screen.blit(label, (430, 850))
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if ev.key == pygame.K_SPACE:
                    # Show cards
                    playerReveal = True
                    allowHit = True
                    drawCard(cardImage(playerCards[0][0], playerCards[0][1]), 675, 650)
                    drawCard(cardImage(playerCards[1][0], playerCards[1][1]), 500, 650)
                    onTable[0] = [cardImage(playerCards[0][0], playerCards[0][1]), 675, 650]
                    onTable[1] = [cardImage(playerCards[1][0], playerCards[1][1]), 500, 650]
                    pygame.draw.rect(screen, (0, 128, 0), (429, 849, 550, 100))

            pygame.display.update()

        else:
            pass