# Перебор через for
for x in range(1, 1000):
    if not ((4 > -(4 + x) * x) <= (30 > x * x)):
        print(x)
        break

# Перебор через while
x = 1
while (4 > -(4 + x) * x) <= (30 > x * x):
    x += 1
print(x)
