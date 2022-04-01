def main():
    read()
def read():
    list = []
    with open('char.txt', 'a') as file:
        for line in file:
            line=line.strip("\n")
            for letter in line.split():
main()
