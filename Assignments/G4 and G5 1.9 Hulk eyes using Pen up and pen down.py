# Task for students: Remove the line coming between the two eyes using pen-up and pen-down.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("red")
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)

t.forward(250)

t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.circle(80)
turtle.done()
