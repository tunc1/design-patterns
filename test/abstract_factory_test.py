from unittest import TestCase
from abstract_factory import *

class PlayerShipFactoryTest(TestCase):
    
    def test_create(self):
        factory=PlayerShipFactory()
        self.assertEqual(type(factory.create("normal")),PlayerNormalShip)
        self.assertEqual(type(factory.create("weaponed")),PlayerWeaponedShip)

class EnemyShipFactoryTest(TestCase):
    
    def test_create(self):
        factory=EnemyShipFactory()
        self.assertEqual(type(factory.create("normal")),EnemyNormalShip)
        self.assertEqual(type(factory.create("weaponed")),EnemyWeaponedShip)