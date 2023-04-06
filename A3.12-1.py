def fill(space, file_sizes):
    count, largest = 0, 0
    for size in file_sizes:
        if space - size >= 0:
            space -= size
            count += 1
            largest = size
        elif space + largest - size >= 0:
            space = space + largest - size
            largest = size

    return count, largest


with open('A3/26-j1.txt', 'r') as file:
    a, b, n = [int(x) for x in file.readline().split()]
    sizes = [int(x) for x in file]

sizes.sort()

large = [x for x in sizes if x > 500]
small = [x for x in sizes if x <= 500]

count_large, max_large = fill(a, large)
count_small, max_small = fill(b, small)

print(count_large + count_small, max_large + max_small)
