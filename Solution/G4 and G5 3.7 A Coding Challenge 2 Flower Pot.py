import turtle
t = turtle.Turtle()
turtle.bgcolor('#f5e1ba') #bgcolor
t.penup()
t.goto(0,-200)
t.backward(100)
t.pendown()
t.begin_fill()
t.color('black','#8a5c01') #pot color
t.forward(150)
t.left(60)
t.forward(200)
t.left(120)
t.forward(350)
t.left(180)
t.right(60)
t.forward(200)

t.penup()
t.left(60)
t.forward(75)
t.left(90)
t.forward(175)
t.pendown()
t.end_fill()

t.width(5)
t.color('green') #line
t.forward(250)
t.left(90)

t.begin_fill()
t.color('red')  #flower color
for i in range(6):
    t.circle(100-i,90)
    t.left(90)
    t.circle(100-i,90)
    t.left(30)
t.end_fill()

t.penup()
t.right(90)
t.forward(20)
t.left(90)
t.pendown()
#t.forward(200)
t.begin_fill()
t.color('#f5e556') #inside flower yellow
t.circle(20)
t.end_fill()

t.penup()
t.left(90)
t.forward(200)
t.left(90)
t.pendown()

t.begin_fill()
t.color('green') #leaf color
t.left(90)
t.circle(50,90)
t.left(90)
t.circle(50,90)

t.penup()
t.right(90)
t.forward(55)
t.left(90)
t.pendown()


t.left(90)
t.circle(-40,90)
t.left(-90)
t.circle(-40,90)

t.end_fill()
t.hideturtle()
turtle.done()
