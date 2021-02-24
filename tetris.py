import pygame
import random

"""
10 x 20 square grid 
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6 (python starts with 0, not 1)
"""

pygame.font.init()

# GLOBALS VARS
sWidth = 800
sHeight = 700
playWidth = 300     # meaning 300 // 10 = 30 width per block
playHeight = 600    # meaning 600 // 20 = 20 height per block
blockSize = 30

topLeft_x = (sWidth - playWidth) // 2
topLeft_y = sHeight - playHeight

# ALL THE SHAPE FORMATS

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

L =  [['.....',
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
shapeColors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
               (255, 165, 0), (128, 0, 128)]

# index 0 - 6 represent shape


class Piece(object):
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapeColors[shapes.index(shape)]


def createGrid(lockedPositions={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in lockedPositions:
                c = lockedPositions[(j, i)]
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
            return T
    return False


def getShape():
    global shapes, shapeColors

    return Piece(5, 0, random.choice(shapes))


def drawTextMiddle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (topLeft_x + playWidth / 2 - (label.get_width() / 2), topLeft_y + playHeight / 2 -
                         label.get_height() / 2))


def drawGrid(surface, row, col):
    pass