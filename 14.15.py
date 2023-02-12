with open('24/24.1.txt', 'r') as file:
    data = file.read()

positions = []
for i in range(len(data) - 3):
    if data[i:i+4] == 'XZYX':
        positions.append(i)

max_delta = 0
for i in range(len(positions) - 1):
    max_delta = max(max_delta, positions[i+1] - positions[i] + 2)

print(max_delta)
