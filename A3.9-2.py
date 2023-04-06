with open('A3/17.txt', 'r') as file:
    numbers = [int(line) for line in file]

max_square = max([x for x in numbers if x % 10 == 7]) ** 2
count = 0
max_sum = 0

for i in range(len(numbers) - 1):
    # Python работает с остатками отрицательных чисел не совсем так, как нам хочется,
    # поэтому мы берём модуль, так как это на решение не влияет
    a, b = abs(numbers[i]), abs(numbers[i + 1])
    if not (a % 10 == 9 and b % 10 != 9 or a % 10 != 9 and b % 10 == 9):
        continue
    if a ** 2 + b ** 2 >= max_square:
        count += 1
        max_sum = max(max_sum, a ** 2 + b ** 2)

print(count, max_sum)
