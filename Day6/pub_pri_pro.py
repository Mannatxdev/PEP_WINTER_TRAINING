# Public Class 
class car():
    def __init__(self,windows,doors,enginetype):
        self.windows= windows
        self.doors= doors
        self.enginetype= enginetype

c = car(4, 4, "Petrol")
print(c.windows)   

# Protected
class car():
    def __init__(self,windows,doors,enginetype):
        self._windows= windows
        self._doors= doors
        self._enginetype= enginetype

class Truck(car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower

# Private
class Car:
    def __init__(self, windows, doors, enginetype):
        self.__engine = enginetype

c = Car(4,4,"Diesel")
print(c._Car__engine) 

