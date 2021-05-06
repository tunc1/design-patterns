from unittest import TestCase
from bridge import Blue,Red,Square,Triangle

class SquareTest(TestCase):
    
    def test_define(self):
        square=Square(Blue())
        self.assertEqual(square.define(),"Blue Square")
        square=Square(Red())
        self.assertEqual(square.define(),"Red Square")

class TriangleTest(TestCase):
    
    def test_define(self):
        triangle=Triangle(Blue())
        self.assertEqual(triangle.define(),"Blue Triangle")
        triangle=Triangle(Red())
        self.assertEqual(triangle.define(),"Red Triangle")