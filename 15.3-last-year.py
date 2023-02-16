file = open('26/26.3.txt', 'r')
N, M = file.readline().split()
N, M = int(N), int(M)
pieces = []
for i in range(N):
    pieces.append(int(file.readline()))
file.close()

pieces.sort(reverse=True)
amount = 0
curr_piece = 0

while sum(pieces) >= M or curr_piece != 0:
    if pieces[0] < (M - curr_piece):
        if curr_piece != 0:
            amount += 1
        curr_piece += pieces[0]
        pieces[0] = 0
        pieces.remove(0)
        continue
    for i in pieces:
        if i == (M - curr_piece):
            pieces[pieces.index(i)] = 0
            amount += 1
            curr_piece = 0
            pieces.remove(0)
            break
    if curr_piece == 0:
        continue
    diff = M
    slicee = 0
    for j in pieces:
        if 0 < (j - (M - curr_piece)) < diff:
            slicee = j
            diff = j - (M - curr_piece)
    pieces.append(diff)
    pieces[pieces.index(slicee)] = 0
    pieces.sort(reverse=True)
    curr_piece = 0
    amount += 1
    pieces.remove(0)

print(amount, len(pieces))
