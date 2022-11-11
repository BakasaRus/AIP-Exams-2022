for A in range(1, 5000):
    for x in range(1, 1000):
        # if not ((x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))):
        # if not ((x & 18 == 0) <= ((x & 51 != 0) <= (x & A != 0))):
        if not (((x & 19 == 0) <= (x & 56 != 0)) <= (x & A != 0)):
            # (x & 19 == 0) <= (x & 56 != 0) and (x & 56 != 0) <= (x & A != 0)
            # 5 <= 6 <= 7 -> 5 <= 6 and 6 <= 7
            break
    else:
        print(A)
        break
