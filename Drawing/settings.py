import pygame

pygame.init()
pygame.font.init()

WHITE = BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (209, 41, 29)
BLUE = (26, 23, 207)
GREEN = (23, 207, 32)
YELLOW = (207, 200, 25)

FPS = 240

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

while True:
    userChoice = input("Do you want grid lines or not. Please enter y/n: ").lower()

    if userChoice == 'y' or userChoice == 'yes':
        print("Sure, you can have grid lines.")
        DRAW_GRID_LINES = True
        break

    elif userChoice == 'n' or userChoice == 'no':
        print("Alright, your choice.")
        DRAW_GRID_LINES = False
        break
    else:
        print("Sorry, please enter y/n.")
        continue


def getFont(size):
    return pygame.font.SysFont("comicsans", size)
