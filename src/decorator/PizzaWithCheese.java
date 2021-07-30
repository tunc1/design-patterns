package decorator;

public class PizzaWithCheese extends PizzaDecorator
{
    public PizzaWithCheese(Pizza decorate)
    {
        super(3, "Cheese", decorate);
    }
}