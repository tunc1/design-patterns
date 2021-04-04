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
    def create_player_ship(self):
        pass

    @abstractmethod
    def create_enemy_ship(self):
        pass

class WeaponedShipFactory(ShipFactory):

    def create_player_ship(self):
        return PlayerWeaponedShip()

    def create_enemy_ship(self):
        return EnemyWeaponedShip()

class NormalShipFactory(ShipFactory):

    def create_player_ship(self):
        return PlayerNormalShip()

    def create_enemy_ship(self):
        return EnemyNormalShip()