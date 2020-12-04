from timeit import default_timer as timer
import random as rd

grids = 8
memo = {}
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

#Memoization
def getPathsMemo(row, column):
    try:
        return memo[row, column]
    except:
        if [row, column] == [grids-1, grids-1]:
            memo[row, column] = 0
            return 0
        if row == grids - 1:
            for i in range(1, grids - column - 2):
                if (row, column+1) in invalid:
                    memo[row, column] = 0
                    return 0
            memo[row, column] = 1
            return 1
        if column == grids - 1:
            for i in range(1, grids - column - 2):
                if (row+1, column) in invalid:
                    memo[row, column] = 0
                    return 0
            memo[row, column] = 1
            return 1
        memo[row, column] = 0
        if (row+1, column) not in invalid:
            memo[row, column] += getPathsMemo(row+1, column)
        if (row, column+1) not in invalid:
            memo[row, column] += getPathsMemo(row, column+1)
        return memo[row, column]

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

print('Espaço ({}, {}) até ({}, {})'.format(m, n, grids-1, grids-1))

recStart = timer()
recursive = getPaths(m, n)
recEnd = timer()

memoStart = timer()
memoization = getPathsMemo(m, n)
memoEnd = timer()

if recursive == memoization:
    print('Número de caminhos: {}'.format(recursive))
else:
    print('Número de caminhos recursivamente: {}'.format(recursive))
    print('Número de caminhos com memoization: {}'.format(memoization))

print('Tempo recursivamente:  {:.10f}'.format(recEnd-recStart))
print('Tempo com memoization: {:.10f}\n'.format(memoEnd-memoStart))

title('Segundo Caso:')

[m, n] = [0, 0]

print('Espaço ({}, {}) até ({}, {})'.format(m, n, grids-1, grids-1))

recStart = timer()
recursive = getPaths(m, n)
recEnd = timer()

memoStart = timer()
memoization = getPathsMemo(m, n)
memoEnd = timer()

if recursive == memoization:
    print('Número de caminhos: {}'.format(recursive))
else:
    print('Número de caminhos recursivamente: {}'.format(recursive))
    print('Número de caminhos com memoization: {}'.format(memoization))

print('Tempo recursivamente:  {:.10f}'.format(recEnd-recStart))
print('Tempo com memoization: {:.10f}\n'.format(memoEnd-memoStart))

printBoard()