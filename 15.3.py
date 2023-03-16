with open('26/26.3.txt', 'r') as file:
    n, m = [int(x) for x in file.readline().split()]
    parts = [int(x) for x in file.readlines()]

parts.sort(reverse=True)

count = 0

while sum(parts) >= m:
    current_size = 0
    for i in range(len(parts)):
        if current_size > 0:
            count += 1
        current_size += parts[i]
        if current_size > m:
            for j in range(i + 1, len(parts)):
                if current_size - parts[i] + parts[j] <= m:
                    current_size = current_size - parts[i] + parts[j]
                    parts[j] = 0
                    break
            parts.append(current_size - m)
            break
        parts[i] = 0
    parts.sort(reverse=True)
    print(current_size, parts)

print(count, sum(parts))
