from tqdm import tqdm


with open('27/27.4-B.txt') as file:
    n = int(file.readline())
    prefixes = [0]
    for line in file:
        x = int(line)
        prefixes.append(prefixes[-1] + x)

max_sum = 0

for i in tqdm(range(n)):
    for j in range(i + 1, n + 1):
        diff = prefixes[j] - prefixes[i]
        if diff % 93 == 0 and diff % 2 == 1 and diff > max_sum:
            max_sum = diff

print(max_sum)
