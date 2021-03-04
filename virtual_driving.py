import pygame
import os

pygame.init()

win = pygame.display.set_mode((1200, 400))
track = pygame.image.load(os.path.join('img4', 'track1.png'))
car = pygame.transform.scale(pygame.image.load(os.path.join('img4', 'tesla.png')), (200, 400))

while True:
    win.blit(track, (0, 0))
    win.blit(car, (0, 0))
    pygame.display.update()
