import unittest
from strategy import *

class StrategyTest(unittest.TestCase):

    def test_attack(self):
        player=Player(Knife())
        self.assertEqual(player.attack(),"Attacked with knife")
        player.weapon=Sword()
        self.assertEqual(player.attack(),"Attacked with sword")