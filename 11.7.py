with open('17.txt') as file:
    data = [int(x) for x in file.readlines()]

max_3 = -10001
for x in data:
    if x % 10 == 3:
        max_3 = max(max_3, x)


count = 0
max_sum = 0

# Идём до предпоследнего элемента
# и берём к нему в пару последний
for i in range(len(data) - 1):
    a, b = abs(data[i]), abs(data[i+1])
    # Ровно одно число из двух оканчивается на 3
    f1 = ((a % 10 == 3) and (b % 10 != 3)) or ((a % 10 != 3) and (b % 10 == 3))
    f2 = (a**2 + b**2) >= max_3**2
    if f1 and f2:
        count += 1
        max_sum = max(max_sum, a**2 + b**2)

print(count, max_sum)
