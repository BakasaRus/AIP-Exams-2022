import math

data = []

with open('27/27.10-A.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        number, count = [int(x) for x in line.split()]
        count = math.ceil(count / 36)
        data.append([number, count])

min_sum = 10 ** 1000
min_number = 0

for i in range(n):
    cur_sum = 0
    for j in range(n):
        price = abs(data[i][0] - data[j][0]) * data[j][1]
        cur_sum += price
    if cur_sum < min_sum:
        min_sum = cur_sum
        min_number = data[i][0]

print(min_sum)
print(min_number)
