import turtle
import time

from turtle import *
from random import *
speed(0)
stamp()
title('Turtle Race')
up()
goto(-50,230)
down()
write('Turtle Race',font=("Arail",20,'bold'))
setup(600,400)
bgcolor('forestgreen')
up()
goto(-300, 200)
down()
color('black','#e08312')
begin_fill()
for i in range(2):
    forward(600)
    right(90)
    forward(400)
    right(90)
end_fill()


up()
home()
goto(200, 200)
down()
color('white','black')
for i in range(10):
    begin_fill()
    forward(30)
    right(90)
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(40)
    up()
    backward(40)
    right(90)
    down()
    end_fill()
up()
home()
backward(100)
down()
blue_turtle = Turtle()
blue_turtle.color("#045edb")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5)
red_turtle.penup()
red_turtle.goto(-300, 50)
red_turtle.pendown()


yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()


white_turtle = Turtle()
white_turtle.color("white")
white_turtle.shape("turtle")
white_turtle.shapesize(1.5)
white_turtle.penup()
white_turtle.goto(-300, -150)
white_turtle.pendown()


while blue_turtle.xcor() <= 200 and red_turtle.xcor() <= 200 and yellow_turtle.xcor() <= 200 and white_turtle.xcor() <= 200:
    blue_turtle.forward(randint(1,10))
    red_turtle.forward(randint(1,10))
    yellow_turtle.forward(randint(1,10))
    white_turtle.forward(randint(1,10))

if blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor() > yellow_turtle.xcor() and blue_turtle.xcor() >  white_turtle.xcor() :
    print('blue wins')
    write('Blue wins',font=('arail', 20, 'bold'))
    color('black')
    for i in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.5)


elif red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor() > yellow_turtle.xcor() and red_turtle.xcor() >  white_turtle.xcor() :
    print('red wins')
    red_turtle.shapesize(2.5)
    color('black')
    write('Red wins',font=('arail', 20, 'bold'))
    for i in range(72):
        red_turtle.right(5)
        red_turtle.shapesize(2.5)

elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > red_turtle.xcor() and yellow_turtle.xcor() >  white_turtle.xcor() :
    print('blue wins')
    yellow_turtle.shapesize(2.5)
    color('black')
    write('Yellow wins',font=('arail', 20, 'bold'))
    for i in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.5)

else:
    print('white wins')
    white_turtle.shapesize(2.5)
    color('black')
    write('White wins',font=('arail', 20, 'bold'))
    for i in range(72):
        white_turtle.right(5)
        white_turtle.shapesize(2.5)
