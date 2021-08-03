package chain_of_responsibility;

public abstract class Chain
{
    private Chain next;
    public Chain(){}
    public Chain(Chain next)
    {
        this.next = next;
    }
    public abstract double doAction(double number1,double number2,String operation);
    public double next(double number1,double number2,String operation)
    {
        if(next!=null)
            return next.doAction(number1, number2, operation);
        else
            throw new IllegalArgumentException("Unsupported operation:"+operation);
    }
}