# STARTER CODE FOR PROJECT 3 - Dungeon Battle

#----------------------------------------------------------#
#                   **** WARNING ****                      #
#    Do not change this code for any reason whatsoever     #
#        or risk losing points on the assignment.          #
#    Modify only the classes in dungeon-p3-TEMPLATE.py     #
#----------------------------------------------------------#


from abc import ABC, abstractmethod
import random



#     WEAPON CLASS     #
#     DO NOT CHANGE    #
class Weapon:
    def __init__(self,name:str,attack:tuple):
        '''Initializing method for the weapon instance'''
        self._name = name
        self._attack = attack
    
    # --- GETTERS --- #
    def get_name(self):
        '''Return weapon name'''
        return self._name

    def get_attack(self):
        '''Return weapon attack range values'''
        return self._attack
    
    # -- METHODS -- #

    def use_weapon(self):
        '''Returns a random amount of attack damage based on _attack'''
        return random.randint(self._attack[0], self._attack[1])




# BASE "ABSTRACT" CLASS     #
#     DO NOT CHANGE         #
class Entity(ABC):
    # initializing function for the entity class and defines (private) properties
    # NOTE: these values should only be accessed by other classes using the getter methods
    def __init__(self,name:str,hp:int,weapon:Weapon):
        self._name = name               # name of the character used in flavor text
        self._max_hp = hp               # maximum HP of the character for battle
        self._cur_hp = hp               # current HP of the character for battle; encounter ends when this is 0
        self._weapon = weapon           # used weapon object of the character (see Weapon class above)


    # ---- GETTERS ---- #

    # RETURN a string with details about the entity
    # name, max HP, current HP, weapon name, and weapon attack
    @abstractmethod
    def __str__(self):
        pass

    # return the name of the entity
    @abstractmethod
    def get_name(self):
        pass

    # return the current hp value
    @abstractmethod
    def get_cur_hp(self):
        pass

    # return the weapon object instance
    @abstractmethod
    def get_weapon(self):
        pass


    # ---- METHODS ---- #

    # subtract the value of the hp attribute by some 
    # random amount between in the self._attack range tuple
    # and prints a message about how much damage was taken
    @abstractmethod
    def dmg(self,amt):
        pass

    # apply damage to the opponent based on the weapon's 
    # use_weapon() method and prints a message
    # from the character with a catchphrase or battle cry
    @abstractmethod
    def fight(self,opp):
        pass
    
    # method that changes increments the hp by some 
    # random amount (not more than maximum hp) and 
    # prints a message about how much HP was restored
    @abstractmethod
    def use_potion(self):
        pass
    
    # print a message from the character with dying words
    @abstractmethod
    def die(self):
        pass





## ------ MAIN GAME LOOP ------ ##

# STATIC DUNGEON CLASS
class Dungeon:
    @staticmethod
    def enter_dungeon(a:Entity,e:Entity):
        '''
            Starts the flavor text for the dungeon battle
            Input: (a (of class Adventurer), e (of class Enemy))
            Output: Printed flavor text of the encounter
        '''
        print("* Adventurer " + a.get_name() + " encounters the Enemy " + e.get_name() + " in the dungeon.")

        # check if the enemy is a boss
        if(e.is_boss()):
            print("* " + e.get_name() + " is a boss! Watch out " + a.get_name() + "!")

        print("")

    @staticmethod
    def showStats(a:Entity,e:Entity):
        '''
            Shows the stats of each party for the dungeon battle
            Input:  (a (of class Adventurer), e (of class Enemy))
            Output: Stat values
        '''
        print(a)
        print(e)


    @staticmethod
    def fight(a:Entity,e:Entity):
        '''
            Inplements a fighting simulation between the Adventurer and the Enemy instances
            Input:  (a (of class Adventurer), e (of class Enemy))
            Output: Printed messages of the battle
        '''
        print("**** FIGHT START ****")

        # internal function for showing the hp
        def showHP(a:Entity,e:Entity):
            '''
                Shows the current hp of each party for the dungeon battle
                Input:  (a (of class Adventurer), e (of class Enemy))
                Output: Current HP values
            '''
            print("==== CURRENT HP ====")
            print(f"{a.get_name()} HP = [{a.get_cur_hp()}]")
            print(f"{e.get_name()} HP = [{e.get_cur_hp()}]")
            print("")


        # fight loop -- only one may leave alive
        while(a.get_cur_hp() > 0):

            # upgrade adventurer weapon if about to die at the boss battle
            if a.get_cur_hp() <= 10 and e.is_boss():
                a.set_weapon(Weapon("Excalibur",(20,100)))
                print(f"* {a.get_name()} uprgraded their weapon to {a.get_weapon().get_name()}!")


            # chance for either party to take the potion
            if(random.random() <= 0.2):        # 20% chance to regain health
                a.use_potion()
            if(random.random() <= 0.05):       # 5% chance to regain health
                e.use_potion()

            # fight action
            a.fight(e)          # adventurer fights first
            if e.get_cur_hp() > 0:       # if enemy still alive, fight back
                e.fight(a)
                if(a.get_cur_hp() <= 0):     # if adventurer died, end the game
                    a.die()
                    break

            else:                   # otherwise, if the enemy died, end the game
                e.die()
                break

            # show current hp 
            showHP(a,e)
        
        # give a battle declaration of who is victorious
        if(a.get_cur_hp() <= 0):
            print("* Adventurer " + a.get_name() + " was defeated! Enemy " + e.get_name() + " is victorious!")
        elif(e.get_cur_hp() <= 0):
            print("* Enemy " + e.get_name() + " was defeated! Adventurer " + a.get_name() + " is victorious!")
        

# the main fight loop
# takes in as input the Adventurer (a), Enemy (e), and Boss (b)
def main(a:Entity,e:Entity,b:Entity):
    
    print("************ DUNGEON START ************")

    # first fight against enemy
    Dungeon.enter_dungeon(a,e)
    Dungeon.showStats(a,e)
    Dungeon.fight(a,e)

    # regenerate adventurer health
    print("")
    a.regen()
    print("")

    # second fight against boss
    Dungeon.enter_dungeon(a,b)
    Dungeon.showStats(a,b)
    Dungeon.fight(a,b)

    
    print("************ END OF DUNGEON ************")