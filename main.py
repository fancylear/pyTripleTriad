#!/usr/bin/env python

from Card import Card
from Grid import Grid
from Player import Player

grid = Grid()
me = Player(**dict(name='Jeff', color='blue'))
oppt = Player(**dict(name='Bob', color='red'))

my_gayla = Card(**dict(name='gayla', color=me.getColor(),
                    upper=2, lower=4, left=4, right=1))
my_geezard = Card(**dict(name='geezard', color=me.getColor(),
                      upper=1, lower=1, left=5, right=4))

oppt_gayla = Card(**dict(name='gayla', color=oppt.getColor(),
                    upper=2, lower=4, left=4, right=1))
oppt_geezard = Card(**dict(name='geezard', color=oppt.getColor(),
                      upper=1, lower=1, left=5, right=4))

grid.placeCard(0, my_gayla)
grid.placeCard(1, oppt_geezard)
grid.placeCard(4, my_geezard)
grid.placeCard(3, oppt_gayla)

print grid.getScore()