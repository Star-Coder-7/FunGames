import turtle
import random
import os

# colors
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'black', 'cyan',
          'turquoise', 'indigo', 'violet', 'magenta', 'maroon']

print("These are all the colors that the game may contain: \n", colors)

user = str(input("\nDo you want to remove any colors? If you want to, enter the color or press enter to stop: ")) \
    .lower()

while user != "":
    if user in colors:
        print("Alright, I will remove that.")
        colors.remove(user)

        user = str(input("\nDo you want to remove any colors? If you want to, enter the color or press enter to stop: ")
                   ).lower()
    else:
        print("Sorry, that's an invalid response!!!")

        user = str(input("\nDo you want to remove any colors? If you want to, enter the color or press enter to stop: ")
                   ).lower()
else:
    print("\nHere is the final color list: \n", colors)
    print("\nAlright, now let's move on to shapes...\n")

# now the shapes
shapes = ["square", "circle", "triangle", "arrow", "classic", "turtle"]

print("These are all the colors that the game may contain: \n", shapes)

user = str(input("\nDo you want to remove any shapes? If you want to, enter the shape or press enter to stop: ")) \
    .lower()

while user != "":
    if user in shapes:
        print("Alright, I will remove that.")
        shapes.remove(user)

        user = str(input("\nDo you want to remove any shapes? If you want to, enter the shape or press enter to stop: ")
                   ).lower()
    else:
        print("Sorry, that's an invalid response!!!")

        user = str(input("\nDo you want to remove any shapes? If you want to, enter the shape or press enter to stop: ")
                   ).lower()
else:
    print("\nHere is the final color list: \n", shapes)
    print("\nAlright, now let's move on to shapes...\n")

win = turtle.Screen()
win.title("Ping Pong")
win.bgcolor(random.choice(colors))
win.setup(width=800, height=600)
win.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape(random.choice(shapes))
paddleA.color(random.choice(colors))
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape(random.choice(shapes))
paddleB.color(random.choice(colors))
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape(random.choice(shapes))
ball.color(random.choice(colors))
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape(random.choice(shapes))
pen.color(random.choice(colors))
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard bindings
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")
win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Right")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and paddleA.ycor() + 50 > ball.ycor() > paddleA.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and paddleB.ycor() + 50 > ball.ycor() > paddleB.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
