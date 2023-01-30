import turtle as t

k = 20

t.color('black', 'red')
t.speed(200)
t.left(90)
t.begin_fill()
for i in range(5):
    t.forward(10 * k)
    t.right(90)
t.end_fill()

count = 0
canvas = t.getcanvas()
for x in range(-10 * k, 20 * k, k):
    for y in range(-10 * k, 20 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')
        # s = canvas.find_overlapping(x, y, x, y)
        # if len(s) == 1:
        #     count += 1

# print(count)

t.done()
