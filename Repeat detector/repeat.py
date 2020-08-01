from matplotlib import pyplot as plt
import numpy as np
data=[]
new=[]
replace=[",",'""','.','?',"!"]
def main():
    total,repeat,counter=choice()
    print(total)
    print(repeat)
    percentage(total,repeat)
    #graph(data,counter)
def line(replace,filename):
    counter=[]
    total=0
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            for i in replace:
                line=line.replace(i, "")
                line=line.strip("\n")
            print(line)
            if line in new:
            #if new.count(line) > 0:
                repeat+=1
                data.append(line)
            else:
                new.append(line)
            total+=1
    #     for g in new:
    #         print(g)
    #         check=data.count(g)
    #         if check==0:
    #             continue
    #         else:
    #             counter.append(check)
    # print(counter)
    # print(data)
    f.close()
    return total,repeat,counter
def word(replace,filename):
    counter=[]
    total=0
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            for i in replace:
                line=line.replace(i, "")
                line=line.strip("\n")
            for word in line.split():
                print(word)
                if new.count(word) > 0:
                    repeat+=1
                else:
                    new.append(word)
                total+=1
            # for g in new:
            #     #print(g)
            #     check=data.count(g)
            #     if check==0:
            #         continue
            #     else:
            #         counter.append(check)
        f.close()
        return total,repeat,counter
def percentage(total,repeat):
    percent = repeat/total*100
    print("This file repeats " +str(percent) + "% of the time.")
def choice():
    filename = input("Please type the name of the text file you wish to open. Please include the .txt.")
    choice = input("Type 1 for counting each line. 2 for each word.")
    if choice == "1":
        total,repeat,counter = line(replace,filename)
        return total,repeat,counter
    if choice == "2":
        total,repeat,counter = word(replace,filename)
        return total,repeat,counter
    if choice != "1" and choice != "2":
        print("Wrong answer please try again.")
        main()
# def graph(data,counter):
#     labels=data
#     fig = plt.figure(figsize =(100,70))
#     plt.pie(counter, labels = data)
#     plt.show()
#     print("You reached graph.")
main()
