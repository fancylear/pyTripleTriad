from collections import Counter

class Grid(object):
    
    def __init__(self):
        # create a dict of x, y tuples for (0, 0) -> (2, 2)
        self.grid = dict([ ((x, y), None) for x in range(3) for y in range(3) ])
        
    def __validPos(self, pos):
        '''Validate a tuple position is valid'''
        if self.grid.has_key(pos):
            return True
        else:
            return False
        
    def __emptyPos(self, pos):
        '''See if tuple position is empty'''
        if self.__validPos(pos):
            if not self.grid.get(pos):
                return True
            else:
                return False
            
    def getPos(self, pos):
        '''Get the Card inside a position'''
        if self.__validPos(pos):
            return self.grid.get(pos)
    
    def __setPos(self, pos, Card):
        '''Set a Card to a position'''
        self.grid[pos] = Card
        
                
    def placeCard(self, pos, Card):
        '''Place a Card object in a position'''
        if self.__validPos(pos):
            if self.__emptyPos(pos):
                self.__setPos(pos, Card)