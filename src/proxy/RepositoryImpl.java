package proxy;

public class RepositoryImpl implements Repository
{
    public RepositoryImpl()
    {
        System.out.println("Creating RepositoryImpl");
    }
    public int count()
    {
        System.out.println("Getting Data From DB");
        return 0;
    }
}