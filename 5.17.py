print('z x y F')
for z in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            f = (x and not y or z) and (y and z or not y)
            print(x, y, z, int(f))

# and, or, not, импликация - <=, эквивал. - ==
