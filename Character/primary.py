from character import character
def main():
    choice1 = int(input("Press 1 for half-orc, 2 for human, 3 for tiefling, 4 for halfling, 5 for dragonborn, or 6 for assimar."))
    race=race_creation(choice1)
    print(race)
def race_creation(i):
    print("What race would you like to be?")
    choice2 ={
    1:"Half-orc",
    2:"Human",
    3:"Tiefling",
    4:"Halfling",
    5:"Dragonborn",
    6:"Assimar"
    }
    return choice2.get(i,"Wrong Answer")
main()
