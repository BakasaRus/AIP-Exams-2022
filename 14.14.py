with open('24/24.1.txt', 'r') as file:
    data = file.read()

# Контрпример: XZYXZYX
# print(data.count('XZYX'))

count = 0
for i in range(len(data) - 3):
    if data[i:i+4] == 'XZYX':
        count += 1

print(count)
