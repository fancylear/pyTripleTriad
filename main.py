#!/usr/bin/env python

from Card import Card
from Grid import Grid
from Player import Player

import time
import Tkinter, ImageTk
from PIL import Image

grid = Grid()
gayla = Card(**dict(name='Gayla', color='red',
                    upper=2, lower=4, left=4, right=1))
geezard = Card(**dict(name='Geezard', color='red',
                    upper=2, lower=4, left=4, right=1))

def callback(event):
    y = int(event.widget.grid_info()['column'])
    x = int(event.widget.grid_info()['row'])
    grid.placeCard((x, y), gayla)
    draw()

def draw():
    for y in range(3):
        for x in range(3):
            pos = (y, x)
           
            if grid.getPos(pos):
                card = grid.getPos(pos)
                image = Image.open(card.getImage())
                globals()['p%s%s' % pos ] = ImageTk.PhotoImage(image)
                label = Tkinter.Label(window, image=globals()['p%s%s' % pos ])
                label.grid(row=pos[0], column=pos[1])
            else:
                image = Image.open('images/empty.png')
                globals()['p%s%s' % pos ] = ImageTk.PhotoImage(image)
                label = Tkinter.Label(window, image=globals()['p%s%s' % pos ])
                label.grid(row=pos[0], column=pos[1])
                label.bind("<Button-1>", callback)

grid.placeCard((0, 0), geezard)

window = Tkinter.Tk()
window.title("pyTripleTriad")
draw()
window.mainloop()