print('x y z w F')
for x in False, True:
    for y in False, True:
        for z in False, True:
            for w in False, True:
                f = (x or y) and not (w <= z)
                if f:
                    print(int(x), int(y), int(z), int(w), int(f))
