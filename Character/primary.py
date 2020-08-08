from character import character
def main():
    choice1 = int(input("Press 1 for half-orc, 2 for human, 3 for tiefling, 4 for halfling, 5 for dragonborn, or 6 for assimar."))
    race=race_creation(choice1)
    print("You chose a "+race+ ".")
    ability_score(race)
def ability_score(race):
    power=input("Press 1 to use a stat array. 2 to roll stats.")
    if power == "1":
        array = input("What array would you like to use? Type 1 for 5 10's and a 16, 2 for all 12's, or 3 for 4 10's and  14's?")
        if array == "1":
            list = [10,10,10,10,10,16]
            list,cscore=charisma(list)
            list,iscore=intel(list)
            list,wscore=wisdom(list)
        if array == "2":
            Character = character(race,10,10,10,10,10,10)
            print("You made it.")
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
    charisma = int(input("What would you like your charisma score to be?"))
    print("You have the following ability scores left.")
    for i in list:
        if i == charisma:
            list.pop(counter)
            break
        if i != charisma:
            counter+=1
    print(list)
    return list,charisma
def intel(list):
    counter=0
    intel = int(input("What would you like your intelligence score to be?"))
    print("You have the following ability scores left.")
    for i in list:
        if i == intel:
            list.pop(counter)
            break
        if i != intel:
            counter+=1
    print(list)
    return list,intel
def wisdom(list):
    counter=0
    wisdom = int(input("What would you like your wisdom score to be?"))
    print("You have the following ability scores left.")
    for i in list:
        if i == wisdom:
            list.pop(counter)
            break
        if i != wisdom:
            counter+=1
    print(list)
    return list,wisdom
main()
