from abc import ABC,abstractmethod

class Shape(ABC):
    
    def __init__(self,color):
        self.color=color
    
    @abstractmethod
    def define(self):
        pass

class Triangle(Shape):
    
    def define(self):
        return self.color.define()+" Triangle"

class Square(Shape):
    
    def define(self):
        return self.color.define()+" Square"

class Color(ABC):
    
    @abstractmethod
    def define(self):
        pass

class Blue(Color):
    
    def define(self):
        return "Blue"

class Red(Color):
    
    def define(self):
        return "Red"