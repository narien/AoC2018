import numpy as np
import collections

def setField(x, y, field, val):
    if val == '#':
        field[y][x] = 1
    elif val == '.':
        field[y][x] = 2
    elif val == '|':
        field[y][x] = 3

def getFieldCounts(field):
    unique, counts = np.unique(field, return_counts=True)
    d = collections.defaultdict(lambda:0)
    d.update(dict(zip(unique, counts)))
    return d

def calcVal(x, y, field):
    d = getFieldCounts(field[y-1:y+2,x-1:x+2])
    if field[y][x] == 1:
        return '#' if d[1] >= 2 and d[3] >= 1 else '.'
    if field[y][x] == 2:
        return '|' if d[3] >= 3 else '.'
    if field[y][x] == 3:
        return '#' if d[1] >= 3 else '|'

def updateField(field):
    changes = {}
    for y in range(1, 51):
        for x in range(1, 51):
            changes[(x, y)] = calcVal(x, y, field)
    for coord, val in changes.items():
        setField(coord[0], coord[1], field, val)

if __name__ == '__main__':
    field = np.zeros((52, 52), dtype=int)
    row = 1
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            col = 1
            for c in line:
                setField(col, row, field, c)
                col += 1
            row +=1

    mem = []
    memCount = []

    for _ in range(11):
        mem.append(field.tostring())
        d = getFieldCounts(field)
        memCount.append(str(d[1]*d[3]))
        updateField(field)

    print('Resource value after 10 minutes is: ' + memCount[-1])

    iterations = 1000000001
    for i in range(11, iterations):
        mem.append(field.tostring())
        d = getFieldCounts(field)
        memCount.append(str(d[1]*d[3]))
        updateField(field)
        if field.tostring() in mem:
            firstRepeatedIx = mem.index(field.tostring())
            modulo = len(mem) - firstRepeatedIx
            finalIx = ((iterations - firstRepeatedIx - 1) % modulo) + firstRepeatedIx
            print('Resource value after 1000000000 minutes is: ' + memCount[finalIx])
            break
