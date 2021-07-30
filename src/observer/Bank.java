package observer;

public class Bank extends Observable
{
    private double euroToDollar=1.2;
    public double getEuroToDollar()
    {
        return euroToDollar;
    }
    public void setEuroToDollar(double euroToDollar)
    {
        this.euroToDollar=euroToDollar;
        update();
    }
    private void update()
    {
        for(Observer observer:observers)
            observer.updateEuroToDollar(euroToDollar);
    }
}