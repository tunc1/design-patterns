package prototype;

public abstract class DatabaseConnection implements Cloneable
{
    public abstract void connect();
    public abstract void disconnect();
    public DatabaseConnection clone()
    {
        try
        {
            return (DatabaseConnection)super.clone();
        } 
        catch (CloneNotSupportedException e)
        {
            return null;
        }
    }
}