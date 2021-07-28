package abstractfactory;

public class EnemyShipWithLazer extends EnemyShip
{
    public void attackToPlayerShip(PlayerShip playerShip)
    {
        System.out.println("Enemy is attacking to: "+playerShip+" with lazer");
    }
}