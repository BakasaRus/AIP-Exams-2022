print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not (y <= (x == w)) and (z <= x)
                if int(f) == 1:
                    print(w, x, y, z, int(f))
