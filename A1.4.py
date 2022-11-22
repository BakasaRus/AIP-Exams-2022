for x in '012345':
    a = int('12' + x + '35', 6)
    b = int('1' + x + '243', 6)
    if (a + b) % 2 == 0:
        print(x)
        print((a + b) // 2)
        break
