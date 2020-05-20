# Entire class was an enhancement on the dog class I created for virtual pets.
# Increased the range of functions it offers by creating methods that are needed for my program.
# Took the food and the multiple functions that added various values from the dog class and refined them here.
import random
class animal:
    def __init__(self,str,dex,con,char,wis,int,health,food):
        self.str=str
        self.dex=dex
        self.con=con
        self.char=char
        self.wis=wis
        self.int=int
        self.health=health
        self.food=food
    def dex_check(self):
        '''
        Does the dexterity check.
        :return: None
        '''
        check=random.randint(1,20)+self.dex #Rolls the dexterity roll
        print(check)
        if check in range(13,18): #This is the realm of the roll succeeding.
            print("You made the check and continue on your way")
        if check in range(18,20): #Tbe roll went really well.
            print("You are seriously dexterous in the moment.")
        if check>=20: # This roll is the phenomenal role.
            print("You were doing cartwheels as you did this")
        if check<13: # roll fails.
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6) #rolls 3 dice and adds them together.
            print("You fail the action and take " +str(damage)+ " damage to your health")
            self.health=self.health-damage # subtracts the damage.
            print("Health:" +str(self.health))
    def str_check(self):
        '''
        Does the strength roll
        :return: None
        '''
        check=random.randint(1,20)+self.str
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You are seriously muscular in the moment.")
        if check>=(20):
            print("You were doing pushup and flexing the whole time you did this")
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("You fail the action and take " +str(damage)+ " damage to your health")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def con_check(self):
        '''
        Does the constitution check.
        :return: none
        '''
        check=random.randint(1,20)+self.con
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You had a stomach of steel")
        if check>=20:
            print("That was the strangest thing you have ever tasted. You gain extra health")
            gain=random.randint(1,6)
            print("You gained " +str(gain)+ " health.")
            self.health+=gain
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("You fail the action and take " +str(damage)+ " damage to your health")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def char_check(self):
        '''
        Does the charisma check.
        :return: None
        '''
        check=random.randint(1,20)+self.char
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You laid the cute animal eyes on thick")
        if check>=20:
            print("You were so smooth they even fed you")
            self.health=self.health+1
            print("Health:" +str(self.health))
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("They hit you and you take " +str(damage)+ " damage to your health. You run by")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def wis_check(self):
        '''
        Does the wisdom check
        :return: None
        '''
        check=random.randint(1,20)+self.wis
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("Your wise thoughts made the challenge a breeze.")
        if check>=20:
            print("You were the wisest you have ever been as you did this")
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("You fail the action and take " +str(damage)+ " emotional damage to your health")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def int_check(self):
        '''
        DOes the intelligence check.
        :return: None
        '''
        check=random.randint(1,20)+self.int
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You easily figured out the answer in the moment.")
        if check>=20:
            print("You did so many smart things it would be impossible to remember it")
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("You fail the action and take " +str(damage)+ " brain damage to your health")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def forage(self):
        '''
        Forages for food and increases the meals if the roll was good enough.
        :return: None
        '''
        if self.food==4: # if you have 4 food, this prevent you from obtaining more.
            print("You have enough food")
            return
        forage=random.randint(1,20) # rolls for the food
        print("You roll a "+str(forage))
        if forage>=10: # If you have a roll higher then 10 you find food.
            forage+=1
            print("You succeed in finding a meal.")
            self.food+=1
            print("Meals:"+str(self.food))
        if forage<10: # Under ten and you fail
            print("You failed to find any food.")
            self.food+=1
    def heal(self):
        '''
        CHaracter loses a meal and heals a random amount,
        :return: None.
        '''
        if self.health>=30: # if you have exactly or over 30 health you cannot heal anymore
            print("You already have full health!")
            return
        increase=random.randint(1,12)
        self.health+=increase
        self.food=self.food-1
        print("You heal " +str(increase)+ " amount of points.")
        print("Health:" +str(self.health))
        print("Meals left:" +str(self.food))
