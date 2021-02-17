import pygame
import random

pygame.init()

winHeight = 600
winWidth = 700
win = pygame.display.set_mode((winWidth, winHeight))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)

buttonFont = pygame.font.SysFont('arial', 20)
guessFont = pygame.font.SysFont('monospace', 24)
lostFont = pygame.font.SysFont('arial', 45)
word = ''
buttons = []
guesses = []
hangmanPics = [pygame.image.load('hangman0.png'), pygame.image.load('hangman1.png'), pygame.image.load('hangman2.png'),
               pygame.image.load('hangman3.png'), pygame.image.load('hangman4.png'), pygame.image.load('hangman5.png'),
               pygame.image.load('hangman6.png')]
limbs = 0


def redrawGameWindow():
    global guesses
    global hangmanPics
    global limbs
    win.fill(GREEN)

    for i in range(len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1], buttons[i][2]), buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1], buttons[i][2]), buttons[i][3] - 2)

            label = buttonFont.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (label.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

    spaced = spacedOut(word, guesses)
    label1 = guessFont.render(spaced, 1, BLACK)
    rect = label1.get_rect()
    length = rect[2]

    win.blit(label1, (winWidth / 2 - length / 2, 400))

    pic = hangmanPics[limbs]
    win.blit(pic, (winWidth / 2 - pic.get_width() / 2 + 20, 150))
    pygame.display.update()


def randomWord():
    file = open('words.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]


def hang(guess):
    global word
    if guess.lower() not in word.lower():
        return True
    else:
        return False


def spacedOut(word, guesses=[]):
    spacedWord = ''
    guessedLetters = guesses
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWord += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWord += word[x].upper() + ' '
        elif word[x] == ' ':
            spacedWord += ' '
    return spacedWord


def buttonHit(x, y):
    for i in range(len(buttons)):
        if buttons[i][1] + 20 > x > buttons[i][1] - 20:
            if buttons[i][2] + 20 > y > buttons[i][2] - 20:
                return buttons[i][5]
    return None


def end(winner=False):
    global limbs
    lostTxt = 'Unlucky, you lost... press any key to play again...'
    winTxt = 'CONGRATS!!!, you won... press any key to play again...'
    redrawGameWindow()
    pygame.time.delay(1000)
    win.fill(GREEN)

    if winner is True:
        label = lostFont.render(winTxt, 1, BLACK)
    else:
        label = lostFont.render(lostTxt, 1, BLACK)

    wordTxt = lostFont.render(word.upper(), 1, BLACK)
    wordWas = lostFont.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth / 2 - wordTxt.get_width() / 2, 295))
    win.blit(wordWas, (winWidth / 2 - wordWas.get_width() / 2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pygame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                again = False
    reset()


def reset():
    global limbs
    global guesses
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4] = True

    limbs = 0
    guesses = []
    word = randomWord()


increase = round(winWidth / 13)
for i in range(26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i - 13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20, True, 65 + i])

word = randomWord()
inPlay = True

while inPlay:
    redrawGameWindow()
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            letter = buttonHit(clickPos[0], clickPos[1])
            if letter is not None:
                guesses.append(chr(letter))
                buttons[letter - 65][4] = False
                if hang(chr(letter)):
                    if limbs != 5:
                        limbs += 1
                    else:
                        end()
                else:
                    print(spacedOut(word, guesses))
                    if spacedOut(word, guesses).count('_') == 0:
                        end(True)

pygame.quit()




