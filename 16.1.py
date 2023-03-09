count = 6
result = 1000000

N = int(input())

prev = [0] * count
prev[0] = float(input())

for i in range(1, count):
    x = float(input())

    prev[i] = min(x, prev[i - 1])

for i in range(count, N):
    x = float(input())

    result = min(result, x * prev[i % count])
    prev[i % count] = min(x, prev[(i - 1) % count])

print(result)

