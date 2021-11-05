# markhus Dammar
# Draws many shapes for Turtle


import turtle, time
t = turtle.Pen()

# Equilateral Triangle
t.reset()
t.speed('fast')
for i in range(3):      # 3 sides in a triangle
    t.forward(200)
    t.left(120)         # 360/x sides of the shape = degrees
time.sleep(0.5)

t.penup()
t.backward(250)
t.pendown()


# Square
t.speed('fast')
for i in range(4):
    t.forward(200)
    t.left(90)
time.sleep(0.5)

t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

# Star
t.clear()
t.speed('fast')
for i in range(5):
    t.forward(100)
    t.left(216)
time.sleep(0.5)

t.penup()
t.forward(150)
t.pendown()

# Pentagon
t.clear()
t.speed('fast')
for i in range(5):
    t.forward(100)
    t.left(72)
time.sleep(0.5)

# Hexagon
t.clear()
t.speed('fast')
for i in range(6):
    t.forward(100)
    t.left(60)
time.sleep(0.5)

# Right Angle Triangle
t.goto(0,0)
t.clear()
t.speed('fast')
for i in range(2):
    t.right(90)
    t.forward(200)
t.right(135)
t.forward(282.84)
t.left(90)
time.sleep(0.5)

# Circle
t.reset()
t.goto(0,0)
t.clear()
t.pensize(5)
t.circle(100)
t.goto(150, 0)
time.sleep(0.5)

# fill shape
t.reset()
t.goto(0,0)
t.clear()
t.pensize(2)
t.pencolor('pink')
t.fillcolor('cyan')
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.right(90)
t.end_fill()
t.mainloop()



