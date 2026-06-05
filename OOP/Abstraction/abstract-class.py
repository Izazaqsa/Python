# abstract class are those classes which contain of the abstract functions 
from abc import ABC , abstractmethod

class Vichels :
    def __init__(self,tyres):
        self.no_of_tyres = tyres 

    @abstractmethod        # this makes the class a abstract class if class does not contain of this class then it wont be abstract class
    def start (self):
        pass


class Cars (Vichels):
    def __init__(self,name,tyres):
        Vichels.__init__(self,tyres)
        self.model_name = name

    def start (self):       # if you inherit the abstract class and dont define the abstract method of that class than the subclass will itself abstract
        print ('start with the switching of the key')   # class and no object of this will be create so you must define the abstractmethod in the subclass


class Bikes (Vichels):
    def __init__(self, tyres,color):
        super().__init__(tyres)
        self.color = color 

    def start (self):
        print ('start the bike with kicking ')

bike1 = Bikes(2,'black')
bike1.start()
print (bike1.no_of_tyres)
print (bike1.color)

car1 = Cars ('supra',4)
car1.start()
print(car1.model_name)