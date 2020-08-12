import random
from character import character
def main():
    choice1 = int(input("Press 1 for half-orc, 2 for human, 3 for tiefling, 4 for halfling, 5 for dragonborn, or 6 for assimar."))
    race=race_creation(choice1)
    print("You chose a "+race+ ".")
    ability_score(race)
def ability_score(race):
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
            Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
        if array == "2":
            Character = character(race,10,10,10,10,10,10)
            print("You made it.")
        if array == "3":
            list = [10,10,10,10,14,14]
            list,cscore=charisma(list)
            list,iscore=intel(list)
            list,wscore=wisdom(list)
            list,sscore=strength(list)
            list,dscore=dexterity(list)
            list,conscore=constitution(list)
            Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
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
        Character = character(race,sscore,dscore,conscore,cscore,wscore,iscore)
def race_creation(i):
    choice2 ={
    1:"Half-orc",
    2:"Human",
    3:"Tiefling",
    4:"Halfling",
    5:"Dragonborn",
    6:"Assimar"
    }
    return choice2.get(i,"Wrong Answer")
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
