import unittest
from singleton import Singleton

class TestSingleton(unittest.TestCase):
    def test_new(self):
        self.assertRaises(RuntimeError,Singleton.__new__,Singleton)
    
    def test_instance(self):
        singleton1=Singleton.instance()
        singleton2=Singleton.instance()
        self.assertEqual(id(singleton1),id(singleton2))