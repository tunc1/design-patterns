package prototype;

public class PostgresDatabaseConnection extends DatabaseConnection
{
    public void connect()
    {
        System.out.println("Connecting to Postgres Database");
    }
    public void disconnect()
    {
        System.out.println("Disconnecting from Postgres Database");
    }
}