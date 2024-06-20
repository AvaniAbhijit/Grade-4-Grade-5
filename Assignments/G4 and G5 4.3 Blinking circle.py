import turtle
import time

t1 = turtle.Turtle()
t1.penup()
t1.goto(15,30)
t1.pendown()
t1.hideturtle()
t1.speed(10)
t1.color("white")

# Draw the face
for i in range(8):
  t1.fillcolor("black")
  t1.begin_fill()
  t1.circle(20)
  t1.end_fill()

  time.sleep(0.001)
  t1.fillcolor("white")
  t1.begin_fill()
  t1.circle(20)
  t1.end_fill()
  time.sleep(0.001)

turtle.done()
