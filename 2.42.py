result = 0

for x in range(8 ** 3, 8 ** 4):
    number = oct(x)[2:]
    if '3' not in number:
        continue
    pos = number.index('3')
    if number.count('3') == 1 and \
            (pos == 0 or number[pos - 1] in '157') and \
            (pos == 3 or number[pos + 1] in '157'):
        result += 1

print(result)
