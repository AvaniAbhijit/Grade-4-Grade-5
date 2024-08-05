import turtle
t = turtle.Turtle()
#Teacher should show drawing square without loop

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.penup()
t.goto(-100,100)
t.pendown()
for i in range(4):
   t.forward(100)
   t.left(90)
turtle.done()
