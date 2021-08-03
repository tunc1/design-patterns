package memento;

public class TextBox
{
    private String text;
    public String getText()
    {
        return text;
    }
    public void setText(String text)
    {
        this.text = text;
    }
    public Memento save()
    {
        return new Memento(text);
    }
    public void restore(Memento memento)
    {
        setText(memento.getState());
    }
}