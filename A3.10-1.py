with open('A3/24-s1.txt', 'r') as file:
    lines = [line.strip() for line in file]

min_string = ''
min_count = 100000000

for line in lines:
    count = 0
    for i in range(len(line) - 1):
        a, b = line[i], line[i + 1]
        if a < b:
            count += 1
    if count < min_count:
        min_count = count
        min_string = line

result = ''
result_count = 0
for letter in reversed('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    count = min_string.count(letter)
    # print(letter, count)
    if count > result_count:
        result_count = count
        result = letter

print(result, result_count)
