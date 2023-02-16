with open('26/26.1.txt', 'r') as file:
    # s, n = [int(x) for x in input().split()]
    s, n = [int(x) for x in file.readline().split()]
    files = []
    for line in file:
        files.append(int(line))

files.sort()
count = 0
total_size = 0
max_size = 0

for size in files:
    if total_size + size <= s:
        total_size += size
        max_size = size
        count += 1
    elif total_size - max_size + size <= s:
        total_size = total_size - max_size + size
        max_size = size
    else:
        break

print(count, max_size)
