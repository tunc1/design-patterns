package abstractfactory;

public abstract class ShipFactory
{
    public abstract EnemyShip createEnemyShip();
    public abstract PlayerShip createPlayerShip();
}