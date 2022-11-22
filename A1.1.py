x = 6 ** 2022 - 6 ** 1020 - 6 ** 300 + 36 ** 200
res = ''
base = 6
while x > 0:
    res = str(x % base) + res
    x //= base
print(res)
print(res.count('5'))
