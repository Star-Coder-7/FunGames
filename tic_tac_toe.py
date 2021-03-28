# Import all the modules we need for this project.
# Set up a list of colors and introduce it to the players.
# Make sure the players are satisfied with the colors.
# Get the players' names and determine who is X and O.
# Create a gui/window to set up for our game.
# Build all the frames needed in the gui and the subheading.
# Introduce a scoreboard for both players.
# Design the reset, newGame, instruction and quit button.
# Produce all the 9 buttons for the board and place them correctly.
# Assemble all the functions needed for the buttons and score.

import tkinter as tk
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from random import choice

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'black', 'cyan',
          'turquoise', 'indigo', 'violet', 'magenta', 'maroon']

print("These are the colors that the window, frames, buttons and writings can be: \n", colors)

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
    print("\nAlright, now let's move on to player names\n")

name1 = input("Please enter player 1's name (X): ")
name2 = input("Please enter player 2's name (O): ")

gameWindow = tk.Tk()
gameWindow.title("Tic Tac Toe")
gameWindow.geometry("1350x750+0+0")
gameWindow.minsize(1250, 650)
gameWindow.maxsize(1450, 850)
gameWindow.config(bg=choice(colors))

topFrame = tk.Frame(gameWindow, bg=choice(colors), width=1350, height=100, relief='ridge', bd=10)
topFrame.grid(row=0, column=0)

heading = tk.Label(topFrame, justify='center', font=('arial', 50, 'bold'), text='Advanced Tic Tac Toe Gui', bd=21,
                   bg=choice(colors), fg=choice(colors))
heading.grid(row=0, column=0)

mainFrame = tk.Frame(gameWindow, width=1350, height=600, bg=choice(colors), relief='ridge', bd=21)
mainFrame.grid(row=1, column=0)

leftFrame = tk.Frame(mainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg=choice(colors), relief='ridge')
leftFrame.pack(side='left')

rightFrame = tk.Frame(mainFrame, bd=10, width=560, height=500, bg=choice(colors), relief='ridge', pady=2, padx=10)
rightFrame.pack(side='right')

rightFrame2 = tk.Frame(rightFrame, bd=10, width=560, height=200, pady=2, padx=10, relief='ridge', bg=choice(colors))
rightFrame2.grid(row=0, column=0)

rightFrame3 = tk.Frame(rightFrame, bd=10, width=560, height=200, bg=choice(colors), pady=2, padx=10, relief='ridge')
rightFrame3.grid(row=1, column=0)

rightFrame4 = tk.Frame(rightFrame, bd=10, width=200, height=200, bg=choice(colors), pady=2, padx=10, relief='ridge')
rightFrame4.grid(row=1, column=1)

playerX = tk.IntVar()
playerO = tk.IntVar()

playerX.set(0)
playerO.set(0)

click = True


def quitGame():
    showinfo(name1 + " and " + name2, "Alright players, you have chosen to quit the game. Thank you for interacting "
                                      "with python, maybe next time!!!")
    gameWindow.destroy()


def checker(buttons):
    global click

    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'X'
        click = False
        scoreKeeper()

    elif buttons['text'] == ' ' and click == False:
        buttons['text'] = 'O'
        click = True
        scoreKeeper()

    elif buttons['text'] != ' ' and click == True:
        showerror(name1, "you cannot place there, because that square is already occupied.")

    else:
        showerror(name2, "you cannot place there, because that square is already occupied.")


def reset():
    global click

    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '

    if click is True:
        click = False

    else:
        click = True


def newGame():
    scoreX = playerX.get() + 1
    scoreO = playerO.get() + 1

    if scoreX > scoreO:
        showinfo(name1, "has won the whole game!!! Well done, X!!!")

    elif scoreO > scoreX:
        showinfo(name2, "has won the whole game!!! Well done, O!!!")

    else:
        showinfo(name1 + " and " + name2, "Wow, the whole game has been tied!!! Well done, X and O!!!")

    reset()

    playerX.set(0)
    playerO.set(0)


def scoreKeeper():
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        score = playerX.get() + 1
        playerX.set(score)
        showinfo(name1, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
        score = playerO.get() + 1
        playerO.set(score)
        showinfo(name2, "WON!!! Well done, you are the winner of this round!!!")
        reset()

    elif button1['text'] != ' ' and button2['text'] != ' ' and button3['text'] != ' ' and button4['text'] != ' ' and \
        button5['text'] != ' ' and button6['text'] != ' ' and button7['text'] != ' ' and button8['text'] != ' ' \
        and button9['text'] != ' ':
        showinfo(name1 + " and " + name2, "No one's won so It's a TIE!!! Well done, X and O!!!")
        reset()


def instructions():
    showinfo(name1 + " and " + name2, "Welcome to Tic Tac Toe, but in an advanced version on a GUI.You two will take "
                                      "turns clicking on squares displaying the letter that you are (X and O). The aim "
                                      "is clicking on squares displaying the letter that you are (X and O) and to get "
                                      "a 3 in a row of your letter without letting the other person doing the same "
                                      "first. Wins can be horizontal, vertical or diagonal. The reset button clears "
                                      "the game board, the new game button clears the game board and resets the scores "
                                      "to 0. The quit button will get you back to the IDE run screen, thus not playing "
                                      "the game anymore. Also, you can minimize the window to a certain point, and "
                                      "maximise it to filling the whole screen. I really hope you enjoy the game!!!")


lblPlayerX = tk.Label(rightFrame2, font=('arial', 40, 'bold'), text=name1, padx=2, pady=2)
lblPlayerX.grid(row=0, column=0, sticky='w')

txtPlayerX = tk.Entry(rightFrame2, font=('arial', 40, 'bold'), bd=2, textvariable=playerX, fg=choice(colors), width=14,
                      justify='left', bg=choice(colors))
txtPlayerX.grid(row=0, column=1)

lblPlayerO = tk.Label(rightFrame2, font=('arial', 40, 'bold'), text=name2, padx=2, pady=2, bg=choice(colors))
lblPlayerO.grid(row=1, column=0, sticky='w')

txtPlayerO = tk.Entry(rightFrame2, font=('arial', 40, 'bold'), bd=2, textvariable=playerO, fg=choice(colors), width=14,
                      justify='left', bg=choice(colors))
txtPlayerO.grid(row=1, column=1)

buttonReset = tk.Button(rightFrame3, text='Reset', font='Times 26 bold', width=20, height=3,
                        command=lambda: reset(), fg=choice(colors), highlightbackground=choice(colors))
buttonReset.grid(row=0, column=0, padx=6, pady=10)

buttonNewGame = tk.Button(rightFrame3, text='New Game', font='Times 26 bold', width=20, height=3, fg=choice(colors),
                          command=lambda: newGame(), highlightbackground=choice(colors))
buttonNewGame.grid(row=1, column=0, padx=6, pady=10)

buttonInstructions = tk.Button(rightFrame4, text='Instructions', font='Times 26 bold', width=10, height=3,
                               highlightbackground=choice(colors), fg=choice(colors), command=lambda: instructions())
buttonInstructions.grid(row=0, column=0, padx=3, pady=5)

buttonQuit = tk.Button(rightFrame4, text='Quit', font='Times 26 bold', width=10, height=2, fg=choice(colors),
                       command=lambda: quitGame(), highlightbackground=choice(colors))
buttonQuit.grid(row=1, column=0, padx=3, pady=5)

button1 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button1), fg=choice(colors))
button1.grid(row=1, column=0, sticky='news')

button2 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button2), fg=choice(colors))
button2.grid(row=1, column=1, sticky='news')

button3 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button3), fg=choice(colors))
button3.grid(row=1, column=2, sticky='news')

button4 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button4), fg=choice(colors))
button4.grid(row=2, column=0, sticky='news')

button5 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button5), fg=choice(colors))
button5.grid(row=2, column=1, sticky='news')

button6 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button6), fg=choice(colors))
button6.grid(row=2, column=2, sticky='news')

button7 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button7), fg=choice(colors))
button7.grid(row=3, column=0, sticky='news')

button8 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button8), fg=choice(colors))
button8.grid(row=3, column=1, sticky='news')

button9 = tk.Button(leftFrame, text=' ', font='Times 26 bold', width=8, height=3, highlightbackground=choice(colors),
                    command=lambda: checker(button9), fg=choice(colors))
button9.grid(row=3, column=2, sticky='news')

gameWindow.mainloop()


