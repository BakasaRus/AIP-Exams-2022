word = 'ЕНОТ'
count = 0

for a in word:
    for b in word:
        for c in word:
            for d in word:
                count += 1
                if 256 - count + 1 == 225:
                    print(count, 256 - count + 1, a+b+c+d)
                    break
