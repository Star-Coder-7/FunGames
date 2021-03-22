from tkinter import *

compiler = Tk()
compiler.title('THE BEST IDE')

menuBar = Menu(compiler)
runBar = Menu(menuBar)
runBar.add_command(label='Run')
menuBar.add_cascade(label='Run', menu=runBar)
compiler.config(menu=menuBar)

editor = Text()
editor.pack()
compiler.mainloop()