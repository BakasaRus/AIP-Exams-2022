with open('A3/17.txt', 'r') as file:
    numbers = [int(line) for line in file]

min_square = min([x for x in numbers if x % 10 == 0]) ** 2
count = 0
max_sum = 0

for i in range(len(numbers) - 1):
    # Python работает с остатками отрицательных чисел не совсем так, как нам хочется,
    # поэтому мы берём модуль, так как это на решение не влияет
    a, b = abs(numbers[i]), abs(numbers[i + 1])
    if not (a % 10 == 1 and b % 10 != 1 or a % 10 != 1 and b % 10 == 1):
        continue
    if a ** 2 + b ** 2 >= min_square:
        count += 1
        max_sum = max(max_sum, a ** 2 + b ** 2)

print(count, max_sum)
