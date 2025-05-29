from turtle import *

t = Turtle()

t.pensize(2)
t.speed(1)
t.up()
t.goto(-50,50)
t.down()
t.color("red")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.rt(144)
t.end_fill()
exitonclick()