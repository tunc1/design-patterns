package state;

public class Phone
{
    private State state;
    public void turnOnWifi()
    {
        state=new WifiTurnedOnState();
    }
    public void turnOffWifi()
    {
        state=new WifiTurnedOffState();
    }
    public boolean canConnect()
    {
        return state.canConnect();
    }
}