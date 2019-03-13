
def print_table(data):
    maxCol = []
    for i in range(len(data[0])):
        x = 0
        for j in range(len(data)):
            x = max(x, len(str(data[j][i])))
        maxCol.append(x)
    length = sum(maxCol)

    strk = (('-' * (6 * len(maxCol)) + '-' * (length-3)))
    print(strk)
	mk = len(data[0])-1
    for i in range(0, len(data)):
        print('|', end='')
        for j in range(len(data[i])):
            if j == (len(data[i]) - 1):
                print(" " * (maxCol[mk] - len(str(data[i][j])) + 1),
		      data[i][j], " |", end='')
            else:
                print(" ", data[i][j],
		      ' ' * (maxCol[j] - len(str(data[i][j]))), '|', end='')
        print()
    print('-' * (sum(maxCol) - 3) + '-' * len(maxCol) * 6)
