def main():
    c=0
    calc(c)
def calc(c):
    while True:
        x = input("What number would you like to add. Type done to be done.")
        if x == "done":
            print(c)
            return
        else:
            x = int(x)
            c=c+x
main()
