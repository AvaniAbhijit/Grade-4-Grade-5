#Task: Make the turtle sleep for different seconds
import turtle
import time

t = turtle.Turtle()

# Move forward and sleep for 2 seconds
t.color("red")
t.forward(100)
time.sleep(2)

# Change color to blue, move forward, and sleep for 1 second
t.color("blue")
t.forward(100)
time.sleep(1)

# Change color to green, move forward, and sleep for 3 seconds
t.color("green")
t.forward(100)
time.sleep(3)

# Change color to yellow and move forward
t.color("yellow")
t.forward(100)

turtle.done()
