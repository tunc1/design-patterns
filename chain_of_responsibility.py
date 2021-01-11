from abc import ABC,abstractmethod 

class Chain(ABC):
    
    def __init__(self,next=None):
        self.next=next
    
    @abstractmethod
    def do(self,number1,number2,operation):
        pass

class SumChain(Chain):
    
    def do(self,number1,number2,operation):
        if operation=="+":
            return float(number1)+float(number2)
        elif self.next!=None:
            return self.next.do(number1,number2,operation)
        else:
            raise RuntimeError

class SubtractChain(Chain):
    
    def do(self,number1,number2,operation):
        if operation=="-":
            return float(number1)-float(number2)
        elif self.next!=None:
            return self.next.do(number1,number2,operation)
        else:
            raise RuntimeError