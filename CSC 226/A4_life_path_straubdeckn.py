######################################################################
# Author: Nick Straub-Deck
# Username: straubdeckn
# Assignment: A4: A Bug's life.
# Purpose: This program was designed to help understand the modulous and practice fruitful functions.
#
######################################################################
# Acknowledgements:
#   Original Author: Nick Straub-Deck
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import time
def day():
    '''
     This function takes the input for day the user provides and turn it into a single digit.
     The function sets the user input to d then takes the input and makes it a list.
     It adds the digits of this list then sets that value to dd. It repeats and eturns the value of dd, sending it
     to the total function. If the number is 11 22 or 33 when the list is added that value is returned and
     the function killed.

    :return:d,dd
    '''





    d=input("What day were you born? ex 21")
    if int(d)%11==0:                       #If the input is a multiple of 11 the value is returned and the function killed.
        return d
        kill
    (list(d))   #Makes the input value a list
    (sum(int(digit) for digit in str(d)))  #Sums the digits of the list together
    dd=str(sum(int(digit) for digit in str(d)))  #Sets dd to the list value
    if int(dd)%11==0:
        return dd
        kill
    (list(dd))  #Lists the answer to the previous list
    (sum(int(digit) for digit in str(dd)))
    return dd #Returns the sum of the of the list
def month():
    '''
     The takes the input from the user and changes it into a single number. It does this by the same method as the
     day function, just with mt and m instead of d and dd. If the number achieved is a master number the number is
     returned and the function is killed.
    :return: mt,m
    '''
    mt=input("What month were you born? ex 8")
    if int(mt)%11==0:
        return mt
        kill
    (list(mt))
    (sum(int(digit) for digit in str(mt)))
    m=(sum(int(digit) for digit in str(mt)))
    if int(m)%11==0:
        return m
        kill
    (list(str(m)))
    (sum(int(digit) for digit in str(m)))
    return m
def year():
    '''
     Same as day and month functions, with the different variables yr,yrr.
    :return:yr,yrr
    '''
    yr=input("What year were you born? ex 1975")
    if int(yr) % 11==0:
        return yr
        kill
    (list(yr))
    (sum(int(digit) for digit in str(yr)))
    yrr=str(sum(int(digit) for digit in str(yr)))
    if int(yrr)%11==0 :
        return yrr
        kill
    (list(yrr))
    (sum(int(digit) for digit in str(yrr)))
    return yrr
def total():
    '''
    Calls the past three functions and adds them together. It then makes them a list, adds them together, makes
    that a list, adds that together then makes it a list a last time, adding them together. It then prints your
    number and what the number can mean. If the at any point the sum equals a master number it prints what the number
    means, returns the value, and kills the function. It sleeps at the end to give the user time to read the answer.
    :return:s,t,tt
    '''
    s=str(year()) + str(month()) + str(day()) #Calls the three functions and adds them together.
    if int(s)%11==0:    #If the sum is a master number it prints what it means,then it is returned and the function killed
        if(s)==11:
             print("This number says you are sensitive but you have a great understanding of others")
        elif(s)==22:
            print("You have great spiritual understanding")
        elif(s)==33:
            print("You seem to be a great spiritual leader. The rarest number of all")
        return s

    (list(s))
    (sum(int(digit) for digit in str(s)))
    t=str(sum(int(digit) for digit in str(s)))
    if int(t)%11==0:    #Sum of the list
        if(t)==11:
            print("This number says you are sensitive but you have a great understanding of others")
        elif(t)==22:
            print("You have great spiritual understanding")
        elif(t)==33:
            print("You seem to be a great spiritual leader. The rarest number of all")
        return t
    (list(t))
    (sum(int(digit) for digit in str(t)))
    tt=str(sum(int(digit) for digit in str(t)))
    if int(tt)%11==0:
        if(tt)==11:
            print("This number says you are sensitive but you have a great understanding of others")
        elif(tt)==22:
            print("You have great spiritual understanding")
        elif(tt)==33:
            print("You seem to be a great spiritual leader. The rarest number of all")
        return(tt)
    (list(tt))
    print(sum(int(digit) for digit in str(tt)))
    x=(sum(int(digit) for digit in str(tt)))
    if(x)==1:                                  #Reads the value of x and prints the message for the corresponding message.
        print("Your number says you are hardoworking and a leader")
    elif(x)==2:
        print("You number says you seek peace and harmony")
    elif(x)==3:
        print("You have a high level of creativity and self expression")
    elif(x)==4:
        print("You seem to be hard working and determined")
    elif(x)==5:
        print("The number says you desire freedom and are restless")
    elif(x)==6:
        print("You seem to be family oriented")
    elif(x)==7:
        print("This number says you tend to be loaner")
    elif(x)==8:
        print("The number says you don't feel safe without financial secruity")
    elif(x)==9:
        print("You seem to be a natural leader")
    elif(x)==11:
        print("This number says you are sensitive but you have a great understanding of others")
    elif(x)==22:
        print("You have great spiritual understanding")
    elif(x)==33:
        print("You seem to be a great spiritual leader. The rarest number of all")

    time.sleep(9)

    return(x)
def main():
    '''
     Calls the total function and sets the whole operation off.
    :return:none
    '''
    total()
main()
