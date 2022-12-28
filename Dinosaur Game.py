from tkinter import *
from PIL import ImageTk, Image
import os

gameWindow = Tk()
playerImage = Image.open((os.getcwd() + '/assets/allsprites.png'))
playerImage = playerImage.resize((50, 50), Image.ANTIALIAS)
playerImage = ImageTk.PhotoImage(playerImage)
player = Label(gameWindow, image=playerImage)

player.image = playerImage
player.pack()


async def dino_jump():
    pass


async def dino_duck():
    pass


async def generate_obstacle():
    pass


def on_key_press(event):
    key = event.keysym
    if key == 'Up':
        dino_jump()
    elif key == 'Down':
        dino_duck()


gameWindow.title('Dinosaur Game')
gameWindow.bind('<KeyPress>', on_key_press)
gameWindow.geometry('1200x500')
gameWindow.minsize(1200, 500)
gameWindow.maxsize(1200, 500)

gameWindow.mainloop()
