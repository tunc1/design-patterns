from unittest import TestCase
from interpreter import NonTerminalExpression

class InterpreterTest(TestCase):
    
    def test_interpret(self):
        expression=NonTerminalExpression("-4+3*2-1+25/5-2+1*5-3/3+4/2*2")
        self.assertEqual(expression.interpret(),12)