package interpreter;

public class TerminalExpression extends Expression
{
    private double data;
    public TerminalExpression(double data)
    {
        this.data=data;
    }
    public double interpret()
    {
        return data;
    }
}