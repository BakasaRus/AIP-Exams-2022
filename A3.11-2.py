def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


initial = 10_000_000
results = []

count = 0
x = initial
while count < 3:
    x -= 1
    if is_prime(x):
        count += 1
        results.append((x, initial - x))

count = 0
x = initial
while count < 3:
    x += 1
    if is_prime(x):
        count += 1
        results.append((x, x - initial))

results.sort()
for res in results:
    print(*res)
