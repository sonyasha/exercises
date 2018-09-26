from math import sqrt

class Rocket():
    '''Define a Rocket object'''
    
    def __init__(self, name, cap, x=0, y=0):
        self.x = x
        self.y = y
        self.name = name
        self.cap = cap
    
    def moving(self, x_move=0, y_move=1):
        self.x += x_move
        self.y += y_move   
    def distance(self, other_rocket):
        dist = sqrt((self.x-other_rocket.x)**2 + (self.y-other_rocket.y)**2)
        return round(int(dist))
    def launch(self):
        return f'captain {self.cap} starts launching of rocket {self.name}'
    def landing(self):
        print(f'before: rocket x: {self.x}, y: {self.y}')
        self.x = 0
        self.y = 0
        print(f'after: rocket x: {self.x}, y: {self.y}')
        
    def secure_check(self, other_rocket):
        if self.distance(other_rocket) == 0:
            return f'Rockets crashed!!'
        elif self.distance(other_rocket) < 5:
            return f'Alarm! Too close'
        else:
            return f'All good!'
    
class Shuttle(Rocket):
    '''Define a Shuttle object with parent class - Rocket'''
    def __init__(self, name, cap, x=0, y=0, flights = 0):
        super().__init__(name, cap, x,y)
        self.flights = flights