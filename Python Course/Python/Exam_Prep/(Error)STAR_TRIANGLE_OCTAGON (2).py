from turtle import *
t=Turtle()
t.pensize(2)
t.speed(0)
t.up()
t.goto(-160,160)
t.down()
for i in range(4):      #Draws A Big Triangle
    t.fd(320)
    t.rt(90)
start_x=-160
start_y=160
squaresize=40
for row in range(8):
    for col in range(8):
        x = start_x + col * squaresize  #Loop 1 = 160 
        y = start_y + col * squaresize  #loop 1 = 480
        if (row + col) % 2 == 0:
            t.fillcolor("White")
        else:
            t.fillcolor("black")
        t.penup()
        t.goto(x,y)
        t.pendown()
        for i in range(4):
            t.fd(squaresize)
            t.rt(90)
        t.end_fill()
    