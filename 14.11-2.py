with open('24/24.1.txt', 'r') as file:
    data = file.read()


max_count = 0
count = 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)
