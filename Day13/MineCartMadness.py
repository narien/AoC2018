import sys

def newDirection(xCoord, yCoord, direction, lastIntersection):
    if lastIntersection == 0:
        newDirection = direction - 1
    elif lastIntersection == 1:
        newDirection = direction
    elif lastIntersection == 2:
        newDirection = direction + 1
    newDirection = newDirection % 4
    newIntersection = (lastIntersection + 1) % 3
    return (xCoord, yCoord, newDirection, newIntersection)

def checkCrash(xCoord, yCoord, carts):
    for cart in carts:
        if cart[0] == xCoord and cart[1] == yCoord:
            print('Crash at: ' + str(xCoord) + ' ' + str(yCoord))
            sys.exit()

def tick(carts, matrix):
    for i in range(len(carts)):
        xCoord = carts[i][0]
        yCoord = carts[i][1]
        if carts[i][2] == 0:
            yCoord -= 1
            if matrix[yCoord][xCoord] == '+':
                cart = newDirection(xCoord, yCoord, carts[i][2], carts[i][3])
            elif matrix[yCoord][xCoord] == '/':
                cart = (xCoord, yCoord, 1, carts[i][3])
            elif matrix[yCoord][xCoord] == '\\':
                cart = (xCoord, yCoord, 3, carts[i][3])
            else:
                cart = (xCoord, yCoord, 0, carts[i][3])
        elif carts[i][2] == 1:
            xCoord += 1
            if matrix[yCoord][xCoord] == '+':
                cart = newDirection(xCoord, yCoord, carts[i][2], carts[i][3])
            elif matrix[yCoord][xCoord] == '/':
                cart = (xCoord, yCoord, 0, carts[i][3])
            elif matrix[yCoord][xCoord] == '\\':
                cart = (xCoord, yCoord, 2, carts[i][3])
            else:
                cart = (xCoord, yCoord, 1, carts[i][3])

        elif carts[i][2] == 2:
            yCoord += 1
            if matrix[yCoord][xCoord] == '+':
                cart = newDirection(xCoord, yCoord, carts[i][2], carts[i][3])
            elif matrix[yCoord][xCoord] == '/':
                cart = (xCoord, yCoord, 3, carts[i][3])
            elif matrix[yCoord][xCoord] == '\\':
                cart = (xCoord, yCoord, 1, carts[i][3])
            else:
                cart = (xCoord, yCoord, 2, carts[i][3])
        else:
            xCoord -= 1
            if matrix[yCoord][xCoord] == '+':
                cart = newDirection(xCoord, yCoord, carts[i][2], carts[i][3])
            elif matrix[yCoord][xCoord] == '/':
                cart = (xCoord, yCoord, 2, carts[i][3])
            elif matrix[yCoord][xCoord] == '\\':
                cart = (xCoord, yCoord, 0, carts[i][3])
            else:
                cart = (xCoord, yCoord, 3, carts[i][3])
        checkCrash(xCoord, yCoord, carts)
        carts[i] = cart



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        matrix = []
        carts = []
        rowIx = 0
        for line in f.readlines():
            matrix.append([])
            for char in line:
                matrix[rowIx].append(char)
                if char in '^>v<': #directions 0, 1, 2, 3
                    if char == '^':
                        cart = (len(matrix[rowIx]) - 1, rowIx, 0, 0)
                    elif char == '>':
                        cart = (len(matrix[rowIx]) - 1, rowIx, 1, 0)
                    elif char == 'v':
                        cart = (len(matrix[rowIx]) - 1, rowIx, 2, 0)
                    else:
                        cart = (len(matrix[rowIx]) - 1, rowIx, 3, 0)
                    carts.append(cart)
            rowIx += 1
    while True:
        carts.sort()
        tick(carts, matrix)



