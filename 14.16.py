with open('24/24.3.txt', 'r') as file:
    data = file.readlines()

length = 0
count = 0

# Warning: \n is in string
print(len(data[1]))
print(ord(data[1][-1]))

for line in data:
    line = line.strip()
    if line.count('A') >= 3:
        length += len(line)
        count += 1

print(length / count)
