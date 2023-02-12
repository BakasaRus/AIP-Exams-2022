with open('24/24.3.txt', 'r') as file:
    data = file.read()

letters = {}

for i in range(len(data) - 1):
    if data[i] != 'B':
        continue
    if data[i + 1] in letters:
        letters[data[i + 1]] += 1
    else:
        letters[data[i + 1]] = 1

max_count = 0
max_letter = ''

for letter in letters:
    if letters[letter] > max_count:
        max_count = letters[letter]
        max_letter = letter

print(max_letter, max_count)
