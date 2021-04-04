from abc import ABC,abstractmethod

class Expression(ABC):

    @abstractmethod
    def interpret(self,context):
        pass

class TerminalExpression(Expression):

    def interpret(self,context):
        return int(context)

class NonTerminalExpression(Expression):

    def interpret(self,context):
        index=context.find("+")
        if index==-1:
            terminal_expression=TerminalExpression()
            return terminal_expression.interpret(context)
        else:
            number=context[:index]
            rest=context[index+1:]
            terminal_expression=TerminalExpression()
            non_terminal_expression=NonTerminalExpression()
            return terminal_expression.interpret(number)+non_terminal_expression.interpret(rest)