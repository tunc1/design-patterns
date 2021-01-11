from abc import ABC,abstractmethod

class Expression(ABC):

    @abstractmethod
    def interpret(self,context):
        pass

    def __init__(self,context,symbol):
        index=context.index(symbol)
        self.left_expression=NonTerminalExpression(context[:index])
        self.right_expression=NonTerminalExpression(context[index+1:])

class NumberExpression(Expression):
    
    def __init__(self,context):
        self.context=context

    def interpret(self):
        return int(self.context)

class MultiplyExpression(Expression):
    
    def __init__(self,context):
        super().__init__(context,"*")

    def interpret(self):
        return self.left_expression.interpret()*self.right_expression.interpret()

class PlusExpression(Expression):
    
    def __init__(self,context):
        super().__init__(context,"+")

    def interpret(self):
        return self.left_expression.interpret()+self.right_expression.interpret()

class DivideExpression(Expression):
    
    def __init__(self,context):
        super().__init__(context,"/")

    def interpret(self):
        return self.left_expression.interpret()/self.right_expression.interpret()

class MinusExpression(Expression):
    
    def __init__(self,context):
        index=context[1:].index("-")+1
        self.left_expression=NonTerminalExpression(context[:index])
        self.right_expression=NonTerminalExpression("-"+context[index+1:])

    def interpret(self):
        return self.left_expression.interpret()+self.right_expression.interpret()

class NonTerminalExpression(Expression):

    def __init__(self,context):
        self.context=context

    def interpret(self):
        symbol=self.get_first_symbol()
        if "+"==symbol:
            return PlusExpression(self.context).interpret()
        elif "-"==symbol:
            return MinusExpression(self.context).interpret()
        elif "/"==symbol:
            return DivideExpression(self.context).interpret()
        elif "*"==symbol:
            return MultiplyExpression(self.context).interpret()
        else:
            return NumberExpression(self.context).interpret()
    
    def get_first_symbol(self):
        for i,char in enumerate(self.context):
            if char=="+" or char=="-":
                if i!=0:
                    return char
        for char in self.context:
            if char=="*":
                return char
        for char in self.context:
            if char=="/":
                return char