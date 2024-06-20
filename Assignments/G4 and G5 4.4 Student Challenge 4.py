#Student Challenge to to create multiple blinking circles. Complete the given code.
import turtle
import time
t1 = turtle.Turtle()
t1.penup()
t1.goto(15,30)
t1.pendown()
t1.speed(10)
t1.hideturtle()
t1.circle(20)

#Create a new turtle and call it t2. Set the turtle speed to 10. Set the turtle to hide.



#Create a new turtle and call it t3. Set the turtle speed to 10. Set the turtle to hide.

t1.fillcolor("red")
t1.begin_fill()
t1.circle(20)
t1.end_fill()

time.sleep(0.01)
t1.fillcolor("white")
t1.begin_fill()
t1.circle(20)
t1.end_fill()

#Give sleep and time delay of 0.01 seconds for turlte t2.


#Give sleep anf time delay of 0.01 seconds for turlte t3.
turtle.done()
