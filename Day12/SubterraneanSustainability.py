def updateState(currentState, notes):
    currentState = [0, 0, 0, 0, 0] + currentState + [0, 0, 0, 0, 0]
    newState = currentState.copy()
    for i in range(2, len(currentState) - 2):
        if str(currentState[i-2:i+3]) in notes:
            newState[i] = 1
        else:
            newState[i] = 0
    return newState


if __name__ == '__main__':
    currentState = []
    notes = set()
    with open('input.txt', 'r') as f:
        inputList = list(f.readline())
        for element in inputList:
            if element == '#':
                currentState.append(1)
            elif element == '.':
                currentState.append(0)
        f.readline()
        for line in f.readlines():
            l = line.split('=>')
            if '#' in l[1]:
                note = []
                for char in l[0]:
                    if char == '#':
                        note.append(1)
                    elif char == '.':
                        note.append(0)
                notes.add(str(note))
    for _ in range(20):
        currentState = updateState(currentState, notes)

    plantScore = 0
    plantIx = -100
    for i in range(len(currentState)):
        if currentState[i] == 1:
            plantScore += plantIx
        plantIx += 1
    print('PlantScore: ' + str(plantScore))