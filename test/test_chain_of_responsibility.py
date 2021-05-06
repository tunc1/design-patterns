import unittest
from chain_of_responsibility import SubtractChain,SumChain

class SubtractChainTest(unittest.TestCase):

    def test_do(self):
        chain=SubtractChain()
        self.assertEqual(chain.do(3,4,"-"),-1)

class SumChainTest(unittest.TestCase):

    def test_do(self):
        chain=SumChain()
        self.assertEqual(chain.do(6,1,"+"),7)

class ChainOfResponsibilityTest(unittest.TestCase):
    
    def test_do(self):
        chain=SubtractChain(SumChain())
        self.assertEqual(chain.do(3,4,"-"),-1)
        self.assertEqual(chain.do(1,5,"+"),6)
        self.assertRaises(RuntimeError,chain.do,7,9,"*")