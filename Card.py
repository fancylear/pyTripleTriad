
class Card(object):
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name').title()
        self.upper = kwargs.get('upper')
        self.lower = kwargs.get('lower')
        self.left = kwargs.get('left')
        self.right = kwargs.get('right')
        self.color = kwargs.get('color')
        self.image = 'images/%s.png' % self.name
        
    def __str__(self):
        # Pretty string rep
        return self.name
    
    def getImage(self):
        '''Get a Image for a Card object'''
        return self.image
    
    def setColor(self, color):
        '''Set a Color for a Card object'''
        self.color = color
        
    def getColor(self):
        '''Get a Color for a Card object'''
        return self.color
        
    def upperPower(self):
        '''Get a Power for a Card object'''
        return self.upper
    
    def lowerPower(self):
        '''Get a Power for a Card object'''
        return self.lower

    def leftPower(self):
        '''Get a Power for a Card object'''
        return self.left
    
    def rightPower(self):
        '''Get a Power for a Card object'''
        return self.right
    
    