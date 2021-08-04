package visitor;

public class ProductDollarVisitor implements ProductVisitor
{
    public double visit(Product product)
    {
        return product.getEuroPrice()*0.8;
    }
}