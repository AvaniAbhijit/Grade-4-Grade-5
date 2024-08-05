import turtle

t=turtle.Turtle()
t.color("black")
t.begin_fill()
t.fillcolor("yellow")
t.circle(100)
t.end_fill()
t.penup()
t.goto(-40,120)
t.pendown()
t.circle(20)

t.penup()
t.goto(40,120)
t.pendown()
t.circle(20)

#Task1: Make Smiley using the knowledge from Activity 2.4
t.penup()
t.goto(-50,70)
t.pendown()
t.right(90)
t.circle(50, 180)    # Draws a semi circle

turtle.done()
