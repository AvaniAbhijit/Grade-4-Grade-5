#Task: Make the turtle sleep for different seconds
import turtle
import time
t = turtle.Turtle()
t.color("red")
t.forward(100)
time.sleep(2)
t.color("blue") #Turtle will change color to blue after sleeps.
t.forward(200)
turtle.done()
