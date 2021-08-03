package memento;

import java.util.Stack;

public class CareTaker
{
    private Stack<Memento> mementos;
    public CareTaker()
    {
        mementos=new Stack<>();
    }
    public void save(Memento memento)
    {
        mementos.add(memento);
    }
    public Memento restore()
    {
        return mementos.pop();
    }
}