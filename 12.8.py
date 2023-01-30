import turtle as t

k = 30

t.color('black', 'red')
t.speed(200)
t.left(90)
t.begin_fill()
for i in range(7):
    t.forward(2 * k)
    t.left(60)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-10 * k, 10 * k, k):
    for y in range(-10 * k, 10 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')
        # s = canvas.find_overlapping(x, y, x, y)
        # if len(s) == 1:
        #     count += 1

# print(count)

t.done()
