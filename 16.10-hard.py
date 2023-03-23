data = []

with open('27/27.10-B.txt', 'r') as file:
    n = int(file.readline())
    for line in file:
        number, count = [int(x) for x in line.split()]
        count = count // 36 + (0 if count % 36 == 0 else 1)
        data.append((number, count))

# Основная идея: берём пункт, считаем префиксную сумму слева и справа от него
# При переходе к следующему пункту изменяем префиксную сумму, учитывая
# добавляемый и удаляемый элементы слева и справа

prices = []
left, right = 0, 0

for i in range(n):
    cur_price = (data[i][0] - data[0][0]) * data[i][1]
    prices.append(cur_price)
    right += cur_price

answers = [right]

# Смещаем лабораторию и пересчитываем префиксные суммы
for i in range(1, n):
    # Начинаем везти контейнеры из предыдущего пункта в текущий
    left += (data[i][0] - data[i-1][0]) * data[i-1][1]
    # Перестаём везти контейнеры из текущего пункта в предыдущий
    right -= (data[i][0] - data[i-1][0]) * data[i][1]
    answers.append(left + right)

print(min(answers))
