import unittest
from chain_of_responsibility import SubtractChain,SumChain

class ChainOfResponsibilityTest(unittest.TestCase):
    
    def test_do(self):
        chain=SubtractChain(SumChain())
        self.assertEqual(chain.do(3,4,"-"),-1)
        self.assertEqual(chain.do(1,5,"+"),6)
        self.assertRaises(RuntimeError,chain.do,7,9,"*")