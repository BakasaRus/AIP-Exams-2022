import turtle as t

k = 50

t.hideturtle()
t.color('red')

for i in range(6):
    t.forward(3 * k)
    t.right(60)

count = 0
canvas = t.getcanvas()
for x in range(-7 * k, 7 * k, k):
    for y in range(-7 * k, 7 * k, k):
        t.penup()
        t.setpos(x, y)
        t.pendown()
        t.dot(4, 'black')
        # s = canvas.find_overlapping(x, y, x, y)
        # if len(s) == 1:
        #     count += 1

t.done()
