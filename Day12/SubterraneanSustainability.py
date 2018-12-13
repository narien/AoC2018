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
    stepsFromPotZero = 0
    for i in range(1000):
        trimmedZeros = 0
        for j in range(len(currentState)):
            if currentState[j] == 0:
                trimmedZeros += 1
            else:
                break
        if trimmedZeros < 5:
            stepsFromPotZero -= (5 - trimmedZeros)
        elif trimmedZeros > 5:
            stepsFromPotZero += (trimmedZeros - 5)
        currentState = np.trim_zeros(currentState)
        currentState = updateState(currentState, notes)

    plantScore = 0
    for i in range(len(currentState)):
        if currentState[i] == 1:
            plantScore += stepsFromPotZero + i + (50000000000 - 1000)
    print('PlantScore: ' + str(plantScore))