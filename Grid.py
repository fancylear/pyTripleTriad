from collections import Counter

class Grid(object):
    
    def __init__(self):
        self.grid = dict([ (str(i), None) for i in range(9) ])
        
    def __validPos(self, pos):
        if self.grid.has_key(str(pos)):
            return True
        else:
            return False
        
    def __emptyPos(self, pos):
        if self.__validPos(pos):
            if not self.grid.get(str(pos)):
                return True
            else:
                return False
            
    def __getPos(self, pos):
        return self.grid.get(str(pos))
    
    def __setPos(self, pos, Card):
        self.grid[str(pos)] = Card
        
    def __combatZones(self, pos):
        '''Get all position our position will combat in'''
        if self.__validPos(pos):
            zones = {}
            for p in [('upper', '- 3'), ('lower', '+ 3'),
                      ('right', '+ 1'), ('left', '- 1')]:
                position = eval('%s %s' % (pos, p[1]))
                if self.__validPos(position):
                    zones[p[0]] = position
        return zones
    
    def __combatSetup(self, pos, Card):
        zones = self.__combatZones(pos)
        for zone in zones:
            if not self.__emptyPos(zones[zone]):
                Defender = self.__getPos(zones[zone])
                apower = getattr(Card, '%sPower' % zone)()
                if zone == 'left':
                    dpower = getattr(Defender, 'rightPower')()
                elif zone == 'right':
                    dpower = getattr(Defender, 'leftPower')()
                elif zone == 'upper':
                    dpower = getattr(Defender, 'lowerPower')()
                elif zone == 'lower':
                    dpower = getattr(Defender, 'upperPower')()
                self.__attack(Card, apower, Defender, dpower)
                
    def __attack(self, Attacker, apower, Defender, dpower):
        if apower >= dpower:
            Defender.setColor(Attacker.getColor())
            
    def getScore(self):
        '''Get the current score'''
        score = []
        for spot in self.grid:
            if not self.__emptyPos(spot):
                card = self.__getPos(spot)
                score.append(card.getColor())
        return Counter(score)
                
    def placeCard(self, pos, Card):
        '''Place a Card object in a position'''
        if self.__validPos(pos):
            if self.__emptyPos(pos):
                self.__setPos(pos, Card)
                self.__combatSetup(pos, Card)