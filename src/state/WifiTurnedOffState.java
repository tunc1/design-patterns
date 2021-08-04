package state;

public class WifiTurnedOffState extends State
{
    public boolean canConnect()
    {
        return false;
    }
}