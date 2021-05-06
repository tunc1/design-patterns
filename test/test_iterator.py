import unittest
from iterator import List

class IteratorTest(unittest.TestCase):
    
    def test_iterator(self):
        list=List()
        list.add(1)
        list.add(3)
        list.add(2)
        for index,item in enumerate(list):
            self.assertEqual(list.get(index),item)