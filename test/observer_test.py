import unittest
from observer import Observable,Observer

class ObserverTest(unittest.TestCase):
    
    def test_update(self):
        observable=Observable()
        observer=Observer(1)
        observable.addObserver(observer)
        observable.updateObservers(2)
        self.assertEqual(observer.data,2)