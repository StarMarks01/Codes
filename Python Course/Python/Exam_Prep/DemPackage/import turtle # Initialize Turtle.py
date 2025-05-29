import turtle # Initialize Turtle 
t = turtle.Turtle()
t.speed(10) #
# Function to draw a horizontal line def

t.penup() 
t.goto(x1, y1) 
t.pendown()
t.goto(x2, y2) # Draw Tic-Tac-Toe board t.width(3) t.color('black')
t.penup() 
t.goto(-150, 50) 
t.pendown() 
t.forward(300) 
t.penup()
t.goto(-150, -50) 
t.pendown() 
t.forward(300) 
t.penup() 
t.goto(-50,150)
t.setheading(-90)
t.pendown()
t.forward(300)
t.penup()
t.goto(50, 150) 
t.pendown() 
t.forward(300) # Keep the window open
turtle.done()
