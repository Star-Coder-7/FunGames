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
playHeight = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

topLeft_x = (sWidth - playWidth) // 2
topLeft_y = sHeight - playHeight


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
shapeColors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shapeColors[shapes.index(shape)]
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
    global shapes, shapeColors

    return Piece(5, 0, random.choice(shapes))


def drawTextMiddle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (topLeft_x + playWidth / 2 - (label.get_width() / 2), topLeft_y + playHeight / 2 -
                         label.get_height() / 2))


def drawGrid(surface, row, col):
    sx = topLeft_x
    sy = topLeft_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i * 30), (sx + playWidth, sy + i * 30))  # horizontal
        for j in range(col):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * 30, sy), (sx + j * 30, sy + playHeight))  # vertical

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
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = topLeft_x + playWidth + 50
    sy = topLeft_y + playHeight / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 30, sy + i * 30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))


def drawWindow(surface):
    surface.fill((0,0,0))
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (topLeft_x + playWidth / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (topLeft_x + j * 30, topLeft_y + i * 30, 30, 30), 0)

    # draw grid and border
    drawGrid(surface, 20, 10)
    pygame.draw.rect(surface, (255, 0, 0), (topLeft_x, topLeft_y, playWidth, playHeight), 5)
    # pygame.display.update()


def main():
    global grid

    locked_positions = {}  # (x,y):(255,0,0)
    grid = createGrid(locked_positions)

    change_piece = False
    run = True
    current_piece = getShape()
    next_piece = getShape()
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    fall_speed = 0.27
    score = 0

    while run:

        grid = createGrid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005


        # PIECE FALLING CODE
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (validSpace(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # move left
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    current_piece.x -= 1
                    if not validSpace(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # move right
                    current_piece.x += 1
                    if not validSpace(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not validSpace(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # move shape down
                    current_piece.y += 1
                    if not validSpace(current_piece, grid):
                        current_piece.y -= 1

                elif event.key == pygame.K_SPACE or event.key == pygame.K_q:
                    run = False
                    pygame.quit()
                    quit()

        shape_pos = convertShapeFormat(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = getShape()
            change_piece = False

            # call four times to check for multiple clear rows
            if clearRows(grid, locked_positions):
                score += 10

        drawWindow(win)
        drawNextShape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if checkLost(locked_positions):
            run = False

    drawTextMiddle("You Lost", 40, (255, 255, 255), win)
    pygame.display.update()
    pygame.time.delay(2000)


def mainMenu():
    run = True
    while run:
        win.fill((0,0,0))
        drawTextMiddle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()


win = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('Tetris')

mainMenu()  # start game