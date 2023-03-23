data = []

with open('27/27.11-B.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        count = int(line)
        data.append(count)

result = 0

for i in range(n):
    if i > n // 2:
        result += data[i] + int((i - n // 2) ** 0.5)
    else:
        result += data[i] + int(i ** 0.5)

print(result)
