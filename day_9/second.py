from abstraction import vehicle

class car(vehicle):
    def start(self):
        print('vehicle is started')
        
    def wheels(self):
        print('car has 4 wheels')
        
car()