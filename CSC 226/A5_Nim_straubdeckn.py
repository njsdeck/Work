######################################################################
# Author: Nick Straub-Deck
# Username: straubdeckn
#
# Assignment: A5: The game of Nim
# Purpose: Practice breaking a larger problem down into smaller "mental chunks"using functions
#Gain practice using loops and modulus (%)
######################################################################
# Acknowledgements:
#   Original Author: Nick Straub-Deck with advice from Roy Smith.
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import random
import time
def user_game(balls):
    while True:
        v=int(input("How many balls would you like to withdraw? 1-4"))
        if v in range(1,5) and v<=balls:
            print("you withdrew " + str(v) + " balls")
            balls=balls-v
            print("There are " + str(balls) +" balls left")
            return balls
def game(balls):
    x = balls%5
    if x == 0:
        z=random.randint(1,4)
        print ("I withdraw " + str (z) + " balls")
        balls=balls-z
        print("There are " + str(balls) + " balls left")
        return balls
    if x>0:
        balls=balls-x
        print("I withdraw " + str(x))
        print("There are " + str(balls) + " balls left")
        return balls
def balls_in_play():
        while True:
            s =int(input("How many balls would you like to put in play? Has to be 15 or higher"))
            if s>=15:
                return s
            elif s<15:
                print("The number is supposed to be higher then 14!")
def main():
    balls=balls_in_play()
    while True:
        balls=user_game(balls)
        if balls==0:
            print("You won!")
            time.sleep(3)
        balls=game(balls)
        if balls==0:
            print("The computer won!")
            time.sleep(3)
main()
