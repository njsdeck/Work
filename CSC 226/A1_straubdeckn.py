######################################################################
# Author: Nick Straub-Deck     TODO: Change this to your name
# Username: straubdeckn           TODO: Change this to your username
#
# Assignment: A1
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1984 and 1995. Also returns your compatibility
# with other animals.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################
import time
# Task 1
# TODO Ask user for their birth year
year = input('What is the year of your birth?[1984-1995]')

# TODO Check the year, print the correct animal for that year
if year == '1985':
    print("Your birth animal is the Ox!")
elif year == '1986':
    print("You are a Tiger!")
elif year == '1987':
    print("You are in the year of the Rabbit!")
elif year == '1988':
    print("You are a Dragon!")
elif year == '1989':
    print("You were born in the year of the Snake!")
elif year == '1990':
    print("You are a Horse!")
elif year == '1991':
    print("Your birth animal is the Goat!")
elif year == '1992':
    print("You are a Monkey!")
elif year == '1993':
    print("You are born a Rooster!")
elif year == '1994':
    print ("You are born in the year of the Dog!")
elif year == '1995':
    print("Your birth animal is the Pig!")
elif year == '1984':
    print("You were born in the year of the Rat!")
elif year == '1998':
    print("You are a Tiger!")

else:
    print("Someone doesn't like to follow instructions")




time.sleep(1.5)
print()

# Task 2
# TODO Ask the user for their friend's birth year
friend = input("What is your friend's year of birth?[1984-1995]")

# TODO Check the year, print the correct animal for that year

if friend == '1985':
    print("Your friend's birth animal is the ox!")
elif friend == '1986':
    print("Your friend is a tiger!")
elif friend == '1987':
    print("Your friend was born in the year of the rabbit!")
elif friend == '1988':
    print("Your friend is a dragon!")
elif friend == '1989':
    print("Your friend was born in the year of the snake!")
elif friend == '1990':
    print("Your friend is a horse!")
elif friend == '1991':
    print("Your friend's birth animal is the goat!")
elif friend == '1992':
    print("Your friend is a monkey!")
elif friend == '1993':
    print("Your friend was born a rooster!")
elif friend == '1994':
    print ("Your friend was born in the year of the dog!")
elif friend == '1995':
    print("Your friend's birth animal is the pig!")
elif friend == '1984':
    print("Your friend was born in the year of the rat!")
else:
    print("If you don't know you might wanna go ask.")
    quit()
time.sleep(3)
print()
print()
print()

my_birth_year = 1998           # TODO change this to your birth year

# Task 3
# TODO Check for compatibility between two birth years
# NOTE: You can assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.
if my_birth_year == 1998:
    print("Lets assume you are a tiger. We will see if your friend is compatable.")
    time.sleep(1)
if friend == '1995' or friend == '1994' or friend == '1990':
     print("You two are a great match! Make sure you don't get hungry however.")
elif friend == ("1992"):
    print("You two have a poor compatability, you clearly don't like bananas.")
elif friend == ('1986'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1987'):
   print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1991'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1989'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1993'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1985'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1988'):
    print('You are an ok match. Should provide a generally guilt free snack.')
elif friend == ('1984'):
   print('You are an ok match. Should provide a generally guilt free snack.')
time.sleep(7)



# TODO print if you are a strong match, no match, or in between


