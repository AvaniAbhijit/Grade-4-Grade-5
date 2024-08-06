# Run the code and check output.
# Task1:- Add the function for right key event refer the code from lines 160 to 165 (Change to x += 20).
# Task2:- Uncomment the code in the line 176 to perform the right key event.

import turtle as t
import random

t.speed(0)
t.up()
t.backward(450)
t.down()
t.begin_fill()
t.color('#54c6ff')
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

t.begin_fill()
t.color('#0bb828')
for i in range(2):
    t.forward(800)
    t.left(90)
    t.forward(400)
    t.left(90)
t.end_fill()

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

for i in range(5):
    t.right(90)
    t.forward(400)
    t.up()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.down()
    t.forward(400)
    t.right(90)
t.up()
t.forward(12)
t.right(90)

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.backward(400)
t.down()

t.forward(800)
t.up()
t.backward(400)
t.left(90)
t.forward(50)
t.right(90)
t.down()
t.circle(-50)
t.up()
t.right(90)
t.forward(50)
t.left(90)
t.forward(330)
t.left(90)
t.down()
t.forward(70)
t.right(180)
t.begin_fill()
t.color('red')
for i in range(3):
    t.forward(30)
    t.left(120)
t.end_fill()
t.up()
t.backward(400)
t.down()
t.width(2)
t.color("#f5f3ed")
t.circle(10, 150)
t.hideturtle()

# Create a turtle and set the GIF image as its shape
t.register_shape("player.gif")
player = t.Turtle()

player.up()
# to change the player x y position
player.goto(50, -60)
player.down()
player.shape("player.gif")

# Create a turtle and set the GIF image as its shape
t.register_shape("player_BV.gif")
player1 = t.Turtle()

player1.up()
# to change the player x y position
player1.goto(60, -210)
player1.down()
player1.shape("player_BV.gif")

t.register_shape("football30.gif")
football = t.Turtle()

# Set initial position of the football
football.up()
football.goto(90,-250)
football.down()
football.shape("football30.gif")

# Move the football to a random x-coordinate between 50 and 150, y-coordinate fixed at -80
random_x = random.randint(10, 200)
target_y = -80
football.speed(0)
football.up()
football.goto(random_x, target_y)


# Define movement functions for the player left.
def move_left():
    x = player.xcor()
    player.up()
    x -= 20
    player.setx(x)

# Define movement functions for the player right.
def move_right():
    x = player.xcor()
    player.up()
    x += 20
    player.setx(x)


# Keyboard bindings
t.listen()
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")

t.done()

