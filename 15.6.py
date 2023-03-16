with open('26/26.6.txt', 'r') as file:
    n = int(file.readline())
    numbers = []
    unique = set()

    for line in file:
        x = int(line)
        numbers.append(x)
        unique.add(x)

count = 0
minimum = 10 ** 9 + 1

for i in range(n - 1):
    if numbers[i] % 2 != 0:
        continue
    for j in range(i + 1, n):
        mean = (numbers[i] + numbers[j]) // 2
        if numbers[j] % 2 == 0 and mean in unique:
            print(numbers[i], numbers[j], mean)
            count += 1
            minimum = min(minimum, mean)

print(count, minimum)
