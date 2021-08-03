package proxy;

public class RepositoryProxy implements Repository
{
    private Repository repository;
    public int count()
    {
        if(repository==null)
            repository=new RepositoryImpl();
        return repository.count();
    }
}