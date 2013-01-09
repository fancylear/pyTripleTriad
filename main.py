#!/usr/bin/env python

from Card import Card
from Grid import Grid

grid = Grid()
gayla = Card(**dict(upper=2, lower=4, left=4, right=1))

grid.placeCard(0, gayla)
print grid.grid

for x in range(3):
    print grid.getPos(x),
print ''
for x in range(3, 6):
    print grid.getPos(x),
print ''
for x in range(6, 9):
    print grid.getPos(x),
print ''