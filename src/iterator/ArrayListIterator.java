package iterator;

import java.util.Iterator;

public class ArrayListIterator<T> implements Iterator<T>
{
    private ArrayList<T> arrayList;
    private int index;
    public ArrayListIterator(ArrayList<T> arrayList)
    {
        index=0;
        this.arrayList = arrayList;
    }
    public boolean hasNext()
    {
        return index<arrayList.size();
    }
    public T next()
    {
        return arrayList.get(index++);
    }
}