package abstractfactory;

public class ShipWithLazerFactory extends ShipFactory
{
    public EnemyShip createEnemyShip()
    {
        return new EnemyShipWithLazer();
    }
    public PlayerShip createPlayerShip()
    {
        return new PlayerShipWithLazer();
    }
}