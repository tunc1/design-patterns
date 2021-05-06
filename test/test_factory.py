import unittest
from factory import *

class FactoryTest(unittest.TestCase):
    
    def test_create(self,):
        factory=MouseFactory()
        mouse=factory.create("wired")
        self.assertEqual(type(mouse),WiredMouse)
        mouse=factory.create("wireless")
        self.assertEqual(type(mouse),WirelessMouse)
        mouse=factory.create("mouse")
        self.assertIsNone(mouse)