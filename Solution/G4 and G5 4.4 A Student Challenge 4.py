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
t2 = turtle.Turtle()

t2.penup()
t2.goto(-45, 30)  # Different position for t2
t2.pendown()
t2.speed(10)
t2.hideturtle()
t2.circle(20)


#Create a new turtle and call it t3. Set the turtle speed to 10. Set the turtle to hide.

t3 = turtle.Turtle()
t3.penup()

t3.goto(75, 30)  # Different position for t3
t3.pendown()
t3.speed(10)
t3.hideturtle()
t3.circle(20)

# Blink the circles repeatedly
for _ in range(10):  # Adjust the range for more blinks
    # Blink t1
    t1.fillcolor("orange")
    t1.begin_fill()
    t1.circle(20)
    t1.end_fill()
    time.sleep(0.01)
    t1.fillcolor("white")
    t1.begin_fill()
    t1.circle(20)
    t1.end_fill()

    # Blink t2
    t2.fillcolor("red")
    t2.begin_fill()
    t2.circle(20)
    t2.end_fill()
    time.sleep(0.01)
    t2.fillcolor("white")
    t2.begin_fill()
    t2.circle(20)
    t2.end_fill()

    # Blink t3
    t3.fillcolor("green")
    t3.begin_fill()
    t3.circle(20)
    t3.end_fill()
    time.sleep(0.01)
    t3.fillcolor("white")
    t3.begin_fill()
    t3.circle(20)
    t3.end_fill()

turtle.done()


