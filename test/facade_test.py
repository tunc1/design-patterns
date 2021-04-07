from unittest import TestCase
from facade import Computer

class ComputerTest(TestCase):

    def test_turn_on(self):
        computer=Computer()
        computer.turn_on()
        self.assertTrue(computer.cpu.has_electricity)
        self.assertTrue(computer.hdd.is_turning)