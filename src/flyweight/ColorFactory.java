package flyweight;

import java.util.HashMap;
import java.util.Map;

public class ColorFactory
{
    private Map<String,Color> map;
    public ColorFactory()
    {
        map=new HashMap<>();
    }
    public Color create(String color)
    {
        color=color.toLowerCase();
        if(map.containsKey(color))
            return map.get(color);
        else
        {
            if(color.equals("blue"))
            {
                Color blue=new Blue();
                map.put(color, blue);
                return blue;
            }
            else if(color.equals("red"))
            {
                Color red=new Red();
                map.put(color, red);
                return red;
            }
        }
        throw new IllegalArgumentException("Invalid Argument: "+color);
    }
}