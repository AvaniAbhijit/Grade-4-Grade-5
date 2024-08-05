import turtle


turtle.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.speed(1)

#Change position of the turtle to left and change color to red.
t.goto(-100,0)
if t.xcor()<0:
  t.color("red")

#change position of the turtle to right and change color to blue.
t.goto(100, 0)
if t.xcor() > 0:
    t.color("blue")

#Change position of the turtle to left and change color to green.
t.goto(-100, 0)
if t.xcor() < 0:
    t.color("green")

#Change position of the turtle to right and change color to yellow.
t.goto(100, 0)
if t.xcor() > 0:
    t.color("yellow")

turtle.done()
