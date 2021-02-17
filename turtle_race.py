import math
import random
import turtle
import time

winLength = 500
winHeight = 500

turtles = 13

turtle.screensize(winLength, winHeight)


class Racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + '0 \n')
    file.close()


def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'cyan', 'turquoise',
              'black', 'maroon']
    start = -(winLength / 2) + 20
    for t in range(turtles):
        newPosX = start + t * winLength // turtles
        tList.append(Racer(colors[t], (newPosX, -230)))
        tList[t].turt.showturtle()

    run = True
    while run:
        for t in tList:
            t.move()

        maxColor = []
        maxDis = 0
        for t in tList:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = [t.color]
            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor = [t.color]

        if len(maxColor) > 0:
            run = False
            print("The winner is: ")
            time.sleep(3)
            for win in maxColor:
                print(win)

    oldScore = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        oldScore.append([color, score])

    file.close()

    file = open('scores.txt', 'w')

    for entry in oldScore:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1]) + 1

        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

    file.close()


bg = input("What color do you want the background to be: ")
try:
    turtle.bgcolor(bg)
except:
    print("Sorry, that isn't a color. Please try again...")
    bg = input("What color do you want the background to be: ")

start = input("Would you like to play?\n Enter yes if you want to play, no if you don't: ").lower()

if start == 'y' or start == 'yes':
    print("Ok, let's begin the game...")
    startGame()
elif start == 'n' or start == 'no':
    print("Thank you for interacting with IntelliJ IDEA.")
else:
    print("Sorry, that is an invalid response. Please enter a valid response.")
    start = input("Would you like to play?\n Enter yes if you want to play, no if you don't: ").lower()

if startGame() is False:
    print("Thx")