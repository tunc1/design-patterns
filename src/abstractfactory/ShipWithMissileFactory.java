package abstractfactory;

public class ShipWithMissileFactory extends ShipFactory
{
    public EnemyShip createEnemyShip()
    {
        return new EnemyShipWithMissile();
    }
    public PlayerShip createPlayerShip()
    {
        return new PlayerShipWithMissile();
    }
}