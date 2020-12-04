import random as rd

grids = 8
invalid = []
nInvalids = (grids ** 2) // 5

#Criando espaços bloqueados aleatóriamente
for i in range(nInvalids):
    row = rd.randint(0, grids - 1)
    column = rd.randint(0, grids - 1)
    while [row, column] == [grids - 1, grids - 1] or [row, column] == [0, 0] or [row, column] == [grids - 2, grids - 2]and (row, column) not in invalid:
        row = rd.randint(0, grids - 1)
        column = rd.randint(0, grids - 1)
    invalid.append((row, column))

#Recursiva
def getPaths(row, column):
    global grids, invalid
    if [row, column] == [grids-1, grids-1]:
        return 0
    if row == grids - 1:
        for i in range(1, grids - column - 2):
            if (row, column+1) in invalid:
                return 0
        return 1
    if column == grids - 1:
        for i in range(1, grids - column - 2):
            if (row+i, column) in invalid:
                return 0
        return 1
    nPaths = 0
    if (row+1, column) not in invalid:
        nPaths += getPaths(row+1, column)
    if (row, column+1) not in invalid:
        nPaths += getPaths(row, column+1)
    return nPaths

def printBoard():
    for i in range(grids):
        for j in range(grids):
            if (i, j) in invalid:
                print('[X]', end='')
            else:
                print('[ ]', end='')
        print('')

def title(string):
    print(string)
    print(len(string) * '-')

title('Primeiro Caso:')

[m, n] = [grids-2, grids-2]

print(getPaths(m, n))

title('Segundo Caso:')

[m, n] = [0, 0]

print(getPaths(m, n))
