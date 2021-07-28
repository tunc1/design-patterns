package abstractfactory;

public class PlayerShipWithLazer extends PlayerShip
{
    public void attackToEnemyShip(EnemyShip enemyShip)
    {
        System.out.println("Player is attacking to: "+enemyShip+" with lazer");
    }
}