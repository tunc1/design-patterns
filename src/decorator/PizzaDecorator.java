package decorator;

public abstract class PizzaDecorator extends Pizza
{
    protected Pizza decorate;
    public PizzaDecorator(double price, String name,Pizza decorate)
    {
        super(price, name);
        this.decorate=decorate;
    }
    public double getPrice()
    {
        return super.getPrice()+decorate.getPrice();
    }
    public String getName()
    {
        return decorate.getName()+" "+super.getName();
    }
}