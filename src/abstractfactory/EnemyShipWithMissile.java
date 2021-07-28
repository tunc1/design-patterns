package abstractfactory;

public class EnemyShipWithMissile extends EnemyShip
{
    public void attackToPlayerShip(PlayerShip playerShip)
    {
        System.out.println("Enemy is attacking to: "+playerShip+" with missile");
    }
}