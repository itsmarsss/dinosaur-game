import asyncio
import time
from threading import Thread
from tkinter import *
from PIL import ImageTk, Image
import os

high_score = 0
curr_score = 0
gameWindow = Tk()
playerImage = Image.open((os.getcwd() + '/assets/allsprites.png'))
playerImage = playerImage.resize((50, 50), Image.ANTIALIAS)
playerImage = ImageTk.PhotoImage(playerImage)


# player = Label(gameWindow, image=playerImage)

# player.image = playerImage
# player.pack()


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


def running_icon():
    num = 0
    while True:
        gameWindow.iconphoto(False, PhotoImage(file=(os.getcwd() + f'/assets/run-{str(num + 1)}.png')))
        time.sleep(0.1)
        num = (num + 1) % 2


anim_icon = Thread(target=running_icon)
anim_icon.start()

gameWindow.title('Dinosaur Game')
gameWindow.bind('<KeyPress>', on_key_press)
gameWindow.geometry('1200x500')
gameWindow.minsize(1200, 500)
gameWindow.maxsize(1200, 500)

gameCanvas = Canvas(gameWindow, width=1200, height=500)

gameCanvas.pack()


def start_counter():
    while True:
        global curr_score
        score_text = Label(gameCanvas, anchor='ne', text=f"HI {str(high_score).zfill(6)}  {str(curr_score).zfill(6)}",
                           font='System 15 bold')
        score_text.place(relx=1, rely=0.0, anchor='ne')
        curr_score = curr_score + 1
        time.sleep(0.1)


gameCounter = Thread(target=start_counter)
gameCounter.start()


def start_floor():
    x_coord = 0
    floor_image = Image.open((os.getcwd() + '/assets/ground.png'))
    floor_image = floor_image.resize((1200, 12), Image.ANTIALIAS)
    floor_image = ImageTk.PhotoImage(floor_image)
    floor = Label(gameCanvas, image=floor_image)
    floor.image = floor_image
    floor.place(x=x_coord, y=450)

    x_coord_2 = 1200
    floor_image_2 = Image.open((os.getcwd() + '/assets/ground.png'))
    floor_image_2 = floor_image_2.resize((1200, 12), Image.ANTIALIAS)
    floor_image_2 = ImageTk.PhotoImage(floor_image_2)
    floor_2 = Label(gameCanvas, image=floor_image_2)
    floor_2.image = floor_image_2
    floor_2.place(x=x_coord_2, y=450)
    while True:
        asyncio.sleep(0.001)
        x_coord = x_coord - 1
        if x_coord == -1200:
            x_coord = 0
        x_coord_2 = x_coord_2 - 1
        if x_coord_2 == 0:
            x_coord_2 = 1200
        floor.place(x=x_coord, y=450)
        floor_2.place(x=x_coord_2, y=450)


gameFloor = Thread(target=start_floor)
gameFloor.start()

gameWindow.mainloop()
