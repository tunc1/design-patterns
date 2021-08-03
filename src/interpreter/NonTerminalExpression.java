package interpreter;

public class NonTerminalExpression extends Expression
{
    private Expression leftExpression,rightExpression;
    public NonTerminalExpression(Expression leftExpression, Expression rightExpression)
    {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
    }
    public double interpret()
    {
        return leftExpression.interpret()+rightExpression.interpret();
    }
}