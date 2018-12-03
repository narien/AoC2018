import numpy as np

id = []
fromLeft = []
fromTop = []
xSize = []
ySize =[]

def fillMatrix(matrix):
    for i in range(len(id)):
        for j in range(fromTop[i], fromTop[i] + ySize[i]):
            for k in range(fromLeft[i], fromLeft[i] + xSize[i]):
                if matrix[j][k] == 1 or matrix[j][k] == 2:
                    matrix[j][k] = 2
                else:
                    matrix[j][k] = 1

def findNonOverlappingSquare(matrix):
    for i in range(len(id)):
        overlapping = False
        for j in range(fromTop[i], fromTop[i] + ySize[i]):
            for k in range(fromLeft[i], fromLeft[i] + xSize[i]):
                if int(matrix[j][k]) == 2:
                    overlapping = True
        if not overlapping:
            return id[i]

# Run program with input.txt in same folder.
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            a, b = line.split('@')
            id.append(a.strip()[1:])
            c, d = b.split(':')
            e, f = c.split(',')
            fromLeft.append(int(e.strip()))
            fromTop.append(int(f.strip()))
            g, h = d.split('x')
            xSize.append(int(g.strip()))
            ySize.append(int(h.strip()))
        print('Data Loaded')
    matrix = np.zeros((1000, 1000))
    fillMatrix(matrix)
    print('Total square inches overlapping: ', str(np.count_nonzero(matrix == 2)))
    print('Id for non-overlapping square: ', findNonOverlappingSquare(matrix))
