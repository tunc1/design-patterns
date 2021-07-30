package observer;

import java.util.LinkedList;
import java.util.List;

public abstract class Observable
{
    protected List<Observer> observers;
    public Observable()
    {
        observers=new LinkedList<>();
    }
    public void addObserver(Observer observer)
    {
        observers.add(observer);
    }
    public void deleteObserver(Observer observer)
    {
        observers.remove(observer);
    }
}