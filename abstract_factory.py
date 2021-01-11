from abc import ABC,abstractmethod

class PlayerShip(ABC):
    pass

class EnemyShip(ABC):
    pass

class PlayerWeaponedShip(PlayerShip):
    pass

class PlayerNormalShip(PlayerShip):
    pass

class EnemyWeaponedShip(EnemyShip):
    pass

class EnemyNormalShip(EnemyShip):
    pass

class ShipFactory(ABC):
    
    @abstractmethod
    def create(self,ship_type):
        pass

class PlayerShipFactory(ShipFactory):
    
    def create(self,ship_type):
        if ship_type=="normal":
            return PlayerNormalShip()
        elif ship_type=="weaponed":
            return PlayerWeaponedShip()
        return None

class EnemyShipFactory(ShipFactory):
    
    def create(self,ship_type):
        if ship_type=="normal":
            return EnemyNormalShip()
        elif ship_type=="weaponed":
            return EnemyWeaponedShip()
        return None