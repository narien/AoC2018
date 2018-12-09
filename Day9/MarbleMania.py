from collections import defaultdict, deque

board = deque([0])

def normalRound(marbleCount):
    global board
    board.rotate(-1)
    board.append(marbleCount)
    return 0

def doRound(marbleCount):
    global board

    if marbleCount % 23:
        return normalRound(marbleCount)
    else:
        points = marbleCount

        board.rotate(7)
        points += board.pop()
        board.rotate(-1)
        return points

def calculate(lastMarbleScore, players):
    global board
    board = deque([0])
    playersScore = defaultdict(int)

    currentPoints = 0
    currentPlayer = 1

    for marbleCount in range(1, lastMarbleScore + 1):
        currentPoints = doRound(marbleCount)
        playersScore[currentPlayer] += currentPoints

        currentPlayer += 1
        if currentPlayer > players:
            currentPlayer = 1
    print('Winning score is: ' + str(max(playersScore.values())))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inputData = f.read().split()
    players = int(inputData[0])
    lastMarbleScore = int(inputData[-2])

    calculate(lastMarbleScore, players)
    calculate(lastMarbleScore*100, players)


