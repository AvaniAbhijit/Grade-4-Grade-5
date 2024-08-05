# Task 1:- Create 3 more turtles and refer to the blue turtle for code.
# Task 2:- Change the color of all three turtles to red, yellow, and white.
# Task 3:- Change the goto position of the turtles on the Y-axis of red, yellow, and white to 50, -50, and -150 respectively.

import turtle
from turtle import Turtle

# Setting up the screen
turtle.setup(600, 400)
turtle.bgcolor('saddle brown')

# Drawing the finish line
turtle.up()
turtle.goto(200, 200)
turtle.down()
turtle.color('white', 'black')
for i in range(10):
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
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
red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5) #New concept
red_turtle.penup()
red_turtle.goto(-285, 150)
red_turtle.pendown()




#task 2: create third turtle of yellow colour
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5) #New concept
yellow_turtle.penup()
yellow_turtle.goto(-285, 150)
yellow_turtle.pendown()





#task 3: create fourth turtle of white colour
white_turtle = Turtle()
white_turtle.color("white")
white_turtle.shape("turtle")
white_turtle.shapesize(1.5) #New concept
white_turtle.penup()
white_turtle.goto(-285, 150)
white_turtle.pendown()





turtle.done()
