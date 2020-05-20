######################################################################
# Author: Nick Straub-Deck
# Username: straubdeckn
#
# Assignment: A8: Error Testing
#
# Purpose: Practice using test functions
#
######################################################################
# Acknowledgements:
#   Original Author: Nick Straub-Deck
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys
def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def parity_test_suite():
    #making sure the input is actually binary.
    testit(is_binary("1100010") == True)
    testit(is_binary("1120010") == False)
    testit(is_binary("11100100") == True)
    testit(is_binary("110001") == False)
    testit(is_binary("-1100010") == False)
    testit(is_binary("1100111")== True)
    #Checking the function to see if it is divisable by 7.
    testit(is_div_by_sevens("10110101") == False)
    testit(is_div_by_sevens("1100111") == True)
    testit(is_div_by_sevens("11001110110101") == True)
    testit(is_div_by_sevens("110011") == False)
    #testing the split into 7.
    testit(split_into_sevens("1100110") == ["1100110"])
    testit(split_into_sevens("11001100110101") == ["1100110", "0110101"])
    testit(split_into_sevens("110011001111111111111") == ["1100110","0111111","1111111"])
    #testing the splits and adding the parity.
    testit(check("1111111")== [['1', '1', '1', '1', '1', '1', '1', '1']])
    testit(check("1010111")== [['1', '1', '0', '1', '0', '1', '1', '1']])
    testit(check("11111111111111")==[['1','1','1','1','1','1','1','1'],['1','1','1','1','1','1','1','1']])


def is_binary(binary):
    ''' To test if the input is a binary number
    :param binary: The binary input.
    :return: True or false
    '''

    for i in binary:
        if i !="1" and i != "0":    # seeing if each part of binary is a one or zero. If they arn't this returns it false.
            return False
    if len(binary)>6:  # seeing if the input is longer then 6 digits.
        return True
    else:
        return False
def is_div_by_sevens(binary):
    '''
    Checks to see if the user input divides into 7 with no remainder.
    :param binary: The input from the user
    :return: true or false
    '''
    if len(binary)%7==0:  #checking to see if the binary paramater divides into 7 evenly.
        return True
    else:
        return False
def split_into_sevens(binary):
    '''
    slits the user input that has been checked into groups of 7
    :param binary: User input that has been checked from the previous functions
    :return: final, the group of chunks
    '''
    final=[] #prepping a list to deposit into
    count=0  # prepping a counter
    pre="" # prepping a starting string
    for i in binary:
        pre=pre+i # adding the value into the string from earlier
        count=count+1
        if count%7==0:  # when the count reaches 7
            final=final+[pre]# converts the pre string into a list and adds it into the final string
            count=0# resets the counters and empties the pre string
            pre=""
    return final
def check(chunks):
    '''
    Add the parity bit to the chunks of code from earlier.
    :param chunks:The group of chunks from the split into seven function
    :return: Finallist. The list with the parity bit appended.
    '''
    newlist=[]# prepping lists and counters.
    finallist=[]
    s=0
    x=0
    for i in chunks:
        for j in i:# getting into the values directly
            x+=1
            newlist.append(j)# adds the value to newlist
            if j == '1': # starts the process of adding the ones together.
                s+=1
            if x==7:# when seven values have passed, or one chunk, set the x to zero
                x=0
                if s%2==0: # if the 1s added are even then prepend a zero
                    newlist[:0]="0"
                if s%2==1:# if the 1s added are odd then prepend a 1
                    newlist[:0]="1"
                s=0#Resets the 1 addition value for the next group
                finallist.append(newlist)# append the newlist to final list
                newlist=[]# reset newlist
    print(finallist)
    return(finallist)
def main():
    '''
Run everything
    :return:none
    '''
    binary=input("enter a seven digit ASCII")
    if is_binary(binary) == True:# prevents continuation of the function if the input is wrong
        is_div_by_sevens(binary)
    if is_div_by_sevens(binary) == True:
        check(split_into_sevens(binary))


    #parity_test_suite()
main()


