from unittest import TestCase
from mediator import *

class AbstractFactoryTest(TestCase):
    
    def test_can_land(self):
        plane=Plane()
        runway=Runway()
        mediator=Mediator(plane,runway)
        runway.is_empty=True
        self.assertTrue(plane.land())
        runway.is_empty=False
        self.assertFalse(plane.land())