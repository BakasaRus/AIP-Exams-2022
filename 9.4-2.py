def play(x, y, move):
    if x + y >= 77 and move == 3:
        return True
    if x + y < 77 and move == 3:
        return False
    if x + y >= 77:
        return False

    if move % 2 == 1:
        # Ходит Петя, все варианты приводят к его выигрышу
        return play(x + 1, y, move + 1) and play(x * 2, y, move + 1) and \
               play(x, y + 1, move + 1) and play(x, y * 2, move + 1)
    else:
        # Ходит Ваня, хотя бы один вариант приводит к его проигрышу
        return play(x + 1, y, move + 1) or play(x * 2, y, move + 1) or \
               play(x, y + 1, move + 1) or play(x, y * 2, move + 1)


for s in range(1, 77 - 7):
    if play(7, s, 0):
        print(s)
