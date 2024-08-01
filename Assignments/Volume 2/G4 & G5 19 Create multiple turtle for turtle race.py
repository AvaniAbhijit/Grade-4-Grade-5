# Task 1:- Create 3 more turtles and refer to the blue turtle for code.
# Task 2:- Change the color of all three turtles to red, yellow, and white.

import turtle
from turtle import Turtle

# Setting up the screen
turtle.setup(600, 400)
turtle.bgcolor('tgreen')

# Drawing the finish line
turtle.up()
turtle.goto(200, 200)
turtle.down()
turtle.color('white', 'black')
for i in range(10):
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.up()
    turtle.backward(40)
    turtle.right(90)
    turtle.down()
    turtle.end_fill()
turtle.hideturtle()

# Adding turtles
blue_turtle = Turtle()
blue_turtle.color("blue")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5) #New concept
blue_turtle.penup()
blue_turtle.goto(-285, 150)
blue_turtle.pendown()

#task 1: create second turtle of red colour





#task 2: create third turtle of yellow colour





#task 3: create fourth turtle of white colour






turtle.done()# Write your code here :-)
