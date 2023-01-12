# _, 7935
count = 0
maximum = 0
for x in range(1016, 7937 + 1):
    if x % 3 == 0 and x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0:
        count += 1
        maximum = max(maximum, x)
print(count, maximum)
