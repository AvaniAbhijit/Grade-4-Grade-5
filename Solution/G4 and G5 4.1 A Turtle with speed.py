#Task: Change the value of the speed
#Q1: What is the maximum value of speed you can put?
# Ans : The maximum value for speed is 0. This sets the turtle to the fastest possible speed, where it will instantly move to its destination.
#Q2: What is the minimum value of speed you can put?
# Ans : The minimum value for speed is 1. This sets the turtle to the slowest possible speed, where it moves very slowly.

import turtle
t = turtle.Turtle()
t.speed(1)
t.forward(250)
turtle.done()
