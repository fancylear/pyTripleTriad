
class Card(object):
    
    def __init__(self, **kwargs):
        
        self.upper = kwargs.get('upper', None)
        self.lower = kwargs.get('lower', None)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        self.image = None
        
    def getUpperPower(self):
        return self.upper
    
    def getLowerPower(self):
        return self.lower

    def getLeftPower(self):
        return self.left
    
    def getRightPower(self):
        return self.right
    
    