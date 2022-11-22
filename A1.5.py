def R(N):
    b = bin(N)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    return int(b, 2)


for n in range(1, 10000):
    if R(n) > 335:
        print(n)
        break
