with open('24/24.1.txt', 'r') as file:
    data = file.read()

max_counter = 0
for i in range(len(data) - 1):
    counter = 0
    for j in range(i + 1, len(data)):
        if data[j - 1] != data[j]:
            counter += 1
        else:
            break
    if counter > max_counter:
        max_counter = counter

print(max_counter + 1)
