import random
from dungeon_start import Entity, Weapon, main


## -----  ADVENTURER / ENEMY / BOSS CLASSES  ----- ##
# NOTE: Refer to the class Weapon and abstract class Entity in 
# "dungeon_start.py" for what functions/methods need to be defined and used


class Adventurer(Entity):
    """
    Represents an Adventurer character in the game.

    Attributes:
        _weapon (Weapon): The weapon assigned to the Adventurer.
        _name (str): The name of the Adventurer --> 'Lancelot'.
        _max_hp (int): The MAXIMUM HP of the Adventurer.
        _cur_hp (int): The CURRENT HP of the Adventurer.

    Methods:
        __str__(): Returns a string with details of the Adventurer.
        dmg(amt): Reduces the Adventurer's health by Enemy damage.
        fight(opp): Attacks an Enemy, dealing random weapon damage.
        use_potion(): Restores a random amount of health.
        die(): Prints a message indicating the Adventurer's death.
        regen(): Restores the Adventurer's health to maximum.
        set_weapon(weapon): Updates the Adventurer's weapon.
        get_cur_hp(): Returns the current health of the Adventurer.
        get_name(): Returns the name of the Adventurer.
        get_weapon(): Returns the Adventurer's weapon.
    """
    def __init__(self):
        # WRITE YOUR CODE HERE #
        self._weapon = Weapon("Caliburn", (1,35))
        super().__init__("Lancelot", 125, self._weapon)

    def __str__(self):
        return f"== ADVENTURER ==\nName: {self._name}\nMax HP: {self._max_hp}\nCur HP: {self._cur_hp}\nWeapon: {self._weapon.get_name()}\nAttack: {self._weapon.get_attack()}\n"
    
    def dmg(self,amt):
        self._cur_hp -= amt
        print(f"* {self._name} took {amt} damage!")

    def fight(self,opp):
        damage = self._weapon.use_weapon()
        print(f"[{self._name}] Feel my blade!")
        opp.dmg(damage)
    
    def use_potion(self):
        restored_hp = random.randint(15, 30)
        self._cur_hp = min(self._cur_hp + restored_hp, self._max_hp)
        print(f"* {self._name} restored {restored_hp} HP!")

    def die(self):
        print(f"\n[{self._name}] \t\"Alas, the blade that served me well shall now rest...\n\t\t Farewell, brave souls, may you fight on in honor where I cannot...\"\n")

    def regen(self):
        self._cur_hp = self._max_hp
        print(f"{self._name} has RESTORED their health back to FULL!")
     
    def set_weapon(self, weapon: Weapon):
        self._weapon = weapon

    def get_cur_hp(self):
        return self._cur_hp
    def get_name(self):
        return self._name

    def get_weapon(self):
        return self._weapon
    
 
class Enemy(Entity):
    """
    Represents a generic Enemy character in the game.

    Attributes:
        _weapon (Weapon): The weapon assigned to the Enemy --> Golden Dagger
        _name (str): The name of the Enemy --> 'Goblin'.
        _max_hp (int): The MAXIMUM HP of the Enemy.
        _cur_hp (int): The CURRENT HP of the Enemy.

    Methods:
        __str__(): Returns a formatted string with details of the Enemy.
        dmg(amt): Reduces the Enemy's health by a specified damage amount.
        fight(opp): Attack the Adventurer, dealing random damage.
        use_potion(): Restores a random amount of health.
        die(): Prints a message indicating the Enemy's death.
        is_boss(): Returns False, indicating that this is a regular Enemy.
        get_cur_hp(): Returns the current health of the Enemy.
        get_name(): Returns the name of the Enemy.
        get_weapon(): Returns the Enemy's weapon.
    """
    def __init__(self):
        # WRITE YOUR CODE HERE #
        self._weapon = Weapon("Golden Dagger", (1,25))
        super().__init__("Goblin", 45, self._weapon)

    def __str__(self):
        return f"== ENEMY ==\nName: {self._name}\nMax HP: {self._max_hp}\nCur HP: {self._cur_hp}\nWeapon: {self._weapon.get_name()}\nAttack: {self._weapon.get_attack()}\n"
    
    def dmg(self,amt):
        self._cur_hp -= amt
        print(f"* {self._name} took {amt} damage!")

    def fight(self,opp):
        damage = self._weapon.use_weapon()
        print(f"[{self._name}] Ehehehehe!")
        opp.dmg(damage)
    
    def use_potion(self):
        restored_hp = random.randint(15, 30)
        self._cur_hp = min(self._cur_hp + restored_hp, self._max_hp)
        print(f"* {self._name} restored {restored_hp} HP!")
    
    def die(self):
        print(f"[{self._name}]: Nooo! Why do I even guard this dungeon!?")
    
    def is_boss(self):
        return False
    
    def get_cur_hp(self):
        return self._cur_hp
    def get_name(self):
        return self._name

    def get_weapon(self):
        return self._weapon


#    WRITE THE BOSS CLASS HERE     #
# Make sure it inherits from Enemy #
class Boss(Enemy):
    """
    Represents a Boss character in the game, a powerful Dragon!

    Attributes:
        _weapon (Weapon): The weapon assigned to the Boss --> Fire Breath
        _name (str): The name of the Boss --> 'Dragon'.
        _max_hp (int): The MAXIMUM HP of the Boss.
        _cur_hp (int): The CURRENT HP of the Boss.

    Methods:
        is_boss(): Returns True, indicating that this is a Boss enemy.
        fight(opp): Attack the Adventurer, dealing random damage.
        die(): Prints a message indicating the Boss's death.
    """
    def __init__(self):
        # WRITE YOUR CODE HERE #
        super().__init__()
        self._name = "Dragon"
        self._max_hp = 250
        self._cur_hp = self._max_hp
        self._weapon = Weapon("Fire Breath", (10, 25))    
    def is_boss(self):
        return True
    def fight(self,opp):
        opp._cur_hp -= self._weapon.use_weapon()
        print(f"[{self._name}] ROOOOOOAARRR!")
        
    def die(self):
        print(f"[{self._name}]: ROOOAAARR! Curse you!")


# -------- WARNING! DO NOT MODIFY BELOW ------- #

# initialize the characters and starts the battle
if __name__ == "__main__":
    adventurer_a = Adventurer()         
    enemy_e = Enemy()             
    boss_b = Boss()     

    main(adventurer_a,enemy_e,boss_b)