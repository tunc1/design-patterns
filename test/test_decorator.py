from unittest import TestCase
from decorator import *

class DecoratorTest(TestCase):
    
    def setUp(self):
        self.pizza=PizzaWithKetchup(PizzaWithTomato(PizzaWithCheese(Pizza())))

    def test_name(self):
        self.assertEqual(self.pizza.get_name(),"Ketchup Tomato Cheese Pizza")

    def test_price(self):
        self.assertEqual(self.pizza.get_price(),7.5)