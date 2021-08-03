package interpreter;

public class Parser
{
    public Expression parse(String expression)
    {
        if(expression.contains("+"))
        {
            int leftIndex=expression.indexOf("+");
            String left=expression.substring(0,leftIndex);
            Expression leftExpression=new TerminalExpression(Double.parseDouble(left));
            String right=expression.substring(leftIndex+1);
            return new NonTerminalExpression(leftExpression,parse(right));
        }
        else
            return new TerminalExpression(Double.parseDouble(expression));
    }
}