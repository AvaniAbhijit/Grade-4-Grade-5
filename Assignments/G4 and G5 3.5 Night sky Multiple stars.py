import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.color("white")
t.penup()
t.goto(250,200)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

#Drawing Star-1
t.penup()
t.goto(-100,200)
t.color("white")
t.pendown()
t.begin_fill()
for i in range(5):
  t.forward(40)
  t.left(144)
t.end_fill()

##Student task to draw star-2 at different location.
#Student task to draw star-3 at different location.





t.hideturtle()
turtle.done()
