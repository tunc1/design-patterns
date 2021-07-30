package observer;

public class ExchangeOffice implements Observer
{
    private double euroToDollar=1.2;
    public double getEuroToDollar()
    {
        return euroToDollar;
    }
    public void setEuroToDollar(double euroToDollar)
    {
        this.euroToDollar=euroToDollar;
    }
    public void updateEuroToDollar(double euroToDollar)
    {
        setEuroToDollar(euroToDollar);
    }
    public double convertEuroToDollar(double euro)
    {
        return euro*euroToDollar*11/10;
    }
}