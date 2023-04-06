import turtle as t

k = 50

t.hideturtle()
t.color('red')

t.penup()
t.right(90)
t.back(5 * k)
t.right(45)
t.pendown()
for i in range(6):
    t.left(45)
    t.forward(3 * k)
    t.left(45)

count = 0
canvas = t.getcanvas()
for x in range(0 * k, 7 * k, k):
    for y in range(0 * k, 7 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')

t.done()
