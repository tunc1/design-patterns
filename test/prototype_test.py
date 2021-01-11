from unittest import TestCase
from prototype import Prototype

class PrototypeTest(TestCase):
    
    def test_clone(self):
        object1=Prototype("object")
        object2=object1.clone()
        self.assertEqual(object1.name,object2.name)
        self.assertNotEqual(id(object1),id(object2))