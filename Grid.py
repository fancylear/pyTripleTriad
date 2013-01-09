
class Grid(object):
    
    def __init__(self):
        self.grid = dict([ (str(i), None) for i in range(9) ])
        
    def placeCard(self, pos, Card):
        if self.__validPos(pos):
            if not self.grid.get(str(pos)):
                self.grid[str(pos)] = Card
            else:
                raise Exception('Position not empty')
        
    def getPos(self, pos):
        if self.__validPos(pos):
           return self.grid.get(str(pos))
        else:
            raise Exception('Not a valid position')
        
    def __validPos(self, pos):
        if self.grid.has_key(str(pos)):
            return True
        else:
            return False