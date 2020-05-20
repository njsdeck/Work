import turtle

def modulo():
    bar = []
    code = (input("Put in a valid 12 digit bar code"))
    if len(code) > 12:
        print("to long")
        modulo()
    elif len(code) <12:
        print("not enough")
        modulo()
    for i in code:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            bar.append(i)
        else:
            print("error")
            modulo()
    odd=int(bar[0]) + int(bar[2]) + int(bar[4]) + int(bar[6]) + int(bar[8]) + int(bar[10])
    even=int(bar[1]) + int(bar[3]) + int(bar[5]) + int(bar[7]) + int(bar[9]) + int(bar[11])
    even*=3
    sum=even + odd

    if sum%10 !=0:
        modul= 10-(sum%10)
    else:
        modul=0
    if modul == int(bar[11]):
        return bar
    else:
        print("bad")
        modulo()

def binary_left(i):
    newlist=["0001101",
             "0011001",
             "0010011",
             "0111101",
             "0100011",
             "0110001",
             "0101111",
             "0101111",
             "0110111",
             "0001011"]
    x = newlist[i]
    return x
def binary(list):
    q = []
    count = 0
    for i in range(12):
        if count <= 5:
            q.append(binary_left(int(list[i])))
            count+=1
        else:
            q.append(binary_right(int(list[i])))
            count+=1
    print(q)


def binary_right(i):

    rightlist=["1110010",
               "1100110",
               "1101100",
               "1000010",
               "1011100",
               "1001110",
               "1010000",
               "1000100",
               "1001000",
               "1110100"]
    x = rightlist[i]
    return x
def turtle_drawing():
    wn=turtle.Screen()
    wn.bgcolor("PeachPuff")
    reader=turtle.Turtle()
    reader.pensize(1)
    reader.speed(0)
    reader.hideturtle()


    if num == 1:
        reader.begin_fill()
        reader.fillcolor("black")
        reader.left(90)
        reader.forward(110)
        reader.left(90)
        reader.forward(3)
        reader.left(90)
        reader.forward(110)
        reader.left(90)
        reader.forward(6)
        reader.end_fill()
        wn.exitonclick()




def turtle(turt,value, guardbar=False,):
    print("hi")




def main():
    list=modulo()
    binary(list)
    #turtle_drawing()

main()
