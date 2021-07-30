package iterator;

import java.util.Iterator;

@SuppressWarnings("unchecked")
public class ArrayList<T> implements Iterable<T>
{
    private T[] objects;
    private int index;
    public ArrayList()
    {
        objects=(T[])new Object[0];
        index=-1;
    }
    public void add(T t)
    {
        if(index==objects.length-1)
        {
            T[] tmp=(T[])new Object[objects.length+1];
            for(int i=0;i<objects.length;i++)
                tmp[i]=objects[i];
            objects=tmp;
        }
        objects[++index]=t;
    }
    public int size()
    {
        return objects.length;
    }
    public T get(int index)
    {
        return objects[index];
    }
    public Iterator<T> iterator()
    {
        return new ArrayListIterator<>(this);
    }
}