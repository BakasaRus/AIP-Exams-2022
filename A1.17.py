print('x y z w F')
for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = (w <= y) and ((x <= z) == (y <= x))
                if f:
                    print(int(x), int(y), int(z), int(w), int(f))
