
import turtle
import math

bob = turtle.Turtle()
bob.speed('fastest')

startX = bob.xcor()
startY = bob.ycor()

angle = 150
size = 75
radius = 100
numShapes = 50

colors = ['red', 'yellow', 'black', 'green', 'orange', 'purple']

for i in range(1, numShapes):
    
    currentRadius = radius * i / 10 + 25
    
    bob.setx(math.sin(i*10) * currentRadius)
    bob.sety(math.cos(i*10) * currentRadius)
    
    bob.pendown()
    startX = bob.xcor()
    startY = bob.ycor()

    bob.color(colors[i*2 % len(colors)], colors[(i*2 + 1) % len(colors)])
    bob.begin_fill()
    while True:
        bob.forward(size)
        bob.left(angle)

        print(bob.pos())

        if abs(bob.xcor() - startX) < 0.1 and abs(bob.ycor() - startY) < 0.1:
            break
    bob.end_fill()
    bob.penup()

turtle.done()