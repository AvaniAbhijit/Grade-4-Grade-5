# Task: Color the star using begin_fill(), color("") and end_fill()

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("yellow")

for i in range(5):
   t.begin_fill()
   t.left(144)
   t.forward(100)
   t.end_fill()
#t.hideturtle()
turtle.done()
