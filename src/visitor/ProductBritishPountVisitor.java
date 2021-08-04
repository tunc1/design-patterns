package visitor;

public class ProductBritishPountVisitor implements ProductVisitor
{
    public double visit(Product product)
    {
        return product.getEuroPrice()*1.2;
    }
}