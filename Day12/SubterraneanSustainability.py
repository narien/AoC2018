import numpy as np
import sys

def updateState(currentState, notes):
    currentState = [0, 0, 0, 0, 0] + currentState + [0, 0, 0, 0, 0]
    newState = currentState.copy()
    for i in range(2, len(currentState) - 2):
        if str(currentState[i-2:i+3]) in notes:
            newState[i] = 1
        else:
            newState[i] = 0
    return newState

def calcRes(i, currentState, memory):
    startIx = memory.index(currentState)
    halfCompleteIx = (int(sys.argv[1]) - i) % (len(memory) - startIx)
    finalState = startIx + halfCompleteIx
    return memory[finalState]





if __name__ == '__main__':
    currentState = []
    notes = set()
    memory = []
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
    stepsFromPotZero = 0
    for i in range(int(sys.argv[1]) + 1):
        trimmedZeros = 0
        for i in range(len(currentState)):
            if currentState[i] == 0:
                trimmedZeros += 1
            else:
                break
        if trimmedZeros < 5:
            stepsFromPotZero -= (5 - trimmedZeros)
        elif trimmedZeros > 5:
            stepsFromPotZero += (trimmedZeros - 5)
        currentState = np.trim_zeros(currentState)
        if currentState in memory:
            currentState = calcRes(i, currentState, memory)
            break
        else:
            memory.append(currentState)
            currentState = updateState(currentState, notes)

    plantScore = 0
    plantIx = -100
    for i in range(len(currentState)):
        if currentState[i] == 1:
            plantScore += stepsFromPotZero + plantIx
        plantIx += 1
    print('PlantScore: ' + str(plantScore))