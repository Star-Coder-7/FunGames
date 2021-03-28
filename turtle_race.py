import turtle
from tkinter.messagebox import showwarning, showinfo
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Black', 'Purple', 'Pink', 'Brown', 'Cyan', 'Gray', 'White',
          'Turquoise']


def getRacers():
    racers = 0
    while True:
        racers = turtle.numinput('Input Window', 'Please enter the number of racers (2 - 12)')
        try:
            if 2 <= racers <= 12:
                return racers
            else:
                showwarning('Warning Window', 'Sorry, your number has to be in range from 2 - 12... PLease try again!')
                continue
        except:
            continue


def race(colors):
    turtles = createTurtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def createTurtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        if racer.color() == screen.bgcolor():
            racer.color(random.choice(COLORS))
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Turtle Racing!')
screen.bgcolor(random.choice(COLORS))

racers = getRacers()
random.shuffle(COLORS)
colors = COLORS[:int(racers)]

winner = race(colors)
time.sleep(3)
showinfo(title="Winner Window", message="The winner is the turtle who's color is: " + winner + "!!!")