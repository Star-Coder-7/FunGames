import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
sWidth = 800
sHeight = 700
playWidth = 300  # meaning 300 // 10 = 30 width per block
playHeight = 600  # meaning 600 // 20 = 30 height per block
blockSize = 30

win = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('TETRIS')

topLeft_x = (sWidth - playWidth) // 2
topLeft_y = sHeight - playHeight

score = 0


# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
colors = [(214, 21, 21), (214, 92, 21), (214, 130, 21), (214, 198, 21), (188, 214, 21), (146, 214, 21),
          (98, 214, 21), (21, 214, 121), (21, 214, 211), (21, 163, 214), (21, 118, 214), (21, 40, 214),
          (101, 21, 214), (143, 21, 214), (195, 21, 214), (214, 21, 172)]

# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = random.choice(colors)
        self.rotation = 0  # number from 0-3


def createGrid(locked_positions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convertShapeFormat(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def validSpace(shape, grid):
    acceptedPositions = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    acceptedPositions = [j for sub in acceptedPositions for j in sub]
    formatted = convertShapeFormat(shape)

    for pos in formatted:
        if pos not in acceptedPositions:
            if pos[1] > -1:
                return False

    return True


def checkLost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def getShape():
    global shapes, colors

    return Piece(5, 0, random.choice(shapes))


def drawTextMiddle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (topLeft_x + playWidth / 2 - (label.get_width() / 2), topLeft_y + playHeight / 2 -
                         label.get_height() / 2))


def displayScore(text, size, color, surface):
    font = pygame.font.SysFont('monospace', size, bold=True)
    label = font.render(text, 1, color)

    sx = topLeft_x + playWidth - 500
    sy = topLeft_y + playHeight / 2 - 100

    surface.blit(label, (sx + 2, sy - 5))


def drawGrid(surface, row, col):
    sx = topLeft_x
    sy = topLeft_y
    for i in range(row):
        pygame.draw.line(surface, (255, 255, 255), (sx, sy + i * 30), (sx + playWidth, sy + i * 30))
        # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (255, 255, 255), (sx + j * 30, sy), (sx + j * 30, sy + playHeight))
            # vertical lines

    # This is the code for horizontal and vertical lines


def clearRows(grid, locked):
    # Need to see if row is clear the shift every other row above down one

    inc = 0
    for i in range(len(grid) - 1, - 1, - 1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def drawNextShape(shape, surface):
    font = pygame.font.SysFont('monospace', 30, bold=True)
    label = font.render('Next Shape', 1, (random.choice(colors)))

    sx = topLeft_x + playWidth + 25
    sy = topLeft_y + playHeight / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    surface.blit(label, (sx + 2, sy - 5))


def drawWindow(surface):
    surface.fill((0, 0, 0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (random.choice(colors)))
    # label2 = font.render('Score:', 1, (random.choice(colors)))

    surface.blit(label, (topLeft_x + playWidth / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (topLeft_x + j * 30, topLeft_y + i * 30, 30, 30), 0)

    # draw grid and border
    drawGrid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (topLeft_x, topLeft_y, playWidth, playHeight), 5)
    # pygame.display.update()


def mainRun():
    global grid, score

    lockedPositions = {}  # (x,y):(255,0,0)
    grid = createGrid(lockedPositions)

    changePiece = False
    run = True
    currentPiece = getShape()
    nextPiece = getShape()
    clock = pygame.time.Clock()
    fallTime = 0
    levelTime = 0
    fallSpeed = 0.27

    while run:

        grid = createGrid(lockedPositions)
        fallTime += clock.get_rawtime()
        levelTime += clock.get_rawtime()
        clock.tick()

        if levelTime / 1000 > 4:
            levelTime = 0
            if fallSpeed > 0.15:
                fallSpeed -= 0.005

        # PIECE FALLING CODE
        if fallTime / 1000 >= fallSpeed:
            fallTime = 0
            currentPiece.y += 1
            if not (validSpace(currentPiece, grid)) and currentPiece.y > 0:
                currentPiece.y -= 1
                changePiece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # move left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    currentPiece.x -= 1
                    if not validSpace(currentPiece, grid):
                        currentPiece.x += 1

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # move right
                    currentPiece.x += 1
                    if not validSpace(currentPiece, grid):
                        currentPiece.x -= 1

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # rotate shape
                    currentPiece.rotation = currentPiece.rotation + 1 % len(currentPiece.shape)
                    if not validSpace(currentPiece, grid):
                        currentPiece.rotation = currentPiece.rotation - 1 % len(currentPiece.shape)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # move shape down
                    currentPiece.y += 1
                    if not validSpace(currentPiece, grid):
                        currentPiece.y -= 1

                elif event.key == pygame.K_SPACE or event.key == pygame.K_q:
                    run = False
                    pygame.quit()
                    quit()

        shape_pos = convertShapeFormat(currentPiece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = currentPiece.color

        # IF PIECE HIT GROUND
        if changePiece:
            score += 1

            for pos in shape_pos:
                p = (pos[0], pos[1])
                lockedPositions[p] = currentPiece.color

            currentPiece = nextPiece
            nextPiece = getShape()
            changePiece = False

            # call four times to check for multiple clear rows
            if clearRows(grid, lockedPositions):
                score += 10

        drawWindow(win)
        drawNextShape(nextPiece, win)
        displayScore(f"Score: {score}", 30, random.choice(colors), win)
        pygame.display.update()

        # Check if user lost
        if checkLost(lockedPositions):
            run = False

    drawTextMiddle("Game ended", 40, (255, 255, 255), win)
    score = 0
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    run = True
    while run:
        win.fill((0, 0, 0))
        drawTextMiddle('Press any key to begin.', 60, (random.choice(colors)), win)

        font = pygame.font.SysFont("Monospace", 20, random.choice(colors), win)
        label = font.render("High Scores (press h to view)", 1, random.choice(colors))
        win.blit(label, (25, 25))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                mainRun()

    pygame.quit()


main()   # start game
