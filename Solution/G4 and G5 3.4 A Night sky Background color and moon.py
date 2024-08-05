#Make the moon at top right corner of the screen
#Hint: You can use either forward or goto, but moon color is white.

import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()
t.hideturtle()

turtle.done()
