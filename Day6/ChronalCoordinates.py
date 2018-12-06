import sys
import numpy
from collections import defaultdict

def manhattanDist(xDest, yDest, x, y):
    return abs(x - xDest) + abs(y - yDest)

def getIdForGrid(xGrid, yGrid, xCoords, yCoords):
    lDist = sys.maxsize
    nearestIx = 0
    partTwoTotal= 0
    for i in range(len(xCoords)):
        dist = manhattanDist(xGrid, yGrid, xCoords[i], yCoords[i])
        partTwoTotal += dist
        if dist == lDist:
            nearestIx = 0
        elif dist < lDist:
            lDist = dist
            nearestIx = 1 + i
    return (nearestIx, True if partTwoTotal < 10000 else False)

def fillGrid(grid, xCoords, yCoords):
    partTwo = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            touple = getIdForGrid(i, j, xCoords, yCoords)
            grid[i][j] = touple[0]
            if touple[1]:
                partTwo += 1
    print('Part2 area size: ' + str(partTwo))

def removeIdsFoundOnBorder(grid):
    for i in range(len(grid)):
        grid[grid == grid[i][0]] = 0
        grid[grid == grid[i][-1]] = 0

    for j in range(len(grid[0])):
        grid[grid == grid[0][j]] = 0
        grid[grid == grid[-1]][j] = 0

def findBiggestArea(grid):
    values = defaultdict(int)
    for line in grid:
        counts = numpy.bincount(line)
        for i in range(len(counts)):
            values[i] += counts[i]
    del values[0]
    print('Largest area is: ' + str(max(values.values())))

# Run program with input.txt in same folder.
if __name__ == '__main__':
    xCoords = []
    yCoords = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            touple = line.split(', ')
            xCoords.append(int(touple[0]))
            yCoords.append(int(touple[1]))
    grid = numpy.zeros((max(xCoords)+1, max(yCoords)+1), dtype=int)
    for i in range(len(xCoords)):
        grid[xCoords[i]][yCoords[i]] = i+1
    fillGrid(grid, xCoords, yCoords)
    removeIdsFoundOnBorder(grid)
    findBiggestArea(grid)

