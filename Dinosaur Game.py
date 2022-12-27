from tkinter import *


def dinoJump():
    pass


def dinoDuch():
    pass


def onKeyPress(event):
    key = event.keysym
    if key == 'Up':
        dinoJump()
    elif key == 'Down':
        dinoDuch()

gameWindow = Tk()
gameWindow.title('Dinosaur Game')
gameWindow.bind('<KeyPress>', onKeyPress)

gameWindow.mainloop()
