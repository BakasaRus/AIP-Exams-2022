with open('A3/24-s2.txt', 'r') as file:
    lines = [line.strip() for line in file]

max_string = ''
max_count = 0

for line in lines:
    count = line.count('Q')
    if count >= max_count:
        max_count = count
        max_string = line

result = ''
result_count = 100000000
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    count = max_string.count(letter)
    if count < result_count:
        result_count = count
        result = letter

print(result, result_count)
