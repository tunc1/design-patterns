package command;

public class Radio implements Device
{
    private boolean isOn;
    public void turnOn()
    {
        isOn=true;
    }
    public void turnOff()
    {
        isOn=false;
    }
    public boolean isOn()
    {
        return isOn;
    }
}