################################
#   Author Nick Straub-Deck    #
#     236 Final project.       #
import random
import time
import sys
from Animal import animal
from Queue import Queue
def choose():
    '''
    Allows the user to chose what character they want to play as
    :return: Character created from the Animal Class.
    '''
    character=input("What animal would you like the play the story as? You can choose bear,raccoon,lynx, honey badger, or wolf. You can also create your own by typing create.")
    if character=="bear":
        Animal=animal(4,0,3,-3,1,1,30,3) #Sets the class up using the bears stats.
        return Animal # Returns the class with the specific stats.
    if character=="raccoon":
        Animal=animal(-3,4,-2,3,0,5,30,3)
        return Animal
    if character=="lynx":
        Animal=animal(-1,4,0,2,-1,1,30,3)
        return Animal
    if character=="honey badger":
        Animal=animal(-1,0,2,0,1,3,30,3)
        return Animal
    if character=="wolf":
        Animal=animal(2,-1,2,4,1,4,30,3)
        return Animal
    if character=="create": #User has selected they want a randomly generated character.
        #Starts code used for big o calculation
        queue1=Queue()  #Creates Queues to use for the creation.
        queue2=Queue()
        queue3=Queue()
        create(queue1) # Creates one of the characters using the create function.
        create(queue2)
        create(queue3)
        choice=input("What roll would you like to use for your animal? 1,2, or 3?") # Allows the user to pick what character they want.
        if choice=="1":
            a=queue1.dequeue() # Dequeues and assigns the corresponding value to a parameter.
            b=queue1.dequeue()
            c=queue1.dequeue()
            d=queue1.dequeue()
            e=queue1.dequeue()
            f=queue1.dequeue()
            Animal=animal(a,b,c,d,e,f,30,3) # Creates the Character using the parameters.
            return Animal
        if choice=="2":
            a=queue2.dequeue()
            b=queue2.dequeue()
            c=queue2.dequeue()
            d=queue2.dequeue()
            e=queue2.dequeue()
            f=queue2.dequeue()
            Animal=animal(a,b,c,d,e,f,30,3)
            return Animal
        if choice=="3":
            a=queue3.dequeue()
            b=queue3.dequeue()
            c=queue3.dequeue()
            d=queue3.dequeue()
            e=queue3.dequeue()
            f=queue3.dequeue()
            Animal=animal(a,b,c,d,e,f,30,3)
            return Animal
def create(x):
    '''
    Creates the character if the user desires.
    :param x: A Queue
    :return: The created character.    '''
    roll=random.randint(-3,5) # rolls a random number to create the stat for the character.
    total1=roll
    x.enqueue(total1) # Adds it to the queue.
    roll=random.randint(-3,5)
    total2=roll
    x.enqueue(total2)
    roll=random.randint(-3,5)
    total3=roll
    x.enqueue(total3)
    roll=random.randint(-3,5)
    total4=roll
    x.enqueue(total4)
    roll=random.randint(-3,5)
    total5=roll
    roll=random.randint(-3,5)
    x.enqueue(total5)
    total6=roll
    x.enqueue(total6)
    #Ends big o calculation code.
    print("You rolled a character with "+str(total1)+" strength, "+str(total2)+" dexterity, "+str(total3)+" constitution, " +str(total4)+" charisma " +str(total5)+ " wisdom and ", str(total6)+ " intelligence.")
    #Describes the character to the user that was created.
    return(animal(total1,total2,total3,total4,total5,total6,30,3)) #Returns the character using the rolls from before.
def story(Animal):
    '''
    Reads the story and allows user interaction.
    :param Animal: The character the user chose
    :return: None
    '''
    for i in range(10):
        print(" ")  # Prints an empty line 10 times  to clean the screen of text.
    t=open("tale.txt","r") # Opens the main story file for future use.
    while True:
        x=t.readline()
        x=x.strip() # Used so the program can recognize the key words in the text. This eliminates the /n from the end of the line
        if x =="You eat it.": # IF x equals one of the key word's we are looking for.
            for i in range(3):
                print(" ") # Helps create distance between the texts.
            con(Animal) # Calls a function to call a constitution check
        if x=="You think hard.":
            for i in range(3):
                print(" ")
            int(Animal)
        if x=="You try to recall past knowledge.":
            for i in range(3):
                print(" ")
            wis(Animal)
        if x=="End": # Program has ended.
            print(x)
            print("Thats the end of the story everyone! Thanks for playing")
            time.sleep(3)
            sys.exit()
        time.sleep(2.5) #Gives user some time to read the text.
        print(x) #Prints the line that was read.
def instructions():
    '''
    Reads the instructions to the user.
    :return: None
    '''
    skip=input("Would you like to skip the instructions? Type y for yes")
    if skip == "y":
        story(choose())
    t=open("instructions.txt","r")
    while True:
        x=t.readline()
        x=x.strip()
        if x == "onward":
            button=input("Press 1 to continue or 2 to quit.")
            if button=="1":
                for i in range(10):
                    print(" ")
                story(choose())
            if button=="2": # If the value is 2 it allows the program to exit and shut down.
                sys.exit()
        time.sleep(2.5)
        print(x)
def con(Animal):
    '''
    Sets up the constitution check.
    :param Animal: The user character
    :return: None
    '''
    print("This is a constitution check.")
    print("Health:"+str(Animal.health)) #Prints the characters health.
    button=input("Press 1 to make the check,2 to forage, and 3 to heal ")
    if button=="1":
        Animal.con_check() #Calls the check itself.
    if button=="2":
        Animal.forage() # Activates hunt for food.
        con(Animal) # Calls the function again.
    if button=="3":
        Animal.heal() # Heals the user.
        con(Animal)
def int(Animal):
    '''
    Sets up the intelligence check.
    :param Animal: User character
    :return: None
    '''
    print("This is an intelligence check.")
    print("Health:"+str(Animal.health))
    button=input("Press 1 to make the check,2 to forage, and 3 to heal ")
    if button=="1":
        Animal.int_check()
    if button=="2":
        Animal.forage()
        int(Animal)
    if button=="3":
        Animal.heal()
        int(Animal)
def wis(Animal):
    '''
    Set's up the wisdom check.
    :param Animal: User character
    :return: None
    '''
    print("This is a wisdom check")
    print("Health:"+str(Animal.health))
    button=input("Press 1 to make the check and 2 to heal ")
    if button=="1":
        Animal.wis_check()
    if button=="2":
        Animal.heal()
        wis(Animal)
def dex(Animal):
    '''
    Sets up the dex check.
    :param Animal: User character
    :return: None
    '''
    print("This will be a dexterity check.")
    print("Health:"+str(Animal.health))
    button=input("Press 1 to make the check")
    if button=="1":
        Animal.dex_check()
def main():
    instructions()
main()
