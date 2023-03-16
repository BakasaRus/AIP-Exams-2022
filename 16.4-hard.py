# Ищем минимальный префикс и максимальный префикс,
# который даёт нечётную разность с минимальным
max_prefixes = [0] * 93
min_prefixes = [10**30] * 93
min_prefixes[0] = 0

with open('27/27.4-B.txt') as file:
    n = int(file.readline())
    s = 0
    for line in file:
        x = int(line)
        s += x
        if min_prefixes[s % 93] == 10**30:
            min_prefixes[s % 93] = s
        elif s > max_prefixes[s % 93] and (s - min_prefixes[s % 93]) % 2 == 1:
            max_prefixes[s % 93] = s

max_sum = 0

for i in range(93):
    diff = max_prefixes[i] - min_prefixes[i]
    print(i, min_prefixes[i], max_prefixes[i], diff)
    max_sum = max(max_sum, diff)

print(max_sum)
