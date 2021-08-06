package command;

public class TurnOnCommand implements Command
{
    private final Device device;
    public TurnOnCommand(Device device)
    {
        this.device=device;
    }
    public void execute()
    {
        device.turnOn();
    }
}