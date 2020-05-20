######################################################################
# Author: Nick Straub-Deck
# Username: straubdeckn
# Assignment: A2
# Purpose: Draw something that made me happy. Show off loops and turtles.
######################################################################
# Acknowledgements:
# Original Author: Nick Straub-Deck
######################################################################
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
sam = turtle.Turtle()
sam.hideturtle()                        #Hiding the turtle so it doesn't get visually in the way
bill = turtle.Turtle()
bill.hideturtle()
jill = turtle.Turtle()
jill.hideturtle()
jill.speed(8)
jack = turtle.Turtle()
jack.hideturtle()
jack.shape("circle")
jack.color("white")
jack.pensize(3)
jack.speed(3)
jack.pencolor("grey")
sam.pencolor("blue")
sam.pensize(2)
sam.speed(3)
sam.penup()
sam.back(200)               #Next four lines are moving it to the bottom left corner so it can prepare to draw.
sam.right(90)
sam.forward(150)
sam.left(90)
sam.pendown()
for i in range(4):          # Drawing square
    sam.forward(400)
    sam.left(90)
jack.penup()                # Early penup so i don't have to write it later.
bill.pencolor("red")
bill.speed(3)
bill.penup()
bill.right(90)    # Bill is now positioning
bill.forward(60)
bill.left(90)
bill.forward(150)
bill.pendown()
jack.left(90)     # More early poistioning for later drawings
jack.forward(70)
jack.right(90)
jack.forward(20)
for f in range(3): # Drawing the triangle
    bill.left(120)
    bill.forward(300)
for g in range(180):    # Drawing the circle
    jill.forward(2)
    jill.left(2)
jack.stamp()        # Stamping out the eyes for jacks position we put him in earlier
jack.left(180)
jack.forward(40)
jack.stamp()
jack.left(90)
jack.forward(15)
jack.pendown()
for g in range(60):      # Drawing the mouth
    jack.forward(1)
    jack.left(3)
wn.exitonclick()
