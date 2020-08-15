import random
#from character import character
class character:
    def __init__(self,race,str,dex,con,char,wis,int):
        self.race=race
        self.str=str
        self.dex=dex
        self.con=con
        self.char=char
        self.wis=wis
        self.int=int
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
        #if check<13: # roll fails.
            # damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6) #rolls 3 dice and adds them together.
            # print("You fail the action and take " +str(damage)+ " damage to your health")
            # self.health=self.health-damage # subtracts the damage.
            # print("Health:" +str(self.health))
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
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
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
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
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
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("They hit you and you take " +str(damage)+ " damage to your health. You run by")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
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
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " emotional damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
    def int_check(self):
        '''
        Does the intelligence check.
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
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " brain damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))

def main():
    cscore,iscore,wscore,sscore,dscore,conscore = ability_score()
    choice1 = int(input("Press 1 for Half-Orc, 2 Human, 3 Tiefling, 4 Halfling, 5 Dragonborn, 6 Aasimar, 7 Kenku, 8 Kobold, or 9 Genasi."))
    race=race_creation(choice1,cscore,iscore,wscore,sscore,dscore,conscore)
    print("You chose a "+race+ ".")
    score_total(race,cscore,iscore,wscore,sscore,dscore,conscore)
def ability_score():
    power=input("Press 1 to use a stat array. 2 to roll stats.")
    if power == "1":
        array = input("What array would you like to use? Type 1 for 5 10's and a 16, 2 for all 12's, or 3 for 4 10's and 2 14's?")
        if array == "1":
            list = [10,10,10,10,10,16]
            list,cscore=charisma(list)
            list,iscore=intel(list)
            list,wscore=wisdom(list)
            list,sscore=strength(list)
            list,dscore=dexterity(list)
            list,conscore=constitution(list)
            return cscore,iscore,wscore,sscore,dscore,conscore
            #Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
        if array == "2":
            cscore = 12
            iscore = 12
            wscore = 12
            sscore = 12
            dscore = 12
            conscore = 12
            return cscore,iscore,wscore,sscore,dscore,conscore
            #Character = character(race,10,10,10,10,10,10)
        if array == "3":
            list = [10,10,10,10,14,14]
            list,cscore=charisma(list)
            list,iscore=intel(list)
            list,wscore=wisdom(list)
            list,sscore=strength(list)
            list,dscore=dexterity(list)
            list,conscore=constitution(list)
            return cscore,iscore,wscore,sscore,dscore,conscore
            #Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
    if power == "2":
        check=[]
        for i in range(6):
            check.append(roll())
        print(check)
        check,cscore=charisma(check)
        check,iscore=intel(check)
        check,wscore=wisdom(check)
        check,sscore=strength(check)
        check,dscore=dexterity(check)
        check,conscore=constitution(check)
        #Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
def race_creation(i,cscore,iscore,wscore,sscore,dscore,conscore):
    choice2 ={
    1:"Half orc",
    2:"Human",
    3:"Tiefling",
    4:"Halfling",
    5:"Dragonborn",
    6:"Assimar",
    7:"Kenku",
    8:"Kobold",
    9:"Genasi"
    }
    func=choice2.get(i,"Wrong Answer")
    return func
def Half_orc(cscore,iscore,wscore,sscore,dscore,conscore):
    sscore+=2
    conscore+=1
    print("Made it")
    print(sscore)
    return cscore,iscore,wscore,sscore,dscore,conscore
def Human(cscore,iscore,wscore,sscore,dscore,conscore):
    pass
def Tiefling(cscore,iscore,wscore,sscore,dscore,conscore):
    cscore+=2
    return cscore,iscore,wscore,sscore,dscore,conscore
def Halfling(cscore,iscore,wscore,sscore,dscore,conscore):
    dscore+=2
    return cscore,iscore,wscore,sscore,dscore,conscore
def Dragonborn(cscore,iscore,wscore,sscore,dscore,conscore):
    sscore+=2
    cscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def Aasimar(cscore,iscore,wscore,sscore,dscore,conscore):
    cscore+=2
    return cscore,iscore,wscore,sscore,dscore,conscore
def Kenku(cscore,iscore,wscore,sscore,dscore,conscore):
    dscore+=2
    wscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def Kobold(cscore,iscore,wscore,sscore,dscore,conscore):
    dscore+=2
    sscore=sscore-2
    return cscore,iscore,wscore,sscore,dscore,conscore
def Genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    conscore+=2
    return cscore,iscore,wscore,sscore,dscore,conscore
def charisma(list):
    counter=0
    char = int(input("What would you like your charisma score to be?"))
    # if char not in list:
    #     print("Not a valid input. Try again.")
    #     charisma(list)
    for i in list:
        if i == char:
            list.pop(counter)
            print("You have the following ability scores left.")
            break
        if i != char:
            counter+=1
    print(list)
    return list,charisma
def intel(list):
    counter=0
    intel = int(input("What would you like your intelligence score to be?"))
    for i in list:
        if i == intel:
            list.pop(counter)
            print("You have the following ability scores left.")
            break
        if i != intel:
            counter+=1
    print(list)
    return list,intel
def wisdom(list):
    counter=0
    wisdom = int(input("What would you like your wisdom score to be?"))
    for i in list:
        if i == wisdom:
            list.pop(counter)
            print("You have the following ability scores left.")
            break
        if i != wisdom:
            counter+=1
    print(list)
    return list,wisdom
def strength(list):
    counter=0
    strength = int(input("What would you like your strength score to be?"))
    for i in list:
        if i == strength:
            list.pop(counter)
            counter=0
            print("You have the following ability scores left.")
            break
        if i != strength:
            counter+=1
    print(list)
    return list,strength
def dexterity(list):
    counter=0
    dex = int(input("What would you like your dexterity score to be?"))
    for i in list:
        if i == dex:
            list.pop(counter)
            counter=0
            print("You have the following ability scores left.")
            break
        if i != dex:
            counter+=1
    print(list)
    return list,dex
def constitution(list):
    counter=0
    con = int(input("What would you like your constitution score to be?"))
    for i in list:
        if i == con:
            list.pop(counter)
            counter=0
            print("You have the following ability scores left.")
            break
        if i != con:
            counter+=1
    return list,con
def score_total(race,cscore,iscore,wscore,sscore,dscore,conscore):
    function_call ={
    "Half orc":Half_orc,
    "Human":Human,
    "Tiefling":Tiefling,
    "Halfling":Halfling,
    "Dragonborn":Dragonborn,
    "Aasimar":Aasimar,
    "Kenku":Kenku,
    "Kobold":Kobold,
    "Genasi":Genasi
    }
    adding=function_call.get(race,"Wrong Answer")
    adding(cscore,iscore,wscore,sscore,dscore,conscore)
def roll():
    rolled=0
    new_roll=[]
    for i in range(4):
        i=random.randint(1,6)
        new_roll.append(i)
    new_roll.sort()
    new_roll.pop(0)
    for i in new_roll:
        rolled=rolled+i
    print(rolled)
    return rolled
main()
