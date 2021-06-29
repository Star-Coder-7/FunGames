from turtle import *

speed(0)
hideturtle()

win = Screen()
win.bgcolor("black")
win.title("Fractal Art")


def tree(size, levels, angle):
    color("purple")
    if levels == 0:
        color("green")
        dot(size)
        color("blue")
        return

    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


def snowflakeSide(length, levels):
    if levels == 0:
        forward(length)
        return

    length /= 3.0

    snowflakeSide(length, levels - 1)
    left(60)
    snowflakeSide(length, levels - 1)
    right(120)
    snowflakeSide(length, levels - 1)
    left(60)
    snowflakeSide(length, levels - 1)


def createSnowflake(sides, length):
    colors = ["red", "orange", "magenta", "yellow"]
    for i in range(sides):
        color(colors[i])
        snowflakeSide(length, sides)
        right(360 / sides)


def differentColors(sides, length):
    colors = ["yellow", "magenta", "orange", "red"]
    for i in range(sides):
        color(colors[i])
        snowflakeSide(length, sides)
        right(360 / sides)


left(90)
tree(80, 8, 30)

right(90)
createSnowflake(4, 200)

right(90)
differentColors(4, 200)

mainloop()
