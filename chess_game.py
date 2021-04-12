"""
The main game / the driver file.
"""

import pygame
import engine
import chess_AI
import os

pygame.init()
pygame.font.init()

chess_icon = pygame.image.load(os.path.join('img3', 'chess_icon.ico'))
pygame.display.set_icon(chess_icon)

BOARD_WIDTH = BOARD_HEIGHT = 720
MOVE_LOG_PANEL_WIDTH = 265
MOVE_LOG_PANEL_HEIGHT = BOARD_HEIGHT
DIMENSIONS = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSIONS
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
    win = pygame.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    pygame.display.set_caption("CHESS GAME")
    clock = pygame.time.Clock()
    win.fill(pygame.Color('white'))
    gs = engine.GameState()
    validMoves = gs.getValidMoves()
    moveLogFont = pygame.font.SysFont("Arial", 14, False, False)
    gameOver = False

    moveMade = False  # Keeps track of player clicks
    animate = False  # Flag variable for when to animate
    playerClicks = []  # keeps track of player clicks

    loadImages()  # Only done once every run
    sqSelected = ()  # for the last square the user clicked

    playerOne = True  # True if human is playing white, otherwise it's False because AI goes first.
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

                    if sqSelected == (row, col) or col >= 8:
                        sqSelected = ()
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
            AImove = chess_AI.findBestNegaMaxAlphaBetaMove(gs, validMoves)
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

        drawGameState(win, gs, validMoves, sqSelected, moveLogFont)

        if gs.checkmate or gs.stalemate:
            gameOver = True

            text = "STALEMATE!!!\nGame has ended due to a stalemate." if gs.stalemate else \
                "CONGRATULATIONS BLACK!!!\nYou won by a checkmate." if gs.whiteToMove else \
                    "CONGRATULATIONS WHITE!!!\nYou won by a checkmate."
            drawEndGameText(win, text)

        clock.tick(MAX_FPS)
        pygame.display.flip()


# -------------------------------------------VERY IMPORTANT FUNCTIONS---------------------------------------------------


def drawGameState(win, gs, validMoves, sqSelected, moveLogFont):
    """
    Responsible for all the drawings amd graphics within a current game state.
    :param win: The window
    :param gs: Game State
    :return: None
    """

    drawBoard(win)
    highlightSquares(win, gs, validMoves, sqSelected)
    drawPieces(win, gs.board)
    drawMoveLog(win, gs, moveLogFont)


def drawBoard(win):
    global colors
    colors = [pygame.Color(232, 128, 128), pygame.Color(20, 62, 217)]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(win, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


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
            s.fill(pygame.Color(204, 148, 18))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    win.blit(s, (move.endCol * SQ_SIZE, move.endRow * SQ_SIZE))


def drawPieces(win, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                win.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draws the move logs
'''


def drawMoveLog(win, gs, font):
    moveLogRect = pygame.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    pygame.draw.rect(win, pygame.Color(0, 0, 0), moveLogRect)
    moveLog = gs.moveLog
    moveTexts = []
    for i in range(0, len(moveLog), 2):
        moveString = str(i // 2 + 1) + '. ' + str(moveLog[i]) + ', '
        if i + 1 < len(moveLog):    # make sure black makes a move
            moveString += str(moveLog[i + 1])

        moveTexts.append(moveString)

    movesPerRow = 3
    padding = 5
    textY = padding
    lineSpacing = 2
    for i in range(0, len(moveTexts), movesPerRow):
        text = ""
        for j in range(movesPerRow):
            if i + j < len(moveTexts):
                text += moveTexts[i + j] + '  '
        textObject = font.render(text, True, pygame.Color(255, 255, 255))
        textLocation = moveLogRect.move(padding, textY)
        win.blit(textObject, textLocation)
        textY += textObject.get_height() + lineSpacing


'''
Animating the chess pieces moving, not just a delete and draw or teleport (except for undoing)
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
            if move.enPassant:
                enPassantRow = move.endRow + 1 if move.pieceCaptured[0] == 'b' else move.endRow - 1
                endSquare = pygame.Rect(move.endCol * SQ_SIZE, enPassantRow * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            win.blit(IMAGES[move.pieceCaptured], endSquare)
        # draw the moving piece
        win.blit(IMAGES[move.pieceMoved], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        pygame.display.update()
        clock.tick(60)


def drawEndGameText(win, text):
    font = pygame.font.SysFont("Helvetica", 32, True, False)
    textObject = font.render(text, 0, pygame.Color(13, 211, 214))
    textLocation = pygame.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - textObject.get_width() / 2,
                                                                     BOARD_HEIGHT / 2 - textObject.get_height() / 2)
    win.blit(textObject, textLocation)
    textObject = font.render(text, 0, pygame.Color(0, 0, 0))
    win.blit(textObject, textLocation.move(2, 2))


if __name__ == '__main__':
    main()
