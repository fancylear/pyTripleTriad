
class Card(object):
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.upper = kwargs.get('upper')
        self.lower = kwargs.get('lower')
        self.left = kwargs.get('left')
        self.right = kwargs.get('right')
        self.color = kwargs.get('color')
        
    def __str__(self):
        return self.name
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
        
    def upperPower(self):
        return self.upper
    
    def lowerPower(self):
        return self.lower

    def leftPower(self):
        return self.left
    
    def rightPower(self):
        return self.right
    
    