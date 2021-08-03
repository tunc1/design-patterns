package chain_of_responsibility;

public class SubtractChain extends Chain
{
    public SubtractChain(){}
    public SubtractChain(Chain next)
    {
        super(next);
    }
    public double doAction(double number1, double number2, String operation)
    {
        if(operation=="-")
            return number1-number2;
        else
            return next(number1, number2, operation);
    }
}