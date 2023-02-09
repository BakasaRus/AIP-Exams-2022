with open('24/24.2.txt', 'r') as file:
    data = file.read()

count = 0
max_count = 0
for i in range(len(data)):
    if data[i] == 'A':
        count += 1
        max_count = max(max_count, count)
    else:
        max_count = max(max_count, count)
        count = 0

print(max_count)
