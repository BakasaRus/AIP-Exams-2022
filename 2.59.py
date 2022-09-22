for x in '0123456789ABCDE':
    a = int('283' + x + '5', 15)
    b = int('1' + x + '243', 15)
    if (a + b) % 11 == 0:
        print(x)
        print((a + b) // 11)
        break
