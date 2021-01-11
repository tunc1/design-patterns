from unittest import TestCase
from state import *

class AbstractFactoryTest(TestCase):
    
    def test_can_connect(self):
        phone=CellPhone(WifiTurnedOnState())
        self.assertTrue(phone.can_connect())
        phone.wifi_state=WifiTurnedOffState()
        self.assertFalse(phone.can_connect())