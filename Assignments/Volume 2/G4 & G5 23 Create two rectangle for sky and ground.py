# Task 1:- Create a grass (green rectangle) of size 800x400
# Refer the code lines 13 to 20.

import turtle as t

# Background and field setup
t.speed(0)
t.up()
t.backward(450)
t.down()

# Sky (Blue Rectangle)
t.begin_fill()
t.color('sky blue')
for i in range(2):
    t.forward(800)
    t.left(90)
    t.forward(250)
    t.left(90)
t.end_fill()

t.up()
t.right(90)
t.forward(350)
t.left(90)
t.down()

# Grass (Green Rectangle)


t.done()
