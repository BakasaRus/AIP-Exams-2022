x = 5 ** 2004 - 5 ** 1016 - 5 ** 400 + 25 ** 250
res = ''
base = 5
while x > 0:
    res = str(x % base) + res
    x //= base
print(res)
print(res.count('4'))
