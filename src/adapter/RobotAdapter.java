package adapter;

public class RobotAdapter extends Person
{
    private Robot robot;
    public RobotAdapter(Robot robot)
    {
        this.robot=robot;
    }
    public String sayHello()
    {
        return robot.makeNoise();
    }
}