import math

data = []

with open('27/27.10-B.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        number, count = [int(x) for x in line.split()]
        count = math.ceil(count / 36)
        data.append([number, count])

left, right = 0, 0
left_count, right_count = 0, 0

for i in range(1, n):
    price = (data[i][0] - data[0][0]) * data[i][1]
    right += price
    right_count += data[i][1]

min_sum = left + right
min_number = 0

for i in range(1, n):
    right = right - right_count * (data[i][0] - data[i-1][0])
    right_count -= data[i][1]
    left_count += data[i-1][1]
    left = left + left_count * (data[i][0] - data[i-1][0])
    if left + right < min_sum:
        min_sum = left + right
        min_number = data[i][0]

print(min_sum)
print(min_number)
