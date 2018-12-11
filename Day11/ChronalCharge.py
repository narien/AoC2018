import sys
import numpy as np

def getPowerLevel(cordX, cordY, inputVal):
    rackId = 10 + cordX
    powerLevel = rackId * cordY
    powerLevel += inputVal
    powerLevel *= rackId
    powerLevel = int(powerLevel/100) % 10
    powerLevel -= 5
    return powerLevel

def findOptimalPowerCells(matrix):
    coords = []
    highestSum = -1
    for i in range(297):
        for j in range(297):
            currSum = np.sum(matrix[j:j+3,i:i+3])
            if currSum > highestSum:
                highestSum = currSum
                coords = [i+1, j+1]
    return coords

def findOptimalPowerCells2(matrix):
    res = []
    highestSum = -1
    for i in range(300):
        for j in range(300):
            for k in range(1, min([300-i, 300-j])):
                currSum = np.sum(matrix[j:j+k,i:i+k])
                if currSum > highestSum:
                    highestSum = currSum
                    res = [i+1, j+1, k]
    return res


if __name__ == '__main__':
    inputVal = int(sys.argv[1])
    matrix =  np.zeros(shape=(300, 300), dtype=int)
    k = 0
    for i in range(300):
        for j in range(300):
            matrix[i][j] = getPowerLevel(j + 1 , i + 1, inputVal)
            k += 1
    print('Part 1 optiomal coords: ' + str(findOptimalPowerCells(matrix)))
    print('part 2 optimal coords and size: ' + str(findOptimalPowerCells2(matrix)))


