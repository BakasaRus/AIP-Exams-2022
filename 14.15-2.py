with open('24/24.1.txt', 'r') as file:
    data = file.read()

max_count = 0
count = 0

for i in range(len(data) - 3):
    if data[i:i+4] != 'XZYX':
        count += 1
        max_count = max(max_count, count)
    else:
        count += 3
        max_count = max(max_count, count)
        count = 0

print(max_count)
