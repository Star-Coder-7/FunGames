import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "bird3.png")))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("img2", "bg.png")))


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCount = 0
        self.vel = 0
        self.height = self.y
        self.imgCount = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tickCount = 0
        self.height = self.y

    def move(self):
        self.tickCount += 1
        displacement = self.vel * self.tickCount + 1.5 * self.tickCount ** 2

        if displacement >= 16:
            displacement = 16
        if displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.imgCount += 1

        if self.imgCount < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.imgCount < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.imgCount < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.imgCount < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.imgCount == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.imgCount = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.imgCount = self.ANIMATION_TIME * 2

        rotatedImage = pygame.transform.rotate(self.img, self.tilt)
        newRect = rotatedImage.get_rect(center=self.img.get_rect(topLeft=(self.x, self.y)).center)
        win.blit(rotatedImage, newRect.topleft())

    def getMask(self):
        return pygame.mask.from_surface(self.img)


