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

grid.placeCard((0, 0), gayla)
grid.placeCard((1, 1), geezard)
grid.placeCard((2, 2), geezard)

window = Tkinter.Tk()
frame = Tkinter.Frame(window, width=279, height=360)
frame.pack(fill=None, expand=False)

for y in range(3):
    for x in range(3):
        pos = (y, x)
       
        if grid.getPos(pos):
            card = grid.getPos(pos)
            image = Image.open(card.getImage())
            globals()['p%s%s' % pos ] = ImageTk.PhotoImage(image)
            label = Tkinter.Label(frame, image=globals()['p%s%s' % pos ])
            label.place(x=pos[0] * 93, y=pos[1] * 120, width=93, height=120)

        
window.mainloop()