package prototype;

public class MySQLDatabaseConnection extends DatabaseConnection
{
    public void connect()
    {
        System.out.println("Connecting to MySQL Database");
    }
    public void disconnect()
    {
        System.out.println("Disconnecting from MySQL Database");
    }
}