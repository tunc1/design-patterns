package factory;

public class PhoneFactory
{
    public Phone create(String type)
    {
        if(type.equalsIgnoreCase("iphone"))
            return new iPhone();
        else if(type.equalsIgnoreCase("android"))
            return new AndroidPhone();
        throw new IllegalArgumentException("Invalid Argument: "+type);
    }
}