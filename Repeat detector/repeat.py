new=[]
def main():
    filename = input("Please type the name of the text file you wish to open. Please include the .txt.")
    total,repeat = count(filename)
    print(total)
    print(repeat)
    percentage(total,repeat)
def count(filename):
    total=0
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            for word in line.split():
                if new.count(word) > 0:
                    repeat+=1
                else:
                    new.append(word)
                total+=1
    f.close()
    return total,repeat
def percentage(total,repeat):
    percent = repeat/total
    percent = percent*100
    print(percent)
main()
