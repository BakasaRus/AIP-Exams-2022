with open('26/26.8.txt', 'r') as file:
    s, k = [int(x) for x in file.readline().split()]
    sizes = [int(x) for x in file]


# s, k = 48, 2
# sizes = [25, 64, 78, 37, 34, 55, 47]

sizes.sort()

summa = 0
for i in range(k):
    summa += sizes[i]

for i in range(-1, -k-1, -1):
    summa += sizes[i]

mean = (sum(sizes[:k]) + sum(sizes[-1:-k-1:-1])) // (2 * k)

selected = 0
for size in sizes:
    # 74 75 76 77 78 79 80
    if 0 <= s - size <= 3:
        selected = size
    elif s - size < 0 and selected == 0:
        selected = size
        break

print(selected, mean)
