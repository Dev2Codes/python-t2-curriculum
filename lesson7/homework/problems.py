import turtle
import time

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

# Problem 1
# Use turtle to draw a filled square inside a larger square.

for x in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.forward(25)
t.left(90)
t.forward(25)
t.right(90)
t.pendown()

t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

time.sleep(2) # turtle.delay() didn't work for me

t.clear()



# Problem 2
# Use turtle to draw a flower with 6 petals.
# Each petal can be made using a small circle arc.
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("pink")

for x in range(6):
    t.begin_fill()
    t.circle(100)
    t.left(60)
    t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

time.sleep(2) # turtle.delay() didn't work for me

t.clear()

# Problem 3
# Use turtle to draw a rainbow:
# Draw 5 semicircles with different colors, each one bigger than the last.

colors = ["red", "orange", "yellow", "green", "blue"]

t.penup()
t.goto(100, 0)
t.pendown()

r = 200
t.left(90)

for count in range(len(colors)):
    t.fillcolor(colors[count])

    t.begin_fill()
    t.circle(r, 180)
    t.left(90)
    t.forward(2*r)
    t.end_fill()
    t.left(90)

    r-=10

    t.penup()
    t.goto(r/2, 0)
    t.pendown()


# Problem 4
# Use turtle to draw a grid of 3x3 small squares.



# Problem 5
# Use turtle to make a simple "logo" using at least 3 different colors and 2 shapes.


turtle.done()
