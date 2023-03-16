from tqdm import tqdm

prefixes = [0]

with open('27/27.5-A.txt') as file:
    n = int(file.readline())
    s = 0
    for line in file:
        x = int(line)
        s += x
        prefixes.append(s)

count = 0

# В префиксных суммах n + 1 число
for i in tqdm(range(n)):
    for j in range(i + 1, min(i + 21, n + 1)):
        diff = prefixes[j] - prefixes[i]
        if diff % 39 == 0:
            count += 1

print(count)
