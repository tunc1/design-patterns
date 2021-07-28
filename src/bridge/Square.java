package bridge;

public class Square extends Shape
{
    public Square(Color color)
    {
        super(color);
    }
    public String define()
    {
        return color.define()+" Square";
    }
}