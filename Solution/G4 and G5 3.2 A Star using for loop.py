#Task 1: Make the star smaller
#Task 2: Create another different size star at some distance from the first star.

import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# for i in range(5): #Initialising loop to draw star
#    t.left(144)     #Rotating turtle 144 degrees to the left
#    t.forward(100)

#Task 1: Make the star smaller solution
t = turtle.Turtle()
t.shape("turtle")
for i in range(5): #Initialising loop to draw star
   t.left(144)     #Rotating turtle 144 degrees to the left
   t.forward(85)

#Task 2: Create another different size star at some distance from the first star solution.
t.penup()
t.goto(-100,100)
t.pendown()
for i in range(5): #Initialising loop to draw star
   t.left(144)     #Rotating turtle 144 degrees to the left
   t.forward(50)
turtle.done()
