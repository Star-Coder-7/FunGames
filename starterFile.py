import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

W, H = 800, 447
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('SIDE SCROLLER')

bg = pygame.image.load(os.path.join('img7', 'bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()

clock = pygame.time.Clock()


class Player(object):
    run = [pygame.image.load(os.path.join('img7', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('img7', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('img7', 'S1.png')), pygame.image.load(os.path.join('img7', 'S2.png')),
             pygame.image.load(os.path.join('img7', 'S2.png')), pygame.image.load(os.path.join('img7', 'S2.png')),
             pygame.image.load(os.path.join('img7', 'S2.png')), pygame.image.load(os.path.join('img7', 'S2.png')),
             pygame.image.load(os.path.join('img7', 'S2.png')), pygame.image.load(os.path.join('img7', 'S2.png')),
             pygame.image.load(os.path.join('img7', 'S3.png')), pygame.image.load(os.path.join('img7', 'S4.png')),
             pygame.image.load(os.path.join('img7', 'S5.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0
            win.blit(self.slide[self.slideCount//10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount//6], (self.x, self.y))
            self.runCount += 1


class Saw(object):

    def __init__(self, x, y, width, height):
        pass


def redrawWindow():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    runner.draw(win)
    pygame.display.update()


runner = Player(200, 313, 64, 64)
pygame.time.set_timer(USEREVENT + 1, 500)
speed = 30
run = True
while run:
    redrawWindow()
    bgX -= 1.4
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT + 1:
            speed += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] or keys[pygame.K_SPACE]:
        run = False
        pygame.quit()
        quit()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if not runner.jumping:
            runner.jumping = True

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if not runner.sliding:
            runner.sliding = True

    clock.tick(speed)