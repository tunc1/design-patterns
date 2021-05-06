from unittest import TestCase
from abstract_factory import *

class WeaponedShipFactoryTest(TestCase):

    def setUp(self):
        self.factory=WeaponedShipFactory()

    def test_create_player_ship(self):
        self.assertEqual(type(self.factory.create_player_ship()),PlayerWeaponedShip)

    def test_create_enemy_ship(self):
        self.assertEqual(type(self.factory.create_enemy_ship()),EnemyWeaponedShip)

class NormalShipFactoryTest(TestCase):

    def setUp(self):
        self.factory=NormalShipFactory()

    def test_create_player_ship(self):
        self.assertEqual(type(self.factory.create_player_ship()),PlayerNormalShip)

    def test_create_enemy_ship(self):
        self.assertEqual(type(self.factory.create_enemy_ship()),EnemyNormalShip)