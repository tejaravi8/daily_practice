from abstract import vehicle

class car(vehicle):
    def start(self):
        print('t')
    
    def wheels(self,n):
        print(f"car has wheels{n}")
    
c=car()
c.start()
c.wheels(4)