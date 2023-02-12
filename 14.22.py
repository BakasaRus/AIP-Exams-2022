with open('24/24.3.txt', 'r') as file:
    data = file.readlines()

string = ''
count_A = 2 ** 20 + 1

for line in data:
    current_count_A = line.count('A')
    # if current_count_A == 0:
    #     continue
    if current_count_A < count_A:
        string = line.strip()
        count_A = current_count_A

print(string, count_A)

max_length = 0

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    first = string.find(letter)
    if first == -1:
        continue
    last = string.rfind(letter)
    if first == last:
        continue
    # ABCDEFA - 0 and 6, but 5 letters
    # ABCDEFAGHA
    max_length = max(max_length, last - first - 1)

print(max_length)
