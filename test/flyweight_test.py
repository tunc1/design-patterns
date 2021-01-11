from unittest import TestCase
from flyweight import *

class FlyweightTest(TestCase):
    
    def test_flyweight(self):
        factory=ScreenFactory()
        tv=TV(factory.create("lcd"))
        tv1=TV(factory.create("lcd"))
        tv2=TV(factory.create("led"))
        tv3=TV(factory.create("led"))
        self.assertEqual(type(tv.screen),LCDScreen)
        self.assertEqual(type(tv2.screen),LEDScreen)
        self.assertEqual(tv.screen,tv1.screen)
        self.assertEqual(tv2.screen,tv3.screen)