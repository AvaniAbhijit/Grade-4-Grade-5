# Task 1:- Change the background color to "saddle brown".
# Task 2:- Increase the width of the boxes of the finish line.

import turtle

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
    turtle.forward(50) #Increase the size here
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50) #Increase the size here
    turtle.right(90)
    turtle.forward(40)
    turtle.up()
    turtle.backward(40)
    turtle.right(90)
    turtle.down()
    turtle.end_fill()
turtle.done()
