from abc import ABC,abstractmethod

class Weapon(ABC):
    
    @abstractmethod
    def attack(self):
        pass

class Player:
    
    def __init__(self,weapon):
        self.weapon=weapon
    
    def attack(self):
        return self.weapon.attack()

class Knife(Weapon):
    
    def attack(self):
        return "Attacked with knife"

class Sword(Weapon):
    
    def attack(self):
        return "Attacked with sword"