def to_base(x, base):
    res = ''
    while x > 0:
        res = str(x % base) + res
        x //= base
    return res


x = 2 * 3**30 + 2 * 3**25 + 3**6 + 7 * 3**4 + 2 * 9**2 + 1
res = to_base(x, 9)
print(res)
print(res.count('0'))
