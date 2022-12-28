import asyncio
import time
from random import randint
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
        time.sleep(0.0001)
        x_coord = x_coord - 10
        if x_coord == -1200:
            x_coord = 0
        x_coord_2 = x_coord_2 - 10
        if x_coord_2 == 0:
            x_coord_2 = 1200
        floor.place(x=x_coord, y=450)
        floor_2.place(x=x_coord_2, y=450)


gameFloor = Thread(target=start_floor)
gameFloor.start()


def getObstacle():
    size = randint(0, 1)
    cacti = randint(1, 3)
    if size == 0:
        cacti_image = Image.open((os.getcwd() + f'/assets/small-{cacti}.png'))
    else:
        cacti_image = Image.open((os.getcwd() + f'/assets/large-{cacti}.png'))

    cacti_image = ImageTk.PhotoImage(cacti_image)
    cacti = Label(gameCanvas, image=cacti_image)
    cacti.image = cacti_image
    if size == 0:
        cacti.place(x=1100, y=390)
    else:
        cacti.place(x=1100, y=375)

    return cacti


def generate_obstacle():
    counter = 100
    cacti = []
    x_coords = []
    while True:
        if counter == 100:
            counter = 0
            cacti.append(getObstacle())
            x_coords.append(1100)

        for i, value in enumerate(cacti):
            x_coords[i] = x_coords[i]-10
            cacti[i].place(x=x_coords[i])
        counter = counter + 1
        time.sleep(0.0001)


gameObstacle = Thread(target=generate_obstacle)
gameObstacle.start()


def run_dino():
    global dino
    num = 0
    while True:
        time.sleep(0.1)
        num = (num + 1) % 2
        #dino_image = dino_image.resize((44, 47), Image.ANTIALIAS)
        dino_image = ImageTk.PhotoImage(file=(os.getcwd() + f'/assets/run-{str(num+1)}.png'))
        dino = Label(gameCanvas, image=dino_image)
        dino.image = dino_image
        dino.place(x=50, y=360)


runDino = Thread(target=run_dino)
runDino.start()

gameWindow.mainloop()
