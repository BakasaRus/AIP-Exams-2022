prev = []

N = int(input())
## четное
min_even = 10 ** 7
## нечетное
min_odd = 10 ** 7
result = 10 ** 7

count = 6

for i in range(count):
    prev.append(int(input()))

for i in range(count, N):
    x = int(input())

    if prev[i % count] % 2 == 0 and prev[i % count] < min_even:
        min_even = prev[i % count]
    elif prev[i % count] % 2 != 0 and prev[i % count] < min_odd:
        min_odd = prev[i % count]

    if x % 2 == 0 and min(min_odd, min_even) * x < result:
        result = min(min_odd, min_even) * x
    elif x % 2 != 0 and min_even * x < result:
        result = min_even * x

    prev[i % count] = x

if result == 10 ** 7:
    print(-1)
else:
    print(result)