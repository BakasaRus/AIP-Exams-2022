min_length = 1000

for left in range(-50, 50):
    for right in range(left + 1, 50):
        for x in range(-1000, 1000):
            x /= 10
            if not ((((15 <= x < 40) <= (left <= x <= right)) <= (11 <= x < 25)) <= (11 <= x < 25)):
                break
        else:
            if right - left < min_length:
                print(left, right, right - left)
                min_length = right - left
