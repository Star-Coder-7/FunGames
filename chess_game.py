"""
The main game / the driver file.
"""

import pygame
import engine
import chess_AI

pygame.init()
pygame.font.init()

WIDTH = HEIGHT = 720
DIMENSIONS = 8
SQ_SIZE = HEIGHT // DIMENSIONS
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dictionary of images. This will only be called once in the main.
'''


def loadImages():
    pieces = ['wR', 'wK', 'wN', 'wP', 'wQ', 'wB', 'bR', 'bK', 'bN', 'bP', 'bQ', 'bB']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("img3/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # Notice that we can access any image by using the variable dictionary IMAGES[piece]


'''
This is the main driver code.
'''


def main():
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CHESS GAME")
    clock = pygame.time.Clock()
    win.fill(pygame.Color('white'))
    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    gameOver = False

    moveMade = False  # Keeps track of player clicks
    animate = False   # Flag variable for when to animate
    playerClicks = []  # keeps track of player clicks

    loadImages()  # Only done once every run
    sqSelected = ()  # for the last square the user clicked

    playerOne = False   # True if human is playing white, otherwise it's False because AI goes first.
    playerTwo = True  # same as above but vice versa

    run = True
    while run:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not gameOver and humanTurn:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE

                    if sqSelected == (row, col):
                        sqSelected = 0
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)

                    if len(playerClicks) == 2:
                        move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                gs.makeMove(validMoves[i])
                                moveMade = True
                                animate = True
                                sqSelected = ()  # reset square selection
                                playerClicks = []  # reset user clicks
                            if not moveMade:
                                playerClicks = [sqSelected]

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_SPACE:
                    run = False
                elif event.key == pygame.K_u or event.key == pygame.K_z:
                    gs.undoMove()
                    moveMade = True
                    animate = False
                    gameOver = False
                elif event.key == pygame.K_r or event.key == pygame.K_x:
                    gs = engine.GameState()
                    validMoves = gs.getValidMoves()
                    sqSelected = ()
                    playerClicks = []
                    moveMade = False
                    animate = False
                    gameOver = False

        # AI move finder
        if not gameOver and not humanTurn:
            AImove = chess_AI.findBestMinMaxMove(gs, validMoves)
            if AImove is None:
                AImove = chess_AI.findRandomMove(validMoves)
            gs.makeMove(AImove)
            moveMade = True
            animate = True

        if moveMade:
            if animate:
                animateMove(gs.moveLog[-1], win, gs.board, clock)
            validMoves = gs.getValidMoves()
            moveMade = False
            animate = False

        drawGameState(win, gs, validMoves, sqSelected)

        if gs.checkmate:
            gameOver = True
            if gs.whiteToMove:
                drawText(win, "CONGRATULATIONS BLACK!!!\nYou won by a checkmate.")
            else:
                drawText(win, "CONGRATULATIONS WHITE!!!\nYou won by a checkmate.")
        elif gs.stalemate:
            gameOver = True
            drawText(win, "STALEMATE!!!\nGame has ended due to a stalemate.")

        clock.tick(MAX_FPS)
        pygame.display.update()


def drawGameState(win, gs, validMoves, sqSelected):
    """
    Responsible for all the drawings amd graphics within a current game state.
    :param win: The window
    :param gs: Game State
    :return: None
    """

    drawBoard(win)
    highlightSquares(win, gs, validMoves, sqSelected)
    drawPieces(win, gs.board)


def drawBoard(win):
    global colors
    colors = [pygame.Color(232, 128, 128), pygame.Color(20, 62, 217)]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(win, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(win, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                win.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def highlightSquares(win, gs, validMoves, sqSelected):
    # Highlight selected square first
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = pygame.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(150)  # transparency value
            s.fill(pygame.Color(38, 232, 16))
            win.blit(s, (c * SQ_SIZE, r * SQ_SIZE))
            # Highlight all the possible valid moves for the square selected
            s.fill(pygame.Color(101, 10, 204))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    win.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))


'''
Animating the chess pieces moving, not just a delete and draw
'''


def animateMove(move, win, board, clock):
    global colors
    dR = move.endRow - move.startRow
    dC = move.endCol - move.startCol
    framesPerSquare = 12
    frameCount = (abs(dR) + abs(dC)) * framesPerSquare
    for frame in range(frameCount + 1):
        r, c = (move.startRow + dR * frame / frameCount, move.startCol + dC * frame / frameCount)
        drawBoard(win)
        drawPieces(win, board)
        # erase the piece moved from its ending square
        color = colors[(move.endRow + move.endCol) % 2]
        endSquare = pygame.Rect(move.endCol * SQ_SIZE, move.endRow * SQ_SIZE, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(win, color, endSquare)
        # draw captured piece onto rectangle
        if move.pieceCaptured != '--':
            win.blit(IMAGES[move.pieceCaptured], endSquare)
        # draw the moving piece
        win.blit(IMAGES[move.pieceMoved], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.update()
        clock.tick(60)


def drawText(win, text):
    font = pygame.font.SysFont("Helvetica", 22, True, True)
    textObject = font.render(text, 0, pygame.Color(13, 211, 214))
    textLocation = pygame.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - textObject.get_width() / 2,
                                                         HEIGHT / 2 - textObject.get_height() / 2)
    win.blit(textObject, textLocation)


if __name__ == '__main__':
    main()
