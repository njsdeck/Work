import sys
#def check():

    #filename = input("Enter the filename: ")
    #try:
        #file = open(filename, "r")
        #return filename
    #except:
        #print("Invalid file name")
        #sys.exit()
def meta(file,fixedfile):
    line=file.readline()
    problems=0
    while line:
        meta = 0
        br=0
        hr=0
        im=0
        #content=file.readlines()
        line=line.replace("<hr>","<hr />")
        problems+=1
        line=line.replace("<br>", "<br />")
        problems+=1
        fixedfile.write(line)

        line=file.readline()
    print(problems)


#def fixed():
    #new=input("Enter the name for the fixed file.")
    #return new

def main():
    filename = input("Enter the filename: ")

    try:
        file = open(filename, "r")
    except:
        print("Invalid file name")
        sys.exit()
    new=input("Enter the name for the fixed file.")
    if new == filename:
        print("can't name the two files the same thing!")
        sys.exit()
    fixedfile=open(new, "w")
    meta(file,fixedfile)
    fixedfile.close()
    file.close()




main()
