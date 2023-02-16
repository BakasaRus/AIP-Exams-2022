with open('26/26.2.txt', 'r') as file:
    n = int(file.readline())
    seats = {}
    # {
    #   3: [3, 4, 7],        -- между 4 и 7 местами есть 5 и 6
    #   20: [3, 6, 9],       -- между 3 и 6 есть 4 и 5, между 6 и 9 - 7 и 8
    #   24: [33, 38, 45, 50] -- не подходит
    # }
    for line in file:
        row, place = [int(x) for x in file.readline().split()]
        if row in seats:
            seats[row].append(place)
        else:
            seats[row] = [place]

max_row = 0
selected_place = 0

for row in seats:
    seats[row].sort()
    for i in range(len(seats[row]) - 1):
        # Есть ровно 2 свободных места между занятыми
        if seats[row][i + 1] - seats[row][i] == 3:
            if max_row < row:
                max_row = row
                selected_place = seats[row][i] + 1
            break

print(max_row, selected_place)
