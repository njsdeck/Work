######################################################################
# Author: Nick Straub-Deck
# Username: straubdeckn
#
# Assignment: A9 XHTML
#
# Purpose: Create a file to fix HTML errors
######################################################################
# Acknowledgements: Tradd Schmidt
#
#

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys
def first():
    '''
    Used to get the input for the file you want to use, then checks to see if it is valid.
    :return: the name of the file, and the file itself.
    '''
    filename = input("Enter the filename: ") # Asks what file you want to open.
    try:
        file = open(filename, "r") # Opens the name for the file.
        return file, filename #returns both the name and the file itself
    except:
        print("Invalid file name")# prints if the file name isn't in the same path as the one you specified.
        sys.exit()  #cancels the program
def new(filename):
    '''
    Takes the input of the file you want to wrtie to and makes sure it isn't the same ame as the previous file.
    :param filename:name of the file you wanted to draw from.
    :return: the name of the file you want to write to.
    '''
    new=input("Enter the name for the fixed file.") #Creates a file to write to.
    if new == filename:
        print("can't name the two files the same thing!") # if the new file is the same as the old it cancels
        sys.exit()
    return new
def closed(line):
    '''
    Checks to see if certain things are in the string, then adds the closing slash and > in the are.
    :param line:The line of text being read at the time.
    :return: the empty string and the amount of problems that occured.
    '''
    empty=""
    if "<me" in line or "<br" in line or "<im"in line or "<hr" in line: # checks for the errors in the line.
        empty +=(line[:-2] + " />\n") #if there is a error adds the closing and enter equivelent to the end of the line.
        problem=1 # sets the amount fixed to one per error.
    else:
        empty+=line # if no errors just puts the whole string like it was normally
        problem=0
    return empty,problem
def fixed(file):
    '''
    Reads the lines and sends the lines to the closed function to be fixes them then takes them back.
    :param file: The file you wanted to read from
    :return: The stored fixed lines and the amount of problems that occured.
    '''
    line=file.readline()
    empty=""
    problem=0
    while line: # while a line is being read do the following function then add it the corresponding groups.
        i, problems=closed(line)
        empty+=i
        problem+=problems
        line=file.readline()
    print(empty)
    return empty,problem
def written(fixedfile, fixed):
    '''
    Writes to the new file you wanted to rite to.
    :param fixedfile: filename you wanted to write to.
    :param fixed: The error free file.
    :return:none
    '''
    fixedfile=open(fixedfile,"w") # actually opens fixedfile to write to.
    fixedfile.write(fixed) # writes the fixed lines into the file
    return fixedfile
def main():
    used_file, name=first()
    fixedone=new(name)
    complete, problems=fixed(used_file)
    print( "There were " + str(problems) + " errors in the file.")
    written(fixedone,complete)
main()
