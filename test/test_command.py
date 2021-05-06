from unittest import TestCase
from command import TV,Remote

class CommandTest(TestCase):
    
    def setUp(self):
        self.tv=TV()
        self.remote=Remote(self.tv)

    def test_turn_on(self):
        self.tv.is_on=False
        self.remote.turn_on()
        self.assertTrue(self.tv.is_on)

    def test_turn_off(self):
        self.tv.is_on=True
        self.remote.turn_off()
        self.assertFalse(self.tv.is_on)