######################################################################
#Author: Nick Straub-Deck
#Username: straubdeckn
#
# Assignment: A3
# Purpose: Learn about the different color methods and complex turtle drawings.
######################################################################
#Acknowledgements
#Original Author: Nick Straub-Deck
######################################################################
import turtle
def make_chimney_and_smoke(a,b,c,d,turn,tur):
    """
 Creates the chimney on the roof and the smoke coming from the chimney.
    :param a: x cord for chimney starting point
    :param b: y cord for chimney starting point
    :param c: x cord for smoke starting point
    :param d: y cord for smoke starting point
    :param turn: 90 degree turn
    :param tur: cry the turtle
    :return: none
    """
    tur.pencolor("Red") #Preparing the turtle for drawing.
    tur.penup()
    tur.speed(0)
    tur.setpos(a,b)
    tur.pendown()
    tur.begin_fill()
    tur.fillcolor("red")
    tur.left(turn)    #Starting the creation of the chimney.
    tur.forward(70)
    tur.right(turn)
    tur.forward(40)
    tur.right(turn)
    tur.forward(70)
    tur.end_fill() #End of chimney creation.
    tur.penup()
    tur.right(turn) #getting into position to create the smoke.
    tur.forward(40)
    tur.right(turn)
    tur.forward(70)
    tur.pendown()
    tur.left(45)
    tur.pencolor("grey")
    for i in range(4):      #Calls the function that creates a smoke section four times.
        for g in range(20): #creates a section of smoke
            tur.forward(2)
            tur.right(3)
        tur.left(45)
    tur.penup()
    tur.setpos(c,d)  #Setting position for the other smoke half.
    tur.pendown()
    tur.right(45)
    for i in range(4):  #same as before just turning left instead of right.
        for g in range(20):
            tur.forward(2)
            tur.left(3)
        tur.right(45)
def draw_tiles(sz,angle,mike):  #just setting up the function. It will be called later to make the horizontal lines.
    """
    Draws the shrinking horizontal lines
    :param sz: size
    :param angle: 135 degree turn
    :param mike: turtle
    :return: none
    """
    mike.pendown()   #Drawing the first horizontal line.
    mike.forward(sz)
    mike.left(angle)
    mike.penup() # Positioning for the next line
    mike.forward(20)
    mike.left(45)
    mike.pendown()
    mike.forward(sz-27) #Subtract the recent line created by 27.
    mike.right(angle)
    mike.penup()
    mike.fd(20)
    mike.right(45)
def draw_building(x,y,z,v):
    '''
    Draw the building and the roof
    :param x: starting x cord for door
    :param y: starting why cord for door
    :param z: starting c cord for the building
    :param v: strting y cord for the building
    :return: none
    '''
    nick = turtle.Turtle()
    mill = turtle.Turtle()
    mill.hideturtle()
    mill.penup()
    mill.speed(0)
    mill.setpos(x,y)  #Prepping the turtle for future door drawing.
    mill.pendown()
    nick.hideturtle()
    nick.penup()
    nick.speed(0)
    nick.setpos(z,v) #Setting the turtle to start drawing the building
    nick.pendown()
    nick.begin_fill()
    nick.left(45) #Drawing the roof structure.
    nick.fd(100)
    nick.right(45)
    nick.fd(200)
    nick.right(45)
    nick.fd(100)
    nick.end_fill()
    nick.right(135)
    nick.begin_fill()
    nick.fillcolor("blue")
    for i in range(2):  #Draws one half of the building
        nick.fd(340)
        nick.left(90)
        nick.fd(300)
        nick.left(90)
    nick.end_fill()
    mill.pencolor("brown")    # setting to brown so it blends with the future fill.
    mill.begin_fill()
    mill.fillcolor("brown")
    mill.left(90)              # starts the drawing of our door.
    mill.fd(50)
    mill.right(90)
    mill.fd(30)
    mill.right(90)
    mill.fd(50)
    mill.end_fill()
def make_tiles(e,f,angle,mike,turn,go):
    '''
    Calls the horizontal line function  while also creating the diagonal lines.
    :param e: starting x point for vertical shingles
    :param f: startying y point for vertical shingles
    :param angle: 135 degree turn
    :param mike: turle
    :param turn: 90 degree turn
    :param go: move forward 15
    :return: none
    '''
    size = 320
    for i in range(2):           # call the draw _tiles function twice.
        draw_tiles(size,135,mike)
        for i in range(2):              # not 100% sure why but I needed to have this run twice for it to work.
            size = size - 26
    em = turtle.Turtle()
    em.hideturtle()
    em.pencolor("grey")
    em.speed(0)
    em.penup()
    em.setpos(e,f)   #prep the turtle for the diagonal lines for shingles.
    em.pencolor("white")
    em.pendown()
    for i in range(12):  # Draws the diagonal lines on the roof that remain the same length.
        em.right(angle)
        em.fd(100)
        em.left(angle)
        em.penup()
        em.forward(go)
        em.left(45)
        em.pendown()
        em.forward(100)
        em.right(45)
    em.penup()   #The rest of the function just draws the smaller lines on the right roof side.
    em.fd(5)   #I would of made this into less code but i have no idea what the math is doing.
    em.right(angle)
    em.forward(100)
    em.left(angle)
    em.fd(go)
    em.left(45)
    em.pendown()
    em.fd(90)
    em.right(turn)
    em.penup()
    em.fd(go)
    em.right(turn)
    em.pendown()
    em.fd(75)
    em.left(angle)
    em.penup()
    em.fd(go)
    em.left(45)
    em.pendown()
    em.fd(65)
    em.right(turn)
    em.penup()
    em.fd(go)
    em.right(turn)
    em.pendown()
    em.fd(50)
    em.left(angle)
    em.penup()
    em.fd(go)
    em.left(45)
    em.pendown()
    em.fd(37)
    em.right(turn)
    em.penup()
    em.fd(go)
    em.right(90)
    em.pendown()
    em.fd(24)
def make_windows(g,h,c,ch):
    '''
    Makes a window and pane dividers.
    :param g: starting x cord for the window
    :param h: starting y cord for the window
    :param c: cry the turtle
    :param ch: 90 degree turn
    :return: none
    '''
    c.penup()
    c.setpos(g,h)
    c.pendown()
    c.begin_fill()
    c.fillcolor("white")
    for i in range(3): #Drawing a side of the window.
        c.fd(40)
        c.right(ch)
    c.fd(40)
    c.right(180)
    c.end_fill()  #Finishing the window and making it white.
    c.fd(20)  #The rest of the code makes the seperate pane indicators.
    c.left(ch)
    c.fd(20)
    c.right(ch)
    c.back(20)
    c.fd(40)
    c.back(20)
    c.left(ch)
    c.fd(20)
def main():
    wn = turtle.Screen()
    wn.colormode(255)
    wn.bgcolor(255, 218, 185)  #The color is peach
    cry = turtle.Turtle()   #setting up future turtles
    cry.hideturtle()
    cry.speed(0)
    mike = turtle.Turtle()
    mike.pencolor("white")
    mike.hideturtle()
    mike.penup()
    mike.speed(0)
    mike.setpos(-190,110)  #Prepping mike for his future job.
    draw_building(-40,-200,-200,100)
    make_tiles(-114,171,135,mike,90,15)
    make_windows(50, 50,cry,90)  #calling the function four times for four windows.
    make_windows(-150, 50,cry,90) # the paramaters called are different so the widows are made in a new location.
    make_windows(50, -100,cry,90)
    make_windows(-150, -100,cry,90)
    make_chimney_and_smoke(-130,170,-90,240,90,cry)
    wn.exitonclick()
main()
