package prototype;

import java.util.HashMap;
import java.util.Map;

public class DatabaseConnectionFactory
{
    private Map<String,DatabaseConnection> map;
    public DatabaseConnectionFactory()
    {
        map=new HashMap<>();
    }
    public DatabaseConnection create(String type)
    {
        type=type.toLowerCase();
        if(map.containsKey(type))
            return map.get(type).clone();
        else
        {
            if(type.equals("mysql"))
            {
                DatabaseConnection mysql=new MySQLDatabaseConnection();
                map.put(type, mysql);
                return mysql;
            }
            else if(type.equals("postgres"))
            {
                DatabaseConnection postgres=new PostgresDatabaseConnection();
                map.put(type, postgres);
                return postgres;
            }
        }
        throw new IllegalArgumentException("Invalid Argument: "+type);
    }
}