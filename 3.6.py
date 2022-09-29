letters = 'ИПТФ'
counter = 0

for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                counter += 1
                if counter == 202:
                    print(a + b + c + d)
