import fnmatch

# Перебираем числа с шагом 2023
for x in range(2023, 10**10 + 1, 2023):
    if fnmatch.fnmatch(str(x), '1?2139*4'):
        print(x, x // 2023)
