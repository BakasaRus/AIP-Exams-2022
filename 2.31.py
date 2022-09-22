x = 27 ** 11 + 3 ** 19 - 9 ** 7 - 9
res = ''
base = 3
while x > 0:
    res = str(x % base) + res
    x //= base
print(res)
print(res.count('2'))
