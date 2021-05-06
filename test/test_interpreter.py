from unittest import TestCase
from interpreter import NonTerminalExpression

class InterpreterTest(TestCase):
    
    def test_interpret(self):
        expression=NonTerminalExpression()
        self.assertEqual(expression.interpret("3+1+5+2"),11)