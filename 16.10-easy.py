from tqdm import tqdm

data = []

with open('27/27.10-B.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        number, count = [int(x) for x in line.split()]
        count = count // 36 + (0 if count % 36 == 0 else 1)
        data.append((number, count))

min_sum = 10 ** 100

for selected_number, _ in tqdm(data):
    cur_sum = 0
    for cur_number, cur_count in data:
        cur_sum += abs(cur_number - selected_number) * cur_count
    min_sum = min(min_sum, cur_sum)

print(min_sum)
