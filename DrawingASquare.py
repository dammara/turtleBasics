# markhus Dammar
# class Exercise 50 pts
# draw a square

import turtle, time
t = turtle.Pen()


def drawASquare(xCoordinate, yCoordinate, size):
    t.reset()
    t.clear()
    t.penup()
    t.goto(xCoordinate, yCoordinate)
    t.pendown()
    t.pencolor('Red')
    t.fillcolor('Yellow')
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    turtle.mainloop()


drawASquare(50, 50, 150)


