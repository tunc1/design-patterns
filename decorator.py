from abc import ABC

class Pizza:
    
    def __init__(self,name="Pizza",price=4):
        self.name=name
        self.price=price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

class PizzaDecorator(Pizza,ABC):
    
    def __init__(self,pizza,name,price):
        super().__init__(name,price)
        self.pizza=pizza
    
    def get_name(self):
        return self.name+" "+self.pizza.get_name()
    
    def get_price(self):
        return self.price+self.pizza.get_price()

class PizzaWithTomato(PizzaDecorator):
    
    def __init__(self,pizza):
        super().__init__(pizza,"Tomato",2)

class PizzaWithCheese(PizzaDecorator):
    
    def __init__(self,pizza):
        super().__init__(pizza,"Cheese",1)

class PizzaWithKetchup(PizzaDecorator):
    
    def __init__(self,pizza):
        super().__init__(pizza,"Ketchup",0.5)