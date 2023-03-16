with open('26/26.7.txt', 'r') as file:
    n = int(file.readline())
    sizes = [int(x) for x in file]

sizes.sort(reverse=True)

count = 0
last = 1000000000

for size in sizes:
    if last - size >= 3:
        count += 1
        last = size

print(count, last)
