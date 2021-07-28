package abstractfactory;

public class FactoryProvider
{
    public ShipFactory provide(String type)
    {
        if(type.equalsIgnoreCase("missile"))
            return new ShipWithMissileFactory();
        else if(type.equalsIgnoreCase("lazer"))
            return new ShipWithLazerFactory();
        throw new IllegalArgumentException("Invalid Argument: "+type);
    }
}