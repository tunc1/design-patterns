package abstractfactory;

public class PlayerShipWithMissile extends PlayerShip
{
    public void attackToEnemyShip(EnemyShip enemyShip)
    {
        System.out.println("Player is attacking to: "+enemyShip+" with missile");
    }
}