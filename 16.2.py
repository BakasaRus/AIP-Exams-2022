## В данной задаче можно оптимизировать память, высчитывая на ходу разность элементов и записывая в переменную для минимальной разности
## Сразу суммировать максимальный элемент из пары, в конце вычесть, если результат кратен 3

file = open("27-B.txt")

N = int(file.readline())

result = 0
pairs = []

for i in range(N):
    pairs.append([int(x) for x in file.readline().split()])

    if pairs[-1][0] > pairs[-1][1]:
        tmp = pairs[-1][1]
        pairs[-1][1] = pairs[-1][0]
        pairs[-1][0] = tmp

    pairs[-1].append(pairs[-1][1] - pairs[-1][0])
    result += pairs[-1][1]

pairs = sorted(pairs, key=lambda pair:pair[2])

if result % 3 == 0:
    for i in range(len(pairs)):
        if pairs[i][2] % 3 != 0:
            result -= pairs[i][2]
            break

print(result)