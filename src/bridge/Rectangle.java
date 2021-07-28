package bridge;

public class Rectangle extends Shape
{
    public Rectangle(Color color)
    {
        super(color);
    }
    public String define()
    {
        return color.define()+" Rectangle";
    }
}