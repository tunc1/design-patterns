package decorator;

public abstract class Pizza
{
    private double price;
    private String name;
    public Pizza(double price, String name)
    {
        this.price=price;
        this.name=name;
    }
    public double getPrice()
    {
        return price;
    }
    public void setPrice(double price)
    {
        this.price=price;
    }
    public String getName()
    {
        return name;
    }
    public void setName(String name)
    {
        this.name=name;
    }
}