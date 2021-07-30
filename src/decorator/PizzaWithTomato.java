package decorator;

public class PizzaWithTomato extends PizzaDecorator
{
    public PizzaWithTomato(Pizza decorate)
    {
        super(2, "Tomato", decorate);
    }
}