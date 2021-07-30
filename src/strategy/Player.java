package strategy;

public class Player
{
    private Weapon weapon;
    public void attack()
    {
        weapon.attack();
    }
    public Weapon getWeapon()
    {
        return weapon;
    }
    public void setWeapon(Weapon weapon)
    {
        this.weapon = weapon;
    }
}