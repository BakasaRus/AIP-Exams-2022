counter = 0
cache = {}

# def F(n):
#     global counter
#     counter += 1
#     if n >= 1:
#         counter += 1
#         F(n - 1)
#         F(n - 3)
#         counter += 1

def F(n):
    global cache
    if n in cache:
        return cache[n]
    if n >= 1:
        cache[n] = F(n - 1) + F(n - 3) + 2 + 1
        return cache[n]
    else:
        cache[n] = 1
        return cache[n]


print(F(500))
print(cache)
