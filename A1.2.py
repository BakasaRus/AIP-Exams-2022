def to_base(x, base):
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res


for i in range(2, 11):
    if len(to_base(636, i)) == 4:
        print(i, to_base(636, i))
