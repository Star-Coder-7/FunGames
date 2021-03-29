import pygame
from constants import WIDTH, HEIGHT, SQ_SIZE, GREEN, BLUE
from checkers_game import Game
from checkers_AI import minimax

pygame.init()

MAX_FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')


def getRowColFromMouse(pos):
    x, y = pos
    row = y // SQ_SIZE
    col = x // SQ_SIZE
    return row, col


def main():
    clock = pygame.time.Clock()
    game = Game(WIN)

    run = True
    while run:
        clock.tick(MAX_FPS)

        if game.turn == GREEN:
            value, newBoard = minimax(game.getBoard(), 3, GREEN, game)
            game.aiMove(newBoard)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getRowColFromMouse(pos)
                game.select(row, col)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_SPACE:
                    run = False

        game.update()

    pygame.quit()


if __name__ == '__main__':
    main()