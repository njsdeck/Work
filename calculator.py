def main():
    calc()
def calc():
    #c=0
    choice = input("What would you like to use? Type + for add,- for subtract, * for multiply, / for divide.")
    if choice == '+':
        c=0
        while True:
            x = input("What number would you like to add. Type done to be done.")
            if x == "done" or x == "Done":
                print(c)
                return
            else:
                x = float(x)
                c+=x
    elif choice == '/':
        while True:
            x = input("What number would you like to divide. Type done to be done.")
            if x == "done" or x == "Done":
                print(c)
                return
            else:
                x = float(x)
                c/=x
    elif choice == '*':
        c=1
        while True:
            x = input("What number would you like to multiply. Type done to be done.")
            if x == "done" or x == "Done":
                print(c)
                return
            else:
                x = float(x)
                c*=x
    elif choice == '-':
        while True:
            x = input("What number would you like to subtract. Type done to be done.")
            if x == "done" or x == "Done":
                print(c)
                return
            else:
                x = float(x)
                c-=x
main()
