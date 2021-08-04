package visitor;

public class Product
{
    private double euroPrice;
    public double getEuroPrice()
    {
        return euroPrice;
    }
    public void setEuroPrice(double euroPrice)
    {
        this.euroPrice=euroPrice;
    }
    public double visit(ProductVisitor visitor)
    {
        return visitor.visit(this);
    }
}