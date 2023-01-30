import turtle as t

k = 30

t.color('black', 'red')
t.speed(200)
t.left(90)
t.begin_fill()

t.penup()
t.forward(5 * k)
t.right(90)
t.left(90)
t.pendown()
for i in range(4):
    t.forward(7 * k)
    t.right(90)

t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-5 * k, 20 * k, k):
    for y in range(-5 * k, 20 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')
        # s = canvas.find_overlapping(x, y, x, y)
        # if len(s) == 1:
        #     count += 1

# print(count)

t.done()
