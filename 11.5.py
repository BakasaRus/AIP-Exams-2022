def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


for x in range(174_457, 174_505 + 1):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0 and is_prime(d) and is_prime(x // d):
            print(d, x // d)
