import matplotlib.pyplot as plotter
data=[]
new=[]
replace=[",",'""','.','?',"!"]
def main():
    total,repeat=choice()
    print(total)
    print(repeat)
    percentage(total,repeat)
def line(replace,filename):
    #counter=[]
    #filename = input("Please type the name of the text file you wish to open. Please include the .txt.")
    total=0
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            for i in replace:
                line=line.replace(i, "")
            print(line)
            if line in new:
            #if new.count(line) > 0:
                repeat+=1
                # line=line.strip("\n")
                # data.append(line)
            else:
                new.append(line)
            total+=1
        # for i in new:
        #     check=data.count(i)
        #     if check==0:
        #         pass
        #     else:
        #         counter.append(check)
    #print(counter)
    f.close()
    #print(data)
    return total,repeat
def word(replace,filename):
    #filename = input("Please type the name of the text file you wish to open. Please include the .txt.")
    total=0
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            for i in replace:
                line=line.replace(i, "")
            for word in line.split():
                print(word)
                if new.count(word) > 0:
                    repeat+=1
                else:
                    new.append(word)
                total+=1
        f.close()
        return total,repeat
def percentage(total,repeat):
    percent = repeat/total*100
    print("This file repeats " +str(percent) + "% of the time.")
def choice():
    filename = input("Please type the name of the text file you wish to open. Please include the .txt.")
    choice = input("Type 1 for counting each line. 2 for each word.")
    if choice == "1":
        total,repeat = line(replace,filename)
        return total,repeat
    if choice == "2":
        total,repeat = word(replace,filename)
        return total,repeat
    if choice != "1" and choice != "2":
        print("Wrong answer please try again.")
        main()
main()
