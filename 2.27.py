x = 4 ** 2014 + 2 ** 2015 - 8
res = bin(x)
print(res[2:].count('1'))
