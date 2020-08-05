import random
import time
def main():
    number=num_gen()
    play(number)
def num_gen():
    number=random.randint(1,10)
    return(number)
def play(number):
    answer = False
    while answer == False:
        guess=int(input("Guess a number between 1 and 10."))
        if guess < number:
            print("Number to low. Guess again")
        if guess > number:
            print("Number to high. Guess again")
        if guess == number:
            print("Correct answer.")
            time.sleep(2)
            answer = True
main()
