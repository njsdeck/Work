import random
from char import character
def main():
    drive()
def drive():
    cscore,iscore,wscore,sscore,dscore,conscore = ability_score()
    choice1 = int(input("Press 1 for Half-Orc, 2 Human, 3 Tiefling, 4 Halfling, 5 Dragonborn, 6 Aasimar, 7 Kenku, 8 Kobold, or 9 Genasi."))
    race=race_creation(choice1,cscore,iscore,wscore,sscore,dscore,conscore)
    speed,cscore,iscore,wscore,sscore,dscore,conscore= score_total(race,cscore,iscore,wscore,sscore,dscore,conscore)
    hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore = class_choice(speed,cscore,iscore,wscore,sscore,dscore,conscore)
    level=level_choice()
    #save(Class,race,cscore,iscore,wscore,sscore,dscore,conscore,speed,level)
    #cscore,iscore,wscore,sscore,dscore,conscore = stat_mod(cscore,iscore,wscore,sscore,dscore,conscore)
    Character = character(hit_dice,Class,race,sscore,dscore,conscore,cscore,wscore,iscore,speed,level)
    Character.test()
    Character.char_mod()
    Character.str_mod()
    Character.int_mod()
    Character.con_mod()
    Character.wis_mod()
    Character.dex_mod()
    Character.save()
def save(Class,race,cscore,iscore,wscore,sscore,dscore,conscore,speed,level):
    with open('char.txt', 'w') as file:
        file.write(" ")
        file.close()
    with open('char.txt', 'a') as file:
        file.write("You are a " +race+ " " +Class+" of level "+level+ ".\n")
        file.write(" strength: " +str(sscore)+"\n")
        file.write(" dexterity: " +str(dscore)+"\n")
        file.write(" wisdom: " +str(wscore)+"\n")
        file.write(" charisma: " +str(cscore)+"\n")
        file.write(" constitution: " +str(conscore)+"\n")
        file.write(" intelligence: " +str(iscore)+"\n")
        file.write(" You can move " +str(speed)+ " feet with your walk action."+'\n')
        file.close()
###########################################################################
#                           Race Creation
def race_creation(choice1,cscore,iscore,wscore,sscore,dscore,conscore):
    choice2 ={
    1:"Half orc",
    2:"Human",
    3:"Tiefling",
    4:"Halfling",
    5:"Dragonborn",
    6:"Aasimar",
    7:"Kenku",
    8:"Kobold",
    9:"Genasi"
    }
    func=choice2.get(choice1,"Wrong Answer")
    return func
def Half_orc(cscore,iscore,wscore,sscore,dscore,conscore):
    sscore+=2
    conscore+=1
    speed = 30
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Human(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    varient = input('Are you playing a varient human. y for yes or n for no')
    if varient == "y":
        for i in range(2):
            score_increase = int(input("What score would you like to add one to? 1 for charisma, 2 for intelligence, 3 for wisdom, 4 for strength, 5 for dexterity, or 6 for con" ))
            cscore, iscore, wscore, sscore, dscore, conscore = varient_human(score_increase,cscore, iscore, wscore, sscore, dscore, conscore)
    if varient == "n":
        cscore+=1
        iscore+=1
        wscore+=1
        sscore+=1
        dscore+=1
        conscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def varient_human(score_increase,cscore,iscore,wscore,sscore,dscore,conscore):
    human_add = {
    1:charisma_increase,
    2:intellligence_increase,
    3:wisdom_increase,
    4:strength_increase,
    5:dex_increase,
    6:con_increase
    }
    new_value=human_add.get(score_increase,"Wrong Race")
    return new_value(cscore,iscore,wscore,sscore,dscore,conscore)
def Tiefling(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    cscore+=2
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Halfling(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 25
    dscore+=2
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Dragonborn(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    sscore+=2
    cscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Aasimar(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    cscore+=2
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Kenku(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    dscore+=2
    wscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Kobold(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    dscore+=2
    sscore-=2
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def Genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    conscore+=2
    which = int(input("Which Genasi type would you like to be? 1 for water, 2 fire, 3 earth, 4 air."))
    which_genasi ={
    1:water_genasi,
    2:fire_genasi,
    3:earth_genasi,
    4:air_genasi
    }
    gen_type=which_genasi.get(which,"Wrong answer")
    return gen_type(cscore,iscore,wscore,sscore,dscore,conscore)
def water_genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    wscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def earth_genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    sscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def air_genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    dscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
def fire_genasi(cscore,iscore,wscore,sscore,dscore,conscore):
    speed = 30
    iscore+=1
    return speed,cscore,iscore,wscore,sscore,dscore,conscore
###########################################################################
#                             Skill Increase and Creation
def ability_score():
    power=input("Press 1 to use a stat array. 2 to roll stats.")
    if power == "1":
        array = input("What array would you like to use? Type 1 for 1 17, 2 12's, 1 11, and 2 10's, 2 for all 13's, or 3 for 2 15's 2 12's and a 10?")
        if array == "1":
            list = [17,12,12,11,10,10]
            print("You have these ability scores.")
            print(list)
            list,cscore=charisma(list)
            list,iscore=intel(list)
            list,wscore=wisdom(list)
            list,sscore=strength(list)
            list,dscore=dexterity(list)
            list,conscore=constitution(list)
            return cscore,iscore,wscore,sscore,dscore,conscore
            #Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
        if array == "2":
            cscore = 13
            iscore = 13
            wscore = 13
            sscore = 13
            dscore = 13
            conscore = 13
            return cscore,iscore,wscore,sscore,dscore,conscore
            #Character = character(race,10,10,10,10,10,10)
        if array == "3":
            list = [15,15,14,11,11,10]
            print("You have these ability scores.")
            print(list)
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
        check.sort()
        print(check)
        check,cscore=charisma(check)
        check,iscore=intel(check)
        check,wscore=wisdom(check)
        check,sscore=strength(check)
        check,dscore=dexterity(check)
        check,conscore=constitution(check)
        return cscore,iscore,wscore,sscore,dscore,conscore
        #Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
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
    return list,char
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
def strength_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    sscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def intellligence_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    iscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def charisma_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    cscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def wisdom_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    wscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def dex_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    dscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
def con_increase(cscore,iscore,wscore,sscore,dscore,conscore):
    conscore+=1
    return cscore,iscore,wscore,sscore,dscore,conscore
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
    adding=function_call.get(race,"Wrong Race")
    return adding(cscore,iscore,wscore,sscore,dscore,conscore)
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
    #print(rolled)
    return rolled
def stat_mod(cscore,iscore,wscore,sscore,dscore,conscore):
    cscore = cscore-10
    cscore = cscore/2
    print(cscore)
    return cscore,iscore,wscore,sscore,dscore,conscore
def level_choice():
    level =input("What level are you?")
    return level
###########################################################################
#                           Class Choice
def class_choice(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    class2 = int(input("What class would you like to be. Press 1 for fighter, 2 for paladin, 3 for warlock, 4 ranger, 5 monk, 6 rogue, 7 cleric, 8 bard, 9 barbarian."))
    class_decision = {
    1:fight,
    2:pala,
    3:war,
    4:rang,
    5:mon,
    6:rog,
    7:cler,
    8:ba,
    9:barb
    }
    func=class_decision.get(class2,"Wrong Answer")
    return func(speed,cscore,iscore,wscore,sscore,dscore,conscore)
def fight(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Fighter"
    hit_dice=10
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def pala(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Paladin"
    hit_dice = 10
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def war(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Warlock"
    hit_dice = 8
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def rang(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Ranger"
    hit_dice = 10
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def mon(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Monk"
    hit_dice = 8
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def rog(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Rogue"
    hit_dice = 8
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def cler(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Cleric"
    hit_dice = 8
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def ba(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Bard"
    hit_dice = 8
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
def barb(speed,cscore,iscore,wscore,sscore,dscore,conscore):
    Class = "Barbarian"
    hit_dice = 12
    return hit_dice,Class,speed,cscore,iscore,wscore,sscore,dscore,conscore
main()
