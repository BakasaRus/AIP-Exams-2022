import turtle as t

k = 40

t.color('black', 'red')
t.speed(200)
t.left(90)
t.begin_fill()
t.penup()
t.forward(5)
t.pendown()
for i in range(4):
    t.right(120)
    t.forward(5 * k)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-5 * k, 5 * k, k):
    for y in range(-5 * k, 5 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')
        # s = canvas.find_overlapping(x, y, x, y)
        # if len(s) == 1:
        #     count += 1

# print(count)

t.done()
