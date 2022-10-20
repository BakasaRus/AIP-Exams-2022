print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or y) and not (y == z) and not w
                if int(f) == 1:
                    print(x, y, z, w, int(f))
