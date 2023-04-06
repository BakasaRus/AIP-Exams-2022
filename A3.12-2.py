with open('A3/26-j2.txt', 'r') as file:
    n, m = [int(x) for x in file.readline().split()]
    boxes = [int(x) for x in file]

boxes.sort()
valuable = [x for x in boxes if 180 <= x <= 200]
others = [x for x in boxes if not (180 <= x <= 200)]
valuable.reverse()

count = 0
total = 0

# Ценные коробки грузим подряд без замены, пока есть место
for box in valuable:
    if m - box >= 0:
        count += 1
        total += box
        m -= box

# Остальные коробки грузим с учётом максимизации их количества
max_box = 0
for box in others:
    if m - box >= 0:
        count += 1
        total += box
        m -= box
        max_box = box
    elif m + max_box - box >= 0:
        total = total - max_box + box
        m = m + max_box - box
        max_box = box

print(count, total)
