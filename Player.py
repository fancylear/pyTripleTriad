
class Player(object):
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.color = kwargs.get('color')
        
    def __str__(self):
        return self.name
    
    def getColor(self):
        return self.color