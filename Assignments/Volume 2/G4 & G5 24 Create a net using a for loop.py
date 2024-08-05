# Task 1:- Create the vertical grid of the goal post.

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
t.begin_fill()
t.color('green')
for i in range(2):
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
t.end_fill()

#Border of the goal post
t.color('white')
t.up()
t.forward(200)
t.left(90)
t.forward(400)
t.right(90)
t.down()
t.width(5)
for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(100)
    t.right(90)

# Grid Lines for the Goal Post
for i in range(13):
    t.color('white')
    t.up()
    t.forward(15)
    t.width(1)
    t.right(90)
    t.down()
    t.forward(100)
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)

t.up()
t.forward(10)
t.right(90)
t.forward(15)
t.down()


t.done()
