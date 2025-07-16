from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def wheels(self,no):
        pass

